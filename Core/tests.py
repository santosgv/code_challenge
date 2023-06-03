from django.test import TestCase
from rest_framework.test import APIClient
from Core.models import Colaborador, Organograma,Empresa
from Core.serializers import ColaboradorSerializer, OrganogramaSerializer

class OrganogramaViewSetTestCase(TestCase):
    # Testes unitatios dos End point da API


    def setUp(self):
        self.client = APIClient()
        # Cria empresas
        self.empresa1 = Empresa.objects.create(name='empresa 1')
        self.empresa2 = Empresa.objects.create(name='empresa 2')

        # Cria gestores
        self.gestor1 = Colaborador.objects.create(nome="Gestor 1",email='email@email.com',empresa=self.empresa1)
        self.gestor2 = Colaborador.objects.create(nome="Gestor 2",email='email@email.com',empresa=self.empresa2)

        # Cria colaboradores
        self.colaborador1 = Colaborador.objects.create(nome="Colaborador 1",email='email@email.com',empresa=self.empresa1)
        self.colaborador2 = Colaborador.objects.create(nome="Colaborador 2",email='email@email.com',empresa=self.empresa2)
        self.colaborador1Empresa2 = Colaborador.objects.create(nome="Colaborador 1 empresa 2",email='email@email.com',empresa=self.empresa2)
        self.colaborador2Empresa2 = Colaborador.objects.create(nome="Colaborador 2 empresa 2",email='email@email.com',empresa=self.empresa2)

        # Cria Organogramas
        self.organograma1 = Organograma.objects.create(gestor=self.gestor1)
        self.organograma1.colaborador.set([self.colaborador1])

        self.organograma2 = Organograma.objects.create(gestor=self.gestor2)
        self.organograma2.colaborador.set([self.colaborador2])


    def test_lista_empresas(self):
        response = self.client.get(f'/api/empresas/')
        self.assertEqual(response.status_code, 200)

    def test_visualiza_empresas(self):
        response = self.client.get(f'/api/empresas/{self.empresa1.pk}/')
        self.assertEqual(response.status_code, 200)

    def test_altera_empresas(self):
        novo_nome ="Nova Empresa"
        data ={'name':novo_nome}
        response = self.client.put(f'/api/empresas/{self.empresa2.pk}/',data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_lista_colaboradores(self):
        response = self.client.get(f'/api/colaboradores/')
        self.assertEqual(response.status_code, 200)

    def test_visualizar_colaborador(self):
        response = self.client.get(f'/api/colaboradores/{self.colaborador1.pk}/')
        self.assertEqual(response.status_code, 200)

    def test_altera_colaborador(self):
        novo_nome ="Novo Colaborador"
        novo_email="novoemail@email.com"
        data ={ 'nome':novo_nome,
                'email':novo_email,
                'empresa': self.empresa1.id
        }

        response = self.client.put(f'/api/colaboradores/{self.colaborador2Empresa2.pk}/',data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_lista_organograma(self):
        response = self.client.get(f'/api/organogramas/')
        self.assertEqual(response.status_code, 200)

    def test_visualizar_organograma(self):
        response = self.client.get(f'/api/organogramas/{self.organograma1.pk}/')
        self.assertEqual(response.status_code, 200)

    def test_lista_colaboradores_associados(self):
        response = self.client.get(f'/api/organogramas/{self.organograma1.pk}/colaboradores/')
        self.assertEqual(response.status_code, 200)

    def test_lista_gestores_diretos(self):
        response = self.client.get(f'/api/organogramas/{self.organograma1.pk}/gestores_diretos/')
        self.assertEqual(response.status_code, 200)

