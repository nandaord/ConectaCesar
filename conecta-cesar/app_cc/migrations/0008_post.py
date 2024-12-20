# Generated by Django 5.0.5 on 2024-06-22 23:30

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cc', '0007_review'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('corpo', models.TextField()),
                ('publicado_em', models.DateTimeField(default=django.utils.timezone.now)),
                ('pdf', models.FileField(blank=True, null=True, upload_to='forum_pdfs/')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-publicado_em'],
            },
        ),
    ]
