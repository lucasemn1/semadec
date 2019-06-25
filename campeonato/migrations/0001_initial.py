# Generated by Django 2.2.2 on 2019-06-22 01:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Modalidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('sexo_permitido', models.CharField(max_length=11)),
            ],
            options={
                'verbose_name': 'modalidade',
                'verbose_name_plural': 'modalidades',
            },
        ),
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, unique=True)),
                ('representacao', models.CharField(max_length=50)),
                ('modalidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campeonato.Modalidade')),
                ('representante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'equipe',
                'verbose_name_plural': 'equipes',
            },
        ),
    ]
