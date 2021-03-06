# Generated by Django 2.2.2 on 2019-06-24 15:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('campeonato', '0003_modalidade_quantidadedevagas'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipe',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='equipe',
            name='participantes',
            field=models.ManyToManyField(related_name='participantes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='equipe',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='equipe',
            name='representante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='representante', to=settings.AUTH_USER_MODEL),
        ),
    ]
