from django.contrib import admin

from .models import Livro, Itenscompra

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ["titulo", "preco", "ano"]
    
    pass 
