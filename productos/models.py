from statistics import mode
from django.db import models

class Zapatilla(models.Model):
    marca_color = models.TextField(max_lenght=100)
    precio = models.FloatField()
    talle = models.FloatField()

class Buzo(models.Model):
    marca_color = models.TextField(max_lenght=100)
    precio = models.FloatField()
    talle = models.TextField(max_lenght=100)

class Campera(models.Model):
    marca_color = models.TextField(max_lenght=100)
    precio = models.FloatField()
    talle = models.TextField(max_lenght=100)





    


