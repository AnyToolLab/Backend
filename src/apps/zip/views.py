import os
import uuid
import zipfile

from django.views.generic import FormView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from config import settings
from . import forms


@method_decorator(csrf_exempt, name='dispatch')
class CreateZipView(FormView):
    form_class = forms.CreateZipForm

    def get(self, request, *args, **kwargs):
        return JsonResponse(
            {
                'status': 'error',
                'message': 'Invalid request method',
                'data': {}
            }
        )

    def form_valid(self, form):
        files = form.cleaned_data.get('files')

        filename = f'{uuid.uuid4()}.zip'
        file_path = f'{settings.MEDIA_ROOT}{settings.ZIP_FILES_MEDIA_DIR}/{filename}'
        file_dir = os.path.dirname(file_path)
        os.makedirs(file_dir, exist_ok=True)
        with zipfile.ZipFile(file_path, "w", zipfile.ZIP_DEFLATED) as zip_file:
            for uploaded_file in files:
                zip_file.writestr(uploaded_file.name, uploaded_file.read())

        return JsonResponse(
            {
                'status': 'success',
                'message': 'Zip file successfully created!',
                'data': {
                    'file_url': f'{settings.MEDIA_URL}{settings.ZIP_FILES_MEDIA_DIR}/{filename}',
                    'file_name': 'archive.zip'
                }
            }
        )

    def form_invalid(self, form):
        return JsonResponse(
            {
                'status': 'error',
                'message': 'Invalid form data',
                'data': {'errors': form.errors.get_json_data()}
            }
        )


@method_decorator(csrf_exempt, name='dispatch')
class ExtractZipView(FormView):
    form_class = forms.ExtractZipForm

    def get(self, request, *args, **kwargs):
        return JsonResponse(
            {
                'status': 'error',
                'message': 'Invalid request method',
                'data': {}
            }
        )

    def form_valid(self, form):
        zip_file = form.cleaned_data.get('file')

        files_dir_name = uuid.uuid4()
        files_dir = f'{settings.MEDIA_ROOT}{settings.ZIP_FILES_MEDIA_DIR}/{files_dir_name}/'
        os.makedirs(files_dir, exist_ok=True)
        with zipfile.ZipFile(zip_file, 'r') as myzip:
            myzip.extractall(files_dir)

        return JsonResponse(
            {
                'status': 'success',
                'message': 'Zip file extracted successfully!',
                'data': {
                    'files': [{
                        'file_url': f'{settings.MEDIA_URL}{settings.ZIP_FILES_MEDIA_DIR}/{files_dir_name}/{file}',
                        'file_name': file,
                        'file_size': os.path.getsize(os.path.join(files_dir, file))
                    } for file in os.listdir(files_dir)],
                    'filе_name': zip_file.name,
                }
            }
        )

    def form_invalid(self, form):
        return JsonResponse(
            {
                'status': 'error',
                'message': 'Invalid form data',
                'data': {'errors': form.errors.get_json_data()}
            }
        )
