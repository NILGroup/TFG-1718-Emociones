import requests

"""
Programa que le pide al usuario que introduzca una palabra para buscarla en el 
servidor y devolver el grado de cada emoción que tiene.
"""
def lista_emociones():
	emocion = ["tristeza", "miedo", "alegria", "enfado", "sorpresa", "neutral"]
	return emocion

def coger_porcentajes(porcentajes):
	numeros = porcentajes.split(", ", 6)
	numeros[0] = numeros[0].lstrip("[")
	numeros[5] = numeros[5].rstrip("]")
	return numeros

def cargar_datos(porcentajes):
	numeros = coger_porcentajes(porcentajes)
	emocion = lista_emociones()
	return numeros, emocion

def mostrar_porcentajes(porcentajes):
	"""
	Muestra la lista de porcentajes correspondientes a cada emoción.
	"""
	numeros, emocion = cargar_datos(porcentajes)
	for i in range(6):
		print("Porcentaje de " + emocion[i] + ": "+ numeros[i] + "%")


def tiene_consensuada(numeros):
	tieneConsensuada = False
	posEmocion = -1
	i = 0
	while((not tieneConsensuada) and i < 6):
		if(numeros[i] == '100'):
			posEmocion = i
			tieneConsensuada = True
		else:
			i = i+1
	return tieneConsensuada, posEmocion

def mostrar_emocion_consensuada(porcentajes):
	numeros, emocion = cargar_datos(porcentajes)
	tieneConsensuada, posEmocion = tiene_consensuada(numeros)
	if(not tieneConsensuada):
		print("La palabra no tiene una emoción consensuada")
	else:
		print("La emoción consensuada es " + emocion[posEmocion])
	
def mostrar_emocion_mayoritaria(porcentajes):
	numeros, emocion = cargar_datos(porcentajes)
	tieneConsensuada, posEmocion = tiene_consensuada(numeros)
	if(tieneConsensuada):
		print("La emoción mayoritaria es " + emocion[posEmocion])
	else:
		emocionMayor = -1
		for i in range(6):
			if(emocionMayor < int(numeros[i])):
				emocionMayor = int(numeros[i])
				posEmocion = i;
		print("La emoción mayoritaria es " + emocion[posEmocion])

def lista_porcentajes():
	URL = 'http://127.0.0.1:8000/emocion/' # URL del servidor
	sufijo = '/porcentajes/' # sufijo de la consulta
	valido = False
	while valido != True:
		print ("Introduzca la palabra que desea buscar:") # se le pide al usuario que introduzca una palabra
		buscar = input()
		buscada = buscar.lower()
		print ("Buscaremos la palabra", buscada)
		destino = URL+buscada+sufijo
		respuesta = requests.get(destino)
		if repr(respuesta) == "<Response [404]>":
			print("No se ha encontrado la palabra. Asegurese de haberla escrito bien.")
		else:
			porcentajes = respuesta.json()
			valido = True

	mostrar_porcentajes(porcentajes)
	mostrar_emocion_consensuada(porcentajes)
	mostrar_emocion_mayoritaria(porcentajes)
	

lista_porcentajes()
