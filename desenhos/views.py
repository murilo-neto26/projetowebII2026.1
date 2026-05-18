from django.shortcuts import render
from .models import Desenho

from django.shortcuts import render

def home(request):
    return render(request, 'desenhos/home.html')

def biblioteca(request):
    return render(request, 'desenhos/biblioteca.html')

def lista(request):

    desenhos = Desenho.objects.all()
    return render(request, 'desenhos/lista.html', {
        'desenhos': desenhos
    })