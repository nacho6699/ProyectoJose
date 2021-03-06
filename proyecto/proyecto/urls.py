from django.conf.urls import patterns, include, url
from django.contrib import admin
from proyecto.apps.usuario.views import *
from django.conf import settings
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^inicio/', include("proyecto.apps.usuario.url")),
    url(r'^inicio/', include("proyecto.apps.pregunta.urls")),    
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
    {'document_root':settings.MEDIA_ROOT,}
    ),

    url(r'^inicio/', include('social.apps.django_app.urls', namespace='social'))
)