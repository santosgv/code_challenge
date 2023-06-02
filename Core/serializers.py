from rest_framework import serializers
from Core.models import Empresa, Colaborador, Organograma

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class ColaboradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colaborador
        fields = '__all__'

class OrganogramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organograma
        fields = '__all__'
