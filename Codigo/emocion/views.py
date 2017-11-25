from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from emocion.models import Emocion
from emocion.serializers import EmocionSerializer
# Create your views here.

@csrf_exempt
def lista_palabras(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        palabras = Emocion.objects.all()
        serializador = EmocionSerializer(palabras, many=True)
        return JsonResponse(serializador.data, safe=False)

@csrf_exempt
def detalle_palabra(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        palabra = Emocion.objects.get(pk=pk)
    except Emocion.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializador = EmocionSerializer(palabra)
        return JsonResponse(serializador.data)

    elif request.method == 'DELETE':
        palabra.delete()
        return HttpResponse(status=204)