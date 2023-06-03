from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
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
        colaboradores_ids = data.get("colaborador")

        if gestor_id and colaboradores_ids:
           gestor = Colaborador.objects.filter(id=gestor_id).first()
           colaborador = Colaborador.objects.filter(id__in=colaboradores_ids)

           if gestor_id != colaboradores_ids:
            if gestor and all(liderado.empresa == gestor.empresa for liderado in colaborador):
                if not gestor.colaborador.exists():
                    return True
                else:
                    print("O gestor já possui liderados")
            else:
                print('Nao pertence a mesma Empresa')


        
        if gestor_id == colaboradores_ids:
            print('O gestor e o mesmo que o liderado')
            return False
    
        
        return False

    @action(detail=True, methods=['get'])
    def pares(self, request, pk=None):
        try:
            organograma = self.get_object()
            liderados = organograma.colaborador.all()
            serializer = ColaboradorSerializer(liderados, many=True)
            return Response(serializer.data)
        except Organograma.DoesNotExist:
            return Response({"error": "Organograma não encontrado"}, status=404)

    @action(detail=True, methods=['get'])
    def liderados_diretos(self, request, pk=None):
        try:
            pass
            # parei aqui
        except Colaborador.DoesNotExist:
            return Response({"error": "Colaborador não encontrado"}, status=404)

    