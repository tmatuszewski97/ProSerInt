from django.shortcuts import render
from django.http import HttpResponse
from .models import Adres, Firma, Klient, Pracownik, Zgloszenie
from . import serializers
from rest_framework import generics
from django.views.generic.edit import CreateView;


# Create your views here.


def index(request):
    return HttpResponse("Witaj na stronie serwisu komputerowego!")


class GetPracownik(generics.ListAPIView):
    queryset = Pracownik.objects.all()
    serializer_class = serializers.PracownikSerializer


class GetFirma(generics.ListAPIView):
    queryset = Firma.objects.all()
    serializer_class = serializers.FirmaSerializer


class WyswietlZgloszenia(generics.ListAPIView):
    queryset = Zgloszenie.objects.all()
    serializer_class = serializers.PracownikZgloszenieSerializer


class DodajZgloszenie(generics.ListCreateAPIView):
    queryset = Zgloszenie.objects.all()
    serializer_class = serializers.ZgloszenieSerializer
