from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.

class Cuadro(models.Model):
    nombre = models.CharField(max_length=200)
    autor =  models.CharField(default="Andrés Honorato", max_length=200)
    coleccion = models.CharField(max_length=200)
    tecnica = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    fecha = models.DateField()
    colores = models.CharField(max_length=200, blank=True)
    cantidad_inicial = models.PositiveIntegerField(blank=True, null=True)
    cantidad_vendida = models.PositiveIntegerField(blank=True, null=True)
    dimension1 = models.CharField(max_length=100, blank=True)
    dimension2 = models.CharField(max_length=100, blank=True)
    dimension3 = models.CharField(max_length=100, blank=True)
    marco1 = models.PositiveIntegerField(blank=True, null=True)
    marco2 = models.PositiveIntegerField(blank=True, null=True)
    marco3 = models.PositiveIntegerField(blank=True, null=True)
    precio1 = models.PositiveIntegerField(blank=True, null=True)
    precio2 = models.PositiveIntegerField(blank=True, null=True)
    precio3 = models.PositiveIntegerField(blank=True, null=True)
    descuento = models.PositiveIntegerField(blank=True, null=True)
    envio1 = models.PositiveIntegerField(blank=True, null=True)
    envio2 = models.PositiveIntegerField(blank=True, null=True)
    envio3 = models.PositiveIntegerField(blank=True, null=True)
    imagen1 = models.ImageField(upload_to='cuadros', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    imagen2 = models.ImageField(upload_to='cuadros', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])], blank=True)
    imagen3 = models.ImageField(upload_to='cuadros', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])], blank=True)
    imagen4 = models.ImageField(upload_to='cuadros', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])], blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    actulizado = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f"{self.nombre} - {self.coleccion}"