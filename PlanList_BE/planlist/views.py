from django.shortcuts import render
from rest_framework import viewsets
from .serializer import MovieSerializer, WishListSerializer, TvShowSerializer
from .models import Movie, WishList, TvShow


class WishListView(viewsets.ModelViewSet):
    serializer_class = WishListSerializer
    queryset = WishList.objects.all()


class MovieView(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

class TvShowView(viewsets.ModelViewSet):
    serializer_class = TvShowSerializer
    queryset = TvShow.objects.all()

# Create your views here.
