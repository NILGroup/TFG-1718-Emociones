from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from emocion import views

urlpatterns = [
    url(r'^emocion/$', views.lista_palabras),
    url(r'^emocion/(?P<pk>[0-9]+)/$', views.detalle_palabra),
]

urlpatterns = format_suffix_patterns(urlpatterns)