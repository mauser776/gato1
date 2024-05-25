# Generated by Django 4.2.5 on 2024-05-25 00:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_alter_cuadro_imagen1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuadro',
            name='imagen1',
            field=models.ImageField(default='ejemplos/en_preparacion.jpg', upload_to='cuadros', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])]),
        ),
    ]
