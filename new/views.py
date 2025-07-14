from django.shortcuts import render
from rest_framework import generics
from .models import Chat
from .serializers import Seri
# Create your views here.
class View(generics.ListCreateAPIView):
    queryset=Chat.objects.all()
    serializer_class=Seri