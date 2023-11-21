from django.shortcuts import render
from .models import Usuario
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('usuario')
    novo_usuario.senha = request.POST.get('senha')
    novo_usuario.save()
    
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    return render(request,'usuarios/usuarios.html',usuarios)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            return redirect('pagina_inicial') 
        
        else:

            pass
    return render(request, 'usuarios/login.html')