from django.apps import AppConfig


class MatConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mat'

    def ready(self):
        import mat.signals