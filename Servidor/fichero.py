#CONFIGURACIÓN DE LOS SETTINGS DE DJANGO
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "servidor.settings")
import django
django.setup()
#IMPORTAR MODELO REST
from emociones.models import Palabra
from emociones.serializers import PalabraSerializer

def main():
    """
    La función de este programa es leer el archivo CSV en el que se encuentra el 
    diccionario afectivo que vamos a utilizar y subir las palabras que este contiene,
    junto a la información sobre ellas.
    """
    leer_diccionario()

def leer_diccionario():
    """
    Función que implementa la funcionalidad principal, lectura y subida de datos.
    """
    fichero = open("diccionario_afectivo.csv")
    fichero.readline() # ignoramos la primera linea 
    linea = fichero.readline()
    while linea != "":
        frase = linea.split(';', 6) # se trocea la línea para obtener los datos
        frase[6] = frase[6].strip("\n") # se elimina el salto de linea
        nueva_palabra = frase[0] # se coge la nueva palabra 
        emociones = []
        for j in range(6): # para cada columna, se traduce el grado de certeza
            emociones.append(parsear_emociones(frase[j+1]))
        subida = Palabra(palabra=nueva_palabra, porcentajes=emociones)
        subida.save()
        linea = fichero.readline() # se lee la siguiente palabra
    serializar_datos(subida)
    fichero.close()

def parsear_emociones(porcentaje):
    """
    Función que se encarga de transformar los datos numéricos sacados del
    CSV a porcentajes, que es lo que vamos a utilizar.
    """
    if porcentaje == "0,00":
        return 0
    elif porcentaje != "1,00":
        return int(porcentaje.lstrip("0,"))
    else:
        return 100
    
def serializar_datos(subida):
    """
    Función que se encarga de serializar los datos obtenidos del CSV.
    """   
    serializador = PalabraSerializer(Palabra.objects.all(), many=True)

main()
