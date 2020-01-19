from django.shortcuts import render
from django.http import HttpResponse
from .models import Adres, DaneUzytkownika, Zgloszenie
from . import serializers
from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth.models import User


# Create your views here.


def index(request):
    return HttpResponse("Witaj na stronie serwisu komputerowego!")


# Widoki pracowników - adminów


class UserList (generics.ListAPIView):
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = User.objects.all()


class UserDetail (generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = User.objects.all()


class ZgloszenieList (generics.ListCreateAPIView):
    serializer_class = serializers.ZgloszenieSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = Zgloszenie.objects.all()


class ZgloszenieDetail (generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ZgloszenieSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = Zgloszenie.objects.all()


class AdresList (generics.ListCreateAPIView):
    serializer_class = serializers.AdresSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = Adres.objects.all()


class AdresDetail (generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.AdresSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = Adres.objects.all()


class DaneUzytkownikaList (generics.ListCreateAPIView):
    serializer_class = serializers.DaneUzytkownikaSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = DaneUzytkownika.objects.all()


class DaneUzytkownikaDetail (generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.DaneUzytkownikaSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = DaneUzytkownika.objects.all()


# Widoki klientów


class ZgloszenieKlientList (generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.ZgloszenieKlientGetSerializer
        else:
            return serializers.ZgloszenieKlientPostUpdateSerializer

    def get_queryset(self):
        user = self.request.user
        return Zgloszenie.objects.filter(tworcaZgloszenia=user)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(tworcaZgloszenia=user)


class ZgloszenieKlientDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.ZgloszenieKlientGetSerializer
        else:
            return serializers.ZgloszenieKlientPostUpdateSerializer

    def get_queryset(self):
        user = self.request.user
        return Zgloszenie.objects.filter(tworcaZgloszenia=user)


class AdresKlientList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.AdresKlientSerializer

    def get_queryset(self):
        user = self.request.user
        return Adres.objects.filter(uzytkownik=user)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(uzytkownik=user)


class AdresKlientDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.AdresKlientSerializer

    def get_queryset(self):
        user = self.request.user
        return Adres.objects.filter(uzytkownik=user)


class DaneUzytkownikaKlientList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.DaneUzytkownikaKlientSerializer

    def get_queryset(self):
        user = self.request.user
        return DaneUzytkownika.objects.filter(uzytkownik=user)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(uzytkownik=user)


class DaneUzytkownikaKlientDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.DaneUzytkownikaKlientSerializer

    def get_queryset(self):
        user = self.request.user
        return DaneUzytkownika.objects.filter(uzytkownik=user)


class KlientPersonalList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.KlientGetSerializer
        else:
            return serializers.KlientPostUpdateSerializer

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(id=user.id)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(id=user.id)


class KlientPersonalDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.KlientGetSerializer
        else:
            return serializers.KlientPostUpdateSerializer

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(id=user.id)


class KlientDataList(generics.ListAPIView):
    serializer_class = serializers.KlientDataSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(id=user.id)
