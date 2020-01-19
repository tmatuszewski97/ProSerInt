from rest_framework import serializers
from .models import Adres, DaneUzytkownika, Zgloszenie
from django.contrib.auth.models import User


# Serializery pracowników - adminów


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_staff']


class ZgloszenieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zgloszenie
        fields = '__all__'


class AdresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adres
        fields = '__all__'


class DaneUzytkownikaSerializer (serializers.ModelSerializer):
    class Meta:
        model = DaneUzytkownika
        fields = '__all__'


# Serializery klientów


class KlientGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class KlientPostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class DanePracownikaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DaneUzytkownika
        fields = ['telefon', 'specjalizacja']


class PracownikSerializer(serializers.ModelSerializer):
    dane = DanePracownikaSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'dane']


class ZgloszenieKlientGetSerializer(serializers.ModelSerializer):
    pracownik = PracownikSerializer(read_only=True)

    class Meta:
        model = Zgloszenie
        fields = ['id', 'dataUtworzenia', 'dataDostarczeniaUrzadzenia', 'dataOdbioruUrzadzenia', 'typZgloszenia',
                  'stanRealizacji', 'urzadzenie', 'trescZgloszenia', 'odpowiedzPracownika', 'cena', 'pracownik']


class ZgloszenieKlientPostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zgloszenie
        exclude = ['dataDostarczeniaUrzadzenia', 'dataOdbioruUrzadzenia', 'stanRealizacji', 'odpowiedzPracownika',
                   'cena', 'pracownik', 'tworcaZgloszenia']


class AdresKlientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adres
        exclude = ['uzytkownik']


class DaneUzytkownikaKlientSerializer(serializers.ModelSerializer):
    class Meta:
        model = DaneUzytkownika
        exclude = ['specjalizacja', 'stazPracy', 'uzytkownik']


class KlientDataSerializer (serializers.ModelSerializer):
    dane = DaneUzytkownikaKlientSerializer(read_only=True)
    adres = AdresKlientSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'dane', 'adres']
