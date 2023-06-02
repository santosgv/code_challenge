from django.db import models

class Empresa(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Colaborador(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    gestor = models.OneToOneField('self', on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return self.nome


class Organograma(models.Model):
    gestor = models.OneToOneField(Colaborador, on_delete=models.CASCADE, related_name='lider')
    liderados = models.ManyToManyField(Colaborador, related_name='liderados')

    def __str__(self):
        return f'Gestor: {self.gestor.name}'
