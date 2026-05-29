from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


from .models import Desenho
from .forms import CadastroForm
from .models import Perfil


def home(request):
    return render(request, 'desenhos/home.html')


def biblioteca(request):
    return render(request, 'desenhos/biblioteca.html')


def lista(request):
    desenhos = Desenho.objects.all()
    return render(request, 'desenhos/lista.html', {
        'desenhos': desenhos
    })

def cadastrar(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            perfil = Perfil.objects.create(
                user=user,
                foto=form.cleaned_data['foto']
            )
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            link = f'http://localhost:8000/ativar/{uid}/{token}/'
            send_mail(
                'Ative sua conta',
                f'Clique aqui: {link}',
                'web2@ifce.edu.br',
                [user.email]
            )
            return render(request, 'cadastro_sucesso.html')
    else:
        form = CadastroForm()
    return render(request, 'cadastrar.html', {
        'form': form
    })

def ativar_conta(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        perfil = user.perfil
        perfil.email_confirmado = True
        perfil.save()
        return redirect('login')
    else:
        return render(request, 'token_invalido.html')
    
@login_required
def home(request):

    if not request.user.perfil.email_confirmado:
        return render(request, 'aguardando_confirmacao.html')

    return render(request, 'home.html')