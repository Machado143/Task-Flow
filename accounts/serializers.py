from rest_framework import serializers  # Importa o módulo de serializers do Django REST Framework
from django.contrib.auth import get_user_model  # Importa a função para obter o modelo de usuário personalizado
from organizations.models import Organization  # Importa o modelo de Organização

# Obtém o modelo de usuário configurado no projeto
User = get_user_model()

# Serializer para registro de usuários
class RegisterSerializer(serializers.ModelSerializer):
    # Campo adicional para o nome da organização, que será usado apenas na criação (write_only=True)
    organization_name = serializers.CharField(max_length=100, write_only=True)

    class Meta:
        # Define o modelo associado ao serializer
        model = User
        # Define os campos que serão serializados/deserializados
        fields = ('id', 'username', 'email', 'password', 'organization_name')
        # Configurações adicionais para os campos
        extra_kwargs = {'password': {'write_only': True}}  # Torna o campo 'password' somente para escrita

    # Método para criar um novo usuário
    def create(self, validated_data):
        # Remove o nome da organização dos dados validados
        org_name = validated_data.pop('organization_name')
        # Busca ou cria uma organização com o nome fornecido
        org, _ = Organization.objects.get_or_create(name=org_name)
        # Cria um novo usuário associado à organização
        user = User.objects.create_user(
            username=validated_data['username'],  # Nome de usuário
            email=validated_data.get('email', ''),  # E-mail (padrão vazio se não fornecido)
            password=validated_data['password'],  # Senha
            organization=org  # Organização associada
        )
        return user  # Retorna o usuário criado

# Serializer para login de usuários
class LoginSerializer(serializers.Serializer):
    # Campo para o nome de usuário
    username = serializers.CharField()
    # Campo para a senha (write_only=True para não ser retornado na resposta)
    password = serializers.CharField(write_only=True)