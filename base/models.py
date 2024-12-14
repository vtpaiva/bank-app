from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from .validators import *

# Create your models here.

class Client(models.Model):
    cpf = models.CharField(
        max_length=11,
        validators=[cpf_validator],
        primary_key=True
    )
    name = models.CharField(max_length=64)
    creation_date = models.DateField(auto_now_add=True)
    balance = models.DecimalField(
        max_digits=15,
        decimal_places=2
    )
    score = models.DecimalField(
        max_digits=4,
        decimal_places=2, 
        validators=[
            MinValueValidator(0.00),
            MaxValueValidator(10.00)
        ]
    )

    def __str__(self):
        return f'Client\'s CPF: {self.cpf}. Client\'s name: {self.name}'