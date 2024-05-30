from django.contrib import admin
from .models import Estado, Municipio, Escola, Curso, Turma, EgressoTurma, EgressoImageContent, TurmaImageContent, TurmaAudioContent 

# Register your models here.
admin.site.register(Estado)
admin.site.register(Municipio)
admin.site.register(Escola)
admin.site.register(Curso)
admin.site.register(Turma)
admin.site.register(EgressoTurma)
admin.site.register(EgressoImageContent)
admin.site.register(TurmaImageContent)
admin.site.register(TurmaAudioContent)
