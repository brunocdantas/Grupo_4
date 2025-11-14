# core/urls.py
from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('usuario/', views.usuario, name='usuario'),
    path('favoritos/', views.favoritos, name='favoritos'),
    path('artistas/', views.artistas, name='artistas'),
    path("", views.home, name="home"),
    path("sobre/", TemplateView.as_view(template_name="core/sobre.html"), name="sobre"),
]
