from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    diagnostico = models.CharField(max_length=700)
    updrs = models.IntegerField()