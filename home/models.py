from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.


class Coleccion(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    fecha = models.DateField()
    creado = models.DateTimeField(auto_now_add=True)
    actulizado = models.DateTimeField(auto_now=True)
    orden = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre}"

    @property
    def cantidad_cuadros(self):
        return self.coleccionX.count()


class Tecnica(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    fecha = models.DateField()
    creado = models.DateTimeField(auto_now_add=True)
    actulizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre}"


class Cuadro(models.Model):
    nombre = models.CharField(max_length=200)
    autor = models.CharField(default="Andrés Honorato", max_length=200)
    coleccion = models.ForeignKey(
        Coleccion, on_delete=models.CASCADE, related_name='coleccionX', blank=True, null=True)
    tecnica = models.ForeignKey(
        Tecnica, on_delete=models.CASCADE, related_name='tecnicaX', blank=True, null=True)
    descripcion = models.TextField(blank=True)
    fecha = models.DateField()
    colores = models.CharField(max_length=200, blank=True)
    cantidad_inicial = models.PositiveIntegerField(blank=True, null=True)
    cantidad_vendida = models.PositiveIntegerField(blank=True, null=True)
    marco_sin = models.CharField(max_length=100, blank=True)
    marco_con = models.CharField(max_length=100, blank=True)
    precio_sin = models.PositiveIntegerField(blank=True, null=True)
    precio_con = models.PositiveIntegerField(blank=True, null=True)
    descuento = models.PositiveIntegerField(blank=True, null=True)
    envio1 = models.PositiveIntegerField(blank=True, null=True)
    envio2 = models.PositiveIntegerField(blank=True, null=True)
    orden = models.PositiveIntegerField(blank=True, null=True)
    vendido = models.BooleanField(default=False)

    imagen1 = models.ImageField(default='cuadros/en_preparacion.jpg', upload_to='cuadros', validators=[FileExtensionValidator(
        ['png', 'jpg', 'jpeg'])])
    imagen2 = models.ImageField(upload_to='cuadros', validators=[
                                FileExtensionValidator(['png', 'jpg', 'jpeg'])], blank=True)
    imagen3 = models.ImageField(upload_to='cuadros', validators=[
                                FileExtensionValidator(['png', 'jpg', 'jpeg'])], blank=True)
    imagen4 = models.ImageField(upload_to='cuadros', validators=[
                                FileExtensionValidator(['png', 'jpg', 'jpeg'])], blank=True)
    imagen5 = models.ImageField(upload_to='cuadros', validators=[
                                FileExtensionValidator(['png', 'jpg', 'jpeg'])], blank=True)
    imagen6 = models.ImageField(upload_to='cuadros', validators=[
                                FileExtensionValidator(['png', 'jpg', 'jpeg'])], blank=True)
    imagen7 = models.ImageField(upload_to='cuadros', validators=[
                                FileExtensionValidator(['png', 'jpg', 'jpeg'])], blank=True)
    imagen8 = models.ImageField(upload_to='cuadros', validators=[
                                FileExtensionValidator(['png', 'jpg', 'jpeg'])], blank=True)
    imagen9 = models.ImageField(upload_to='cuadros', validators=[
                                FileExtensionValidator(['png', 'jpg', 'jpeg'])], blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    actulizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre}"

    def cuadros_disponibles(self):
        if self.cantidad_inicial:
            cuadros_disponibles = self.cantidad_inicial - self.cantidad_vendida
            return cuadros_disponibles

    def delete(self, *args, **kwargs):
        for field_name in ['imagen1', 'imagen2', 'imagen3', 'imagen4', 'imagen5', 'imagen6', 'imagen7', 'imagen8', 'imagen9']:
            image_field = getattr(self, field_name)
            if image_field:
                image_field.delete()
        super().delete(*args, **kwargs)

    def get_coleccion(self):
        return self.coleccion_set.all()

    @property
    def precio_punto_sin(self):
        if self.precio_sin is not None:
            coma = f"{self.precio_sin:,}"
            punto = coma.replace(',', '.')
            return punto
        else:
            return "Pendiente"

    @property
    def precio_punto_con(self):
        if self.precio_con is not None:
            coma = f"{self.precio_con:,}"
            punto = coma.replace(',', '.')
            return punto
        else:
            return "Pendiente"
