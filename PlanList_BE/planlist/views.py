from django.shortcuts import render
from rest_framework import viewsets
from .serializer import BookSerializer
from .models import Books

class testButton(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Books.objects.all()

# Create your views here.
