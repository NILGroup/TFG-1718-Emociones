from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from emociones import views

urlpatterns = [
	url(r'^e/$',views.index),
	url(r'^emociones/$', views.ListaPalabras.as_view()),
	url(r'^(?P<pk>\w+)/$', views.DetallePalabra.as_view()),
	url(r'^porcentajes/(?P<pk>\w+)/$', views.ObtenerPorcentajes.as_view()),
	url(r'^consensuada/(?P<pk>\w+)/$', views.ObtenerConsensuada.as_view()),
	url(r'^mayoritaria/(?P<pk>\w+)/$', views.ObtenerMayoritaria.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)