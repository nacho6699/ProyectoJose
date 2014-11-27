from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tema(models.Model):
	nombre=models.CharField(max_length=10,unique=True)
	def __str__(self):
		return self.nombre
class Pregunta(models.Model):
	nombre=models.CharField(max_length=500)
	tema=models.ForeignKey(Tema)
	def __str__(self):
		return self.nombre

class Respuesta(models.Model):
	respuesta_correcta=models.CharField(max_length=500)
	respuesta_opcional_1=models.CharField(max_length=500)	
	respuesta_opcional_2=models.CharField(max_length=500)	
	respuesta_opcional_3=models.CharField(max_length=500)	
	respuesta_opcional_4=models.CharField(max_length=500)	
	pregunta=models.ForeignKey(Pregunta)
	def __str__(self):
		return self.pregunta