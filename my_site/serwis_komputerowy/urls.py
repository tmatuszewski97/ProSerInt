from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Widoki pracowników - adminów
    path('admin/user/', views.UserList.as_view(), name='UserList'),
    path('admin/user/<int:pk>/', views.UserDetail.as_view(), name='UserDetail'),
    path('admin/order/', views.ZgloszenieList.as_view(), name='ZgloszenieList'),
    path('admin/order/<int:pk>/', views.ZgloszenieDetail.as_view(), name='ZgloszenieDetail'),
    path('admin/adress/', views.AdresList.as_view(), name='AdresList'),
    path('admin/adress/<int:pk>/', views.AdresDetail.as_view(), name='AdresDetail'),
    path('admin/personal/', views.DaneUzytkownikaList.as_view(), name='DaneUzytkownikaList'),
    path('admin/personal/<int:pk>/', views.DaneUzytkownikaDetail.as_view(), name='DaneUzytkownikaDetail'),
    # Widoki klientów
    path('accounts/profile/', views.KlientDataList.as_view(), name='KlientDataList'),
    path('accounts/profile/personal', views.KlientPersonalList.as_view(), name='KlientPersonalList'),
    path('accounts/profile/personal/<int:pk>/', views.KlientPersonalDetail.as_view(), name='KlientPersonalDetail'),
    path('accounts/profile/tel', views.DaneUzytkownikaKlientList.as_view(), name='DaneUzytkownikaKlientList'),
    path('accounts/profile/tel/<int:pk>/', views.DaneUzytkownikaKlientDetail.as_view(), name='ZgloszenieKlientDetail'),
    path('accounts/profile/order', views.ZgloszenieKlientList.as_view(), name='ZgloszenieKlientList'),
    path('accounts/profile/order/<int:pk>/', views.ZgloszenieKlientDetail.as_view(), name='ZgloszenieKlientDetail'),
    path('accounts/profile/adress', views.AdresKlientList.as_view(), name='AdresKlientList'),
    path('accounts/profile/adress/<int:pk>/', views.AdresKlientDetail.as_view(), name='AdresKlientDetail'),
]
