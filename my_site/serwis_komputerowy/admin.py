from django.contrib import admin
from .models import Adres, Firma, Klient, Pracownik, Zgloszenie

# Register your models here.

admin.site.register(Adres)
admin.site.register(Firma)
admin.site.register(Klient)
admin.site.register(Pracownik)
admin.site.register(Zgloszenie)
