from django.db import models

class Categoria(models.Model):
    nome = models.CharField("Nome",max_length=50)
    etiqueta = models.SlugField("Etiqueta",max_length=50)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField("Nome",max_length=50)
    etiqueta = models.SlugField("Etiqueta",max_length=50)
    preco = models.DecimalField("Preco",decimal_places=2,max_digits=8)
    categoria = models.ForeignKey(Categoria)

    def __str__(self):
        return self.nome
# Create your models here.
