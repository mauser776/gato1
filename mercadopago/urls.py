from django.urls import path
from .views import mercadopago_view
app_name = 'mercadopago'

urlpatterns = [
    path('', mercadopago_view, name='mercadopago-view'),








]
