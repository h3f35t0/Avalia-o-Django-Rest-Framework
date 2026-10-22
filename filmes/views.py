
from .models import Filmes, Generos
from rest_framework import viewsets
from django.shortcuts import render
from .serializers import FilmesSerializer, GenerosSerializer
from django_filters.rest_framework import DjangoFilterBackend

class GenerosViewSet(viewsets.ModelViewSet):
    queryset = Generos.objects.all()
    serializer_class = GenerosSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nome']

class FilmesViewSet(viewsets.ModelViewSet):
    queryset = Filmes.objects.all()
    serializer_class = FilmesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['titulo', 'genero', 'ano_lancamento']

def inicio(request):
    return render(request, 'filmes/inicio.html')