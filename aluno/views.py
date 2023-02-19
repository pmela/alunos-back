from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions

from aluno.models import Aluno
from aluno.serializers import UserSerializer, AlunoSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    # permission_classes = [permissions.IsAuthenticated]
