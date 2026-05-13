from django.db import models

class Desenho(models.Model):

    GENEROS = [
        ('comedia', 'Comédia'),
        ('aventura', 'Aventura'),
        ('misterio', 'Mistério'),
        ('acao', 'Ação'),
    ]
    
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()
    genero = models.CharField(max_length=20, choices=GENEROS)
    descricao = models.TextField()

    def __str_(self):
        return self.nome