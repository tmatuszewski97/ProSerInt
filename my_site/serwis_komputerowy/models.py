from django.db import models

# Create your models here.


class Adres(models.Model):
    idAdresu = models.AutoField(primary_key=True)
    miasto = models.CharField(max_length=35, blank=True)
    kodPocztowy = models.CharField(max_length=6, blank=True)
    nrDomu = models.IntegerField(max_length=3, blank=True)
    nrLok = models.IntegerField(max_length=3)


class Klient (models.Model):
    idKlienta = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=25, blank=True)
    nazwisko = models.CharField(max_length=35, blank=True)
    telefon = models.IntegerField(max_length=9, blank=True)
    adresEmail = models.CharField(max_length=35)
    Adres_idAdresu = models.OneToOneField(Adres, on_delete=models.CASCADE, primary_key=True)


class Pracownik (models.Model):
    idPracownika = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=25, blank=True)
    nazwisko = models.CharField(max_length=35, blank=True)
    telefon = models.IntegerField(max_length=9, blank=True)
    dataZatrudnienia = models.DateField(blank=True)
    dataZwolnienia = models.DateField()
    Adres_idAdresu = models.OneToOneField(Adres, on_delete=models.CASCADE)


class Zgloszenie (models.Model):
    idZgloszenia = models.AutoField(primary_key=True)
    dataPrzyjecia = models.DateField(blank=True)
    dataOdbioru = models.DateField()
    typ = models.CharField(max_length=35, blank=True)
    cenaOstateczna = models.CharField(max_length=35)
    Klient_idKlienta = models.ForeignKey(Klient, on_delete=models.CASCADE)


class Realizacja (models.Model):
    idRealizacji = models.AutoField(primary_key=True)
    stan = models.CharField(max_length=35, blank=True)
    urzadzenie = models.CharField(max_length=35, blank=True)
    opisUsterki = models.CharField(max_length=100, blank=True)
    aktualnaWycena = models.CharField(max_length=35, blank=True)
    Pracownik_idPracownika = models.ForeignKey(Pracownik, on_delete=models.CASCADE)
    Zgloszenie_idZgloszenia = models.ForeignKey(Zgloszenie, on_delete=models.CASCADE)
