import requests

def consensuada(palabra):
	"""
	Devuelve la emocion consensuada para una palabra.

	>>> consensuada("mesa")
	AGREED: NEUTRAL
	>>> consensuada("corazon")
	NO AGREED EMOTION
	>>> consensuada("te")
	{u'detail': u'Not found.'}
	"""
	URL = 'http://127.0.0.1:8000/emociones/' # URL del servidor
	sufijo = '/agreed/' # sufijo de la consulta
	buscar = palabra
	buscada = buscar.lower()
	destino = URL+buscada+sufijo
	respuesta = requests.get(destino)
	consensuada = respuesta.json()
	print(consensuada)

if __name__ == "__main__":
	import doctest
	failure, test = doctest.testmod(verbose=True)
	if failure > 0:
		raise ValueError("TEST AGREED_EMOTION FAILED")