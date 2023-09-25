from django.urls import path
from .views import home_view, proyectos_view, sobre_mi_view, contacto_view

app_name = 'home'

urlpatterns = [
    path('', home_view),
    path('proyectos/', proyectos_view),
    path('sobre-mi/', sobre_mi_view),
    path('contacto/', contacto_view),
    # path('q/mis-quieros/', mis_quieros_view, name='mis-quieros-view'),
  
]
