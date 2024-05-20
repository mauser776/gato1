# Generated by Django 4.2.5 on 2024-05-16 19:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_cuadro_marco_con_cuadro_marco_sin'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuadro',
            name='imagen5',
            field=models.ImageField(blank=True, upload_to='cuadros', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])]),
        ),
        migrations.AddField(
            model_name='cuadro',
            name='imagen6',
            field=models.ImageField(blank=True, upload_to='cuadros', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])]),
        ),
    ]