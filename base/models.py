from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import MaxValueValidator, MinValueValidator
from polymorphic.models import PolymorphicModel

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
    
    def add_balance(self, value):
        self.balance += value

    def decrease_balance(self, value):
        self.balance -= value

    def update_score(self, transfer_amount):
        self.score = min(10.00, transfer_amount/1000 + self.score)
    
class Transaction(models.Model):
    value = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        validators=[
            MinValueValidator(0.0)
        ]
    )
    creation_data = models.DateTimeField(
        auto_now_add=True,
    )
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='transactions'
    )

    def __str__(self):
        return f'Transaction\'s ID: {self.id}'
    
class TransactionOption(PolymorphicModel):
    value = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        validators=[
            MinValueValidator(0.0)
        ]
    )

    def __str__(self):
        return f'Option\'s ID: {self.id}'

class TransactionExecuted(models.Model):
    transaction = models.ForeignKey(
        Transaction, 
        on_delete=models.CASCADE, 
        related_name='executed_option'
    )
    option = models.ForeignKey(
        TransactionOption, 
        on_delete=models.CASCADE, 
        related_name='executed_transaction'
    )
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'Executed Transaction - Transaction ID: {self.transaction.id} - Quantity: {self.quantity}'
    
class InvestmentOption(TransactionOption):
    name = models.CharField(
        max_length=64
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

    def decrease_quantity(self, value):
        self.quantity -= value

class LoanOption(TransactionOption):
    installments = models.PositiveIntegerField()
    interest_ratio = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(10.0)
        ]
    )
    min_score = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(10.0)
        ]
    )
    
class InsuranceOption(TransactionOption):
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

class DepositOption(TransactionOption):
    method = models.CharField(
        max_length=32
    )

class TransferOption(TransactionOption):
    destiny = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='destiny'
    )