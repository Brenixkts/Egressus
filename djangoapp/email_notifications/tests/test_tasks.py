from django.test import TestCase
from django.utils import timezone
from django.core import mail
from unittest.mock import patch
from email_notifications.tasks import enviar_notificacoes_agendadas, enviar_notificacoes_automaticas
from email_notifications.models import Notificacao
from egressus_app.models import EgressoTurma, Curso, Estado, Municipio, Escola, Turma
from account.models import Account
from core import settings


class TestEnvioNotificacoesAgendadas(TestCase):

    def setUp(self):
        self.curso = Curso.objects.create(curso='Curso Teste')
        self.estado = Estado.objects.create(estado="Ceará", codigo_estado="CE")
        self.municipio = Municipio.objects.create(municipio="Maranguape", estado=self.estado)
        self.escola = Escola.objects.create(nome_escola="IFCE campus Maranguape", municipio=self.municipio)
        self.user1 = Account.objects.create_user(cpf='46681423019', email='user1@example.com', username='user1', password='password')
        self.user2 = Account.objects.create_user(cpf='36795730069', email='user2@example.com', username='user2', password='password')
        self.turma = Turma.objects.create(nome_turma='Turma Teste', data_formatura=timezone.now().date(), curso=self.curso, escola=self.escola)
        EgressoTurma.objects.create(user=self.user1, turma=self.turma)
        EgressoTurma.objects.create(user=self.user2, turma=self.turma)
        self.notificacao = Notificacao.objects.create(
            titulo='Título da Notificação',
            mensagem='Mensagem da notificação',
            tipo_de_mensagem=1,
            data_de_postagem=timezone.now(),
            curso_alvo=self.curso,
            enviar_para_todos=False
        )

    @patch('email_notifications.tasks.send_mail')
    def test_enviar_notificacoes_agendadas(self, mock_send_mail):
        # Executa a tarefa que envia notificações agendadas
        enviar_notificacoes_agendadas()

        # Verifica se a função send_mail foi chamada
        self.assertTrue(mock_send_mail.called)
        
        egressos_ids = EgressoTurma.objects.filter(turma__curso=self.notificacao.curso_alvo).values_list('user_id', flat=True)
        destinatarios = [egresso.user.email for egresso in EgressoTurma.objects.filter(user_id__in=egressos_ids)]
        
        # Verifica os parâmetros com que a função send_mail foi chamada        
        mock_send_mail.assert_called_once_with(
            'Título da Notificação',
            'Mensagem da notificação',
            settings.EMAIL_HOST_USER,
            destinatarios  # ['user1@example.com', 'user2@example.com']
        )

        # Verifica se a notificação foi deletada após o envio
        self.assertEqual(Notificacao.objects.filter(id=self.notificacao.id).count(), 0)


class TestEnvioNotificacoesAutomaticas(TestCase):

    def setUp(self):
        self.hoje = timezone.now().date()
        self.estado = Estado.objects.create(estado="Ceará", codigo_estado="CE")
        self.municipio = Municipio.objects.create(municipio="Maranguape", estado=self.estado)
        self.escola = Escola.objects.create(nome_escola="IFCE campus Maranguape", municipio=self.municipio)
        self.curso = Curso.objects.create(curso='Curso Teste')
        self.user1 = Account.objects.create_user(cpf='46681423019', email='user1@example.com', username='user1', password='password', date_of_birth=self.hoje)
        self.user2 = Account.objects.create_user(cpf='36795730069', email='user2@example.com', username='user2', password='password', date_of_birth=self.hoje)
        self.turma = Turma.objects.create(nome_turma='Turma Teste', data_formatura=self.hoje, curso=self.curso, escola=self.escola)
        EgressoTurma.objects.create(user=self.user1, turma=self.turma)
        EgressoTurma.objects.create(user=self.user2, turma=self.turma)

    @patch('email_notifications.tasks.send_mail')
    def test_enviar_notificacoes_automaticas(self, mock_send_mail):
        # Executa a tarefa que envia notificações automáticas
        enviar_notificacoes_automaticas()

        # Verifica se a função send_mail foi chamada
        self.assertTrue(mock_send_mail.called)

        # Verifica os parâmetros com que a função send_mail foi chamada para aniversários de formatura
        mock_send_mail.assert_any_call(
            'Feliz Aniversário de Formatura!',
            f'Parabéns pela formatura! Hoje comemoramos o aniversário de formatura da turma {self.turma.nome_turma}.',
            settings.EMAIL_HOST_USER,
            ['user1@example.com', 'user2@example.com']
        )

        # Verifica os parâmetros com que a função send_mail foi chamada para aniversários pessoais
        mock_send_mail.assert_any_call(
            'Feliz Aniversário!',
            f'Parabéns, {self.user1.get_short_name()}! Desejamos a você um ótimo aniversário!',
            settings.EMAIL_HOST_USER,
            ['user1@example.com']
        )

        mock_send_mail.assert_any_call(
            'Feliz Aniversário!',
            f'Parabéns, {self.user2.get_short_name()}! Desejamos a você um ótimo aniversário!',
            settings.EMAIL_HOST_USER,
            ['user2@example.com']
        )

        # Verifica os parâmetros com que a função send_mail foi chamada para informar os colegas sobre o aniversário
        mock_send_mail.assert_any_call(
            f"Aniversário do colega {self.user1.get_short_name()}",
            f"Hoje é aniversário do {self.user1.get_full_name()}!",
            settings.EMAIL_HOST_USER,
            ['user2@example.com']
        )

        mock_send_mail.assert_any_call(
            f"Aniversário do colega {self.user2.get_short_name()}",
            f"Hoje é aniversário do {self.user2.get_full_name()}!",
            settings.EMAIL_HOST_USER,
            ['user1@example.com']
        )
