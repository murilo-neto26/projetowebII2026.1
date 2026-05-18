from django.db import models

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
