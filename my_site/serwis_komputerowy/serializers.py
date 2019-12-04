from rest_framework import serializers
from .models import Adres, Firma, Klient, Pracownik, Zgloszenie


class AdresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adres
        fields = '__all__'


class FirmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firma
        exclude = ['id', 'adres']


class KlientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klient
        fields = '__all__'


class PracownikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pracownik
        exclude = ['id', 'login', 'haslo', 'telefon', 'czyZalogowany', 'adres']


class ZgloszenieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zgloszenie
        fields = '__all__'


class PracownikZgloszenieSerializer(serializers.ModelSerializer):
    pracownik = PracownikSerializer()

    class Meta:
        model = Zgloszenie
        fields = ('dataUtworzenia', 'dataDostarczeniaUrzadzenia', 'typZgloszenia',
                  'stanRealizacji', 'urzadzenie', 'trescZgloszenia',  'pracownik', 'odpowiedzPracownika', 'cena',
                  'dataOdbioruUrzadzenia')
