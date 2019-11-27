from django.shortcuts import render
from django.http import HttpResponse
from .models import Adres, Firma, Klient, Pracownik, Zgloszenie
from . import serializers
from rest_framework import generics

# Create your views here.


def index(request):
    return HttpResponse("Witaj, znajdujesz sie w indeksie serwisu komputerowego.")


class GetAdres (generics.ListAPIView):
    queryset = Adres.objects.all()
    serializer_class = serializers.AdresSerializer
