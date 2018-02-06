import requests

def mayoritaria(palabra):
	"""
	Devuelve la emocion consensuada para una palabra.

	>>> mayoritaria("mesa")
	MAIN: NEUTRAL || %: 100
	>>> mayoritaria("corazon")
	MAIN: JOY, NEUTRAL || %: 50
	>>> mayoritaria("diamante")
	MAIN: JOY || %: 83
	>>> mayoritaria("te")
	{u'detail': u'Not found.'}
	"""
	URL = 'http://127.0.0.1:8000/emociones/' # URL del servidor
	sufijo = '/main/' # sufijo de la consulta
	buscar = palabra
	buscada = buscar.lower()
	destino = URL+buscada+sufijo
	respuesta = requests.get(destino)
	mayoritaria = respuesta.json()
	print(mayoritaria)

if __name__ == "__main__":
	import doctest
	failure, test = doctest.testmod(verbose=True)
	if failure > 0:
		raise ValueError("TEST MAIN_EMOTION FAILED")