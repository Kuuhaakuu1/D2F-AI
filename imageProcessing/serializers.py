# your_app/serializers.py
from rest_framework import serializers

class DataSerializer(serializers.Serializer):
    message = serializers.CharField()
    url = serializers.CharField()