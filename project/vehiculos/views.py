from django.shortcuts import render, redirect
from .models import Vehiculo
from .forms import VehiculoForm
from django.db.models import Q

def alta_vehiculo(request):
    form = VehiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_vehiculos')
    return render(request, 'vehiculos/alta_vehiculo.html', {'form': form})


def lista_vehiculos(request):
    query = request.GET.get('q')
    anio = request.GET.get('anio')
    precio_min = request.GET.get('precio_min')
    precio_max = request.GET.get('precio_max')

    vehiculos = Vehiculo.objects.filter(activo=True)

    if query:
        vehiculos = vehiculos.filter(
            Q(modelo__icontains=query) | Q(marca__icontains=query)
        )

    if anio:
        vehiculos = vehiculos.filter(anio=anio)

    if precio_min:
        vehiculos = vehiculos.filter(precio__gte=precio_min)
    if precio_max:
        vehiculos = vehiculos.filter(precio__lte=precio_max)

    context = {
        'vehiculos': vehiculos,
        'query': query,
        'anio': anio,
        'precio_min': precio_min,
        'precio_max': precio_max,
    }
    return render(request, 'vehiculos/lista_vehiculos.html', context)
