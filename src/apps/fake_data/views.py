import json

from dict2xml import dict2xml
from django.http import JsonResponse
from django.views.generic import FormView

from src.apps.fake_data import forms
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
        save_format = form.cleaned_data.get('save_format')

        generated_fake_data = {}
        for i in fake_data:
            generated_fake_data[i] = [FAKE_DATA[i]() for _ in range(rows)]

        if save_format == 'csv':
            generated_fake_data = dict2xml(generated_fake_data)
        elif save_format == 'json':
            generated_fake_data = json.dumps(generated_fake_data)
        # elif save_format == 'xml':
        #     generated_fake_data = dict2xml(generated_fake_data)

        return JsonResponse(
            {
                'status': 'success',
                'message': 'QRCode successfully generated!',
                'data': {
                    'url': file_instance.file.url
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
