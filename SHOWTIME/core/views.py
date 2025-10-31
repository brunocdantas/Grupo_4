from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def usuario(request):
    return render(request, 'core/usuario.html')
