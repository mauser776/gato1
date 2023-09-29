from django.shortcuts import render
from .models import Cuadro


# Create your views here.


def home_view(request):

    cuadros = Cuadro.objects.all()
    lista_cuadros = []
    for x in cuadros:
        lista_cuadros.append(x)

    lista_cuadros.reverse()

    context = {
        'lista_cuadros': lista_cuadros,
    }

    return render(request, 'home/home.html', context)


def proyectos_view(request):
    return render(request, 'home/proyectos.html')


def contacto_view(request):
    return render(request, 'home/contacto.html')


def sobre_mi_view(request):
    return render(request, 'home/sobre_mi.html')


def galeria_view(request, coleccion):

    coleccion_cuadros = Cuadro.objects.get(coleccion=coleccion)

    context = {
        'coleccion_cuadros': coleccion_cuadros,
    }

    return render(request, 'home/galeria.html', context)


def cuadro_detail_view(request, id):

    cuadro = Cuadro.objects.get(id=id)

    cuadro_imagenes = []
    lista_prueba = [cuadro.imagen1, cuadro.imagen2,
                    cuadro.imagen3, cuadro.imagen4]

    for imagen in lista_prueba:
        if imagen:
            cuadro_imagenes.append(imagen)

    context = {
        'cuadro': cuadro,
        'cuadro_imagenes': cuadro_imagenes,
    }

    return render(request, 'home/cuadro.html', context)
