from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Mer_Cuadro
import random


from django.http import HttpResponse


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
