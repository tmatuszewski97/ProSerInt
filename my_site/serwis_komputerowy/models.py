from django.db import models
from django.contrib import admin

# Create your models here.


class Adres(models.Model):
    miasto = models.CharField(max_length=35)
    ulica = models.CharField(max_length=35)
    nrDomu = models.IntegerField()
    nrLok = models.IntegerField(blank=True, null=True)
    kodPocztowy = models.CharField(max_length=6)

    def __str__(self):
        return '%s %s %s %s %s' % (self.miasto, self.ulica, self.nrDomu, self.nrLok, self.kodPocztowy)


class Klient(models.Model):
    imie = models.CharField(max_length=35)
    nazwisko = models.CharField(max_length=35)
    telefon = models.CharField(max_length=15, blank=True, null=True)
    adresEmail = models.CharField(max_length=35)
    adres = models.OneToOneField(Adres, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s %s' % (self.imie, self.nazwisko, self.telefon, self.adresEmail)


class Pracownik(models.Model):
    imie = models.CharField(max_length=35)
    nazwisko = models.CharField(max_length=35)
    specjalizacja = models.CharField(max_length=35)
    login = models.CharField(max_length=35)
    haslo = models.CharField(max_length=35)
    telefon = models.CharField(max_length=15)
    adresEmail = models.CharField(max_length=35)
    czyZalogowany = models.BooleanField()
    adres = models.OneToOneField(Adres, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s %s %s %s %s %s' % (self.imie, self.nazwisko, self.specjalizacja, self.login, self.haslo,
                                            self.telefon, self.adresEmail, self.czyZalogowany)


class Firma(models.Model):
    nazwa = models.CharField(max_length=35)
    adres = models.OneToOneField(Adres, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.nazwa


class Zgloszenie(models.Model):
    rodzajZgloszenia = (
        ('NAPRAWA', 'Naprawa'),
        ('REKLAMACJA', 'Reklamacja'),
        ('INSTALACJA/AKTUALIZACJA OPROGRAMOWANIA', "Instalacja/aktualizacja oprogramowania"),
        ('ODZYSKIWANIE DANYCH', 'Odzyskiwanie danych'),
        ('DZIALANIE ANTYWIRUSOWE', "Działanie antywirusowe"),
    )
    rodzajRealizacji = (
        ('NOWE', 'Nowe'),
        ('W TRAKCIE REALIZACJI', 'W trakcie realizacji'),
        ('GOTOWE DO ODBIORU', 'Gotowe do odbioru'),
    )
    dataUtworzenia = models.DateField()
    dataDostarczeniaUrzadzenia = models.DateField(blank=True, null=True)
    dataOdbioruUrzadzenia = models.DateField(blank=True, null=True)
    typZgloszenia = models.CharField(choices=rodzajZgloszenia, default='NAPRAWA', max_length=50)
    stanRealizacji = models.CharField(choices=rodzajRealizacji, default='NOWE', max_length=50)
    urzadzenie = models.CharField(max_length=120)
    trescZgloszenia = models.CharField(max_length=120, blank=True, null=True)
    odpowiedzPracownika = models.CharField(max_length=120, blank=True, null=True)
    cena = models.CharField(max_length=35, blank=True, null=True)
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    pracownik = models.ForeignKey(Pracownik, on_delete=models.CASCADE)
    firma = models.ForeignKey(Firma, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s %s %s %s %s %s %s' % (self.dataUtworzenia, self.dataDostarczeniaUrzadzenia,
                                               self.dataOdbioruUrzadzenia, self.typZgloszenia, self.stanRealizacji,
                                               self.urzadzenie, self.trescZgloszenia, self.odpowiedzPracownika,
                                               self.cena)
