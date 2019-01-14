from django.contrib import admin

# Register your models here.

from .models import *
admin.site.site_header = 'Painel de Controle'
admin.site.index_title = 'Recursos'
admin.site.site_title = 'JARDESSON/ANDERSON'


class ItemTemaAdmin(admin.ModelAdmin):

    list_display = ('cod_item', 'nome', 'descricao')

admin.site.register(ItemTema, ItemTemaAdmin)

class TemaAdmin(admin.ModelAdmin):

    list_display = ('cod_tema', 'nome', 'valor_aluguel', 'cor_toalha','cod_item')

admin.site.register(Tema, TemaAdmin)


class EnderecoAdmin(admin.ModelAdmin):

    list_display = ('cod_endere', 'cidade', 'uf', 'logradouro', 'bairro','numero', 'cep')

admin.site.register(Endereco,EnderecoAdmin)

class ClienteAdmin(admin.ModelAdmin):

   list_display = ('cod_cliente', 'nome', 'telefone')

admin.site.register(Cliente,ClienteAdmin)

class AluguelAdmin(admin.ModelAdmin):

    list_display = ('cod_aluguel', 'data_festa', 'hora_inicio', 'hora_termino', 'valor_cobrado', 'cod_endere', 'cod_cliente', 'cod_tema')

admin.site.register(Aluguel, AluguelAdmin)
