import json
import csv
import uuid
from io import BytesIO, StringIO

from dict2xml import dict2xml
from django.http import JsonResponse
from django.views.generic import FormView
from django.core.files.base import ContentFile

from src.apps.fake_data import forms
from src.apps.fake_data.models import File
from src.apps.fake_data.utils import FAKE_DATA


class GenerateFakeDataView(FormView):
    form_class = forms.GenerateFakeDataForm

    def get(self, request, *args, **kwargs):
        return JsonResponse(
            {
                'status': 'error',
                'message': 'Invalid request method',
                'data': {}
            }
        )

    def form_valid(self, form):
        fake_data = form.cleaned_data.get('fake_data')
        rows = form.cleaned_data.get('rows')
        save_format = form.cleaned_data.get('save_format').lower()

        generated_fake_data = {}
        for i in fake_data:
            generated_fake_data[i] = [FAKE_DATA[i]() for _ in range(rows)]

        filename = f'{uuid.uuid4()}.{save_format}'
        file_data = ''

        if save_format == 'xml':
            file_data = dict2xml(generated_fake_data)
        elif save_format == 'json':
            file_data = json.dumps(generated_fake_data)
        elif save_format == 'csv':
            file_data = StringIO()
            field_names = list(generated_fake_data.keys())
            writer = csv.DictWriter(file_data, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(generated_fake_data)

            file_data.seek(0)
            file_data = file_data.getvalue()

        file_instance = File()
        file_instance.file.save(filename, ContentFile(file_data))
        file_instance.save()

        return JsonResponse(
            {
                'status': 'success',
                'message': 'Fake data generated successfully!',
                'data': {
                    'url': file_instance.file.url,
                    'filename': filename,
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
