from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from emocion import views

urlpatterns = [
    url(r'^emocion/$', views.ListaPalabras.as_view()),
    url(r'^emocion/(?P<pk>[0-9]+)/$', views.DetallePalabra.as_view()),
    url(r'^emocion/(?P<pk>\w+)/porcentajes/$', views.ObtenerPorcentajes.as_view()),
    url(r'^emocion/(?P<pk>\w+)/majority/$', views.getMajority.as_view()),
    url(r'^emocion/(?P<pk>\w+)/consensual/$', views.getConsensual.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)