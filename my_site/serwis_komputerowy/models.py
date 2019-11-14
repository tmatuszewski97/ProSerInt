from django.db import models
from django.core.validators import MinLengthValidator
from django.core.validators import MaxLengthValidator

# Create your models here.


class Adres(models.Model):
    idAdresu = models.AutoField(primary_key=True)
    miasto = models.CharField(max_length=35, null=False)
    kodPocztowy = models.CharField(max_length=6, null=False)
    nrDomu = models.IntegerField(validators=[MaxLengthValidator(3)], null=False)
    nrLok = models.IntegerField(validators=[MaxLengthValidator(3)])


class Klient (models.Model):
    idKlienta = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=25, null=False)
    nazwisko = models.CharField(max_length=35, null=False)
    telefon = models.IntegerField(validators=[MinLengthValidator(9), MaxLengthValidator(9)], null=False)
    adresEmail = models.CharField(max_length=35)
    adres = models.OneToOneField(Adres, on_delete=models.CASCADE)


class Pracownik (models.Model):
    idPracownika = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=25, null=False)
    nazwisko = models.CharField(max_length=35, null=False)
    telefon = models.IntegerField(validators=[MaxLengthValidator(9)], null=False)
    dataZatrudnienia = models.DateField(null=False)
    dataZwolnienia = models.DateField()
    adres = models.OneToOneField(Adres, on_delete=models.CASCADE)


class Zgloszenie (models.Model):
    idZgloszenia = models.AutoField(primary_key=True)
    dataPrzyjecia = models.DateField(null=False)
    dataOdbioru = models.DateField()
    typ = models.CharField(max_length=35, null=False)
    cenaOstateczna = models.CharField(max_length=35)
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)


class Realizacja (models.Model):
    idRealizacji = models.AutoField(primary_key=True)
    stan = models.CharField(max_length=35, null=False)
    urzadzenie = models.CharField(max_length=35, null=False)
    opisUsterki = models.CharField(max_length=100, null=False)
    aktualnaWycena = models.CharField(max_length=35, null=False)
    pracownik = models.ForeignKey(Pracownik, on_delete=models.CASCADE)
    zgloszenie = models.ForeignKey(Zgloszenie, on_delete=models.CASCADE)
