from django.urls import path
from .views import home_view, obras_view, sobre_mi_view, contacto_view, galerias_view, cuadro_view

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.views.static import serve
from django.conf.urls import url


app_name = 'home'

urlpatterns = [
    path('', home_view, name='home-view'),
    path('obras/', obras_view, name='obras-view'),
    path('sobre-mi/', sobre_mi_view, name='sobre_mi-view'),
    path('contacto/', contacto_view, name='contacto-view'),
    path('galerias/', galerias_view, name='galerias-view'),
    path('cuadro/<id>/', cuadro_view, name='cuadro-view'),

    url(r'^media/(?P<path>.*)$', serve,
        {'document_root':       settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,
        {'document_root': settings.STATIC_ROOT}),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
