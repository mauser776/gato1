from django.urls import path
from .views import mercadopago_view, cuadro_view_pago, comprar_cuadro

app_name = 'mercadopago'

urlpatterns = [
    path('', mercadopago_view, name='mercadopago-view'),
    path('mer_cuadro/<int:id>/', cuadro_view_pago, name='cuadro-view'),
    path('comprar/<int:id>/', comprar_cuadro, name='comprar-cuadro'),
]
