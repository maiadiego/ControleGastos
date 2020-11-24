from django.http import HttpResponse
import datetime
from django.shortcuts import render, redirect
from .models import Transacao  # importando uma tabela do meu banco de dados
from .models import Categoria
from .form import TransacaoForm # importando a classe para formulários


def home(request):
    # aqui dentro vai o html
    # html = "<html><body> Testando </body></html>"
    # return HttpResponse(html)
    data = {}
    data['now'] = datetime.datetime.now() # passando uma variável q vai ser manipulada dentro do html
    data['transacoes'] = ['t1', 't2', 't3']
    return render(request, 'contas/home.html', data) # para retornar um template ao invés de um html puro



def listagem(request):
    """ objects é um manager, que é uma classe que o django impelementa
        para todos os models para poder realizar operações de busca, listagem, etc. """
    data = {}
    data['transacoes'] = Transacao.objects.all()
    data['categorias'] = Categoria.objects.all()

    return render(request, 'contas/tabela.html', data)


def nova_transacao(request):
    form = TransacaoForm(request.POST or None)
    data = {}
    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data['form'] = form
    return render(request, 'contas/form.html', data)


def update(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data = {}
    data['form'] = form
    data['transacao'] = transacao   # mandar o objeto para o form.html
    return render(request, 'contas/form.html', data)


def delete(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    return redirect('url_listagem')





