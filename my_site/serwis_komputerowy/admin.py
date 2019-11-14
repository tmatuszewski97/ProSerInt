from django.contrib import admin
from .models import Adres, Klient, Pracownik, Zgloszenie, Realizacja

# Register your models here.

admin.site.register(Adres)
admin.site.register(Klient)
admin.site.register(Pracownik)
admin.site.register(Zgloszenie)
admin.site.register(Realizacja)