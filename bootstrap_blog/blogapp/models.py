from django.db import models


# Create your models here.

class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    apellidoM=models.CharField(max_length=50)
    correo=models.EmailField(max_length=100)
    pais=models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    razon_social=models.CharField(max_length=50)
    contacto=models.CharField(max_length=50)
    correo=models.EmailField(max_length=100)
    
    def __str__(self):
        return self.razon_social


