from rest_framework import viewsets,status
from rest_framework.response import Response
from Core.models import Empresa, Colaborador, Organograma
from Core.serializers import EmpresaSerializer, ColaboradorSerializer, OrganogramaSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class ColaboradorViewSet(viewsets.ModelViewSet):
    queryset = Colaborador.objects.all()
    serializer_class = ColaboradorSerializer

    def list_by_empresa(self, request, empresa_id=None):
        colaboradores = self.queryset.filter(empresa=empresa_id)
        serializer = self.get_serializer(colaboradores, many=True)
        return Response(serializer.data)

class OrganogramaViewSet(viewsets.ModelViewSet):
    queryset = Organograma.objects.all()
    serializer_class = OrganogramaSerializer

    def create(self, request, *args, **kwargs):
        if self.validar_dados(request.data):
            return super().create(request, *args, **kwargs)
        else:
            return Response({"error": "Dados inválidos"}, status=400)

    def validar_dados(self, data):
        # Implemente as validações necessárias com base nos dados recebidos
        # Retorne True se os dados forem válidos e False caso contrário

        gestor = data.get("gestor")
        liderados = data.get("liderados")

        # valida se o gestor e o mesmo que o liderado
        if gestor is None or liderados is None or gestor == liderados:
            return False
        return True