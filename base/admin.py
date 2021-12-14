from django.contrib import admin
from base.models import Biblioteca, Titulo, Exemplar

@admin.register(Biblioteca)
class BibliotecaAdmin(admin.ModelAdmin):
    list_display = 'nome',


@admin.register(Titulo)
class TituloAdmin(admin.ModelAdmin):
    list_display = 'nome', 'categoria', 'imagem',
    ordering = 'nome',
    list_filter = 'categoria',


@admin.register(Exemplar)
class ExemplarAdmin(admin.ModelAdmin):
    list_display = 'data_aquisicao', 'titulo', 'ativo',
    ordering = 'titulo',

