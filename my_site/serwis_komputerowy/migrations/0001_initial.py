# Generated by Django 2.2.7 on 2020-01-19 13:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Zgloszenie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataUtworzenia', models.DateField(auto_now=True)),
                ('dataDostarczeniaUrzadzenia', models.DateField(blank=True, null=True)),
                ('dataOdbioruUrzadzenia', models.DateField(blank=True, null=True)),
                ('typZgloszenia', models.CharField(choices=[('NAPRAWA', 'Naprawa'), ('REKLAMACJA', 'Reklamacja'), ('INSTALACJA/AKTUALIZACJA OPROGRAMOWANIA', 'Instalacja/aktualizacja oprogramowania'), ('ODZYSKIWANIE DANYCH', 'Odzyskiwanie danych'), ('DZIALANIE ANTYWIRUSOWE', 'Działanie antywirusowe')], default='NAPRAWA', max_length=50)),
                ('stanRealizacji', models.CharField(choices=[('NOWE', 'Nowe'), ('W TRAKCIE REALIZACJI', 'W trakcie realizacji'), ('GOTOWE DO ODBIORU', 'Gotowe do odbioru'), ('ZAKONCZONE', 'Zakończone')], default='NOWE', max_length=50)),
                ('urzadzenie', models.CharField(max_length=120)),
                ('trescZgloszenia', models.CharField(blank=True, max_length=200, null=True)),
                ('odpowiedzPracownika', models.CharField(blank=True, max_length=200, null=True)),
                ('cena', models.CharField(blank=True, max_length=35, null=True)),
                ('pracownik', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pracownik', to=settings.AUTH_USER_MODEL)),
                ('tworcaZgloszenia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='klient', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'zgloszenia',
            },
        ),
        migrations.CreateModel(
            name='DaneUzytkownika',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefon', models.CharField(max_length=35)),
                ('specjalizacja', models.CharField(blank=True, max_length=35, null=True)),
                ('stazPracy', models.CharField(blank=True, max_length=35, null=True)),
                ('uzytkownik', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='dane', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'dane uzytkownikow',
            },
        ),
        migrations.CreateModel(
            name='Adres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miasto', models.CharField(max_length=35)),
                ('ulica', models.CharField(max_length=35)),
                ('nrDomu', models.IntegerField()),
                ('nrLok', models.IntegerField(blank=True, null=True)),
                ('kodPocztowy', models.CharField(max_length=6)),
                ('uzytkownik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adres', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'adresy',
            },
        ),
    ]
