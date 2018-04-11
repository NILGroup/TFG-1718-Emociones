from interprete_palabras import InterpretePalabras
from procesador_emocional import PalabrasEmocionales

"""
Programa que se encarga de procesar una frase, buscando las palabras emocionales de esta
en el servicio web, y devolver la información que tiene sobre ella.
"""

interpreta = InterpretePalabras() # nos permitirá interpretar las palabras emocionales
procesador = PalabrasEmocionales() # nos permitirá encontrar las palabras emocionales

URL = 'http://127.0.0.1:8000/emociones/' # URL base del servicio web

emociones = ["Tristeza", "Miedo", "Alegría", "Enfado", "Sorpresa", "Neutral"] # lista de emociones con las que trabajamos

def obtener_url_porcentajes(palabra):
	"""
	Función que dada una palabra devuelve la URL que hay que usar para
	obtener sus porcentajes.
	"""
	servicio = '/porcentajes/'
	palabra = palabra.lower()
	return URL+palabra+servicio

def obtener_url_mayoritaria(palabra):
	"""
	Función que dada una palabra devuelve la URL que hay que usar para
	obtener su emoción mayoritaria.
	"""
	servicio = '/mayoritaria/'
	palabra = palabra.lower()
	return URL+palabra+servicio

def obtener_url_consensuada(palabra):
	"""
	Función que dada una palabra devuelve la URL que hay que usar para
	obtener su emoción consensuada.
	"""
	servicio = '/consensuada/'
	palabra = palabra.lower()
	return URL+palabra+servicio

def obtener_medias(porcentajes,num_palabras):
	"""
	Función que dada una lista de porcentajes y un número de palabras a partir
	de las que se han obtenido, haya las medias para cada emoción. Devuelve una
	lista con los porcentajes medios.
	"""
	if num_palabras > 0:
		for i in range(6):
			porcentajes[i] = str(round(porcentajes[i] / num_palabras,2))
		return porcentajes
	else: # si no hay ninguna palabra emocional en la frase entonces esta es neutral
		return ["0","0","0","0","0","100"]

def actualizar_porcentajes_frase(actuales,nuevos,peso):
	for i in range(len(actuales)):
		actuales[i] = actuales[i] + (int(nuevos[i])*peso)

def actualizar_porcentajes(emocion,contadores,porcentajes,porcentaje):
	i = emociones.index(emocion)
	contadores[i] = contadores[i] + 1
	porcentajes[i] = porcentajes[i] + int(porcentaje)

def calcular_mayoritaria(contadores,porcentajes):
	mayor = -1
	indices = []
	for i in range(6):
		if contadores[i] > 0:
			media = round(porcentajes[i]/contadores[i],2)
			if media > mayor:
				mayor = media
				indices = [i]
			elif media == mayor:
				indices.append(i)
	return indices,mayor

class InterpreteFrases():

	@staticmethod
	def emociones_frase(frase):
		"""
		Función que dada una frase obtiene las palabras emocionales que contiene e interpreta
		los porcentajes de cada emoción. Devuelve los porcentajes y las palabras que permiten
		llegar a ellos.
		"""
		lista_palabras,lexemas = procesador.procesar_frase(frase) # lista de palabras emocionales
		num_lexemas = len(lexemas)
		if num_lexemas == 0: # si no hay ninguna, la frase es 100% neutral
			return ["0","0","0","0","0","100"], []
		else:
			emociones_frase = [0,0,0,0,0,0] 
			num_palabras = 0 # contador de palabras emocionales que están en nuestro diccionario
			positiva = True
			i = 0
			for i in range(num_lexemas):
				if (i == 0) or (i > 0 and lexemas[i] != lexemas[i-1]):
					destino = obtener_url_porcentajes(lexemas[i]) # obtenemos URL para realizar la consulta
					porcentajes = interpreta.interpretar_porcentajes(destino) # obtenemos los porcentajes de la palabra
					if len(porcentajes) > 0: # si la encontramos, actualizamos los porcentajes de la frase
						if i < num_lexemas-1 and lexemas[i+1] == lexemas[i]: # si es un verbo cuenta el doble
							actualizar_porcentajes_frase(emociones_frase,porcentajes,2)
							num_palabras = num_palabras + 2
						else:
							actualizar_porcentajes_frase(emociones_frase,porcentajes,1)
							num_palabras = num_palabras + 1
			emociones = obtener_medias(emociones_frase,num_palabras)
			return emociones,lista_palabras

	@staticmethod
	def emociones_mayoritaria_frase(frase):
		"""
		Función que dada una frase obtiene las palabras emocionales que contiene e interpreta
		la emoción mayoritaria para cada una. Lleva un contador con el número de apariciones
		de cada emoción como mayoritarias. Devuelve la lista de mayoritarias y su porcentaje.
		"""
		palabras_dicc,palabras = procesador.procesar_frase(frase) # lista de palabras emocionales
		contadores = [0,0,0,0,0,0] # lista de contadores
		porcentajes = [0,0,0,0,0,0] # porcentajes parciales
		indices = [] # posiciones de la lista de emociones principal que se corresponden con las mayoritarias

		for palabra in palabras:
			destino = obtener_url_mayoritaria(palabra) # obtenemos URL para realizar la consulta
			mayoritarias,porcentaje = interpreta.interpretar_mayoritaria(destino) # obtenemos los resultados
			# actualizamos la información según si la palabra tiene una o dos emociones mayoritarias
			if len(mayoritarias) == 1:
				actualizar_porcentajes(mayoritarias[0],contadores,porcentajes,porcentaje)
			elif len(mayoritarias) == 2:
				actualizar_porcentajes(mayoritarias[0],contadores,porcentajes,porcentaje)
				actualizar_porcentajes(mayoritarias[1],contadores,porcentajes,porcentaje)

		ind,porcent = calcular_mayoritaria(contadores,porcentajes)
		# devolvemos la/s emocion/es mayoritaria/s y su porcentaje
		if len(ind) == 1:
			i = ind[0]
			return [emociones[i]],porcent
		elif len(ind) == 2:
			i = ind[0]
			j = ind[1]
			return [emociones[i],emociones[j]],porcent/2
		else: # si no hay palabras emocionales, la frase es mayormente neutral
			return ["Neutral"],"100"

	@staticmethod
	def emocion_mayoritaria_frase(porcentajes):
		mayor = -1
		indice = []
		for i in range(6):
			if float(porcentajes[i]) > mayor:
				mayor = float(porcentajes[i])
				indice = [i]
			elif float(porcentajes[i]) == mayor:
				indice.append(i)
		if len(indice) == 1:
			return [emociones[indice[0]]],str(mayor)
		elif len(indice) == 2:
			return [emociones[indice[0]],emociones[indice[1]]],str(mayor)

	@staticmethod
	def emocion_consensuada_frase(frase):
		palabras = procesador.procesar_frase(frase)
		contadores = [0,0,0,0,0,0]
		mayor = -1
		pocentaje_frase = 0
		indices = []
		for palabra in palabras:
			destino = obtener_url_consensuada(palabra)
			consensuada = interpreta.interpretar_consensuada(destino)
			if len(consensuada) == 1:
				i = emociones.index(consesuada[0])
				mayor,indices,pocentaje_frase = incr_contador_mayoritarias(contadores,i,mayor,indices,pocentaje_frase,pocentaje)
		if len(indices) == 1:
			i = indices[0]
			return [emociones[i]],pocentaje_frase
		else:
			return ["Neutral"],"100"
