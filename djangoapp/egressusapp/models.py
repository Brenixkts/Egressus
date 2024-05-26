from django.db import models
from django.contrib.auth.models import User

class Estado(models.Model):
    id_estado = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=40)
    codigo_estado = models.CharField(max_length=2)

    class Meta:
        managed = True
        db_table = 'estados'
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

    def __str__(self):
        return f'{self.estado} ({self.codigo_estado})'


class Municipio(models.Model):
    id_municipio = models.AutoField(primary_key=True)
    municipio = models.CharField(max_length=100)
    id_estado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='id_estado')

    class Meta:
        managed = True
        db_table = 'municipios'
        verbose_name = 'Município'
        verbose_name_plural = 'Municípios'

    def __str__(self):
        return self.municipio


class Escola(models.Model):
    id_escola = models.AutoField(primary_key=True)
    nome_escola = models.CharField(max_length=200)
    id_municipio = models.ForeignKey(Municipio, models.DO_NOTHING, db_column='id_municipio')

    class Meta:
        managed = True
        db_table = 'escolas'
        verbose_name = 'Escola'
        verbose_name_plural = 'Escolas'

    def __str__(self):
        return self.nome_escola


class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    curso = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'cursos'
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.curso


class Turma(models.Model):
    id_turma = models.AutoField(primary_key=True)
    nome_turma = models.CharField(max_length=200, blank=True)
    data_formatura = models.DateField()
    id_curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='id_curso')
    id_escola = models.ForeignKey(Escola, models.DO_NOTHING, db_column='id_escola')

    class Meta:
        managed = True
        db_table = 'turmas'
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'

    def __str__(self):
        if self.nome_turma:
            return self.nome_turma
        else:
            return f'Turma {self.id_turma}'


class EgressoTurma(models.Model):
    id_egresso = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    id_turma = models.ForeignKey(Turma, models.DO_NOTHING, db_column='id_turma')
    is_class_representant = models.BooleanField(default=False)

    class Meta:
        managed = True
        db_table = 'egresso_turmas'
        verbose_name = 'Egresso da Turma'
        verbose_name_plural = 'Egressos da Turma'

    def __str__(self):
        return f'Egresso {self.user.username} da turma {self.id_turma}'


class EgressoImageContent(models.Model):
    id_egresso = models.ForeignKey(EgressoTurma, models.DO_NOTHING, db_column='id_egresso')
    egresso_media_url = models.URLField()

    class Meta:
        managed = True
        db_table = 'egresso_image_contents'
        verbose_name = 'Conteúdo de Imagem do Egresso'
        verbose_name_plural = 'Conteúdos de Imagem do Egresso'

    def __str__(self):
        return f'Imagem do Egresso {self.id_egresso}'


class TurmaImageContent(models.Model):
    id_turma = models.ForeignKey(Turma, models.DO_NOTHING, db_column='id_turma')
    turma_image_url = models.URLField()

    class Meta:
        managed = True
        db_table = 'turma_image_contents'
        verbose_name = 'Conteúdo de Imagem da Turma'
        verbose_name_plural = 'Conteúdos de Imagem das Turma'

    def __str__(self):
        return f'Imagem da Turma {self.id_turma}'


class TurmaAudioContent(models.Model):
    id_turma = models.ForeignKey(Turma, models.DO_NOTHING, db_column='id_turma')
    turma_audio_url = models.URLField()

    class Meta:
        managed = True
        db_table = 'turma_audio_contents'
        verbose_name = 'Conteúdo de Áudio da Turma'
        verbose_name_plural = 'Conteúdos de Áudio da Turma'

    def __str__(self):
        return f'Áudio da Turma {self.id_turma}'
