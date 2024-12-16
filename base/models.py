from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser, Group, Permission, BaseUserManager
from django.core.validators import MaxValueValidator, MinValueValidator

from .validators import *

class UserManager(BaseUserManager):
    def create_user(self, CPF, first_name, last_name, email, password, **extra_fields):

        email = self.normalize_email(email)
        user = self.model(
            CPF=CPF, 
            email=email, 
            first_name=first_name, 
            last_name=last_name, 
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, CPF, first_name, last_name, email, password, **extra_fields):
        
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(CPF, first_name, last_name, email, password, **extra_fields)
    
class User(AbstractUser):
    id = None
    username=None
    CPF = models.CharField(
        max_length=11,
        validators=[cpf_validator],
        primary_key=True
    )
    balance = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0.0
    )
    score = models.DecimalField(
        max_digits=4,
        decimal_places=2, 
        default=0.0,
        validators=[
            MinValueValidator(0.00),
            MaxValueValidator(10.00)
        ]
    )

    USERNAME_FIELD = 'CPF'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'password']

    objects = UserManager()

    def __str__(self):
        return f'User\'s CPF: {self.CPF}'
    
class InvestmentOption(models.Model):
    name = models.CharField(
        max_length=64
    )
    price = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        validators=[
            MinValueValidator(0.0)
        ]
    )
    quantity = models.PositiveIntegerField(
        default=0
    )
    month_profitability = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(1.0)
        ]
    )
    risk = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(10.0)
        ]
    )
    liquidity = models.DateField(
        validators=[MinValueValidator(now().date())]
    )
    image = models.URLField()

    def __str__(self):
        return f'Option\'s ID: {self.id}'
    
class InsuranceOption(models.Model):
    price = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        validators=[
            MinValueValidator(0.0)
        ]
    )
    category = models.CharField(
        max_length=32,
        default='General'
    )
    min_score = models.DecimalField(
        max_digits=4,
        decimal_places=2, 
        default=0.0,
        validators=[
            MinValueValidator(0.00),
            MaxValueValidator(10.00)
        ]
    )

    def __str__(self):
        return f'Option\'s ID: {self.id}'
    
    def __repr__(self):
        return 'Insurance option'