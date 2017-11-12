from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.models import Curso, Aluno

class AlunoAdmin(UserAdmin):
    list_display = ('ra', 'email', 'nome', 'curso')
    list_filter = ('perfil',)
    fieldsets = ( (None, {'fields': ('ra','email', 'nome', 'curso')}),)
    add_fieldsets = (
        (None, {
             'fields': ('ra', 'nome', 'email', 'curso','password1', 'password1')
            }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

# Register your models here.

admin.site.register(Curso)
admin.site.register(Aluno, AlunoAdmin)
