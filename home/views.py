from django.shortcuts import render
from .models import Cuadro
from django.db.models import Q


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


def obras_view(request):
    cuadros = Cuadro.objects.all()

    # Crear un diccionario para organizar los cuadros por técnica
    cuadros_por_tecnica = {}
    for cuadro in cuadros:
        tecnica = cuadro.tecnica
        if tecnica in cuadros_por_tecnica:
            cuadros_por_tecnica[tecnica].append(cuadro)
        else:
            cuadros_por_tecnica[tecnica] = [cuadro]

    # Crear un diccionario para organizar los cuadros por colección
    cuadros_por_coleccion = {}
    for cuadro in cuadros:
        coleccion = cuadro.coleccion
        if coleccion in cuadros_por_coleccion:
            cuadros_por_coleccion[coleccion].append(cuadro)
        else:
            cuadros_por_coleccion[coleccion] = [cuadro]

    cuadros_tec_col = {**cuadros_por_coleccion, **cuadros_por_tecnica}

    context = {
        'cuadros_por_tecnica': cuadros_por_tecnica,
        'cuadros_por_coleccion': cuadros_por_coleccion,
        'cuadros_tec_col': cuadros_tec_col,
    }

    return render(request, 'home/obras.html', context)


def contacto_view(request):
    return render(request, 'home/contacto.html')


def sobre_mi_view(request):
    return render(request, 'home/sobre_mi.html')


def galerias_view(request):
    galeria = request.GET.get('galeria')

    cuadros_filtrados = Cuadro.objects.filter(
        Q(coleccion=galeria) | Q(tecnica=galeria))

    context = {'galeria': galeria,
               'cuadros_filtrados': cuadros_filtrados,
               }

    return render(request, 'home/galerias.html', context)


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
