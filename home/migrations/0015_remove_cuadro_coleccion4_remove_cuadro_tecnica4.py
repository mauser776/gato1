# Generated by Django 4.2.5 on 2023-10-02 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_cuadro_tecnica'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuadro',
            name='coleccion4',
        ),
        migrations.RemoveField(
            model_name='cuadro',
            name='tecnica4',
        ),
    ]