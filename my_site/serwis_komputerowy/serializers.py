from rest_framework import serializers
from .models import Adres, DaneUzytkownika, Zgloszenie
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class AdresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adres
        fields = '__all__'


class DaneUzytkownikaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DaneUzytkownika
        fields = '__all__'


class ZgloszenieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zgloszenie
        exclude = ['tworcaZgloszenia']


class ZgloszenieUserSerializer (serializers.ModelSerializer):
    class Meta:
        model = Zgloszenie
        fields = ['urzadzenie', 'trescZgloszenia']


class UzytkownicyAdresZgloszenieSerializer(serializers.ModelSerializer):
    adres = AdresSerializer(read_only=True, many=True)
    zgloszenie = ZgloszenieSerializer(source="Klienci", read_only=True, many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'adres', 'zgloszenie']