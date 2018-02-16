import spacy
from interprete_palabras import InterpretePalabras
import corrector

interpreta = InterpretePalabras()
nlp = spacy.load('es')
URL = 'http://127.0.0.1:8000/emociones/'
emociones = ["tristeza", "miedo", "alegria", "enfado", "sorpresa", "neutral"]

def palabras_emocionales(doc):
		palabras = []
		for token in doc:
			palabras.append(token.text)
		return palabras

def obtener_url(palabra):
	servicio = '/percentages/'
	palabra = palabra.lower()
	palabra = corrector.traducir(palabra)
	return URL+palabra+servicio

def obtener_url_mayoritaria(palabra):
	servicio = '/percentages/'
	palabra = palabra.lower()
	palabra = corrector.traducir(palabra)
	return URL+palabra+servicio

def obtener_medias(lista,n):
	for i in range(6):
		lista[i] = str(lista[i] / n)
	return lista

class InterpreteFrases():

	@staticmethod
	def mostrar_emociones_frase(emociones):
		interpreta.mostrar_porcentajes(emociones)

	@staticmethod
	def emociones_frase(frase):
		doc = nlp(frase)
		palabras = palabras_emocionales(doc)
		emociones_fr = [0,0,0,0,0,0]
		for palabra in palabras:
			destino = obtener_url(palabra)
			emociones_pal = interpreta.interpretar_porcentajes(destino)
			for i in range(6):
				emociones_fr[i] = emociones_fr[i] + int(emociones_pal[i])
		emociones = obtener_medias(emociones_fr,len(palabras))
		return emociones

	@staticmethod
	def emociones__mayoritaria_frase(frase):
		doc = npl(frase)
		palabras = palabras_emocionales(doc)
		contadores = [0,0,0,0,0,0]
		for palabra in palabras:
			destino = obtener_url_mayoritaria(palabra)
			mayoritarias,pocentaje = interpreta.interpretar_mayoritaria(destino)
