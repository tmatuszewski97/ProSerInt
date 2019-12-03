from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('zgloszenia', views.ZgloszenieList.as_view(), name="Lista zgłoszeń"),
    path('pracownicy', views.GetPracownik.as_view(), name="Lista pracowników"),
    path('klienci', views.GetKlient.as_view(), name="Lista klientów")
]