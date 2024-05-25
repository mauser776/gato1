from django.shortcuts import render
from .models import Coleccion, Cuadro, Tecnica
from django.db.models import Q
import random


# Create your views here.


def home_view(request):

    # colecciones = Coleccion.objects.prefetch_related('coleccionX').all()
    colecciones = Coleccion.objects.prefetch_related(
        'coleccionX').order_by('orden').all()

    tecnicas = Tecnica.objects.prefetch_related('tecnicaX').all()

    cuadros = Cuadro.objects.all()
    lista_cuadros = []
    for x in cuadros:
        lista_cuadros.append(x)
    lista_cuadros.reverse()

    context = {
        'colecciones': colecciones,
        'tecnicas': tecnicas,
        'lista_cuadros': lista_cuadros,
    }

    return render(request, 'home/obras.html', context)

    # return render(request, 'home/home.html', context)


def obras_view(request):

    # colecciones = Coleccion.objects.prefetch_related('coleccionX').all()
    colecciones = Coleccion.objects.prefetch_related(
        'coleccionX').order_by('orden').all()

    tecnicas = Tecnica.objects.prefetch_related('tecnicaX').all()

    context = {
        'colecciones': colecciones,
        'tecnicas': tecnicas,
    }

    return render(request, 'home/obras.html', context)


def galerias_view(request):
    galeria = request.GET.get('galeria')

    if galeria:
        try:
            coleccion = Coleccion.objects.get(nombre=galeria)
            cuadros = Cuadro.objects.filter(coleccion=coleccion)
        except Coleccion.DoesNotExist:
            try:
                tecnica = Tecnica.objects.get(nombre=galeria)
                cuadros = Cuadro.objects.filter(tecnica=tecnica)
            except Tecnica.DoesNotExist:
                cuadros = Cuadro.objects.none()
    else:
        cuadros = Cuadro.objects.none()

    context = {
        'cuadros': cuadros,
        'galeria': galeria,
    }

    return render(request, 'home/galerias.html', context)


def cuadro_view(request, id):
    cuadro = Cuadro.objects.get(id=id)
    cuadros = Cuadro.objects.all()

    coleccion_ordenada = cuadro.coleccion.coleccionX.all().order_by('orden')

# Random
    lista_cuadros = list(cuadros)  # Convertir el queryset a una lista
    random.shuffle(lista_cuadros)  # Aleatorizar la lista

    context = {
        'cuadro': cuadro,
        'lista_cuadros': lista_cuadros,
        'coleccion_ordenada': coleccion_ordenada,
        # 'cuadro_imagenes': cuadro_imagenes,
    }

    return render(request, 'home/cuadro.html', context)


def contacto_view(request):
    return render(request, 'home/contacto.html')


def sobre_mi_view(request):
    return render(request, 'home/sobre_mi.html')
