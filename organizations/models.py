from django.db import models  # Importa o módulo de modelos do Django

# Modelo para representar uma organização
class Organization(models.Model):
    # Nome da organização (único)
    name = models.CharField(max_length=100, unique=True)
    # Data de criação da organização (preenchida automaticamente)
    created_at = models.DateTimeField(auto_now_add=True)

    # Representação em string do modelo
    def __str__(self):
        return self.name