# Generated by Django 4.2.5 on 2023-10-01 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_rename_coleccion_cuadro_coleccion4'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuadro',
            name='coleccion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cuadrosX', to='home.coleccion'),
        ),
    ]
