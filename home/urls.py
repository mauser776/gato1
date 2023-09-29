from django.urls import path
from .views import home_view, proyectos_view, sobre_mi_view, contacto_view, galeria_view, cuadro_detail_view

app_name = 'home'

urlpatterns = [
    path('', home_view, name='home-view'),
    path('proyectos/', proyectos_view, name='proyectos-view'),
    path('sobre-mi/', sobre_mi_view, name='sobre_mi-view'),
    path('contacto/', contacto_view, name='contacto-view'),
    path('galeria/<coleccion>/', galeria_view, name='galeria-view'),
    path('cuadro/<id>/', cuadro_detail_view, name='cuadro-detail-view'),

]
