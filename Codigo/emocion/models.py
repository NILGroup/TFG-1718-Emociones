from django.db import models
from django.core.validators import validate_comma_separated_integer_list

EMOCIONES = ((0, "TRISTEZA"), (1, "MIEDO"), (2, "ALEGRIA"), (3, "ENFADO"), (4, "SORPRESA"), (5,"NEUTRAL"))

VALIDADOR = [(validate_comma_separated_integer_list, '0,17,33,50,67,83,100', None)]

# Create your models here.
class Emocion(models.Model):
	palabra = models.CharField(max_length=30, blank=True, default="")
	porcentajes = models.CharField(validators=VALIDADOR, max_length = 100)
	emocion_mayor = models.CharField(choices = EMOCIONES, default = "NEUTRAL", max_length = 10)

	class Meta:
		ordering = ('palabra',)