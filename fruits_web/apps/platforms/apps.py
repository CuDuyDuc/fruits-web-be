from django.apps import AppConfig


class PlatformsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fruits_web.apps.platforms'
    
    def ready(self):
        import fruits_web.apps.platforms.signals
