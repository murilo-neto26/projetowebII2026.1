from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .forms import ListaForm
from .models import Lista
from .models import Desenho
from .forms import CadastroForm
from .models import Perfil

def biblioteca(request):
    desenhos = Desenho.objects.all()
    busca = request.GET.get('busca')
    genero = request.GET.get('genero')
    decada = request.GET.get('decada')
    estudio = request.GET.get('estudio')
    emissora = request.GET.get('emissora')
    if busca:
        desenhos = desenhos.filter(nome__icontains=busca)
    if genero:
        desenhos = desenhos.filter(genero=genero)
    if decada:
        inicio = int(decada)
        fim = inicio + 9
        desenhos = desenhos.filter(ano__gte=inicio,ano__lte=fim)
    if estudio:
        desenhos = desenhos.filter(estudio__icontains=estudio)
    if emissora:
        desenhos = desenhos.filter(emissora__icontains=emissora)
    return render(request,'desenhos/biblioteca.html',{'desenhos': desenhos})

def lista(request):

    Lista.objects.get_or_create(
        nome='Favoritos'
    )

    Lista.objects.get_or_create(
        nome='Assistidos'
    )

    listas = Lista.objects.all()

    return render(
        request,
        'desenhos/lista.html',
        {'listas': listas}
    )
    listas = Lista.objects.all()
    return render(
        request,
        'desenhos/lista.html',
        {'listas': listas}
    )

def cadastrar(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()
            Perfil.objects.create(
                user=user,
                foto=form.cleaned_data['foto']
            )
            token = default_token_generator.make_token(user)
            print("TOKEN GERADO:", token)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            link = f'http://localhost:8000/ativar/{uid}/{token}/'
            send_mail(
                'Ative sua conta',
                f'Clique aqui: {link}',
                'web2@ifce.edu.br',
                [user.email]
            )
            return render(request, 'desenhos/cadastro_sucesso.html')
    else:
        form = CadastroForm()
    return render(request, 'desenhos/cadastrar.html', {
        'form': form
    })

def ativar_conta(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    print("UID:", uid)
    print("TOKEN:", token)
    print("USER:", user)
    print("TOKEN RECEBIDO:", token)

    resultado = default_token_generator.check_token(user, token)

    print("TOKEN VALIDO?", resultado)
    resultado = default_token_generator.check_token(user, token)

    print("TOKEN VALIDO?", resultado)
    if user is not None and default_token_generator.check_token(user, token):
        perfil = user.perfil
        perfil.email_confirmado = True
        perfil.save()
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return render(request, 'desenhos/token_invalido.html')

def detalhes_lista(request, lista_id):
    lista = get_object_or_404(Lista, id=lista_id)

    return render(
        request,
        'desenhos/detalhes_lista.html',
        {'lista': lista}
    )

@login_required
def home(request):
    if not request.user.perfil.email_confirmado:
        return render(request, 'desenhos/aguardando_confirmacao.html')
    desenhos = Desenho.objects.all()[:6]
    return render(request, 'desenhos/home.html', {
        'desenhos': desenhos
    })

@login_required
def criar_lista(request):
    if request.method == 'POST':
        form = ListaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = ListaForm()
    return render(request,'desenhos/criar_lista.html',{'form': form}
    )

@login_required
def excluir_lista(request, lista_id):
    lista = get_object_or_404(
        Lista,
        id=lista_id
    )
    if request.method == 'POST':
        lista.delete()
        return redirect('lista')
    return render(request,'desenhos/excluir_lista.html',{'lista': lista}
    )

@login_required
def favoritar_desenho(request, desenho_id):

    desenho = get_object_or_404(
        Desenho,
        id=desenho_id
    )

    favoritos, criado = Lista.objects.get_or_create(
        nome='Favoritos'
    )

    favoritos.desenhos.add(desenho)

    return render(
        request,
        'desenhos/favoritado.html'
    )

@login_required
def marcar_assistido(request, desenho_id):

    desenho = get_object_or_404(
        Desenho,
        id=desenho_id
    )

    assistidos, criado = Lista.objects.get_or_create(
        nome='Assistidos'
    )

    assistidos.desenhos.add(desenho)

    return render(
        request,
        'desenhos/assistido.html'
    )