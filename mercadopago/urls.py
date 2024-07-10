from django.urls import path
from .views import cuadro_view_pago, pagar_cuadro, pago_exitoso, pago_fallido, pago_pendiente

app_name = 'mercadopago'

urlpatterns = [
    path('mer_cuadro/<int:id>/', cuadro_view_pago, name='mer-cuadro-view'),

    path('pagar/<int:cuadro_id>/', pagar_cuadro, name='pagar_cuadro'),
    path('pago-exitoso/', pago_exitoso, name='pago_exitoso'),
    path('pago-fallido/', pago_fallido, name='pago_fallido'),
    path('pago-pendiente/', pago_pendiente, name='pago_pendiente'),
]
