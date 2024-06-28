# Generated by Django 4.2.5 on 2024-06-28 17:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mer_Coleccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField(blank=True)),
                ('fecha', models.DateField()),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actulizado', models.DateTimeField(auto_now=True)),
                ('orden', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mer_Tecnica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField(blank=True)),
                ('fecha', models.DateField()),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actulizado', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mer_Cuadro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('autor', models.CharField(default='Andrés Honorato', max_length=200)),
                ('descripcion', models.TextField(blank=True)),
                ('fecha', models.DateField()),
                ('colores', models.CharField(blank=True, max_length=200)),
                ('cantidad_inicial', models.PositiveIntegerField(blank=True, null=True)),
                ('cantidad_vendida', models.PositiveIntegerField(blank=True, null=True)),
                ('marco_sin', models.CharField(blank=True, max_length=100)),
                ('marco_con', models.CharField(blank=True, max_length=100)),
                ('precio_sin', models.PositiveIntegerField(blank=True, null=True)),
                ('precio_con', models.PositiveIntegerField(blank=True, null=True)),
                ('descuento', models.PositiveIntegerField(blank=True, null=True)),
                ('envio1', models.PositiveIntegerField(blank=True, null=True)),
                ('envio2', models.PositiveIntegerField(blank=True, null=True)),
                ('orden', models.PositiveIntegerField(blank=True, null=True)),
                ('vendido', models.BooleanField(default=False)),
                ('imagen1', models.ImageField(default='cuadros/en_preparacion.jpg', upload_to='cuadros', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])])),
                ('imagen2', models.ImageField(blank=True, upload_to='cuadros', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])])),
                ('imagen3', models.ImageField(blank=True, upload_to='cuadros', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])])),
                ('imagen4', models.ImageField(blank=True, upload_to='cuadros', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])])),
                ('imagen5', models.ImageField(blank=True, upload_to='cuadros', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])])),
                ('imagen6', models.ImageField(blank=True, upload_to='cuadros', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])])),
                ('imagen7', models.ImageField(blank=True, upload_to='cuadros', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])])),
                ('imagen8', models.ImageField(blank=True, upload_to='cuadros', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])])),
                ('imagen9', models.ImageField(blank=True, upload_to='cuadros', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])])),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actulizado', models.DateTimeField(auto_now=True)),
                ('coleccion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='coleccionX', to='mercadopago.mer_coleccion')),
                ('tecnica', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tecnicaX', to='mercadopago.mer_tecnica')),
            ],
        ),
    ]