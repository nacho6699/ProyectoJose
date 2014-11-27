from django.conf.urls import patterns, include, url
from .views import *
urlpatterns = patterns('',
    
    url(r'^registro/tema/$',registro_tema, name='Tema'),
    url(r'^tema/add/(\d+)/$',add_pregunta, name='agregarPregunta'),
    url(r'^tema/edit/(\d+)/$',ver_pregunta, name='verPregunta'),
    url(r'^pregunta/edit/(\d+)/$',edit_pregunta, name='editarPregunta'),
    url(r'^pregunta/eliminar/(\d+)/$',del_pregunta, name='eliminarPregunta'),
    #url(r'^registro/pregunta/$',registro_pregunta, name='Pregunta'),
)
