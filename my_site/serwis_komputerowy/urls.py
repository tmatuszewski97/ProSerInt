from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.UserList.as_view(), name='UserList'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='UserDetail'),
    path('users/data/', views.DaneUzytkownikaList.as_view(), name='UserData'),
    path('users/data/<int:pk>/', views.DaneUzytkownikaDetail.as_view(), name='UserDataDetail'),
    path('adressess/', views.AdresList.as_view(), name='AdressList'),
    path('adressess/<int:pk>/', views.AdresDetail.as_view(), name='AdressDetail'),
    path('notifications/', views.ZgloszenieList.as_view(), name='NotificationList'),
    path('notifications/<int:pk>/', views.ZgloszenieDetail.as_view(), name='NotificationDetail'),
]
