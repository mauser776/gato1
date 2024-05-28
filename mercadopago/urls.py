from django.urls import path
from .views import mercadopago_view, procesar_pago, confirmacion_pago

app_name = 'mercadopago'

urlpatterns = [
    path('', mercadopago_view, name='mercadopago-view'),

    path('procesar_pago/', procesar_pago, name='procesar_pago'),
    path('confirmacion_pago/', confirmacion_pago, name='confirmacion_pago'),
]
