from django.shortcuts import redirect, render

from usuarios.models import Usuario

# Create your views here.
def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        status = request.GET.get('status')
        apelido = str(usuario.apelido).upper()        

        context = {
            'status':status,
            'usuario': usuario,
            'apelido' : apelido,
        }

        return render(request, 'home.html', context)
    else:
        
        return redirect('auth/login/')