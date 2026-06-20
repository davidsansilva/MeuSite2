from django.shortcuts import render

# Create your views here.

def home(request):

    context = {
        'nome': 'David', 
        'sobrenome': 'Santos'
    }

    #o segundo parametro é o caminho do HTML
    return render(request, 'home.html', context)

def contato(request):
    return render(request, 'contato.html')

def exibir_produtos(request):

    produtos = ['Bonés', 'Camisetas', 'Agasalhos']
    context = {
        'produtos' : produtos

    }

    return render(request, 'produtos.html', context)