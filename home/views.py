from django.shortcuts import redirect, render

from usuarios.models import Usuario
from home.models import Contrato

# Create your views here.
def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        status = request.GET.get('status')
        apelido = str(usuario.apelido).upper()        

        contratos = Contrato.objects.all()
        context = {
            'status':status,
            'usuario': usuario,
            'apelido' : apelido,
            'contratos' : contratos,
        }

        return render(request, 'home.html', context)
    else:
        
        return redirect('auth/login/')
    

def contrato(request, id):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        status = request.GET.get('status')
        apelido = str(usuario.apelido).upper()        

        contrato = Contrato.objects.get(id = id)

        mes = converte_mes(contrato.data_contrato.month)

        context = {
            'status':status,
            'usuario': usuario,
            'apelido' : apelido,
            'contrato' : contrato,
            'mes' : mes,
        }

        return render(request, 'contrato.html', context)
    else:
        
        return redirect('auth/login/')
    

def cadastro_contrato(request):
    if request.session.get('usuario'):

        descricao = request.POST.get('descricao')
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        rua = request.POST.get('rua')
        numero = request.POST.get('numero')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')
        salao = request.POST.get('salao')
        festa = request.POST.get('festa')
        outra_festa = request.POST.get('outra_festa')
        qtd_convidados = request.POST.get('qtd_convidados')
        qtd_garcons = request.POST.get('qtd_garcons')
        data_evento = request.POST.get('data_evento')
        valor_aluguel = request.POST.get('valor_aluguel')
        valor_buffet = request.POST.get('valor_buffet')
        data_pagar = request.POST.get('data_pagar')

        if outra_festa != "" and outra_festa != None:
            festa = outra_festa

        try: 
            contrato = Contrato(descricao = descricao, 
                                nome_contratante = nome,
                                cpf_contratante =  cpf,
                                rua_contratante = rua,
                                numero_contratante = numero,
                                cidade_contratante = cidade,
                                estado_contratante = estado,
                                salao = salao,
                                evento = festa,
                                qtd_convidados = qtd_convidados,
                                qtd_garcons= qtd_garcons,
                                data_evento = data_evento,
                                valor = valor_aluguel,
                                valor_buffet = valor_buffet,
                                data_pagar = data_pagar)
            contrato.save()

            return redirect("/?status=1")
        except:
            return redirect("/?status=0")

    else:
        return redirect('auth/login/')
    

def converte_mes(n):
    if n == 1:
        n = "Janeiro"
    elif n == 2:
        n = "Feveriero"
    elif n == 3:
        n = "Março"
    elif n == 4:
        n = "Abril"
    elif n == 5:
        n = "Maio"
    elif n == 6:
        n = "Junho"
    elif n == 7:
        n = "Julho"
    elif n == 8:
        n = "Agosto "
    elif n == 9:
        n = "Setembro"
    elif n == 10:
        n = "Outubro"
    elif n == 11:
        n = "Novembro"
    elif n == 12:
        n = "Dezembro"

    return n