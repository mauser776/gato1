from django.shortcuts import render, redirect
from django.urls import reverse
from home.models import Cuadro


from django.http import HttpResponse


def mercadopago_view(request):
    return HttpResponse("¡Bienvenido a la integración de MercadoPago!")


def procesar_pago(request):
    if request.method == 'POST':
        cuadro_id = request.POST.get('cuadro_id')
        cantidad = request.POST.get('cantidad')
        # Lógica para procesar el pago y redireccionar a MercadoLibre
        # Aquí deberías hacer la integración con la API de MercadoLibre
        # Una vez procesado el pago, redirecciona al usuario a una página de confirmación
        cuadro = Cuadro.objects.get(id=cuadro_id)
        return redirect('home:confirmacion_pago', id=cuadro.id)
    else:
        # Redirige a la página de inicio si no se envía un formulario POST
        return redirect('home:inicio')


def confirmacion_pago(request):
    # Página de confirmación de pago
    return render(request, 'mercadopago/confirmacion_pago.html')
