# Generated by Django 4.2.5 on 2023-10-02 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_rename_tecnica_cuadro_tecnica4'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tecnica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField(blank=True)),
                ('fecha', models.DateField()),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actulizado', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='cuadro',
            name='tecnica',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tecnicasX', to='home.tecnica'),
        ),
    ]
