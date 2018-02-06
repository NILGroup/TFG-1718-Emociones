import requests

"""
Programa que le pide al usuario que introduzca una palabra para buscarla en el 
servidor y devolver el grado de cada emoción que tiene.
"""
def lista_emociones():
	emocion = ["tristeza", "miedo", "alegria", "enfado", "sorpresa", "neutral"]
	return emocion

def coger_porcentajes(porcentajes):
	tokens = porcentajes.split(" || ")
	numeros = []
	for i in range(6):
		emocion = tokens[i].split(':')
		porcentaje = emocion[1][:2]
		if porcentaje[0] == '0':
			numeros.append("0")
		elif porcentaje == "10":
			numeros.append("100")
		else:
			numeros.append(porcentaje)
	return numeros

def cargar_datos(porcentajes):
	numeros = coger_porcentajes(porcentajes)
	emocion = lista_emociones()
	return numeros, emocion

def quitar_acento(palabra,acento,letra):
	pos = palabra.index(acento)
	pre = palabra[:pos]
	suf = palabra[pos+1:]
	sin_acento = pre+letra+suf
	return sin_acento

def traducir(palabra):
	if 'á' in palabra:
		palabra = quitar_acento(palabra,'á', "a")
	elif 'é' in palabra:
		palabra = quitar_acento(palabra,'é', "e")
	elif 'í' in palabra:
		palabra = quitar_acento(palabra,'í', "i")
	elif 'ó' in palabra:
		palabra = quitar_acento(palabra,'ó', "o")
	elif 'ú' in palabra:
		palabra = quitar_acento(palabra,'ú', "u")
	if 'ñ' in palabra:
		palabra = quitar_acento(palabra,'ñ', "ny")	
	return palabra

"""
--------
PALABRAS
--------
"""
def mostrar_todo(destino):
	respuesta = requests.get(destino)
	if repr(respuesta) == "<Response [404]>":
		print("No se ha encontrado la palabra. Asegurese de haberla escrito bien.")
	else:
		porcentajes = respuesta.json()
	numeros, emocion = cargar_datos(porcentajes)
	mayoritarias = []
	mayor_porcentaje = -1
	contador = 0
	for i in range(6):
		print("Porcentaje de " + emocion[i] + ": "+ numeros[i] + "%")
		if mayor_porcentaje < int(numeros[i]):
			mayor_porcentaje = int(numeros[i])
			mayoritarias = []
			mayoritarias.append(i)
			contador = 0
		elif mayor_porcentaje == int(numeros[i]):
			contador = contador + 1
			mayoritarias.append(i)
	if mayor_porcentaje == 100:
		print("La emoción mayoritaria es " + emocion[mayoritarias[0]] + " y además es consensuada.")
	elif contador == 0:
		print("La emoción mayoritaria es " + emocion[mayoritarias[0]] + " con porcentaje " + str(mayor_porcentaje) + ", por lo que no es consensuada")
	elif contador == 1:
		print("Hay dos emociones mayoritarias: " + emocion[mayoritarias[0]] + " y " + emocion[mayoritarias[1]] + " con porcentaje " + str(mayor_porcentaje))

def interpretar_porcentajes(destino):
	respuesta = requests.get(destino)
	if repr(respuesta) == "<Response [404]>":
		print("No se ha encontrado la palabra. Asegurese de haberla escrito bien.")
	else:
		porcentajes = respuesta.json()
		numeros, emocion = cargar_datos(porcentajes)
		for i in range(6):
			print("Porcentaje de " + emocion[i] + ": "+ numeros[i] + "%")

def traducir_emocion(ingles):
	if ingles == "SADNESS":
		return "Tristeza"
	elif ingles == "FEAR":
		return "Miedo"
	elif ingles == "JOY":
		return "Alegria"
	elif ingles == "MADNESS":
		return "Enfado"
	elif ingles == "SURPRISE":
		return "Sorpresa"
	else:
		return "Neutral"

def interpretar_consensuada(destino):
	respuesta = requests.get(destino)
	if repr(respuesta) == "<Response [404]>":
		print("No se ha encontrado la palabra. Asegurese de haberla escrito bien.")
	else:
		consensuada = respuesta.json()
		if consensuada[:2] == "NO":
			print("No hay emocion consensuada.")
		else:
			emocion = consensuada.split(" ")
			print(traducir_emocion(emocion[1]))

def interpretar_mayoritaria(destino):
	respuesta = requests.get(destino)
	if repr(respuesta) == "<Response [404]>":
		print("No se ha encontrado la palabra. Asegurese de haberla escrito bien.")
	else:
		mayoritaria = respuesta.json()
		tokens = mayoritaria.split(" ")
		if ',' in mayoritaria:
			tokens[1] = tokens[1].rstrip(',')
			emocion1 = tokens[1]
			emocion2 = tokens[2]
			print("Hay dos emociones mayoritarias: " + traducir_emocion(emocion1) + " y " + traducir_emocion(emocion2) + " con un " + tokens[5] + "%")
		else:
			emocion = tokens[1]
			print(traducir_emocion(emocion) + " con un " + tokens[4] + "%")

def leer_palabra():
	print("Introduzca la palabra que desea buscar:") # se le pide al usuario que introduzca una palabra
	buscar = input()
	buscada = buscar.lower()
	buscada = traducir(buscada)
	return buscada

def menu_palabra():
	print("1.Porcentajes")
	print("2.Consensuada")
	print("3.Mayoritaria")
	print("4.Todo")
	print("0.Salir")
	print("Introduzca una opcion:")
	opcion = input()
	return int(opcion)

def interpretar_palabra(URL):
	seguir = False
	servicios = ['/percentages/', '/agreed/', '/main/']
	while seguir == False:
		opcion = menu_palabra()
		if opcion == 0:
			seguir = True
		elif opcion == 1:
			palabra = leer_palabra()
			destino = URL+palabra+servicios[0]
			interpretar_porcentajes(destino)
		elif opcion == 2:
			palabra = leer_palabra()
			destino = URL+palabra+servicios[1]
			interpretar_consensuada(destino)
		elif opcion == 3:
			palabra = leer_palabra()
			destino = URL+palabra+servicios[2]
			interpretar_mayoritaria(destino)
		elif opcion == 4:
			palabra = leer_palabra()
			destino = URL+palabra+servicios[0]
			mostrar_todo(destino)

def menu():
	print("1.Palabra")
	print("2.Frase")
	print("3.Texto")
	print("0.Salir")
	print("Introduzca una opcion:")
	opcion = input()
	return int(opcion)

"""
------
FRASES
------
"""
def interpretar_frase(URL):
	print("INTERPRETAR FRASE")

"""
------
TEXTOS
------
"""
def interpretar_texto(URL):
	print("INTERPRETAR TEXTO")

def main():
	URL = 'http://127.0.0.1:8000/emociones/' # URL del servidor
	seguir = False
	while seguir == False:
		opcion = menu()
		if opcion == 0:
			seguir = True
		elif opcion == 1:
			interpretar_palabra(URL)
		elif opcion == 2:
			interpretar_frase(URL)
		elif opcion == 3:
			interpretar_texto(URL)
		else:
			print("Opcion Incorrecta!")

main()
