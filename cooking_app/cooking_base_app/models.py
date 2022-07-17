from django.db import models

# Create your models here.

class Peso(models.Model):
    idPesoTipo = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=30)

class Receta(models.Model):
    idReceta = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    rendimiento = models.CharField(max_length=20)
    totalCost = models.IntegerField()
    desc_receta = models.CharField(max_length=500)

class Ingredientes(models.Model):
    idIngredientes = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=60)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)
    idPesoTipo = models.ForeignKey(Peso, on_delete=models.CASCADE)

class Preparacion(models.Model):
    idPreparacion = models.IntegerField(primary_key=True)
    idReceta = models.ForeignKey(Receta, models.CASCADE)
    idIngredientes = models.ForeignKey(Ingredientes, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)
    idPesoTipo = models.ForeignKey(Peso, on_delete=models.CASCADE)



