from django.urls import path
from .views import home_view, obras_view, sobre_mi_view, contacto_view, coleccion_view, cuadro_view, cuadro_detail, coleccion_view_expo

app_name = 'home'

urlpatterns = [
    path('', home_view, name='home-view'),
    path('obras/', obras_view, name='obras-view'),
    path('sobre-mi/', sobre_mi_view, name='sobre_mi-view'),
    path('contacto/', contacto_view, name='contacto-view'),
    path('coleccion/', coleccion_view, name='coleccion-view'),
    path('cuadro/<id>/', cuadro_view, name='cuadro-view'),

    # EXPO
    path('coleccion-expo/', coleccion_view_expo, name='coleccion-view-expo'),


    path('cuadro_detail/<int:id>/', cuadro_detail, name='cuadro_detail'),



]
