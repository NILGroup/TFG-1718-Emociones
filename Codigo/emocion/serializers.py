from rest_framework import serializers
from emocion.models import Emocion

class EmocionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emocion
        fields = ('id', 'palabra', 'porcentajes')