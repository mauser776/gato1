# Generated by Django 4.2.5 on 2024-06-28 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mercadopago', '0002_alter_mer_cuadro_cantidad_inicial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mer_cuadro',
            name='cantidad_vendida',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
    ]
