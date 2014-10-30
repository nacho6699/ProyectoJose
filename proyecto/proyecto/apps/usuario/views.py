from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from .forms import *
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout

# Create your views here.
def view_principal(request):
	return render_to_response("inicio.html", {},context_instance=RequestContext(request))

def view_registrar(request):
	if request.method=="POST":
		formularioRegistro=fUsuario(request.POST)
		if formularioRegistro.is_valid():
			nuevo_usuario=request.POST['username']
			formularioRegistro.save()
			usuario=User.objects.get(username=nuevo_usuario)
			usuario.is_active=False
			usuario.save()
			
			perfil=Perfil.objects.create(user=usuario)
			return HttpResponse("Se registro correctamente ")
	else:
		formularioRegistro=fUsuario()
	return render_to_response("usuario/registrar.html",{'formulario':formularioRegistro},context_instance=RequestContext(request))

def view_login(request):
	if request.method=="POST":
		formulario=AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuario=request.POST['username']
			contrasena=request.POST['password']
			acceso=authenticate(username=usuario,password=contrasena)
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
					return HttpResponseRedirect("/inicio/perfil/")
				else:
					login(request, acceso)
					return HttpResponseRedirect("/inicio/activarcuenta/")
			else:
				return HttpResponse("<h1>Error al entrar verifica tus datos</h1>")
	else:
		formulario=AuthenticationForm()
	return render_to_response("usuario/login.html",{'formulario':formulario},context_instance=RequestContext(request))
						
def view_logout(request):
	logout(request)
	return HttpResponseRedirect("/inicio/")

def view_perfil(request):
	return render_to_response("usuario/perfil.html",{},context_instance=RequestContext(request))

def view_activarcuenta(request):
	if request.user.is_authenticated():
		usuario=request.user
		if usuario.is_active:
			return HttpResponseRedirect("/inicio/perfil/")
		else:
			if request.method=="POST":
				u=User.objects.get(username=usuario)
				perfil=Perfil.objects.get(user=u)
				formulario=fPerfil(request.POST,request.FILES,instance=perfil)
				if formulario.is_valid():
					formulario.save()
					u.is_active=True
					u.save()
					return HttpResponseRedirect("/inicio/perfil/")
			else:
				formulario=fPerfil()
			return render_to_response("usuario/activarcuenta.html",{'formulario':formulario},context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect("/login/")