# core/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Artist


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


def coringa_page(request):
    query = request.GET.get("q", "").strip()

    if query == "":
        return render(request, "core/artist_not_found.html")

    artist = Artist.objects.filter(name__icontains=query).first()

    if not artist:
        return render(request, "core/artist_not_found.html", {"query": query})

    top_musics_list = [x.strip() for x in artist.top_musics.split(",")]

    return render(request, "core/coringa.html", {
        "artist": artist,
        "top_musics": top_musics_list,
    })