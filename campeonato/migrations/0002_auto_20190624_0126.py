# Generated by Django 2.2.2 on 2019-06-24 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campeonato', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modalidade',
            old_name='sexo_permitido',
            new_name='sexoPermitido',
        ),
    ]
