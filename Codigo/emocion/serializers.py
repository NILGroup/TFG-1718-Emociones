from rest_framework import serializers
from emocion.models import Emocion, EMOCIONES, TEST_DATA

class EmocionSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	palabra = serializers.CharField(required = True, max_length=30, allow_blank=True)
	porcentajes = serializers.CharField(validators=[TEST_DATA], max_length = 100)
	emocion_mayor = serializers.ChoiceField(choices = EMOCIONES, default = "NEUTRAL")

	def create(self, validated_data):
		"""
		Create and return a new "emocion" instance, given the validated data
		"""
		return Emocion.objects.create(**validated_data)

	def update(self, instance, validated_data):
		"""
		Update and return an existing "emocion" instance, given the validated data.
		"""
		instance.palabra = validated_data.get('palabra', instance.palabra)
		instance.porcentajes = validated_data.get('porcentajes', instance.porcentajes)
		instance.emocion_mayor = validated_data.get('emocion_mayor', instance.emocion_mayor)
		instance.save()
		return instance