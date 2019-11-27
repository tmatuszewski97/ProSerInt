from rest_framework import serializers
from .models import Adres, Firma, Klient, Pracownik, Zgloszenie


class AdresSerializer (serializers.ModelSerializer):
    class Meta:
        model = Adres
        fields = '__all__'


class FirmaSerializer (serializers.ModelSerializer):
    class Meta:
        model = Firma
        fields = '__all__'


class KlientSerializer (serializers.ModelSerializer):
    class Meta:
        model = Klient
        fields = '__all__'


class PracownikSerializer (serializers.ModelSerializer):
    class Meta:
        model = Pracownik
        fields = '__all__'
        read_only_fields = ['czyZalogowany']


class ZgloszenieSerializer (serializers.ModelSerializer):
    class Meta:
        model = Zgloszenie
        fields = '__all__'