# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('usuario/', views.usuario, name='usuario'),
    path('favoritos/', views.favoritos, name='favoritos'),
     path('artistas/', views.artistas, name='artistas'),
]
