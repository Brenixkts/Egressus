from django.test import TestCase
from django.contrib.auth import get_user_model
from egressus_app.models import Estado, Municipio, Escola, Curso, Turma, TurmaImageContent, TurmaAudioContent, EgressoTurma, EgressoImageContent

User = get_user_model()

class EstadoModelTest(TestCase):
    def setUp(self):
        self.estado = Estado.objects.create(estado="São Paulo", codigo_estado="SP")

    def test_estado_creation(self):
        self.assertIsInstance(self.estado, Estado)
        self.assertEqual(self.estado.__str__(), "São Paulo (SP)")

class MunicipioModelTest(TestCase):
    def setUp(self):
        self.estado = Estado.objects.create(estado="São Paulo", codigo_estado="SP")
        self.municipio = Municipio.objects.create(municipio="Campinas", estado=self.estado)

    def test_municipio_creation(self):
        self.assertIsInstance(self.municipio, Municipio)
        self.assertEqual(self.municipio.__str__(), "Campinas")

class EscolaModelTest(TestCase):
    def setUp(self):
        self.estado = Estado.objects.create(estado="São Paulo", codigo_estado="SP")
        self.municipio = Municipio.objects.create(municipio="Campinas", estado=self.estado)
        self.escola = Escola.objects.create(nome_escola="Escola Estadual", municipio=self.municipio)

    def test_escola_creation(self):
        self.assertIsInstance(self.escola, Escola)
        self.assertEqual(self.escola.__str__(), "Escola Estadual")

class CursoModelTest(TestCase):
    def setUp(self):
        self.curso = Curso.objects.create(curso="Engenharia")

    def test_curso_creation(self):
        self.assertIsInstance(self.curso, Curso)
        self.assertEqual(self.curso.__str__(), "Engenharia")

class TurmaModelTest(TestCase):
    def setUp(self):
        self.curso = Curso.objects.create(curso="Engenharia")
        self.estado = Estado.objects.create(estado="São Paulo", codigo_estado="SP")
        self.municipio = Municipio.objects.create(municipio="Campinas", estado=self.estado)
        self.escola = Escola.objects.create(nome_escola="Escola Estadual", municipio=self.municipio)
        self.turma = Turma.objects.create(nome_turma="Turma 2024", data_formatura="2024-12-01", curso=self.curso, escola=self.escola)

    def test_turma_creation(self):
        self.assertIsInstance(self.turma, Turma)
        self.assertEqual(self.turma.__str__(), "Turma 2024")

class TurmaImageContentModelTest(TestCase):
    def setUp(self):
        self.curso = Curso.objects.create(curso="Engenharia")
        self.estado = Estado.objects.create(estado="São Paulo", codigo_estado="SP")
        self.municipio = Municipio.objects.create(municipio="Campinas", estado=self.estado)
        self.escola = Escola.objects.create(nome_escola="Escola Estadual", municipio=self.municipio)
        self.turma = Turma.objects.create(nome_turma="Turma 2024", data_formatura="2024-12-01", curso=self.curso, escola=self.escola)
        self.turma_image_content = TurmaImageContent.objects.create(turma=self.turma, turma_image_url="http://example.com/image.jpg")

    def test_turma_image_content_creation(self):
        self.assertIsInstance(self.turma_image_content, TurmaImageContent)
        self.assertEqual(self.turma_image_content.__str__(), f"Imagem da Turma {self.turma_image_content.turma}")

class TurmaAudioContentModelTest(TestCase):
    def setUp(self):
        self.curso = Curso.objects.create(curso="Engenharia")
        self.estado = Estado.objects.create(estado="São Paulo", codigo_estado="SP")
        self.municipio = Municipio.objects.create(municipio="Campinas", estado=self.estado)
        self.escola = Escola.objects.create(nome_escola="Escola Estadual", municipio=self.municipio)
        self.turma = Turma.objects.create(nome_turma="Turma 2024", data_formatura="2024-12-01", curso=self.curso, escola=self.escola)
        self.turma_audio_content = TurmaAudioContent.objects.create(turma=self.turma, turma_audio_url="http://example.com/audio.mp3")

    def test_turma_audio_content_creation(self):
        self.assertIsInstance(self.turma_audio_content, TurmaAudioContent)
        self.assertEqual(self.turma_audio_content.__str__(), f"Áudio da Turma {self.turma_audio_content.turma}")

class EgressoTurmaModelTest(TestCase):
    def setUp(self):
        self.curso = Curso.objects.create(curso="Engenharia")
        self.estado = Estado.objects.create(estado="São Paulo", codigo_estado="SP")
        self.municipio = Municipio.objects.create(municipio="Campinas", estado=self.estado)
        self.escola = Escola.objects.create(nome_escola="Escola Estadual", municipio=self.municipio)
        self.turma = Turma.objects.create(nome_turma="Turma 2024", data_formatura="2024-12-01", curso=self.curso, escola=self.escola)
        self.user = User.objects.create_user(
            cpf='46681423019',
            email='testuser@example.com',
            username='testuser',
            password='password123',
            first_name='Test',
            last_name='User',
            date_of_birth='1990-01-01'
        )
        self.egresso_turma = EgressoTurma.objects.create(user=self.user, turma=self.turma)

    def test_egresso_turma_creation(self):
        self.assertIsInstance(self.egresso_turma, EgressoTurma)
        self.assertEqual(self.egresso_turma.__str__(), f"Egresso {self.egresso_turma.user} da turma {self.egresso_turma.turma}")

class EgressoImageContentModelTest(TestCase):
    def setUp(self):
        self.curso = Curso.objects.create(curso="Engenharia")
        self.estado = Estado.objects.create(estado="São Paulo", codigo_estado="SP")
        self.municipio = Municipio.objects.create(municipio="Campinas", estado=self.estado)
        self.escola = Escola.objects.create(nome_escola="Escola Estadual", municipio=self.municipio)
        self.turma = Turma.objects.create(nome_turma="Turma 2024", data_formatura="2024-12-01", curso=self.curso, escola=self.escola)
        self.user = User.objects.create_user(
            cpf='46681423019',
            email='testuser@example.com',
            username='testuser',
            password='password123',
            first_name='Test',
            last_name='User',
            date_of_birth='1990-01-01'
        )
        self.egresso_turma = EgressoTurma.objects.create(user=self.user, turma=self.turma)
        self.egresso_image_content = EgressoImageContent.objects.create(egresso=self.egresso_turma, egresso_image_url="http://example.com/egresso.jpg")

    def test_egresso_image_content_creation(self):
        self.assertIsInstance(self.egresso_image_content, EgressoImageContent)
        self.assertEqual(self.egresso_image_content.__str__(), f"Imagem do Egresso {self.egresso_image_content.egresso}")
