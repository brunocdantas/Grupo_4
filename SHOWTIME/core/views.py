# core/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'core/home.html')

def usuario(request):
    if request.method == "POST":
        return redirect('home')
    return render(request, 'core/usuario.html')

@login_required
def favoritos(request):
    return render(request, 'core/favoritos.html')

def artistas(request):
    return render(request, 'core/artistas.html')

def custom_logout(request):
    """Faz logout e volta para a home."""
    logout(request)         
    return redirect('home') 
