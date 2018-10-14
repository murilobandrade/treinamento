from django.contrib import admin

from .models import Pessoa


# Register your models here.
class PessoaAdmin(admin.ModelAdmin):
    fields = ['nome', 'data_nascimento', 'apelido', 'estado_civil']

    list_display = ('nome',)


admin.site.register(Pessoa, PessoaAdmin)
