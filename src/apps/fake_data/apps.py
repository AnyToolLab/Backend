from django.apps import AppConfig


class FakeDataConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src.apps.fake_data'
