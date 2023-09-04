from datetime import date
from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    apelido = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField( null=True, blank=True)
    senha = models.CharField(max_length=64, null=False, blank=False)

    def __str__(self):
        return self.apelido