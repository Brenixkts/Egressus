from django.db import models
from django.core.exceptions import ValidationError
from egressus_app.models import Curso
from django.utils import timezone

TIPO_DE_MENSAGEM_CHOICES = [
    (1, 'Vagas de Emprego'),
    (2, 'Eventos'),
]

class Notificacao(models.Model):
    titulo = models.CharField(max_length=255)
    mensagem = models.TextField()
    tipo_de_mensagem = models.IntegerField(choices=TIPO_DE_MENSAGEM_CHOICES)
    data_de_postagem = models.DateTimeField(default=timezone.now)
    curso_alvo = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True, blank=True, db_column='id_curso')
    enviar_para_todos = models.BooleanField(default=False)

    class Meta:
        managed = True
        verbose_name = 'Notificação'
        verbose_name_plural = 'Notificações'

    def clean(self):
        if not self.enviar_para_todos and self.curso_alvo is None:
            raise ValidationError('Você deve selecionar um curso alvo se "enviar_para_todos" estiver desmarcado.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.titulo