from django.urls import path
from .views import home_view, obras_view, sobre_mi_view, contacto_view, galerias_view, cuadro_view

from django.conf import settings
from django.conf.urls.static import static


app_name = 'home'

urlpatterns = [
    path('', home_view, name='home-view'),
    path('obras/', obras_view, name='obras-view'),
    path('sobre-mi/', sobre_mi_view, name='sobre_mi-view'),
    path('contacto/', contacto_view, name='contacto-view'),
    path('galerias/', galerias_view, name='galerias-view'),
    path('cuadro/<id>/', cuadro_view, name='cuadro-view'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
