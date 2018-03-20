from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from emocion.models import Emocion
from emocion.serializers import EmocionSerializer

class ListaPalabras(APIView):
    """
    Muestra la lista de palabras o añade una nueva.
    """
    def get(self,request,format=None):
        palabras = Emocion.objects.all()
        serializador = EmocionSerializer(palabras, many=True)
        return Response(serializador.data)

    def post(self,request,format=None):
        serializador = EmocionSerializer(data=request.data)
        if serializador.is_valid():
            seralizador.save()
            return Response(serializador.data, status=status.HTTP_201_CREATED)
        return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)

class DetallePalabra(APIView):
    """
    Muestra, actualiza o elimina una palabra concreta de la lista.
    """
    def get_object(self,pk):
        try:
            return Emocion.objects.get(pk=pk)
        except Emocion.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        palabra = self.get_object(pk)
        serializador = EmocionSerializer(palabra)
        return Response(serializador.data)

    def put(self,request,pk,format=None):
        palabra = self.get_object(pk)
        serializador = EmocionSerializer(palabra,data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response(seralizador.data)
        return Response(serializador.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        palabra = self.get_object(pk)
        palabra.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ObtenerPorcentajes(APIView):
    """
    Muestra, actualiza o elimina una palabra concreta de la lista.
    """
    def get_object(self,pk):
        try:
            return Emocion.objects.get(palabra=pk)
        except Emocion.DoesNotExist:
            raise Http404()

    def get_percentages(self,numeros):
        numeros = numeros.split(", ", 6)
        numeros[0] = numeros[0].lstrip("[")
        numeros[5] = numeros[5].rstrip("]")
        return numeros
        
    def get(self,request,pk,format=None):
        emociones = ["SADNESS", "FEAR", "JOY", "MADNESS", "SORPRISE", "NEUTRAL"]
        palabra = self.get_object(pk)
        porcentajes = palabra.porcentajes
        numeros = self.get_percentages(porcentajes)
        respuesta = ""
        for i in range(6):
            respuesta = respuesta + emociones[i] + ":" + str(numeros[i]) + "% "
            if i < 5:
                respuesta = respuesta + "|| "
        return Response(respuesta)

class getMain(APIView):

    def get_object(self,pk):
        try:
            return Emocion.objects.get(palabra=pk)
        except Emocion.DoesNotExist:
            raise Http404()
        
    def get(self,request,pk,format=None):
        emociones = ["SADNESS", "FEAR", "JOY", "MADNESS", "SORPRISE", "NEUTRAL"]
        palabra = self.get_object(pk)
        porcentajes = palabra.porcentajes
        numeros = ObtenerPorcentajes.get_percentages(self,porcentajes)
        respuesta = ""
        mayoritarias = [] 
        entro = False
        mayor = -1;
        for i in range(6):
            if(int(mayor) < int(numeros[i])):
                mayor = numeros[i]
                mayoritarias = []
                entro = False
                mayoritarias.append(i)
            elif (int(mayor) == int(numeros[i])):
                entro = True
                mayoritarias.append(i)
        if(entro):
            respuesta = "MAIN: " +  emociones[mayoritarias[0]] + ", " +  emociones[mayoritarias[1]]  + " || %: " + numeros[mayoritarias[0]]
        else:
            respuesta = "MAIN: " + emociones[mayoritarias[0]] + " || %: " + numeros[mayoritarias[0]]
        return Response(respuesta)

class getAgreed(APIView):

    def get_object(self,pk):
        try:
            return Emocion.objects.get(palabra=pk)
        except Emocion.DoesNotExist:
            raise Http404()
        
    def get(self,request,pk,format=None):
        emociones = ["SADNESS", "FEAR", "JOY", "MADNESS", "SORPRISE", "NEUTRAL"]
        palabra = self.get_object(pk)
        porcentajes = palabra.porcentajes
        numeros = ObtenerPorcentajes.get_percentages(self,porcentajes)
        respuesta = ""
        entro = False
        contador = 0
        while entro == False and contador < 6:
            if(100 == int(numeros[contador])):
                entro = True;
            else:
                contador = contador + 1
        if(entro):
            respuesta = "AGREED: " + emociones[contador]
        else:  
            respuesta = "NO AGREED EMOTION"
        return Response(respuesta)
        