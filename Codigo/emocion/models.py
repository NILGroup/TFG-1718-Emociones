from django.db import models
from django.core.validators import validate_comma_separated_integer_list

#VALIDADOR DE PORCENTAJES 
VALIDADOR = [(validate_comma_separated_integer_list, '0,17,33,50,67,83,100', None)]

# Modelo que utilizará el servicio web
class Emocion(models.Model):
	"""
	Los campos que tiene el modelo son: la palabra en sí, el grado de certeza con el
	que se puede afirmar que una emoción la caracreriza expresados en porcentajes y
	la emoción que destaca entre esos porcentajes.
	"""
	palabra = models.CharField(max_length=30)
	porcentajes = models.CharField(validators=VALIDADOR, max_length = 100)

	def __str__(self):
		return self.palabra

	class Meta:
		ordering = ('palabra',)