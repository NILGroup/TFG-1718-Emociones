import requests
from interprete_palabras import InterpretePalabras

def porcentajes(op,destino):
	"""
	Devuelve los porcentajes de emocion para una palabra.

	>>> porcentajes(0,"http://127.0.0.1:8000/emociones/mesa/percentages/")
	Porcentaje de tristeza: 0%
	Porcentaje de miedo: 0%
	Porcentaje de alegria: 0%
	Porcentaje de enfado: 0%
	Porcentaje de sorpresa: 0%
	Porcentaje de neutral: 100%
	>>> porcentajes(0,"http://127.0.0.1:8000/emociones/aranya/percentages/")
	Porcentaje de tristeza: 0%
	Porcentaje de miedo: 67%
	Porcentaje de alegria: 0%
	Porcentaje de enfado: 0%
	Porcentaje de sorpresa: 0%
	Porcentaje de neutral: 33%
	>>> porcentajes(0,"http://127.0.0.1:8000/emociones/corazon/percentages/")
	Porcentaje de tristeza: 0%
	Porcentaje de miedo: 0%
	Porcentaje de alegria: 50%
	Porcentaje de enfado: 0%
	Porcentaje de sorpresa: 0%
	Porcentaje de neutral: 50%
	>>> porcentajes(0,"http://127.0.0.1:8000/emociones/te/percentages/")
	No se ha encontrado la palabra. Asegurese de haberla escrito bien.

	>>> porcentajes(1,"http://127.0.0.1:8000/emociones/mesa/agreed/")
	Neutral
	>>> porcentajes(1,"http://127.0.0.1:8000/emociones/aranya/agreed/")
	No hay emocion consensuada.
	>>> porcentajes(1,"http://127.0.0.1:8000/emociones/corazon/agreed/")
	No hay emocion consensuada.
	>>> porcentajes(1,"http://127.0.0.1:8000/emociones/te/agreed/")
	No se ha encontrado la palabra. Asegurese de haberla escrito bien.

	>>> porcentajes(2,"http://127.0.0.1:8000/emociones/mesa/main/")
	Neutral con un 100%
	>>> porcentajes(2,"http://127.0.0.1:8000/emociones/aranya/main/")
	Miedo con un 67%
	>>> porcentajes(2,"http://127.0.0.1:8000/emociones/corazon/main/")
	Hay dos emociones mayoritarias: Alegria y Neutral con un 50%
	>>> porcentajes(2,"http://127.0.0.1:8000/emociones/te/main/")
	No se ha encontrado la palabra. Asegurese de haberla escrito bien.
	"""
	interpreta = InterpretePalabras()
	if op == 0:
		porcentajes = interpreta.interpretar_porcentajes(destino)
		interpreta.mostrar_porcentajes(porcentajes)
	elif op == 1:
		consensuada = interpreta.interpretar_consensuada(destino)
		interpreta.mostrar_consensuada(consensuada)
	elif op == 2:
		mayoritarias,porcentaje = interpreta.interpretar_mayoritaria(destino)
		interpreta.mostrar_mayoritaria(mayoritarias,porcentaje)

if __name__ == "__main__":
	import doctest
	failure, test = doctest.testmod(verbose=True)
	if failure > 0:
		raise ValueError("TEST WORDS FAILED")