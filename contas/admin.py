from django.contrib import admin
from .models import User

class UsuarioAdmin(admin.ModelAdmin):

    list_display = ['username', 'name', 'email','is_staff','is_professor','data_entrou','data_atualizou']
    search_fields = ['username', 'name','email']
    # prepopulated_fields = {'slug': ('nome','tipo')}

admin.site.register(User,UsuarioAdmin)
