
emociones = ["tristeza", "miedo", "alegria", "enfado", "sorpresa", "neutral"]

class Salida():

	@staticmethod
	def mostrar_porcentajes(porcentajes):
		if len(porcentajes) == 6:
			for i in range(6):
				print("Porcentaje de " + emociones[i] + ": "+ porcentajes[i] + "%")
		else:
			print("No se ha encontrado la palabra. Asegurese de haberla escrito bien.")

	@staticmethod
	def mostrar_consensuada(consensuada):
		print(consensuada)

	@staticmethod
	def mostrar_mayoritaria(mayoritarias,porcentaje):
		if len(mayoritarias) == 1:
			print("La mayoritaria es " + mayoritarias[0] + " con un " + porcentaje + "%")
		elif len(mayoritarias) == 2:
			print("Hay dos emociones mayoritarias: " + mayoritarias[0] + " y " + mayoritarias[1] + " con un " + porcentaje + "%")
		else:
			print("No se ha encontrado la palabra. Asegurese de haberla escrito bien.")