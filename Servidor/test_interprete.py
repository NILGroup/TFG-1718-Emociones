import requests
from interprete import InterpretePalabras

def porcentajes(destino):
	"""
	Devuelve los porcentajes de emocion para una palabra.

	>>> porcentajes("http://127.0.0.1:8000/emociones/mesa/percentages/")
	Porcentaje de tristeza: 0%
	Porcentaje de miedo: 0%
	Porcentaje de alegria: 0%
	Porcentaje de enfado: 0%
	Porcentaje de sorpresa: 0%
	Porcentaje de neutral: 100%
	>>> porcentajes("http://127.0.0.1:8000/emociones/aranya/percentages/")
	Porcentaje de tristeza: 0%
	Porcentaje de miedo: 67%
	Porcentaje de alegria: 0%
	Porcentaje de enfado: 0%
	Porcentaje de sorpresa: 0%
	Porcentaje de neutral: 33%
	>>> porcentajes("http://127.0.0.1:8000/emociones/corazon/percentages/")
	Porcentaje de tristeza: 0%
	Porcentaje de miedo: 0%
	Porcentaje de alegria: 50%
	Porcentaje de enfado: 0%
	Porcentaje de sorpresa: 0%
	Porcentaje de neutral: 50%
	>>> porcentajes("http://127.0.0.1:8000/emociones/te/percentages/")
	No se ha encontrado la palabra. Asegurese de haberla escrito bien.
	"""
	interprete = InterpretePalabras()
	interprete.interpretar_porcentajes(destino)

if __name__ == "__main__":
	import doctest
	failure, test = doctest.testmod(verbose=True)
	if failure > 0:
		raise ValueError("TEST PERCENTAGES FAILED")