# filepath: c:\Codigo\taskflow\accounts\models.py
from django.contrib.auth.models import AbstractUser  # Importa o modelo de usuário base do Django
from django.db import models  # Importa o módulo de modelos do Django

# Modelo personalizado de usuário
class User(AbstractUser):
    # Campo para associar o usuário a uma organização
    organization = models.ForeignKey(
        'organizations.Organization',  # Referência ao modelo de Organização
        on_delete=models.CASCADE,  # Exclui o usuário se a organização for excluída
        related_name='members',  # Nome relacionado para acessar os membros da organização
        null=True,  # Permite que o campo seja nulo temporariamente
    )

    # Adiciona related_name para evitar conflitos com o modelo base do Django
    groups = models.ManyToManyField(
        'auth.Group',  # Referência ao modelo de grupos de permissões
        related_name='custom_user_set',  # Nome relacionado personalizado
        blank=True,  # Permite que o campo seja vazio
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',  # Referência ao modelo de permissões
        related_name='custom_user_set',  # Nome relacionado personalizado
        blank=True,  # Permite que o campo seja vazio
    )