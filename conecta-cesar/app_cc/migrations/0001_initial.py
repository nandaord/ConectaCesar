<<<<<<< HEAD:app_cc/migrations/0001_initial.py
# Generated by Django 5.0.4 on 2024-05-24 18:58
=======
# Generated by Django 5.0.4 on 2024-05-29 20:57
>>>>>>> eff11cadb53bf6d859484ed08b7fdf418d668f18:conecta-cesar/app_cc/migrations/0001_initial.py

import app_cc.models
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
            name='Aviso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('corpo', models.TextField()),
                ('publicado', models.DateTimeField(auto_now_add=True)),
                ('imagem', models.ImageField(null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('ra', models.CharField(default=app_cc.models.generate_unique_ra, max_length=10, unique=True)),
                ('foto_perfil', models.ImageField(blank=True, null=True, upload_to='profile_pictures/')),
                ('usuario', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='aluno', to=settings.AUTH_USER_MODEL)),
                ('turma', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='alunos', to='app_cc.turma')),
            ],
        ),
        migrations.CreateModel(
            name='Diario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, null=True)),
                ('texto', models.TextField()),
                ('data', models.DateField(auto_now_add=True)),
                ('disciplina', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='diarios', to='app_cc.disciplina')),
            ],
        ),
        migrations.CreateModel(
            name='Falta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('justificada', models.BooleanField(default=False)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faltas', to='app_cc.aluno')),
                ('disciplina', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='faltas', to='app_cc.disciplina')),
            ],
        ),
        migrations.CreateModel(
            name='FaltaRelatorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faltas', models.IntegerField(default=0)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_cc.aluno')),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, null=True)),
                ('archive', models.ImageField(upload_to='')),
                ('horas_extras', models.FloatField(default=0)),
                ('aluno', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='arquivos', to='app_cc.aluno')),
            ],
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField(default='0', null=True)),
                ('aluno', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notas', to='app_cc.aluno')),
                ('disciplina', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notas', to='app_cc.disciplina')),
            ],
        ),
        migrations.CreateModel(
            name='NotaRelatorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.FloatField(default=0, null=True)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_cc.aluno')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('ra', models.CharField(default=app_cc.models.generate_unique_ra, max_length=10, unique=True)),
                ('foto_perfil', models.ImageField(blank=True, null=True, upload_to='profile_pictures/')),
                ('usuario', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='professor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descricao', models.TextField(blank=True)),
                ('data', models.DateField()),
                ('horario', models.TimeField(blank=True, null=True)),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_cc.disciplina')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_cc.professor')),
            ],
        ),
        migrations.AddField(
            model_name='disciplina',
            name='professor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='disciplinas', to='app_cc.professor'),
        ),
        migrations.CreateModel(
            name='Relatorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alunos_frequencia_abaixo', models.ManyToManyField(related_name='relatorios_frequencia_abaixo', through='app_cc.FaltaRelatorio', to='app_cc.aluno')),
                ('alunos_nota_abaixo', models.ManyToManyField(related_name='relatorios_nota_abaixo', through='app_cc.NotaRelatorio', to='app_cc.aluno')),
                ('disciplina', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='relatorios', to='app_cc.disciplina')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relatorios', to='app_cc.professor')),
            ],
        ),
        migrations.AddField(
            model_name='notarelatorio',
            name='relatorio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_cc.relatorio'),
        ),
        migrations.AddField(
            model_name='faltarelatorio',
            name='relatorio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_cc.relatorio'),
        ),
        migrations.AddField(
            model_name='disciplina',
            name='turmas',
            field=models.ManyToManyField(related_name='disciplinas', to='app_cc.turma'),
        ),
    ]
