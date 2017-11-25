from django.conf.urls import url
from emocion import views

urlpatterns = [
    url(r'^emocion/$', views.lista_palabras),
    url(r'^emocion/(?P<pk>[0-9]+)/$', views.detalle_palabra),
]