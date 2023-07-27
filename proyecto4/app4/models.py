from django.db import models
# Create your models here.

class usuario(models.Model):
    nombre = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=30)
    carrera = models.CharField(max_length=30)
    def __str__(self):
        return (self.nombre, self.ciudad, self.carrera)
    
