from django.urls import path

from . import views

app_name = 'qrcode'

urlpatterns = [
    path('convert/', views.ImageConverterView.as_view(), name='convert'),
]
