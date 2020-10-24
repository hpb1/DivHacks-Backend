from rest_framework import serializers
from .models import ShelterModel

class ShelterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShelterModel
        fields = '__all__'