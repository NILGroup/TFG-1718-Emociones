import Stemmer
import spacy

stemmer = Stemmer.Stemmer('spanish')
nlp = spacy.load('es')

iguales = ["amig","espos","guap","habit","her","jubil","novi","odi","pioj"]
buscar_iguales = ["amigo","esposo","guapo","habitante","herido","jubiloso","novio","odio","piojo"]

derivables = ["afect","asesin","com","inspir","libr","salud","verd"]
derivadas = [["afecto","afectivo","afectiva","afectuso","afectividad"],["asesino","asesinato"],["comida","comedor"],["inspirado","inspiración"],["libre","librar"],["saludar","saludo"],["verde","verdoso","verdear"]]
buscar_derivables = ["afectar","asesinar","comer","inspirar","libro","salud","verdad"]

no_derivables = ["beb","pen","chic","call","cur","gener","muert","orden","orgull","sol","tont","victim","viv"]
alternativas = ["bebé","pene","chica","calle","cura","género","muerto","ordenador","orgullo","soleado","tontería","victimismo","vivido"]
buscar_no_derivables = ["bebida","pena","chico","callado","curar","generoso","muerte","ordenado","orgulloso","sol","tonto","victim","vivo"]

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
				procesada = procesar_palabra(token.text,palabra)
				palabras.append(procesada)
	return palabras

def procesar_palabra(palabra,lexema):
	if lexema in iguales:
		i = iguales.index(lexema)
		return buscar_iguales[i]
	elif lexema in no_derivables:
		i = no_derivables.index(lexema)
		if alternativas[i] == palabra:
			return palabra
		else:
			return buscar_no_derivables[i]
	elif lexema in derivables:
		i = derivables.index(lexema)
		if palabra in derivadas[i]:
			return derivadas[i][0]
		else:
			return buscar_derivables[i]
	else:
		return lexema

class PalabrasEmocionales():

	@staticmethod
	def procesar_frase(frase):
		doc = nlp(frase)
		palabras = descartar_palabras(doc)
		return palabras
