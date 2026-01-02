from django.contrib import admin  # Importa o módulo de administração do Django
from django.urls import path, include  # Importa funções para definir rotas de URL
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView  # Importa visualizações para documentação da API

# Lista de padrões de URL do projeto
urlpatterns = [
    path('admin/', admin.site.urls),  # Rota para o painel de administração
    path('api/v1/auth/', include('accounts.urls')),  # Rotas relacionadas à autenticação
    path('api/v1/organizations/', include('organizations.urls')),  # Rotas relacionadas a organizações
    path('api/v1/projects/', include('projects.urls')),  # Rotas relacionadas a projetos
    path('api/v1/tasks/', include('tasks.urls')),  # Rotas relacionadas a tarefas
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),  # Rota para o esquema da API
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),  # Rota para a documentação Swagger
]
