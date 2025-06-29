from django.contrib import admin

from .models import *

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ["titulo", "preco", "ano"]
    

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):    
    list_display = ('__str__', 'email', 'ativo')
    search_fields = ('nome', 'sobrenome')
    list_filter = ('ativo',)

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'cliente', 'status')
    search_fields = (
        'cliente__nome',
        'cliente__sobrenome',
        'cliente__email',
    )
    list_filter = ('status',)
    date_hierarchy = 'created'