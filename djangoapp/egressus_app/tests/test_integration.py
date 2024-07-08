from django.test import TestCase
from egressus_app.models import Curso, Estado, Municipio, Escola, Turma, EgressoTurma
from django.contrib.auth import get_user_model

User = get_user_model()

class IntegrationTest(TestCase):
    def setUp(self):
        # Criando os dados necessários
        self.curso = Curso.objects.create(curso="Engenharia")
        self.estado = Estado.objects.create(estado="São Paulo", codigo_estado="SP")
        self.municipio = Municipio.objects.create(municipio="Campinas", estado=self.estado)
        self.escola = Escola.objects.create(nome_escola="Escola Estadual", municipio=self.municipio)
        self.turma = Turma.objects.create(nome_turma="Turma 2024", data_formatura="2024-12-01", curso=self.curso, escola=self.escola)
        self.user = User.objects.create_user(
            email='integrationuser@example.com',
            username='integrationuser',
            password='integrationpass',
            first_name='Integration',
            last_name='User',
            date_of_birth='1990-01-01'
        )

    def test_create_egresso_turma(self):
        # Criando um egresso associado a uma turma
        egresso_turma = EgressoTurma.objects.create(user=self.user, turma=self.turma)
        self.assertIsInstance(egresso_turma, EgressoTurma)
        self.assertEqual(egresso_turma.user, self.user)
        self.assertEqual(egresso_turma.turma, self.turma)
