# coding=utf-8

from django.contrib import admin
from .models import Curso, Categoria,Modulo,Atividade,Material,Aluno_curso

class CategoriasAdmin(admin.ModelAdmin):

    list_display = ['nome', 'slug']
    search_fields = ['nome', 'slug']
    # prepopulated_fields = {'slug': ('nome',)}

class CursosAdmin(admin.ModelAdmin):

    list_display = ['curso', 'slug', 'categoria', 'is_approved']
    search_fields = ['curso', 'slug']
    # prepopulated_fields = {'slug': ('curso','categoria','data_inicio','professor')}

# class AlunosAdmin(admin.ModelAdmin):
#
#     list_display = ['nome', 'slug', 'email', 'telefone']
#     search_fields = ['nome', 'slug']
    # prepopulated_fields = {'slug': ('nome','email')}

class ModulosAdmin(admin.ModelAdmin):

    list_display = ['nome', 'slug', 'descricao']
    search_fields = ['nome', 'slug']
    # prepopulated_fields = {'slug': ('nome','descricao',)}

class AtividadeAdmin(admin.ModelAdmin):

    list_display = ['nome', 'slug', 'tipo']
    search_fields = ['nome', 'slug']
    # prepopulated_fields = {'slug': ('nome','tipo')}

class MaterialAdmin(admin.ModelAdmin):

    list_display = ['nome', 'slug', 'tipo']
    search_fields = ['nome', 'slug']
    # prepopulated_fields = {'slug': ('nome','tipo')}

admin.site.register(Curso,CursosAdmin)
# admin.site.register(Aluno,AlunosAdmin)
admin.site.register(Categoria,CategoriasAdmin)
admin.site.register(Modulo,ModulosAdmin)
admin.site.register(Atividade,AtividadeAdmin)
admin.site.register(Material,MaterialAdmin)
admin.site.register(Aluno_curso)
