from word import Palabra
from django.core.management import setup_environ
from palabra import settings
setup_environ(settings)
from models import Emocion
from serializers import EmocionSerializer

def parsear_emociones(porcentaje):
    if porcentaje == "0,00":
        return 0
    elif porcentaje != "1,00":
        return int(porcentaje.lstrip("0,"))
    else:
        return 100
       
def serializar_datos(subida):
    serializador = EmocionSerializer(Emocion.objects.all(), many=True)
    print(serializador.data)

def leer_diccionario():
    fichero = open("diccionario_afectivo.csv")
    fichero.readline() # ignoramos la primera linea 
    fichero.readline()
    fichero.readline()
    fichero.readline()
    fichero.readline()
    linea = fichero.readline()
    for i in range(4):
        frase = linea.split(';', 6) # se trocea la línea para obtener los datos
        frase[6] = frase[6].strip("\n") # se elimina el salto de linea
        pal = Palabra(frase[0])
        emociones = []
        for j in range(6):
            emociones.append(parsear_emociones(frase[j+1]))
        pal.porcentajes = emociones
        #palabra.subir(subida)
        subida = Emocion(palabra=pal.palabra, procentajes=pal.porcentajes)
        subida.save()
        #palabra.show()
        linea = fichero.readline()
    serializar_datos(subida)
    fichero.close()

def main():
    leer_diccionario()
 
main()
