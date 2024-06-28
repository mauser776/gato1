from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Mer_Cuadro
import random


def mercadopago_view(request):
    return HttpResponse("¡Bienvenido a la integración de MercadoPago!")


def cuadro_view_pago(request, id):
    cuadro = get_object_or_404(Mer_Cuadro, id=id)
    cuadros = Mer_Cuadro.objects.all()

    coleccion_ordenada = cuadro.coleccion.coleccionX.all().order_by('orden')

    # Random
    lista_cuadros = list(cuadros.exclude(id=id))
    random.shuffle(lista_cuadros)

    context = {
        'cuadro': cuadro,
        'lista_cuadros': lista_cuadros,
        'coleccion_ordenada': coleccion_ordenada,
    }

    return render(request, 'mercadopago/mer_cuadro.html', context)


def comprar_cuadro(request, id):
    cuadro = get_object_or_404(Mer_Cuadro, id=id)
    if request.method == 'POST':
        if cuadro.cantidad_inicial and cuadro.cantidad_vendida < cuadro.cantidad_inicial:
            cuadro.cantidad_vendida += 1
            cuadro.save()
            return redirect('mercadopago:cuadro-view', id=cuadro.id)
        else:
            return HttpResponse("No hay más cuadros disponibles")
    return redirect('mercadopago:cuadro-view', id=cuadro.id)
