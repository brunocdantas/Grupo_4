from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('usuario/', views.usuario, name='usuario'),
    path('favoritos/', views.favoritos, name='favoritos'),
    path('artistas/', views.artistas, name='artistas'),
    path('sobre/', TemplateView.as_view(template_name='core/sobre.html'), name='sobre'),
    path('logout/', views.custom_logout, name='logout'),
    path("coringa/", views.coringa_page, name="coringa_page"),
]
