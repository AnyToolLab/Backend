import time
from io import BytesIO
import os
from uuid import uuid4

from PIL import Image

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView
from django.http import JsonResponse
from django.core.files.base import ContentFile

from config import settings
from . import forms
from .models import File


@method_decorator(csrf_exempt, name='dispatch')
class ImageConverterView(FormView):
    form_class = forms.ImageConverterForm

    def get(self, request, *args, **kwargs):
        return JsonResponse(
            {
                'status': 'error',
                'message': 'Invalid request method',
                'data': {}
            }
        )

    def form_valid(self, form):
        images = form.cleaned_data.get('images')
        convert_to_formats = form.cleaned_data.get('convert_to_formats')

        file_instances = []
        image_names = []
        for image_file, convert_format in zip(images, convert_to_formats):
            if image_file and convert_format:
                with Image.open(image_file) as img:
                    img_format = convert_format.upper()

                    if img.mode == 'RGBA' and img_format == 'JPEG':
                        background = Image.new('RGB', img.size, (255, 255, 255))
                        background.paste(img, (0, 0), img)
                        img = background

                    img_converted = BytesIO()
                    img.save(img_converted, format=img_format)
                    img_converted.seek(0)

                    original_name = os.path.splitext(image_file.name)[0]
                    unique_name = f"{uuid4()}.{convert_format.lower()}"

                    file_instance = File()
                    file_instance.file.save(unique_name, ContentFile(img_converted.read()), save=False)

                    image_names.append(f"{original_name}.{convert_format.lower()}")
                    file_instances.append(file_instance)

        File.objects.bulk_create(file_instances)

        converted_image_urls = [f'{settings.DOWNLOAD_URL}{file_instance.file.url}' for file_instance in file_instances]
        invalid_image_indexes = [i for i in range(len(images)) if i == False]

        return JsonResponse(
            {
                'status': 'success',
                'message': 'Images converted successfully!',
                'data': {
                    'converted_image_urls': converted_image_urls,
                    'converted_image_names': image_names,
                    'invalid_image_indexes': invalid_image_indexes
                }
            }
        )

    def form_invalid(self, form):
        return JsonResponse(
            {
                'status': 'error',
                'message': 'Invalid form data',
                'data': {'errors': form.errors}
            }
        )
