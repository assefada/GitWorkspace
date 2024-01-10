from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Drink
from .models import Event
from .serializers import DrinkSerializers
from .serializers import EventSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# FOR the DRINK OBJECT
@api_view(['GET', 'POST'])
def drink_list(request, format=None):
    if request.method == 'GET':
    #get all the drinks
    #serialize them
    #return jason
        drinks = Drink.objects.all()
        serializer = DrinkSerializers(drinks, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = DrinkSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request,id, format=None):
    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DrinkSerializers(drink)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = DrinkSerializers(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# FOR the EVENT OBJECT
@api_view(['GET', 'POST'])
def event_list(request,format=None):
    if request.method == 'GET':
        events = Event.objects.all()
        serializer = EventSerializers(events, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = EventSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def event_detail(request,id, format=None):
    try:
        event = Event.objects.get(pk=id)
    except Event.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EventSerializers(event)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = EventSerializers(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)