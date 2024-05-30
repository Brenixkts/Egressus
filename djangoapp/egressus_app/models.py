from django.contrib.auth import get_user_model
from django.db import models


class Estado(models.Model):
    id_estado = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=40)
    codigo_estado = models.CharField(max_length=2)

    class Meta:
        managed = True
        db_table = 'estados'
        verbose_name = 'estado'
        verbose_name_plural = 'estados'

    def __str__(self):
        return f'{self.estado} ({self.codigo_estado})'


class Municipio(models.Model):
    id_municipio = models.AutoField(primary_key=True)
    municipio = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='id_estado')

    class Meta:
        managed = True
        db_table = 'municipios'
        verbose_name = 'município'
        verbose_name_plural = 'municípios'

    def __str__(self):
        return self.municipio


class Escola(models.Model):
    id_escola = models.AutoField(primary_key=True)
    nome_escola = models.CharField(max_length=200)
    municipio = models.ForeignKey(Municipio, models.DO_NOTHING, db_column='id_municipio')

    class Meta:
        managed = True
        db_table = 'escolas'
        verbose_name = 'escola'
        verbose_name_plural = 'escolas'

    def __str__(self):
        return self.nome_escola


class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    curso = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'cursos'
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'

    def __str__(self):
        return self.curso


class Turma(models.Model):
    id_turma = models.AutoField(primary_key=True)
    nome_turma = models.CharField(max_length=200, blank=True)
    data_formatura = models.DateField()
    curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='id_curso')
    escola = models.ForeignKey(Escola, models.DO_NOTHING, db_column='id_escola')

    class Meta:
        managed = True
        db_table = 'turmas'
        verbose_name = 'turma'
        verbose_name_plural = 'turmas'

    def __str__(self):
        if self.nome_turma:
            return self.nome_turma
        else:
            return f'Turma {self.id_turma}'


class EgressoTurma(models.Model):
    id_egresso = models.AutoField(primary_key=True)
    user = models.OneToOneField(get_user_model(), models.CASCADE)
    turma = models.ForeignKey(Turma, models.DO_NOTHING, db_column='id_turma')
    representante_de_turma = models.BooleanField(default=False)
    data_nascimento = models.DateField()

    class Meta:
        managed = True
        db_table = 'egresso_turma'
        verbose_name = 'Egresso'
        verbose_name_plural = 'Egressos'

    def __str__(self):
        return f'Egresso {self.user.username} da turma {self.turma}'


class EgressoImageContent(models.Model):
    egresso = models.ForeignKey(EgressoTurma, models.DO_NOTHING, db_column='id_egresso')
    egresso_media_url = models.URLField(unique=True, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'egresso_image_contents'
        verbose_name = 'Conteúdo de Imagem de Egresso'
        verbose_name_plural = 'Conteúdos de Imagem de Egressos'

    def __str__(self):
        return f'Imagem do Egresso {self.egresso}'


class TurmaImageContent(models.Model):
    turma = models.ForeignKey(Turma, models.DO_NOTHING, db_column='id_turma')
    turma_image_url = models.URLField(unique=True, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'turma_image_contents'
        verbose_name = 'Conteúdo de Imagem da Turma'
        verbose_name_plural = 'Conteúdos de Imagem das Turmas'

    def __str__(self):
        return f'Imagem da Turma {self.turma}'


class TurmaAudioContent(models.Model):
    turma = models.ForeignKey(Turma, models.DO_NOTHING, db_column='id_turma')
    turma_audio_url = models.URLField(unique=True, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'turma_audio_contents'
        verbose_name = 'Conteúdo de Áudio da Turma'
        verbose_name_plural = 'Conteúdos de Áudio das Turmas'

    def __str__(self):
        return f'Áudio da Turma {self.turma}'
