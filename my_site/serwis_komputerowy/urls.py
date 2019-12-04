from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('zgloszenie', views.WyswietlZgloszenia.as_view(), name="Lista zgłoszeń"),
    path('zgloszenie/dodaj', views.DodajZgloszenie.as_view(), name="Nowe zgłoszenie"),
    path('pracownicy', views.GetPracownik.as_view(), name="Lista pracowników"),
    path('firma', views.GetFirma.as_view(), name="Nazwa firmy"),
]
