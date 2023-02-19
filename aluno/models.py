from django.db import models


class Materia(models.Model):
    descricao = models.CharField(max_length=16)


class Nota(models.Model):
    pontuacao = models.PositiveIntegerField()
    materia = models.ForeignKey(Materia, on_delete=models.PROTECT)
    aprovado = models.BooleanField(default=False)


class Aluno(models.Model):
    nome = models.CharField(max_length=64)
    cpf = models.CharField(max_length=11)
    nascimento = models.DateField()
    notas = models.ManyToManyField(Nota)
