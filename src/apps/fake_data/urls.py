from django.urls import path

from . import views

app_name = 'fake_data'

urlpatterns = [
    path('generate/', views.GenerateFakeDataView.as_view(), name='generate'),
]
