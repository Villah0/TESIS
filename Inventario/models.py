from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Inventario(models.Model):
    Nombre = models.CharField(max_length=100)
    Marca = models.CharField(max_length=100)
    Descripcion = models.TextField(blank=True)
    Valor = models.IntegerField(null=True)
    Unidades = models.IntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.Nombre + " " + self.Marca