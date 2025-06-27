from django.db import models

class Livro(models.Model):

    titulo = models.CharField()
    ano = models.DateField()
    preco = models.FloatField()
    quantidade = models.IntegerField()
    descricao = models.CharField(max_length=154, blank=True, null=True)

    #! adicionar o campo de autores 

    def __str__(self):
        return self.titulo
    

class Itenscompra(models.Model):

    livro = models.ForeignKey(Livro, on_delete=models.SET_NULL, null=True)
    quantidade = models.IntegerField()


    def __str__(self):
        #* deve retornar o nome do livro 
        return f'compra:{self.id}-{self.livro}-{self.quantidade}'