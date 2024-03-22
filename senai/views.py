from rest_framework import viewsets
from senai.models import Aluno
from senai.serializer import AlunoSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    """Endpoint para exibir os dados de alunos"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer