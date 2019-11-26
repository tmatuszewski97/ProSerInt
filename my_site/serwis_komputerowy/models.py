from django.db import models

# Create your models here.


class Adres(models.Model):
    miasto = models.CharField(max_length=35)
    ulica = models.CharField(max_length=35)
    nrDomu = models.IntegerField()
    nrLok = models.IntegerField()
    kodPocztowy = models.CharField(max_length=6)

    def __str__(self):
        return '%s %s %s %s %s' % (self.miasto, self.ulica, self.nrDomu, self.nrLok, self.kodPocztowy)


class Klient(models.Model):
    imie = models.CharField(max_length=35)
    nazwisko = models.CharField(max_length=35)
    telefon = models.CharField(max_length=15)
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
        ('NAP', 'Naprawa'),
        ('REK', 'Reklamacja'),
        ('INS_AKT_OPR', "Instalacja/aktualizacja oprogramowania"),
        ('ODZ_DAN', 'Odzyskiwanie danych'),
        ('DZI_ANT', "Działanie antywirusowe"),
    )
    rodzajRealizacji = (
        ('NOW', 'Nowe'),
        ('W_TRA', 'W trakcie realizacji'),
        ('GOT_DO_ODB', 'Gotowe do odbioru'),
    )
    dataUtworzenia = models.DateField()
    dataDostarczeniaUrzadzenia = models.DateField()
    dataOdbioruUrzadzenia = models.DateField()
    typZgloszenia = models.CharField(choices=rodzajZgloszenia, default='NAP', max_length=50)
    stanRealizacji = models.CharField(choices=rodzajRealizacji, default='NOW', max_length=50)
    urzadzenie = models.CharField(max_length=120)
    trescZgloszenia = models.CharField(max_length=120)
    odpowiedzPracownika = models.CharField(max_length=120)
    cena = models.CharField(max_length=35)
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    pracownik = models.ForeignKey(Pracownik, on_delete=models.CASCADE)
    firma = models.ForeignKey(Firma, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s %s %s %s %s %s %s' % (self.dataUtworzenia, self.dataDostarczeniaUrzadzenia,
                                               self.dataOdbioruUrzadzenia, self.typZgloszenia, self.stanRealizacji,
                                               self.urzadzenie, self.trescZgloszenia, self.odpowiedzPracownika,
                                               self.cena)
