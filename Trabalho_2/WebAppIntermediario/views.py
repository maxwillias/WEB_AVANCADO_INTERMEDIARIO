from django.shortcuts import render
from WebAppIntermediario.models import Produto

# Create your views here.


def index(request):
    produtos = Produto.objects.all()

    chaveProduto = {
        'produtos': produtos
    }

    return render(request, 'index.html', chaveProduto)


def produto(request, id):
    produto = Produto.objects.get(id=id)

    context = {
        'produto': produto
    }

    return render(request, 'produto.html', context)