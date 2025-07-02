from django.urls import path
from . import views

urlpatterns = [
    path('alta/', views.alta_vehiculo, name='alta_vehiculo'),
    path('', views.lista_vehiculos, name='lista_vehiculos'),
]