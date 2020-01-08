from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.UserList.as_view(), name='UserList'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='UserDetail'),
    path('adress/', views.AdresList.as_view(), name='AdresList'),
    path('adress/<int:pk>/', views.AdresDetail.as_view(), name='AdresDetail'),
    path('notification/', views.ZgloszenieList.as_view(), name='NotificationList'),
    path('notification/<int:pk>/', views.ZgloszenieDetail.as_view(), name='NotificationDetail'),
]
