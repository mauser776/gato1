# Generated by Django 4.2.5 on 2024-06-28 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mercadopago', '0003_alter_mer_cuadro_cantidad_vendida'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mer_cuadro',
            name='cantidad_inicial',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mer_cuadro',
            name='cantidad_vendida',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
