from django.urls import path
from . import views

urlpatterns = [
    # path('welcome', views.welcome, name='welcome'),
    path('alta/', views.alta_vehiculo, name='alta_vehiculo'),
    path('', views.lista_vehiculos, name='lista_vehiculos'),
    path('eliminar/<int:vehiculo_id>/', views.eliminar_vehiculo, name='eliminar_vehiculo'),
]