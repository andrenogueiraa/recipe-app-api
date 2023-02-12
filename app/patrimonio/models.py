from django.db import models
from django.contrib.auth.models import Group
from django.conf import settings


class Patrimonio(models.Model):
    """Item de patrimônio."""
    tipo = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)
    cor = models.CharField(max_length=255)
    responsavel = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    setor = models.ForeignKey(Group, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.tipo} {self.marca} {self.modelo}'
