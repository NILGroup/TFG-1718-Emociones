import Stemmer
import spacy

stemmer = Stemmer.Stemmer('spanish')
nlp = spacy.load('es')

def es_verbo(pos):
	return pos == "VERB"

def es_adjetivo(pos):
	return pos == "ADJ"

def es_sustantivo(pos):
	return pos == "NOUN"

def descartar_palabras(doc):
	palabras = []
	for token in (doc):
		pos = token.pos_
		palabra = stemmer.stemWord(token.text)
		if (es_verbo(pos) == True) or (es_adjetivo(pos) == True) or (es_sustantivo(pos) == True):
			if "trist" in palabra:
				palabras.append("trist")
			else:
				palabras.append(palabra)
	return palabras

class PalabrasEmocionales():

	@staticmethod
	def procesar_frase(frase):
		doc = nlp(frase)
		palabras = descartar_palabras(doc)
		return palabras