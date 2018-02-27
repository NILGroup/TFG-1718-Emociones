from interprete_palabras import InterpretePalabras
from procesador_emocional import PalabrasEmocionales
import corrector

interpreta = InterpretePalabras()
procesador = PalabrasEmocionales()
URL = 'http://127.0.0.1:8000/emociones/'
emociones = ["Tristeza", "Miedo", "Alegria", "Enfado", "Sorpresa", "Neutral"]

def obtener_url(palabra):
	servicio = '/percentages/'
	palabra = palabra.lower()
	palabra = corrector.traducir(palabra)
	return URL+palabra+servicio

def obtener_url_mayoritaria(palabra):
	servicio = '/main/'
	palabra = palabra.lower()
	palabra = corrector.traducir(palabra)
	return URL+palabra+servicio

def obtener_url_consensuada(palabra):
    servicio = '/agreed/'
    palabra = palabra.lower()
    palabra = corrector.traducir(palabra)
    return URL+palabra+servicio

def obtener_medias(lista,n):
	if n > 0:
		for i in range(6):
			lista[i] = str(round(lista[i] / n,2))
		return lista
	else:
		return ["0","0","0","0","0","100"]

def incrementar_contador(contadores,i,mayor,indices,pocentaje_frase,pocentaje_palabra):
	contadores[i] = contadores[i]+1
	if contadores[i] > mayor:
		lista = [i]
		return contadores[i],lista,pocentaje_palabra
	elif contadores[i] == mayor:
		indices.append(i)
		return mayor,indices,pocentaje_frase
	else:
		return mayor,indices,pocentaje_frase

class InterpreteFrases():

	@staticmethod
	def emociones_frase(frase):
		palabras = procesador.procesar_frase(frase)
		emociones_frase = [0,0,0,0,0,0]
		no_encontradas = 0
		for palabra in palabras:
			destino = obtener_url(palabra)
			emociones_pal = interpreta.interpretar_porcentajes(destino)
			if len(emociones_pal) > 0:
				for i in range(6):
					emociones_frase[i] = emociones_frase[i] + int(emociones_pal[i])
			else:
				no_encontradas = no_encontradas + 1
		n = len(palabras) - no_encontradas
		emociones = obtener_medias(emociones_frase,n)
		return emociones

	@staticmethod
	def emociones_mayoritaria_frase(frase):
		palabras = procesador.procesar_frase(frase)
		contadores = [0,0,0,0,0,0]
		mayor = -1
		pocentaje_frase = 0
		indices = []
		for palabra in palabras:
			destino = obtener_url_mayoritaria(palabra)
			mayoritarias,pocentaje = interpreta.interpretar_mayoritaria(destino)
			if len(mayoritarias) == 1:
				i = emociones.index(mayoritarias[0])
				mayor,indices,pocentaje_frase = incrementar_contador(contadores,i,mayor,indices,pocentaje_frase,pocentaje)
			elif len(mayoritarias) == 2:
				i = emociones.index(mayoritarias[0])
				mayor,indices,pocentaje_frase = incrementar_contador(contadores,i,mayor,indices,pocentaje_frase,pocentaje)
				j = emociones.index(mayoritarias[1])
				mayor,indices,pocentaje_frase = incrementar_contador(contadores,j,mayor,indices,pocentaje_frase,pocentaje)
		if len(indices) == 1:
			i = indices[0]
			return [emociones[i]],pocentaje_frase
		elif len(indices) == 2:
			i = indices[0]
			j = indices[1]
			return [emociones[i],emociones[j]],pocentaje_frase
		else:
			return ["Neutral"],"100"
        
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
				mayor,indices,pocentaje_frase = incrementar_contador(contadores,i,mayor,indices,pocentaje_frase,pocentaje)
		if len(indices) == 1:
			i = indices[0]
			return [emociones[i]],pocentaje_frase
		else:
			return ["Neutral"],"100"
