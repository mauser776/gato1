# Generated by Django 4.2.5 on 2024-05-24 23:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_coleccion_orden'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuadro',
            name='imagen1',
            field=models.ImageField(default='static\\ejemplos\\en_preparacion.jpg', upload_to='cuadros', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])]),
        ),
    ]
