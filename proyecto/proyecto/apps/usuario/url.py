from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chatgrafico.views.home', name='home'),
    #url(r'^blog/', include('blog.urls')),
	url(r'^$', view_principal),
	url(r'^registrar/$',view_registrar),
	url(r'^login/$',view_login),
	url(r'^logout/$',view_logout),
	url(r'^registrar/$',view_registrar),
	url(r'^perfil/$',view_perfil),
	url(r'^activarcuenta/$',view_activarcuenta),
	url(r'^modificar/$',modificar_perfil),
	url(r'^saladechat/$',sala_chat),
)
