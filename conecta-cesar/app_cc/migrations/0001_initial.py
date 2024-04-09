from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disciplina', models.CharField(max_length=100)),
                ('titulo', models.CharField(max_length=100)),
                ('texto', models.TextField()),
                ('data', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Diários',
                'use_in_migrations': True,  # Defina como True ou False conforme necessário
            },
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disciplina', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Disciplinas',
                'use_in_migrations': True,  # Defina como True ou False conforme necessário
            },
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'use_in_migrations': True,  # Defina como True ou False conforme necessário
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem', models.CharField(max_length=200)),
                ('details', models.TextField()),
                ('created_date', models.DateTimeField(verbose_name='Created on')),
            ],
            options={
                'use_in_migrations': True,  # Defina como True ou False conforme necessário
            },
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.DecimalField(decimal_places=2, max_digits=5)),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_cc.disciplina')),
            ],
            options={
                'verbose_name_plural': 'Notas',
                'use_in_migrations': True,  # Defina como True ou False conforme necessário
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_cc.question')),
            ],
            options={
                'verbose_name_plural': 'Entries',
                'use_in_migrations': True,  # Defina como True ou False conforme necessário
            },
        ),
    ]
