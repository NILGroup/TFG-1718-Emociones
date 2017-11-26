from word import Palabra
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "palabra.settings")
import django
django.setup()
from emocion.models import Emocion
from emocion.serializers import EmocionSerializer

def parsear_emociones(porcentaje):
    if porcentaje == "0,00":
        return 0
    elif porcentaje != "1,00":
        return int(porcentaje.lstrip("0,"))
    else:
        return 100
       
def serializar_datos(subida):
    serializador = EmocionSerializer(Emocion.objects.all(), many=True)
    #print(serializador.data)

def leer_diccionario():
    fichero = open("diccionario_afectivo.csv")
    fichero.readline() # ignoramos la primera linea 
    linea = fichero.readline()
    while linea != "":
        frase = linea.split(';', 6) # se trocea la línea para obtener los datos
        frase[6] = frase[6].strip("\n") # se elimina el salto de linea
        pal = Palabra(frase[0])
        emociones = []
        for j in range(6):
            emociones.append(parsear_emociones(frase[j+1]))
        pal.porcentajes = emociones
        subida = Emocion(palabra=pal.palabra, porcentajes=pal.porcentajes)
        subida.save()
        linea = fichero.readline()
    serializar_datos(subida)
    fichero.close()

def main():
    leer_diccionario()
 
main()
