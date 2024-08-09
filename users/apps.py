from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        from .signals import create_profile


image = models.ImageField(default='media/profile_pics/default.png', upload_to='profile_pics')