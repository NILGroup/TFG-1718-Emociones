import requests

def porcentajes(palabra):
	"""
	Devuelve los porcentajes de emocion para una palabra.

	>>> porcentajes("mesa")
	SADNESS:0% || FEAR:0% || JOY:0% || MADNESS:0% || SORPRISE:0% || NEUTRAL:100% 
	>>> porcentajes("aranya")
	SADNESS:0% || FEAR:67% || JOY:0% || MADNESS:0% || SORPRISE:0% || NEUTRAL:33% 
	>>> porcentajes("corazon")
	SADNESS:0% || FEAR:0% || JOY:50% || MADNESS:0% || SORPRISE:0% || NEUTRAL:50% 
	>>> porcentajes("te")
	{'detail': 'Not found.'}
	"""
	URL = 'http://127.0.0.1:8000/emocion/' # URL del servidor
	sufijo = '/percentages/' # sufijo de la consulta
	buscar = palabra
	buscada = buscar.lower()
	destino = URL+buscada+sufijo
	respuesta = requests.get(destino)
	porcentajes = respuesta.json()
	print(porcentajes)

if __name__ == "__main__":
	import doctest
	failure, test = doctest.testmod(verbose=True)
	if failure > 0:
		raise ValueError("TEST PERCENTAGES FAILED")