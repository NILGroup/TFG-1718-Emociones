from models import Emocion
from serializer import EmocionSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

class Palabra:
	
	EMOCIONES = ["TRISTEZA", "MIEDO", "ALEGRIA", "ENFADO", "SORPRESA", "NEUTRAL"]

	def __init__(self,palabra):
		self.palabra = palabra
		self.porcentajes = []
		self.emocion_mayor = self.EMOCIONES[5]

	def subir(subida):
		subida = Emocion(palabra=self.palabra, procentajes=self.porcentajes)
		subida.save()

	def show(self):
		print("Palabra: " + self.palabra)
		print("Grado de tristeza: " + repr(self.porcentajes[0]))
		print("Grado de miedo: " + repr(self.porcentajes[1]))
		print("Grado de alegria: " + repr(self.porcentajes[2]))
		print("Grado de enfado: " + repr(self.porcentajes[3]))
		print("Grado de sorpresa: " + repr(self.porcentajes[4]))
		print("Grado de neutral: " + repr(self.porcentajes[5]))
		print("Predomina la emocion: " + repr(self.emocion_mayor))
		print("---------------------------")