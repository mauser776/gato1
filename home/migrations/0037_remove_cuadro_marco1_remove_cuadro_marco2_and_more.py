# Generated by Django 4.2.5 on 2024-12-04 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0036_cuadro_marco1_cuadro_marco2_cuadro_marco3_and_more'),
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
        migrations.RemoveField(
            model_name='cuadro',
            name='marco4',
        ),
        migrations.RemoveField(
            model_name='cuadro',
            name='marco5',
        ),
    ]
