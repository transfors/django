from django.db import models

# Create your models here.

class productos(models.Model):
    nombre = models.CharField(max_length=30)
    categoria = models.CharField(max_length=40)
    precio = models.IntegerField()
    proveedor = models.CharField(max_length=30,null=True)
    def __str__(self):
        # return 'El nombre es: %s, la categoria es: %s, el precio es: %s y el proveedor es: %s' %(self.nombre,self.categoria,self.precio,self.proveedor)
        return (self.nombre, self.categoria, self.precio, self.proveedor)

class usuarios(models.Model):
    nombre = models.CharField(max_length=40)
    pais = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.CharField(max_length=10)
    def __str__(self):
        return self.nombre

class pedidos(models.Model):
    cantidad = models.IntegerField()
    fecha = models.DateField()
    enviado = models.BooleanField()