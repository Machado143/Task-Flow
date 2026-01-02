# filepath: c:\Codigo\taskflow\organizations\urls.py
from django.urls import path  # Importa a função para definir rotas de URL
from django.http import JsonResponse  # Importa a função para retornar respostas JSON

# Exemplo de visualização para a API de organizações
def example_view(request):
    return JsonResponse({"message": "Organizations API"})  # Retorna uma mensagem JSON

# Lista de padrões de URL para o app de organizações
urlpatterns = [
    path('example/', example_view, name='organizations-example'),  # Rota de exemplo
]