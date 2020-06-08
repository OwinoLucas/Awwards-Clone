from rest_framework import serializers
from .models import Events

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ('id', 'event', 'description', 'price')