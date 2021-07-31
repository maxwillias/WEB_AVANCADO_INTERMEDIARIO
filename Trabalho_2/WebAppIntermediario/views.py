from django.shortcuts import render
from WebAppIntermediario.models import Aluno

# Create your views here.


def index(request):
    alunos = Aluno.objects.all()

    chaveAluno ={
        'alunos': alunos
    }

    return render(request, 'index.html', chaveAluno)


def aluno(request, id):
    aluno = Aluno.objects.get(id=id)

    context = {
        'aluno': aluno
    }

    return render(request, 'aluno.html', context)