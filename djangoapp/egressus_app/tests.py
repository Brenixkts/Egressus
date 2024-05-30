from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Estado, Municipio, Escola, Curso, Turma, EgressoTurma, EgressoImageContent, TurmaImageContent, TurmaAudioContent
from datetime import date

class ModelsSetUpTests(TestCase):

    @classmethod
    def setUp(self):
        # Criando um usuário para o Egresso
        self.user1 = get_user_model().objects.create_user(username='João', password='joaotest')
        self.user2 = get_user_model().objects.create_user(username='Vitor', password='vitortest')

        # Criando dados de Estado
        self.estado = Estado.objects.create(estado='Ceará', codigo_estado='CE')

        # Criando dados de Município
        self.municipio = Municipio.objects.create(municipio='Maranguape', estado=self.estado)

        # Criando dados de Escola
        self.escola = Escola.objects.create(nome_escola='IFCE Campus Maranguape', municipio=self.municipio)

        # Criando dados de Curso
        self.curso = Curso.objects.create(curso='Técnico Integrado em Informática')

        # Criando dados de Turma
        ## Turma com nome
        self.turma1 = Turma.objects.create(nome_turma='Turma 1', data_formatura=date(2022, 12, 31), curso=self.curso, escola=self.escola)
        ## Turma sem nome
        self.turma2 = Turma.objects.create(data_formatura=date(2023, 12, 31), curso=self.curso, escola=self.escola)

        # Criando dados de EgressoTurma
        self.egresso_turma1 = EgressoTurma.objects.create(user=self.user1, turma=self.turma1, data_nascimento=date(2005, 1, 14), representante_de_turma=True)
        self.egresso_turma2 = EgressoTurma.objects.create(user=self.user2, turma=self.turma2, data_nascimento=date(2006, 1, 14), representante_de_turma=False)

        # Criando dados de EgressoImageContent
        self.egresso_image_content1 = EgressoImageContent.objects.create(egresso=self.egresso_turma1, egresso_media_url='http://example.com/egresso_image1.jpg')
        self.egresso_image_content2 = EgressoImageContent.objects.create(egresso=self.egresso_turma2, egresso_media_url='http://example.com/egresso_image2.jpg')

        # Criando dados de TurmaImageContent
        self.turma_image_content1 = TurmaImageContent.objects.create(turma=self.turma1, turma_image_url='http://example.com/turma_image1.jpg')
        self.turma_image_content2 = TurmaImageContent.objects.create(turma=self.turma2, turma_image_url='http://example.com/turma_image2.jpg')

        # Criando dados de TurmaAudioContent
        self.turma_audio_content1 = TurmaAudioContent.objects.create(turma=self.turma1, turma_audio_url='http://example.com/turma_audio1.mp3')
        self.turma_audio_content2 = TurmaAudioContent.objects.create(turma=self.turma2, turma_audio_url='http://example.com/turma_audio2.mp3')

    def test_models_instancias_count(self):
        # Verificar se os objetos foram criados corretamente
        self.assertEqual(Estado.objects.count(), 1)
        self.assertEqual(Municipio.objects.count(), 1)
        self.assertEqual(Escola.objects.count(), 1)
        self.assertEqual(Curso.objects.count(), 1)
        self.assertEqual(Turma.objects.count(), 2)
        self.assertEqual(EgressoTurma.objects.count(), 2)
        self.assertEqual(EgressoImageContent.objects.count(), 2)
        self.assertEqual(TurmaImageContent.objects.count(), 2)
        self.assertEqual(TurmaAudioContent.objects.count(), 2)

    def test_models_concordancia_dos_dados(self):
        # Verificar os valores dos objetos criados
        self.assertEqual(self.estado.estado, 'Ceará')
        self.assertEqual(self.municipio.municipio, 'Maranguape')
        self.assertEqual(self.escola.nome_escola, 'IFCE Campus Maranguape')
        self.assertEqual(self.curso.curso, 'Técnico Integrado em Informática')
        self.assertEqual(self.turma1.nome_turma, 'Turma 1')
        self.assertEqual(self.turma2.nome_turma, '')
        self.assertEqual(self.egresso_turma1.user.username, 'João')
        self.assertEqual(self.egresso_turma2.user.username, 'Vitor')
        self.assertTrue(self.egresso_turma1.representante_de_turma)
        self.assertFalse(self.egresso_turma2.representante_de_turma)
        self.assertEqual(self.egresso_image_content1.egresso_media_url, 'http://example.com/egresso_image1.jpg')
        self.assertEqual(self.egresso_image_content2.egresso_media_url, 'http://example.com/egresso_image2.jpg')
        self.assertEqual(self.turma_image_content1.turma_image_url, 'http://example.com/turma_image1.jpg')
        self.assertEqual(self.turma_image_content2.turma_image_url, 'http://example.com/turma_image2.jpg')
        self.assertEqual(self.turma_audio_content1.turma_audio_url, 'http://example.com/turma_audio1.mp3')
        self.assertEqual(self.turma_audio_content2.turma_audio_url, 'http://example.com/turma_audio2.mp3')

    def test_login(self):
        pass