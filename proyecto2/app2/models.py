from django.db import models

# Create your models here.

class productos(models.Model):
    nombre = models.CharField(max_length=30)
    categoria = models.CharField(max_length=40)
    precio = models.IntegerField()
    proveedor = models.CharField(max_length=30,null=True)

class usuarios(models.Model):
    nombre = models.CharField(max_length=40)
    pais = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.CharField(max_length=10)

class pedidos(models.Model):
    cantidad = models.IntegerField()
    fecha = models.DateField()
    enviado = models.BooleanField()