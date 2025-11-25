from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import Coleccion, Cuadro, Tecnica, BannerDoble
import random
from django.core.mail import EmailMessage
from .forms import FormularioContacto
import re

# Create your views here.


def home_view(request):


# --- LÓGICA PARA DETECTAR MÓVIL ---
    user_agent = request.META.get('HTTP_USER_AGENT', '').lower()
    mobile_agents = r'mobile|android|webos|iphone|ipad|ipod|blackberry|iemobile|opera mini'
    
    if re.search(mobile_agents, user_agent):
        # 1. Es dispositivo móvil: mostramos el carrusel de banners exclusivo
        try:
            # Filtramos los banners que pertenecen a la colección con nombre 'Mobile1'
            banners = BannerDoble.objects.filter(coleccion__nombre='Mobile1').order_by('creado')
        except Exception:
            # En caso de que el modelo BannerDoble o Coleccion no existan
            banners = [] 
            
        context = {
            'banners': banners,
        }
        # Renderizamos el nuevo template sin nav ni footer
        return render(request, 'home/home_mobile.html', context) # <-- Nuevo Home Móvil
    
    else:
        # 2. Es escritorio: (Tu lógica original para el home de escritorio)
        colecciones = Coleccion.objects.prefetch_related(
            'coleccionX').order_by('orden').all()
        tecnicas = Tecnica.objects.prefetch_related('tecnicaX').all()
        
        cuadros = Cuadro.objects.all()
        lista_cuadros = []
        for x in cuadros:
            lista_cuadros.append(x)
        lista_cuadros.reverse()
        
        expo = Cuadro.objects.filter(
            id__in=[49, 48, 46, 27, 30, 28, 51, 31, 47, 1, 43, 44, 50, 45, 53, 41, 1])

        context = {
            'colecciones': colecciones,
            'tecnicas': tecnicas,
            'lista_cuadros': lista_cuadros,
            'expo': expo,
        }
        # Renderizamos el template de escritorio
        return render(request, 'home/obras.html', context)


def obras_view(request):

    # colecciones = Coleccion.objects.prefetch_related('coleccionX').all()
    colecciones = Coleccion.objects.prefetch_related(
        'coleccionX').order_by('orden').all()

    tecnicas = Tecnica.objects.prefetch_related('tecnicaX').all()

    expo = Cuadro.objects.filter(
        id__in=[49, 48, 46, 27, 30, 28, 51, 31, 47, 1, 43, 44, 50, 45, 53, 41, 1])

    context = {
        'colecciones': colecciones,
        'tecnicas': tecnicas,
        'expo': expo,
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
    # Convertir el queryset a una lista
    lista_cuadros = list(cuadros.exclude(id=id))
    random.shuffle(lista_cuadros)  # Aleatorizar la lista

    context = {
        'cuadro': cuadro,
        'lista_cuadros': lista_cuadros,
        'coleccion_ordenada': coleccion_ordenada,
        # 'cuadro_imagenes': cuadro_imagenes,
    }

    return render(request, 'home/cuadro.html', context)
    # return render(request, 'home/cuadro_marcos.html', context)


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


def coleccion_view_expo(request):

    cuadros = Cuadro.objects.filter(
        id__in=[49, 48, 46, 27, 30, 28, 51, 31, 47, 1, 43, 44, 50, 45, 53, 41, 1])

    context = {
        'cuadros': cuadros,
    }

    return render(request, 'home/coleccion_expo.html', context)
