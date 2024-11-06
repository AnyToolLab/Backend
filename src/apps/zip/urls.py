from django.urls import path

from . import views

app_name = 'zip'

urlpatterns = [
    path('create/', views.CreateZipView.as_view(), name='create'),
    path('extract/', views.ExtractZipView.as_view(), name='extract')
]
