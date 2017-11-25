from word import Palabra

def parsear_emociones(porcentaje):
    if porcentaje == "0,00":
        return 0
    elif porcentaje != "1,00":
        return int(porcentaje.lstrip("0,"))
    else:
        return 100

"""        
def serializar_datos(subida):
    serializador = EmocionSerializer(subida)
    serializador.data
    content = JSONRenderer().render(serializador.data)
    print(content)
"""

def leer_diccionario():
    fichero = open("diccionario_afectivo.csv")
    fichero.readline() # ignoramos la primera linea 
    linea = fichero.readline()
    for i in range(4):
        frase = linea.split(';', 6) # se trocea la línea para obtener los datos
        frase[6] = frase[6].strip("\n") # se elimina el salto de linea
        palabra = Palabra(frase[0])
        emociones = []
        for j in range(6):
            emociones.append(parsear_emociones(frase[j+1]))
        palabra.porcentajes = emociones
        #palabra.subir(subida)
        palabra.show()
        linea = fichero.readline()
    #serializar_datos(subida)
    fichero.close()

def main():
    leer_diccionario()
 
main()
