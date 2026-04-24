from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.

from preco.models import Preco

# Create your views here.


def pesquisar(request):
    # formulário usando select, pegando id do medicamento
    medicamento_id = request.POST.get('medicamento_id')

    if not medicamento_id:

        messages.error(
            request, 'Selecione um medicamento para pesquisar.')

        return redirect('base:index')

    # Busca preços filtrando pelo ID
    precos = Preco.objects.filter(medicamento_id=medicamento_id) \
        .select_related('farmacia', 'medicamento') \
        .order_by('-data_hora')

    # Pegar da lista de preços apenas o mais recente por farmácia
    precos_unicos = {}
    for preco in precos:

        if preco.farmacia_id not in precos_unicos:
            precos_unicos[preco.farmacia_id] = preco

    return render(
        request,
        'pesquisa/precos.html',
        {
            'precos': precos_unicos.values(),
            'medicamento': precos[0].medicamento if precos else None
        })
