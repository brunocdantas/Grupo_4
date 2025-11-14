from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def usuario(request):
    return render(request, 'core/usuario.html')

def favoritos(request):
    return render(request, 'core/favoritos.html')
from django.shortcuts import render, redirect

def home(request):
    user_email = request.session.get('user_email')  # pega email se estiver logado
    return render(request, 'core/home.html', {'user_email': user_email})

from django.shortcuts import render, redirect

def home(request):
    # se quiser, dá pra usar request.session aqui depois
    return render(request, 'core/home.html')

def usuario(request):
    if request.method == "POST":
        # aqui dá pra checar email/senha depois
        return redirect('home')
    return render(request, 'core/usuario.html')

def favoritos(request):
    return render(request, 'core/favoritos.html')

def artistas(request):
    return render(request, 'core/artistas.html')

