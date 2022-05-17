from django.db import models
from django.utils import timezone

# Create your models here.
class Producto(models.Model) :
    serie_producto = models.CharField(max_length=32)
    marca = models.CharField(max_length=32)
    código = models.CharField(max_length=32)
    nombre = models.CharField(max_length=32)
    precio_actual = models.IntegerField()
    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.nombre


