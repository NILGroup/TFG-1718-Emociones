from django.db import models
from django.core.validators import validate_comma_separated_integer_list

#LISTA DE POSIBLES EMOCIONES
EMOCIONES = ((0, "TRISTEZA"), (1, "MIEDO"), (2, "ALEGRIA"), (3, "ENFADO"), (4, "SORPRESA"), (5,"NEUTRAL"))

#VALIDADOR DE PORCENTAJES 
VALIDADOR = [(validate_comma_separated_integer_list, '0,17,33,50,67,83,100', None)]

# Modelo que utilizará el servicio web
class Emocion(models.Model):
	"""
	Los campos que tiene el modelo son: la palabra en sí, el grado de certeza con el
	que se puede afirmar que una emoción la caracreriza expresados en porcentajes y
	la emoción que destaca entre esos porcentajes.
	"""
	palabra = models.CharField(max_length=30, blank=True, default="")
	porcentajes = models.CharField(validators=VALIDADOR, max_length = 100)
	emocion_mayor = models.CharField(choices = EMOCIONES, default = "NEUTRAL", max_length = 10)

	class Meta:
		ordering = ('palabra',)