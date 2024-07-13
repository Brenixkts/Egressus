# email_notifications/tests/test_models.py
from django.test import TestCase
from django.core.exceptions import ValidationError
from email_notifications.models import Notificacao
from egressus_app.models import Curso
from django.utils import timezone

class NotificacaoModelTest(TestCase):
    def setUp(self):
        self.curso = Curso.objects.create(curso="Engenharia")
        self.notificacao = Notificacao.objects.create(
            titulo="Teste de Notificação",
            mensagem="Essa é uma mensagem de teste",
            tipo_de_mensagem=1,
            curso_alvo=self.curso,
            enviar_para_todos=False
        )

    def test_notificacao_creation(self):
        self.assertIsInstance(self.notificacao, Notificacao)
        self.assertEqual(self.notificacao.titulo, "Teste de Notificação")
        self.assertEqual(self.notificacao.mensagem, "Essa é uma mensagem de teste")
        self.assertEqual(self.notificacao.tipo_de_mensagem, 1)
        self.assertEqual(self.notificacao.curso_alvo, self.curso)
        self.assertFalse(self.notificacao.enviar_para_todos)

    def test_notificacao_str(self):
        self.assertEqual(str(self.notificacao), "Teste de Notificação")

    def test_notificacao_no_curso(self):
        notificacao_sem_curso = Notificacao.objects.create(
            titulo="Teste Sem Curso",
            mensagem="Mensagem sem curso",
            tipo_de_mensagem=2,
            enviar_para_todos=True,
            curso_alvo=None
        )
        self.assertIsInstance(notificacao_sem_curso, Notificacao)
        self.assertEqual(notificacao_sem_curso.titulo, "Teste Sem Curso")
        self.assertEqual(notificacao_sem_curso.mensagem, "Mensagem sem curso")
        self.assertEqual(notificacao_sem_curso.tipo_de_mensagem, 2)
        self.assertTrue(notificacao_sem_curso.enviar_para_todos)
        self.assertIsNone(notificacao_sem_curso.curso_alvo)

    def test_notificacao_enviar_para_todos_false_sem_curso(self):
        notificacao = Notificacao(
            titulo="Teste",
            mensagem="Mensagem de teste",
            tipo_de_mensagem=1,
            enviar_para_todos=False,
            curso_alvo=None
        )
        with self.assertRaises(ValidationError):
            notificacao.save()
