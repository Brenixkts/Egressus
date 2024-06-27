# Generated by Django 5.0.6 on 2024-06-27 03:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id_curso', models.AutoField(primary_key=True, serialize=False)),
                ('curso', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'curso',
                'verbose_name_plural': 'cursos',
                'db_table': 'cursos',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id_estado', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(max_length=40)),
                ('codigo_estado', models.CharField(max_length=2)),
            ],
            options={
                'verbose_name': 'estado',
                'verbose_name_plural': 'estados',
                'db_table': 'estados',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EgressoTurma',
            fields=[
                ('id_egresso', models.AutoField(primary_key=True, serialize=False)),
                ('representante_de_turma', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Egresso',
                'verbose_name_plural': 'Egressos',
                'db_table': 'egresso_turma',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EgressoImageContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('egresso_image_url', models.URLField(blank=True, null=True, unique=True)),
                ('egresso', models.ForeignKey(db_column='id_egresso', on_delete=django.db.models.deletion.DO_NOTHING, to='egressus_app.egressoturma')),
            ],
            options={
                'verbose_name': 'Conteúdo de Imagem de Egresso',
                'verbose_name_plural': 'Conteúdos de Imagem de Egressos',
                'db_table': 'egresso_image_contents',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id_municipio', models.AutoField(primary_key=True, serialize=False)),
                ('municipio', models.CharField(max_length=100)),
                ('estado', models.ForeignKey(db_column='id_estado', on_delete=django.db.models.deletion.DO_NOTHING, to='egressus_app.estado')),
            ],
            options={
                'verbose_name': 'município',
                'verbose_name_plural': 'municípios',
                'db_table': 'municipios',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Escola',
            fields=[
                ('id_escola', models.AutoField(primary_key=True, serialize=False)),
                ('nome_escola', models.CharField(max_length=200)),
                ('municipio', models.ForeignKey(db_column='id_municipio', on_delete=django.db.models.deletion.DO_NOTHING, to='egressus_app.municipio')),
            ],
            options={
                'verbose_name': 'escola',
                'verbose_name_plural': 'escolas',
                'db_table': 'escolas',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id_turma', models.AutoField(primary_key=True, serialize=False)),
                ('nome_turma', models.CharField(blank=True, max_length=200)),
                ('data_formatura', models.DateField()),
                ('curso', models.ForeignKey(db_column='id_curso', on_delete=django.db.models.deletion.DO_NOTHING, to='egressus_app.curso')),
                ('escola', models.ForeignKey(db_column='id_escola', on_delete=django.db.models.deletion.DO_NOTHING, to='egressus_app.escola')),
            ],
            options={
                'verbose_name': 'turma',
                'verbose_name_plural': 'turmas',
                'db_table': 'turmas',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='egressoturma',
            name='turma',
            field=models.ForeignKey(db_column='id_turma', on_delete=django.db.models.deletion.DO_NOTHING, to='egressus_app.turma'),
        ),
        migrations.CreateModel(
            name='TurmaAudioContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turma_audio_url', models.URLField(blank=True, null=True, unique=True)),
                ('turma', models.ForeignKey(db_column='id_turma', on_delete=django.db.models.deletion.DO_NOTHING, to='egressus_app.turma')),
            ],
            options={
                'verbose_name': 'Conteúdo de Áudio da Turma',
                'verbose_name_plural': 'Conteúdos de Áudio das Turmas',
                'db_table': 'turma_audio_contents',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TurmaImageContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turma_image_url', models.URLField(blank=True, null=True, unique=True)),
                ('turma', models.ForeignKey(db_column='id_turma', on_delete=django.db.models.deletion.DO_NOTHING, to='egressus_app.turma')),
            ],
            options={
                'verbose_name': 'Conteúdo de Imagem da Turma',
                'verbose_name_plural': 'Conteúdos de Imagem das Turmas',
                'db_table': 'turma_image_contents',
                'managed': True,
            },
        ),
    ]
