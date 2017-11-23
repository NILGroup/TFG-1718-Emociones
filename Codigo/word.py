class Palabra:
	
	def __init__(self,palabra):
		self.palabra = palabra
		self.porcentajes = []

	def show(self):
		print("Palabra: " + self.palabra)
		print("Grado de tristeza: " + repr(self.porcentajes[0]))
		print("Grado de miedo: " + repr(self.porcentajes[1]))
		print("Grado de alegria: " + repr(self.porcentajes[2]))
		print("Grado de enfado: " + repr(self.porcentajes[3]))
		print("Grado de sorpresa: " + repr(self.porcentajes[4]))
		print("Grado de neutral: " + repr(self.porcentajes[5]))
		print("---------------------------")