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
    genero = models.CharField(max_length=20, choices=GENEROS)
    estudio = models.CharField(max_length=100)
    emissora = models.CharField(max_length=100)
    sinopse = models.TextField()

    def __str_(self):
        return self.nome