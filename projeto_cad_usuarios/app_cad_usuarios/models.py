from django.db import models
from django.core import validators

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key = True)
    usuario = models.CharField(max_length=255)
    senha = models.CharField(max_length=128, validators=[validators.MinLengthValidator(8)])