from datetime import date, datetime, timedelta
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Pessoa

def home(request):
    pessoa = Pessoa.objects.all()
    return render(request, "index.html", {"pessoa":pessoa})


def salvar(request):
    vnome = request.POST.get("nome")
    vdata = request.POST.get("data")
    vhora = request.POST.get("hora")
    
    # Converter a string da data e hora para objetos de data e hora
    data = datetime.strptime(vdata, "%Y-%m-%d").date()
    hora = datetime.strptime(vhora, "%H:%M").time()

     # Obter a data e hora atuais
    data_atual = date.today()
    hora_atual = datetime.now().time()

    # Verificar se a data é anterior à data atual
    if data < data_atual:
        messages.error(request, "Não é possível agendar para uma data anterior à data atual.")
        return redirect(home)
    
    # Verificar se a data é igual à data atual e a hora é anterior à hora atual
    if data == data_atual and hora < hora_atual:
        messages.error(request, "Não é possível agendar para um horário anterior ao horário atual.")
        return redirect(home)

    # Verificar se já existe uma pessoa agendada para a mesma data e hora
    agendamentos_existentes = Pessoa.objects.filter(data=data, hora=hora)
    if agendamentos_existentes.exists():
        messages.error(request, "Já existe um agendamento para essa data e hora.")
        return redirect(home)
    
    horarios_disponiveis = []
    if not agendamentos_existentes.exists():
        horarios_disponiveis.append(hora_atual.strftime("%H:%M"))
    
    """
    else:
        # Definir o horário de início e fim permitido para agendamento
        hora_inicio = datetime.strptime("07:00", "%H:%M").time()
        hora_fim = datetime.strptime("22:00", "%H:%M").time()

        # Verificar se a hora fornecida está dentro do intervalo permitido
        if hora < hora_inicio or hora > hora_fim:
            messages.error(request, "A hora de agendamento está fora do intervalo permitido.")
        else:
            # Calcular o próximo horário disponível com intervalo de 45 minutos
            prox_hora = hora
            while Pessoa.objects.filter(data=data, hora=prox_hora).exists():
                prox_hora = (datetime.combine(date.today(), prox_hora) + timedelta(minutes=45)).time()

                # Verificar se o próximo horário está fora do intervalo permitido
        if prox_hora > hora_fim:
            messages.error(request, "Não há horários disponíveis dentro do intervalo permitido.")
            return redirect(home)
    """

    # Gravar no banco de dados do Django
    Pessoa.objects.create(nome=vnome, data=data, hora=hora)
    messages.success(request, "Agendamento realizado com sucesso.")
    
    # Retorna no html para visualização 
    pessoa = Pessoa.objects.all()
    return render(request, "index.html", {"pessoa": pessoa, "horarios_disponiveis": horarios_disponiveis})

def editar(request, pessoa_id):
    pessoa = Pessoa.objects.get(id=pessoa_id)
    if request.method == 'POST':
        vnome = request.POST.get('nome')
        vdata = request.POST.get('data')
        vhora = request.POST.get('hora')

        data = datetime.strptime(vdata, '%Y-%m-%d').date()
        hora = datetime.strptime(vhora, '%H:%M').time()

        pessoa.nome = vnome
        pessoa.data = data
        pessoa.hora = hora
        pessoa.save()

        messages.success(request, 'Agendamento atualizado com sucesso.')
        return redirect(home)

    return render(request, 'editar.html', {'pessoa': pessoa})

def deletar(request, pessoa_id):
    pessoa = Pessoa.objects.get(id=pessoa_id)
    pessoa.delete()
    #messages.success(request, 'Agendamento deletado com sucesso.')
    return redirect(home)