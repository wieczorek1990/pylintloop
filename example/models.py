from django.db import models

from example import typing


class Example(models.Model):
    class Enum(models.TextChoices):
        EXAMPLE = typing.string_auto("e", "Example")

    enum = models.CharField(max_length=1, choices=Enum.choices)
