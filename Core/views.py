from rest_framework import viewsets
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
        gestor_id = data.get("gestor")
        liderados_ids = data.get("liderados", [])
        
        if gestor_id and liderados_ids:
            gestor = Colaborador.objects.filter(id=gestor_id).first()
            liderados = Colaborador.objects.filter(id__in=liderados_ids)
            print(data.get('gestor'))
            print(data.get('liderados'))
            if gestor and all(liderado.empresa == gestor.empresa for liderado in liderados):
                return True
            
        if gestor_id is None or liderados_ids is None or gestor_id == liderados:
            return False
        
        return False