# Generated by Django 4.2.5 on 2024-05-24 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_cuadro_imagen7_cuadro_imagen8_cuadro_imagen9'),
    ]

    operations = [
        migrations.AddField(
            model_name='coleccion',
            name='orden',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
