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
        file_path = f'{settings.MEDIA_ROOT}/{settings.ZIP_FILES_MEDIA_DIR}/{filename}'
        with zipfile.ZipFile(file_path, "w", zipfile.ZIP_DEFLATED) as zip_file:
            for uploaded_file in files:
                zip_file.writestr(uploaded_file.name, uploaded_file.read())


        return JsonResponse(
            {
                'status': 'success',
                'message': 'QRCode successfully generated!',
                'data': {
                    'url': f'{settings.MEDIA_URL}{settings.ZIP_FILES_MEDIA_DIR}/{filename}',
                    'filename': 'your-archive.zip'
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
