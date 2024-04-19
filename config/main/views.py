from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status 
from .models import *
from .serializers import *

# Create your views here.
class GameListCreateAPIView(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    

