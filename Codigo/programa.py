import requests

"""
Programa que le pide al usuario que introduzca una palabra para buscarla en el 
servidor y devolver el grado de cada emoción que tiene.
"""
def mostrar_porcentajes(porcentajes):
	"""
	Muestra la lista de porcentajes correspondientes a cada emoción.
	"""
	numeros = porcentajes.split(", ", 6)
	numeros[0] = numeros[0].lstrip("[")
	numeros[5] = numeros[5].rstrip("]")
	print("Porcentaje de tristeza: " + numeros[0] + "%")
	print("Porcentaje de miedo: " + numeros[1] + "%")
	print("Porcentaje de alegria: " + numeros[2] + "%")
	print("Porcentaje de enfado: " + numeros[3] + "%")
	print("Porcentaje de sorpresa: " + numeros[4] + "%")
	print("Porcentaje de neutral: " + numeros[5] + "%")

URL = 'http://127.0.0.1:8000/emocion/' # URL del servidor
sufijo = '/porcentajes/' # sufijo de la consulta
print ("Introduzca la palabra que desea buscar:") # se le pide al usuario que introduzca una palabra
buscar = input()
print ("Buscaremos la palabra", buscar)
destino = URL+buscar+sufijo
respuesta = requests.get(destino)
porcentajes = respuesta.json()
mostrar_porcentajes(porcentajes)

