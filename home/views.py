from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request, 'home/home.html')

def proyectos_view(request):
    return render(request, 'home/proyectos.html')

def contacto_view(request):
    return render(request, 'home/contacto.html')

def sobre_mi_view(request):
    return render(request, 'home/sobre_mi.html')