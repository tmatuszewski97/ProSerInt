from django.db import models
from django.contrib import admin
from django.conf import settings

# Create your models here.


class Adres(models.Model):
    miasto = models.CharField(max_length=35)
    ulica = models.CharField(max_length=35)
    nrDomu = models.IntegerField()
    nrLok = models.IntegerField(blank=True, null=True)
    kodPocztowy = models.CharField(max_length=6)
    uzytkownik = models.ForeignKey('auth.User', related_name='adres', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'adresy'

    def __str__(self):
        return '%s %s %s %s %s' % (self.miasto, self.ulica, self.nrDomu, self.nrLok, self.kodPocztowy)


class DaneUzytkownika(models.Model):
    telefon = models.CharField(max_length=35)
    specjalizacja = models.CharField(max_length=35, blank=True, null=True)
    stazPracy = models.CharField(max_length=35, blank=True, null=True)
    uzytkownik = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'dane uzytkownikow'

    def __str__(self):
        return '%s %s %s' % (self.telefon, self.specjalizacja, self.stazPracy)


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
        ('ZAKONCZONE', 'Zakończone'),
    )
    dataUtworzenia = models.DateField(auto_now=True)
    dataDostarczeniaUrzadzenia = models.DateField(blank=True, null=True)
    dataOdbioruUrzadzenia = models.DateField(blank=True, null=True)
    typZgloszenia = models.CharField(choices=rodzajZgloszenia, default='NAPRAWA', max_length=50)
    stanRealizacji = models.CharField(choices=rodzajRealizacji, default='NOWE', max_length=50)
    urzadzenie = models.CharField(max_length=120)
    trescZgloszenia = models.CharField(max_length=200, blank=True, null=True)
    odpowiedzPracownika = models.CharField(max_length=200, blank=True, null=True)
    cena = models.CharField(max_length=35, blank=True, null=True)
    pracownik = models.ForeignKey('auth.User', related_name='Pracownicy', blank=True, null=True, on_delete=models.CASCADE)
    tworcaZgloszenia = models.ForeignKey('auth.User', related_name='Klienci', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'zgloszenia'

    def __str__(self):
        return '%s %s %s %s %s %s %s %s %s' % (self.dataUtworzenia, self.dataDostarczeniaUrzadzenia,
                                               self.dataOdbioruUrzadzenia, self.typZgloszenia, self.stanRealizacji,
                                               self.urzadzenie, self.trescZgloszenia, self.odpowiedzPracownika,
                                               self.cena)


