from django.db import models

class Vehiculo(models.Model):
    MARCAS_GM = [
        ('Buick', 'Buick'),
        ('Chevrolet', 'Chevrolet'),
        ('Cadillac', 'Cadillac'),
        ('GMC', 'GMC'),
    ]

    marca = models.CharField(max_length=20, choices=MARCAS_GM)
    modelo = models.CharField(max_length=100)
    anio = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.marca} {self.modelo} ({self.anio})'
