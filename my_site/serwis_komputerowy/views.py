from django.shortcuts import render
from django.http import HttpResponse
from .models import Adres, DaneUzytkownika, Zgloszenie
from . import serializers
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import permissions, authentication
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.contrib.auth.models import User, Group


# Create your views here.

def index(request):
    return HttpResponse("Witaj na stronie serwisu komputerowego!")


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UzytkownicyAdresZgloszenieSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UzytkownicyAdresZgloszenieSerializer


class DaneUzytkownikaList(generics.ListCreateAPIView):
    queryset = DaneUzytkownika.objects.all()
    serializer_class = serializers.DaneUzytkownikaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class DaneUzytkownikaDetail(generics.RetrieveUpdateAPIView):
    queryset = DaneUzytkownika.objects.all()
    serializer_class = serializers.DaneUzytkownikaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AdresList(generics.ListCreateAPIView):
    queryset = Adres.objects.all()
    serializer_class = serializers.AdresSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AdresDetail(generics.RetrieveUpdateAPIView):
    queryset = Adres.objects.all()
    serializer_class = serializers.AdresSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ZgloszenieList(generics.ListCreateAPIView):
    queryset = Zgloszenie.objects.all()
    serializer_class = serializers.ZgloszenieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ZgloszenieDetail(generics.RetrieveUpdateAPIView):
    queryset = Zgloszenie.objects.all()
    serializer_class = serializers.ZgloszenieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
