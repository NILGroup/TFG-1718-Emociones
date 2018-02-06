from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from emociones import views

urlpatterns = [
	url(r'^emociones/$', views.ListaPalabras.as_view()),
	url(r'^emociones/(?P<pk>\w+)/$', views.DetallePalabra.as_view()),
	url(r'^emociones/(?P<pk>\w+)/percentages/$', views.ObtenerPorcentajes.as_view()),
	url(r'^emociones/(?P<pk>\w+)/agreed/$', views.ObtenerConsensuada.as_view()),
	url(r'^emociones/(?P<pk>\w+)/main/$', views.ObtenerMayoritaria.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)