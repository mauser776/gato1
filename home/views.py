from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import Coleccion, Cuadro, Tecnica
from django.db.models import Q
import random
from django.core.mail import EmailMessage
from .forms import FormularioContacto

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


def coleccion_view(request):
    coleccion = request.GET.get('coleccion')

    if coleccion:
        try:
            coleccion = Coleccion.objects.get(nombre=coleccion)
            cuadros = Cuadro.objects.filter(coleccion=coleccion)
        except Coleccion.DoesNotExist:
            try:
                tecnica = Tecnica.objects.get(nombre=coleccion)
                cuadros = Cuadro.objects.filter(tecnica=tecnica)
            except Tecnica.DoesNotExist:
                cuadros = Cuadro.objects.none()
    else:
        cuadros = Cuadro.objects.none()

    context = {
        'cuadros': cuadros,
        'coleccion': coleccion,
    }

    return render(request, 'home/coleccion.html', context)


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


def cuadro_detail(request, id):
    cuadro = Cuadro.objects.get(id=id)
    procesar_pago_url = reverse('mercadopago:procesar_pago')
    return render(request, 'home/cuadro_detail.html', {'cuadro': cuadro, 'procesar_pago_url': procesar_pago_url})


def contacto_view(request):
    if request.method == 'POST':
        formulario = FormularioContacto(request.POST)
        if formulario.is_valid():
            nombre = formulario.cleaned_data['nombre']
            correo = formulario.cleaned_data['correo']
            mensaje = formulario.cleaned_data['mensaje']

            # Crea el correo electrónico
            email = EmailMessage(
                subject=f'Mensaje de {nombre}',
                body=mensaje,
                from_email=correo,
                to=['andreshonoratoarte@gmail.com'],
                headers={'Reply-To': correo}
            )
            email.send(fail_silently=False)
            # Redirige a una página de éxito
            return render(request, 'home/sobre_mi.html')
    else:
        formulario = FormularioContacto()

    return render(request, 'home/contacto.html', {'formulario': formulario})


def sobre_mi_view(request):
    return render(request, 'home/sobre_mi.html')
