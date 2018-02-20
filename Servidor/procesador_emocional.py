import spacy

nlp = spacy.load('es')
adj_plural = ["abejas", "apuros", "celos", "piojos"] 
sus_plural =["aplausos", "deportes", "ganancias", "gérmenes", "noticias", "nubes", "recuerdos", "tijeras", "viajes"]

def es_participio(etiqueta):
	return "VerbForm=Part" in etiqueta.split("|")

def es_verbo(pos):
	return pos == "VERB"

def es_adjetivo(pos):
	return pos == "ADJ"

def es_sustantivo(pos):
	return pos == "NOUN"

def derivado_verbo(lexema,pos):
	doc = nlp(lexema)
	return (pos == "NOUN" and doc[0].pos_ == "VERB")

def procesar_palabra(palabra):
		lexema = palabra.lemma_
		pos = palabra.pos_
		etiqueta = palabra.tag_
		if (es_participio(etiqueta) == True):
			return True, palabra.text
		elif (es_verbo(pos) == True):
			return True, lexema
		elif (es_adjetivo(pos) == True):
			if palabra.text in adj_plural:
				return True, palabra.text
			else:
				return True, lexema
		elif (es_sustantivo(pos) == True):
			if palabra.text in sus_plural:
				return True, palabra.text
			else:
				return True, lexema
		elif (derivado_verbo(lexema,pos) == True):
			return True, palabra.text
		else:
			return False, ""
class PalabrasEmocionales():

	@staticmethod
	def procesar_frase(frase):
		palabras = []
		doc = nlp(frase)
		for token in (doc):
			emocional, palabra = procesar_palabra(token)
			if emocional == True:
				palabras.append(palabra)
		return palabras