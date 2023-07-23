from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "djblogger.blog"

    def ready(self):
        import djblogger.blog.signals  # Agrega esta línea para importar el archivo signals.py