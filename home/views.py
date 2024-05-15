from django.shortcuts import render
from .models import Coleccion, Cuadro, Tecnica
from django.db.models import Q


# Create your views here.


def home_view(request):
    cuadros = Cuadro.objects.all()
    lista_cuadros = []
    for x in cuadros:
        lista_cuadros.append(x)

    lista_cuadros.reverse()

    colecciones = Coleccion.objects.prefetch_related('coleccionX').all()
    tecnicas = Tecnica.objects.prefetch_related('tecnicaX').all()

    context = {
        'colecciones': colecciones,
        'tecnicas': tecnicas,
        'lista_cuadros': lista_cuadros,
    }

    return render(request, 'home/obras.html', context)

    # return render(request, 'home/home.html', context)


def obras_view(request):

    colecciones = Coleccion.objects.prefetch_related('coleccionX').all()
    tecnicas = Tecnica.objects.prefetch_related('tecnicaX').all()

    context = {
        'colecciones': colecciones,
        'tecnicas': tecnicas,
    }

    return render(request, 'home/obras.html', context)

    # context = {
    #     'cuadros_por_tecnica': cuadros_por_tecnica,
    #     'cuadros_por_coleccion': cuadros_por_coleccion,
    # }
#


def contacto_view(request):
    return render(request, 'home/contacto.html')


def sobre_mi_view(request):
    return render(request, 'home/sobre_mi.html')


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
