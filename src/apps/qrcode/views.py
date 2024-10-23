import time
import uuid
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView
import segno

from config.settings import MEDIA_URL, MEDIA_ROOT

from . import forms


@method_decorator(csrf_exempt, name='dispatch')
class QRCodeGIFGenerateView(FormView):
    form_class = forms.QRCodeGIFGenerateForm


    def form_valid(self, form):
        file = form.cleaned_data['file']
        text = form.cleaned_data['text']

        qrcode = segno.make(text, error='h')
        qrcode_name = f'qrcode-{uuid.uuid4()}.gif'
        qrcode.to_artistic(background=file, target=f'{MEDIA_ROOT}/qrcode/{qrcode_name}', scale=8)

        return JsonResponse({'message': 'success', 'url': f'http://192.168.88.116:8000{MEDIA_URL}qrcode/{qrcode_name}'})
    

    def form_invalid(self, form):
        return JsonResponse({'message': 'error'})