from django import apps


class ExampleConfig(apps.AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "example"
