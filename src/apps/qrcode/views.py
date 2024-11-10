from uuid import uuid4
import os

import segno

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core.files import File as DjangoFile
from django.views.generic import FormView

from config import settings

from . import forms
from .models import File


@method_decorator(csrf_exempt, name='dispatch')
class QRCodeGenerateView(FormView):
    form_class = forms.QRCodeGenerateForm

    def get(self, request, *args, **kwargs):
        return JsonResponse(
            {
                'status': 'error',
                'message': 'Invalid request method',
                'data': {}
            }
        )

    def form_valid(self, form):
        content = form.cleaned_data.get('content')
        color = form.cleaned_data.get('color')
        background_img = form.cleaned_data.get('background_img')
        background_color = form.cleaned_data.get('background_color')
        save_format = form.cleaned_data.get('save_format')

        qrcode = segno.make(content, error='m', version=15)
        qrcode_name = f'{uuid4()}{save_format}'
        file_path = os.path.join(settings.MEDIA_ROOT, 'qrcode_temp', qrcode_name)

        if background_img:
            artistic_kwargs = {
                'background': background_img,
                'target': file_path,
                'scale': 5,
                'dark': color,
                'data_dark': color,
                'data_light': background_color,
            }
            qrcode.to_artistic(**artistic_kwargs)

        else:
            pil_kwargs = {
                'dark': color,
                'data_dark': color,
                'data_light': background_color,
                'scale': 5,
            }
            qrcode.to_pil(**pil_kwargs).save(file_path)

        with open(file_path, 'rb') as f:
            django_file = DjangoFile(f)
            file_instance = File.objects.create(file=django_file)

        os.remove(file_path)

        return JsonResponse(
            {
                'status': 'success',
                'message': 'QRCode successfully generated!',
                'data': {
                    'url': file_instance.file.url,
                    'filename': f'qrcode{save_format}'
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
