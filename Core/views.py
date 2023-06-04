from rest_framework import viewsets,status
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
        response = self.validar_dados(request.data)
        if isinstance(response, Response):  
            return response
        else:
            return super().create(request, *args, **kwargs)

    def validar_dados(self, data):
        gestor_id = data.get("gestor")
        colaboradores_ids = data.get("colaborador")

        if gestor_id and colaboradores_ids:
           gestor = Colaborador.objects.filter(id=gestor_id).first()
           colaborador = Colaborador.objects.filter(id__in=colaboradores_ids)

           if gestor_id != colaboradores_ids:
            if gestor and all(liderado.empresa == gestor.empresa for liderado in colaborador):
                if not gestor.colaborador.exists():
                    return None
                else:
                    return Response({"error": "O gestor já possui liderados"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"error": "Não pertence à mesma Empresa"}, status=status.HTTP_400_BAD_REQUEST)


        
        if gestor_id == colaboradores_ids:
            return Response({"error": "O gestor é o mesmo que o liderado"}, status=status.HTTP_400_BAD_REQUEST)
    
        
        return False

    @action(detail=True, methods=['get'])
    def colaboradores(self, request, pk=None):
        try:
            organograma = self.get_object()
            colaborador = organograma.colaborador.all()
            serializer = ColaboradorSerializer(colaborador, many=True)
            return Response(serializer.data)
        except Organograma.DoesNotExist:
            return Response({"error": "Organograma não encontrado"}, status=404)

    @action(detail=True, methods=['get'])
    def gestores_diretos(self, request, pk=None):
        try:
            organograma = self.get_object()
            gestor = organograma.gestor
            gestor_serializer = ColaboradorSerializer(gestor)
   
            return Response(gestor_serializer.data)
        except Organograma.DoesNotExist:
            return Response({"error": "Organograma não encontrado"}, status=404)

    