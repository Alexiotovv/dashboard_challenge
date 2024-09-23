from django.db import models

#Creamos el modelo Persona
class Persona(models.Model):
    nombre = models.CharField(max_length=100)  
    edad = models.IntegerField()  
    ciudad = models.CharField(max_length=100) 
    salario = models.DecimalField(max_digits=10, decimal_places=2) 

    def __str__(self):
        return f'{self.nombre} - {self.ciudad}'