from django.urls import path

from . import views

app_name = 'qrcode'

urlpatterns = [
    path('generate/', views.QRCodeGIFGenerateView.as_view(), name='generate_qr_with_gif'),
]
