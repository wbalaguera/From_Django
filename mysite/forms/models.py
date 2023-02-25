from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre=models.CharField(max_length=15)
    telefono=models.CharField(max_length=12)
    fecha_de_nacimiento=models.DateField()
    email=models.EmailField(max_length=254)