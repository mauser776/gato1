from django.shortcuts import render
from .models import Cuadro

# Create your views here.

def home_view(request):
    return render(request, 'home/home.html')

def proyectos_view(request):
    return render(request, 'home/proyectos.html')

def contacto_view(request):
    return render(request, 'home/contacto.html')

def sobre_mi_view(request):
    return render(request, 'home/sobre_mi.html')

def galeria_view(request):
    cuadros = Cuadro.objects.all()
    
    lista_cuadros = []
    for x in cuadros:
        lista_cuadros.append()

    context = {
        'cuadros': cuadros,
        'lista_cuadros': lista_cuadros,
    }

    return render(request, 'home/galeria.html', context)

def cuadro_detail_view(request, id):

    cuadro = Cuadro.objects.get(id=id)


    if cuadro.cantidad_inicial is not None:
        cuadros_restantes = cuadro.cantidad_inicial - cuadro.cantidad_vendida
        print(cuadros_restantes)   
        context = {
            'cuadro': cuadro,
            'cuadros_restantes': cuadros_restantes,
        }
    else:
        context = {
            'cuadro': cuadro,
        }
        

    return render(request, 'home/cuadro.html', context)