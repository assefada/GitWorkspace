from rest_framework import serializers
from .models import Drink, Event

class DrinkSerializers(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id', 'name', 'description']

class EventSerializers(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'description','qr_code', 'date']