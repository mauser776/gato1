# Generated by Django 4.2.5 on 2024-05-14 01:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_remove_cuadro_coleccion4_remove_cuadro_tecnica4'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuadro',
            name='marco1',
        ),
        migrations.RemoveField(
            model_name='cuadro',
            name='marco2',
        ),
        migrations.RemoveField(
            model_name='cuadro',
            name='marco3',
        ),
    ]
