from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from emocion.models import Emocion
from emocion.serializers import EmocionSerializer

@api_view(['GET', 'POST'])
def lista_palabras(request, format=None):
    """
    Muestra la lista de palabras o añade una nueva.
    """
    if request.method == 'GET':
        palabras = Emocion.objects.all()
        serializador = EmocionSerializer(palabras, many=True)
        return Response(serializador.data)
    elif request.method == 'POST':
        serializador = EmocionSerializer(data=request.POST)
        if serializador.is_valid():
            seralizador.save()
            return Response(serializador.data, status=status.HTTP_201_CREATED)
        return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def detalle_palabra(request, pk, format=None):
    """
    Muestra, añade o elimina una palabra concreta de la lista.
    """
    try:
        palabra = Emocion.objects.get(pk=pk)
    except Emocion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializador = EmocionSerializer(palabra)
        return Response(serializador.data)
    elif request.method == 'PUT':
        serializador = EmocionSerializer(palabra,data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response(seralizador.data)
        return Response(serializador.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        palabra.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)