from django.contrib import admin
from .models import Aluno


class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ingresso', 'nota', 'situacao')

# Register your models here.


admin.site.register(Aluno, AlunoAdmin)