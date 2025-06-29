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
    
class Cliente(models.Model):
    nome = models.CharField()
    sobrenome = models.CharField()
    email = models.EmailField()
    ativo = models.BooleanField()

    class Meta: 
        ordering = ['nome']
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome or ""}'.strip()
    

    def __str__(self):
        return self.nome_completo


STATUS = (
    ('p','Pendente'),
    ('a','Aprovado'),
    ('c','Cancelado'),
)


class Pedido(models.Model):
    status = models.CharField(max_length=1, choices=STATUS, default='p')
    
    cliente = models.ForeignKey(
        Cliente, 
        on_delete=models.SET_NULL,
        related_name='pedidos',
        null=True,
        blank=True
        )
    
    created = models.DateTimeField('criado em', auto_now_add=True, auto_now=False)

    class Meta: 
        ordering = ['-pk']
        verbose_name = 'ordem de compra'
        verbose_name_plural = 'ordens de compra'
    
    def __str__(self):

        if self.cliente:
            return f'{str(self.pk).zfill(3)}-{self.cliente}'

        return f'{str(self.pk).zfill(3)}'


METODO_PAGAMENTO = (
    ("di", "dinheiro"),
    ("cr", "crédito"),
    ("de", "débito"),
    ("pi", "Pix"),
)


class Venda(models.Model):
    pedido = models.OneToOneField(
        Pedido,
        on_delete=models.CASCADE,
        verbose_name='ordem de compra'
    )
    status = models.BooleanField('pago', default=False)
    data_pagamento = models.DateTimeField('data de pagamento', null=True, blank=True)
    metodo = models.CharField('forma de pagamento', max_length=3, choices=METODO_PAGAMENTO)
    entrega = models.PositiveSmallIntegerField('prazo de entrega', default=15)
    created = models.DateTimeField('criado em', auto_now_add=True, auto_now=False)

    class Meta:
        ordering = ('-pk',)
        verbose_name = 'venda'
        verbose_name_plural = 'vendas'

    def __str__(self):
        if self.pedido:
            return f'{str(self.pk).zfill(3)}-{self.pedido}'

        return f'{str(self.pk).zfill(3)}'