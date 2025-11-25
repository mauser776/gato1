from django.contrib import admin
from .models import Cuadro, Coleccion, Tecnica, BannerDoble
# Register your models here.

# admin.site.register(Cuadro)
# admin.site.register(Coleccion)
admin.site.register(Tecnica)


@admin.register(Cuadro)
class ColeccionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'coleccion', 'orden', 'fecha', 'id')
    ordering = ('coleccion',)


@admin.register(Coleccion)
class ColeccionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'orden', 'fecha', 'cantidad_cuadros')
    ordering = ('orden',)

@admin.register(BannerDoble)
class BannerDobleAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'coleccion', 'cuadro_1', 'cuadro_2', 'creado')
    search_fields = ('nombre',)