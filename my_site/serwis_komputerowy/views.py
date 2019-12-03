from django.shortcuts import render
from django.http import HttpResponse
from .models import Adres, Firma, Klient, Pracownik, Zgloszenie
from . import serializers
from rest_framework import generics
from rest_framework import authentication, permissions

# Create your views here.


def index(request):
    return HttpResponse("Witaj, znajdujesz sie w indeksie serwisu komputerowego.")


class GetPracownik (generics.ListAPIView):
    queryset = Pracownik.objects.all()
    serializer_class = serializers.PracownikSerializer


class ZgloszenieList (generics.ListCreateAPIView):
    queryset = Zgloszenie.objects.all()
    serializer_class = serializers.ZgloszenieSerializer


class GetKlient(generics.ListAPIView):
    queryset = Klient.objects.all()
    serializer_class = serializers.KlientSerializer


