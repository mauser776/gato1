from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Mer_Cuadro
import random
import mercadopago


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


def pagar_cuadro(request, cuadro_id):
    cuadro = get_object_or_404(Mer_Cuadro, id=cuadro_id)

    # Generar la preferencia de MercadoPago
    init_point = cuadro.pagar_con_mercadopago()

    # Redirigir al usuario a la página de MercadoPago
    return redirect(init_point)


def pago_exitoso(request):
    # Aquí procesamos el pago exitoso después de que MercadoPago redirige al usuario
    # Podemos obtener el ID del pago o cualquier parámetro que necesitemos para actualizar el estado del cuadro

    # Por ejemplo, si el pago es exitoso, actualizamos la cantidad disponible y vendida del cuadro
    # Esto dependerá de cómo MercadoPago devuelve el ID o la información necesaria
    cuadro_id = request.GET.get('id')
    cuadro = get_object_or_404(Mer_Cuadro, id=cuadro_id)

    if cuadro.cantidad_disponible > 0:
        cuadro.cantidad_disponible -= 1
        cuadro.cantidad_vendida += 1
        cuadro.save()
        messages.success(
            request, 'Pago exitoso. Se ha actualizado la disponibilidad del cuadro.')
    else:
        messages.warning(request, 'El cuadro ya no está disponible.')

    return render(request, 'pago_exitoso.html')


def pago_fallido(request):
    return render(request, 'pago_fallido.html')


def pago_pendiente(request):
    return render(request, 'pago_pendiente.html')
