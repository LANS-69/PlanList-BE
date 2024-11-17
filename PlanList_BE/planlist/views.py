from django.shortcuts import render
from rest_framework import viewsets
from .serializer import BookSerializer, WishListSerializer
from .models import Books, WishList

class testButton(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Books.objects.all()

class WishListView(viewsets.ModelViewSet):
    serializer_class = WishListSerializer
    queryset = WishList.objects.all()

# Create your views here.
