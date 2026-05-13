from django.shortcuts import render
from .models import Desenho

def lista_desenhos(request):
    
    desenhos = Desenho.objects.all()

    return render(request, 'lista.html', {'desenhos': desenhos})

# Create your views here.
