# Generated by Django 4.2.5 on 2024-06-28 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mercadopago', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mer_cuadro',
            name='cantidad_inicial',
            field=models.PositiveIntegerField(blank=True, editable=False, null=True),
        ),
    ]
