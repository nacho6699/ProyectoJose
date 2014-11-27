from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class ftema(ModelForm):
	class Meta:
		model=Tema

class fpregunta(ModelForm):
	nombre=forms.CharField(required=True,label="Pregunta :")
	class Meta:
		model=Pregunta	
		exclude=['tema']	

class frespuesta(ModelForm):
	class Meta:
		model=Respuesta	
		exclude=['pregunta']		