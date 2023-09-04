from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render
from .models import Usuario
from hashlib import sha256 ## 

def login(request):
    if request.session.get('usuario'):
        return redirect('/')
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})


def valida_login(request):
    apelido = request.POST.get('apelido')
    senha = request.POST.get('senha')
    
    usuario = Usuario.objects.filter(apelido = apelido).filter(senha = senha)

    ## SE apelido ou senha for igual a zero 
    if len(apelido.strip()) == 0 or len(senha.strip()) == 0: ##len() se refere ao tamanho e .strip() retira os espaços do inicio e do final.
        return redirect('/auth/login/?status=1')
    elif(len(usuario) == 0):
        return redirect('/auth/login/?status=1')## se não existir o usuario no sistema redireciona para login com status 1
    elif len(usuario) > 0:
        request.session['usuario'] = usuario[0].id ##session funciona como se fosse uma variavel global para autenticar o usuario.
        return redirect('home')


def sair(request):
    ## request.session = None
    request.session.flush() ## .flush() garante que a session esteja completamente vazia! 
    return redirect('/auth/login')