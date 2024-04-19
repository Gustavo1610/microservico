from django.db import models
import uuid
from django.utils import timezone

class MicroServico(models.Model):
    codigo = models.CharField(
        max_length=8,
        null=False,
        blank=False
    )
  
    produto = models.CharField(
        max_length=20,
        null=False,
        blank=False
    )
  
    valor = models.DecimalField(
        null=False,
        blank=False,
        max_digits=5,
        decimal_places=2
    )
  
    data_criacao = models.DateTimeField(auto_now_add=True)
    