from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import*
from .models import*
# Create your views here.

def registro_tema(request):
	titulo="Registro de temas"
	temas=Tema.objects.all()
	if(request.method=="POST"):
		formulario=ftema(request.POST)
		if formulario.is_valid():
			formulario.save()
			estado=True
			
			datos={'titulo':titulo,'formulario':formulario,'estado':estado,'temas':temas}
			return render_to_response("preguntas/registroTema.html",datos,context_instance=RequestContext(request))
	else:
		formulario=ftema
	datos={'titulo':titulo,'formulario':formulario,'temas':temas}
	return render_to_response("preguntas/registroTema.html",datos,context_instance=RequestContext(request))	

def add_pregunta(request,id):
	tema=Tema.objects.get(id=int(id))
	titulo="Registro pregunta para el tema "+tema.nombre
	titulo2="Registre las respuestas"
	if request.method=="POST":
		formulario=fpregunta(request.POST)
		formulario2=frespuesta(request.POST)
		if formulario.is_valid() and formulario2.is_valid():
			pregunta=formulario.save(commit=False)
			pregunta.tema=tema
			pregunta.save()
			respuesta=formulario2.save(commit=False)
			respuesta.pregunta=pregunta
			respuesta.save()
			estado=True
			formulario=fpregunta()
			datos={'titulo':titulo,'formulario':formulario,'estado':estado,'titulo2':titulo2,'formulario2':formulario2}
			return HttpResponseRedirect("/inicio/tema/edit/"+str(id)+"/")	

	else:
		formulario=fpregunta()
		formulario2=frespuesta()
	datos={'titulo':titulo,'titulo2':titulo2,'formulario':formulario,'formulario2':formulario2}	
	return render_to_response("preguntas/registroPregunta.html",datos,context_instance=RequestContext(request))	

def ver_pregunta(request,id):
	tema=Tema.objects.get(id=int(id))
	preguntas=Pregunta.objects.filter(tema=tema)
	datos={'tema':tema,'preguntas':preguntas}
	return render_to_response("preguntas/verPregunta.html",datos,context_instance=RequestContext(request))

def edit_pregunta(request,id):
	pregunta=Pregunta.objects.get(id=int(id))
	respuesta=Respuesta.objects.get(pregunta=pregunta)
	id=pregunta.tema.id
	titulo="Editar pregunta"
	titulo2="Editar las respuestas"
	if request.method=="POST":
		formulario=fpregunta(request.POST,instance=pregunta)
		formulario2=frespuesta(request.POST,instance=respuesta)
		if formulario.is_valid() and formulario2.is_valid():
			formulario.save()
			formulario2.save()
			estado=True
			datos={'titulo':titulo,'formulario':formulario,'estado':estado,'titulo2':titulo2,'formulario2':formulario2}
			return HttpResponseRedirect("/inicio/tema/edit/"+str(id)+"/")
	else:
		formulario=fpregunta(instance=pregunta)
		formulario2=frespuesta(instance=respuesta)
	datos={'titulo':titulo,'titulo2':titulo2,'formulario':formulario,'formulario2':formulario2}
	return render_to_response("preguntas/registroPregunta.html",datos,context_instance=RequestContext(request))

def del_pregunta(request,id):
	pregunta=Pregunta.objects.get(id=int(id))
	id=pregunta.tema.id
	respuesta=Respuesta.objects.get(pregunta=pregunta)
	pregunta.delete()
	respuesta.delete()
	return HttpResponseRedirect("/inicio/tema/edit/"+str(id)+"/")
