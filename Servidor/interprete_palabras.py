import requests

"""
Programa que le pide al usuario que introduzca una palabra para buscarla en el 
servidor y devolver el grado de cada emoción que tiene.
"""
emocion = ["tristeza", "miedo", "alegria", "enfado", "sorpresa", "neutral"]

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

class InterpretePalabras():

	@staticmethod
	def mostrar_todo(destino):
		respuesta = requests.get(destino)
		if repr(respuesta) == "<Response [404]>":
			print("No se ha encontrado la palabra. Asegurese de haberla escrito bien.")
		else:
			porcentajes = respuesta.json()
		numeros = coger_porcentajes(porcentajes)
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

	@staticmethod
	def interpretar_porcentajes(destino):
		respuesta = requests.get(destino)
		numeros = []
		if repr(respuesta) != "<Response [404]>":
			porcentajes = respuesta.json()
			numeros = coger_porcentajes(porcentajes)
		return numeros

	@staticmethod
	def interpretar_consensuada(destino):
		respuesta = requests.get(destino)
		if repr(respuesta) == "<Response [404]>":
			return "No se ha encontrado la palabra. Asegurese de haberla escrito bien."
		else:
			consensuada = respuesta.json()
			if consensuada[:2] == "NO":
				return "No hay emocion consensuada."
			else:
				emocion = consensuada.split(" ")
				return traducir_emocion(emocion[1])

	@staticmethod
	def interpretar_mayoritaria(destino):
		respuesta = requests.get(destino)
		mayoritarias = []
		if repr(respuesta) == "<Response [404]>":
			return mayoritarias,"0"
		else:
			mayoritaria = respuesta.json()
			tokens = mayoritaria.split(" ")
			if ',' in mayoritaria:
				tokens[1] = tokens[1].rstrip(',')
				mayoritarias.append(traducir_emocion(tokens[1]))
				mayoritarias.append(traducir_emocion(tokens[2]))
				porcentaje = tokens[5]
				return mayoritarias,porcentaje
			else:
				emocion = traducir_emocion(tokens[1])
				mayoritarias.append(emocion)
				porcentaje = tokens[4]
				return mayoritarias,porcentaje
