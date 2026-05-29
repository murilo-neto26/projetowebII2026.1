from django.db import models
from django.contrib.auth.models import User

class Desenho(models.Model):

    GENEROS = [
        ('comedia', 'Comédia'),
        ('aventura', 'Aventura'),
        ('misterio', 'Mistério'),
        ('acao', 'Ação'),
        ('romance', 'Romance'),
        ('fantasia', 'Fantasia'),
        ('ficcao_cientifica', 'Ficção científica'),
    ]

    nome = models.CharField(max_length=100)
    ano = models.IntegerField()
    genero = models.CharField(max_length=100, choices=GENEROS)
    estudio = models.CharField(max_length=100)
    emissora = models.CharField(max_length=100)
    sinopse = models.TextField()
    capa = models.ImageField(
        upload_to='capas/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.nome


class Lista(models.Model):
    nome = models.CharField(max_length=100)
    desenhos = models.ManyToManyField(Desenho)
    

class Perfil(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='perfis/',null=True,blank=True)
    bio = models.TextField(max_length=500,blank=True)
    email_confirmado = models.BooleanField(default=False)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Perfil de {self.user.username}'