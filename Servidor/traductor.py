import requests
from interprete_palabras import InterpretePalabras
from interprete_frases import InterpreteFrases
from salida import Salida
import corrector

_salida = Salida()
URL = 'http://127.0.0.1:8000/emociones/' # URL del servidor

def interpretar_palabra(palabra):
	servicios = ['/percentages/', '/agreed/', '/main/']
	destinos = []
	interpreta = InterpretePalabras()
	buscada = palabra.lower()
	#buscada = corrector.traducir(buscada)
	for i in range(3):
		dest = URL + palabra + servicios[i]
		destinos.append(dest)
	porcentajes = interpreta.interpretar_porcentajes(destinos[0])
	_salida.mostrar_porcentajes(porcentajes)
	consensuada = interpreta.interpretar_consensuada(destinos[1])
	_salida.mostrar_consensuada(consensuada)
	mayoritarias, porcentaje = interpreta.interpretar_mayoritaria(destinos[2])
	_salida.mostrar_mayoritaria(mayoritarias,porcentaje)

def interpretar_frase(frase):
	interpreta = InterpreteFrases()
	porcentajes = interpreta.emociones_frase(frase)
	_salida.mostrar_porcentajes(porcentajes)
	mayoritarias,porcentaje = interpreta.emociones_mayoritaria_frase(frase)
	_salida.mostrar_mayoritaria(mayoritarias,porcentaje)

def main():
	print("Introduce tu texto:")
	texto = input()
	while texto != "salir" and texto != "Salir":
		print("-----------------------------------------------------------")
		if len(texto.split(" ")) == 1:
			interpretar_palabra(texto)
		elif len(texto.split('.')) <= 2:
			interpretar_frase(texto)
		else:
			print("Es un texto")
		print("-----------------------------------------------------------")
		texto = input()
main()