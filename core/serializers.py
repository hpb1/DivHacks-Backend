from rest_framework import serializers
from .models import TreeModel

class TreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreeModel
        fields = '__all__'