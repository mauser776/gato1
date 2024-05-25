from django.contrib import admin
from .models import Cuadro, Coleccion, Tecnica
# Register your models here.

# admin.site.register(Cuadro)
# admin.site.register(Coleccion)
admin.site.register(Tecnica)


@admin.register(Cuadro)
class ColeccionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'coleccion', 'orden', 'fecha')
    ordering = ('coleccion',)


@admin.register(Coleccion)
class ColeccionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'orden', 'fecha', 'cantidad_cuadros')
    ordering = ('orden',)
