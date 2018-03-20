import requests
from interprete_frases import InterpreteFrases
from salida import Salida

def porcentajes(op,frase):
	"""
	Devuelve los porcentajes de emocion para una palabra.

	>>> porcentajes(0,"Ana está triste y avergonzada")
	Porcentaje de tristeza: 100.0%
	Porcentaje de miedo: 0.0%
	Porcentaje de alegria: 0.0%
	Porcentaje de enfado: 0.0%
	Porcentaje de sorpresa: 0.0%
	Porcentaje de neutral: 0.0%
	>>> porcentajes(0,"Llevaba una escopeta")
	Porcentaje de tristeza: 0.0%
	Porcentaje de miedo: 100.0%
	Porcentaje de alegria: 0.0%
	Porcentaje de enfado: 0.0%
	Porcentaje de sorpresa: 0.0%
	Porcentaje de neutral: 0.0%
	>>> porcentajes(0,"Mañana es mi boda")
	Porcentaje de tristeza: 0.0%
	Porcentaje de miedo: 0.0%
	Porcentaje de alegria: 100.0%
	Porcentaje de enfado: 0.0%
	Porcentaje de sorpresa: 0.0%
	Porcentaje de neutral: 0.0%
	>>> porcentajes(0,"Ese tipo es un arrogante")
	Porcentaje de tristeza: 0.0%
	Porcentaje de miedo: 0.0%
	Porcentaje de alegria: 0.0%
	Porcentaje de enfado: 100.0%
	Porcentaje de sorpresa: 0.0%
	Porcentaje de neutral: 0.0%
	>>> porcentajes(0,"Me ha sorprendido su actitud")
	Porcentaje de tristeza: 0.0%
	Porcentaje de miedo: 0.0%
	Porcentaje de alegria: 0.0%
	Porcentaje de enfado: 0.0%
	Porcentaje de sorpresa: 100.0%
	Porcentaje de neutral: 0.0%
	>>> porcentajes(0,"Pásame un tenedor")
	Porcentaje de tristeza: 0.0%
	Porcentaje de miedo: 0.0%
	Porcentaje de alegria: 0.0%
	Porcentaje de enfado: 0.0%
	Porcentaje de sorpresa: 0.0%
	Porcentaje de neutral: 100.0%
	>>> porcentajes(0,"Hola")
	Porcentaje de tristeza: 0%
	Porcentaje de miedo: 0%
	Porcentaje de alegria: 0%
	Porcentaje de enfado: 0%
	Porcentaje de sorpresa: 0%
	Porcentaje de neutral: 100%
	>>> porcentajes(0,"Me voy a dormir")
	Porcentaje de tristeza: 0.0%
	Porcentaje de miedo: 0.0%
	Porcentaje de alegria: 50.0%
	Porcentaje de enfado: 0.0%
	Porcentaje de sorpresa: 0.0%
	Porcentaje de neutral: 50.0%
	>>> porcentajes(0,"Ana está triste porque se ha roto su ascensor")
	Porcentaje de tristeza: 55.67%
	Porcentaje de miedo: 0.0%
	Porcentaje de alegria: 0.0%
	Porcentaje de enfado: 11.0%
	Porcentaje de sorpresa: 0.0%
	Porcentaje de neutral: 33.33%
	>>> porcentajes(1,"Ana está triste y avergonzada")
	Tristeza con un 100%
	>>> porcentajes(1,"Llevaba una escopeta")
	Miedo con un 100%
	>>> porcentajes(1,"Mañana es mi boda")
	Alegria con un 100%
	>>> porcentajes(1,"Ese tipo es un arrogante")
	Enfado con un 100%
	>>> porcentajes(1,"Me ha sorprendido su actitud")
	Sorpresa con un 100%
	>>> porcentajes(1,"Pásame un tenedor")
	Neutral con un 100%
	>>> porcentajes(1,"Hola")
	Neutral con un 100%
	>>> porcentajes(1,"Me voy a dormir")
	Hay dos emociones mayoritarias: Alegria y Neutral con un 50%
	>>> porcentajes(1,"Ana está triste porque se ha roto su ascensor")
	Tristeza con un 67%
	"""
	interpreta = InterpreteFrases()
	_salida = Salida()
	if op == 0:
		porcentajes = interpreta.emociones_frase(frase)
		_salida.mostrar_porcentajes(porcentajes)
	elif op == 1:
		mayoritarias,porcentaje = interpreta.emociones_mayoritaria_frase(frase)
		_salida.mostrar_mayoritaria(mayoritarias,porcentaje)

if __name__ == "__main__":
	import doctest
	failure, test = doctest.testmod(verbose=True)
	if failure > 0:
		raise ValueError("TEST SENTENCES FAILED")