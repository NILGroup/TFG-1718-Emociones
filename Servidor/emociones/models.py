from django.db import models
from django.core.validators import validate_comma_separated_integer_list

# Modelo que utilizará el servicio web
class Palabra(models.Model):
	"""
	Los campos que tiene el modelo son: la palabra en sí, su lexema y el grado de certeza con el
	que se puede afirmar que una emoción la caracteriza expresados en porcentajes.
	"""

	palabra = models.CharField(max_length=30)
	lexema = models.CharField(max_length=30)
	porcentajes = models.CharField(validators=[validate_comma_separated_integer_list], max_length = 100)

	def __str__(self):
		return self.palabra

	class Meta:
		ordering = ('palabra',)
