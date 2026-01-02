# filepath: c:\Codigo\taskflow\accounts\models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    organization = models.ForeignKey(
        'organizations.Organization',
        on_delete=models.CASCADE,
        related_name='members',
        null=True,  # temporário até criarmos organização
    )

    # Adicione os related_name para evitar conflitos
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
    )