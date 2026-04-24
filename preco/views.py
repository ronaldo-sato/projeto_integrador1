from django.contrib import messages

from django.shortcuts import redirect, render, get_object_or_404

from .models import Preco, Farmacia, Medicamento

# Create your views here.


def cadastrar(request):

    if request.method == 'POST':
        # Do formulário vem os ids de farmacia e medicamento (são
        # selecionados a partir de listagem)
        farmacia_id = request.POST.get('farmacia_id')
        medicamento_id = request.POST.get('medicamento_id')
        preco_entrada = request.POST.get('valor_preco')
        # data_hora = request.POST.get('data_hora')

        if not farmacia_id or not medicamento_id or not preco_entrada:

            messages.error(
                request,
                'Por favor, selecione a farmácia e o medicamento,' +
                ' e informe o valor.')

            return redirect('base:index')

        try:
            # Converte valor para float/decimal (tratando vírgula
            # se necessário)
            preco = float(preco_entrada.replace(',', '.'))

            # Cria o registro na tabela preco
            Preco.objects.create(
                farmacia_id=farmacia_id,
                medicamento_id=medicamento_id,
                preco=preco
            )

            messages.success(request, "Preço cadastrado com sucesso!")

        except Exception as e:

            messages.error(
                request, "Erro ao cadastrar preço. Verifique os dados.")

        return redirect('base:index')

    return redirect('base:index')


def listar(request):

    # .select_related já traz o nome do medicamento e da farmácia
    # associados ao preço, já que na tabela preco tem-se esses ids
    precos = Preco.objects.all().select_related('farmacia', 'medicamento')

    # Renderiza a tabela de preços
    return render(
        request, 'preco/listar.html', {'precos': precos})


def deletar(request, id):
    preco = get_object_or_404(Preco, id=id)

    preco.delete()

    return redirect('index')


def atualizar(request, id):
    preco = get_object_or_404(Preco, id=id)

    if request.method == 'POST':
        preco_novo = request.POST.get('valor_preco')

        if not preco_novo:

            messages.error(request, "O campo preço é obrigatório.")

            return render(
                request, 'preco/atualizar.html', {'preco': preco})

        try:
            # Trata a vírgula e converte para float
            preco.preco = float(preco_novo.replace(',', '.'))
            preco.save()

            messages.success(
                request, "Preço atualizado com sucesso!")

            return redirect('preco:listar')

        except ValueError:
            messages.error(request, "Valor de preço inválido.")

    return render(
        request, 'preco/atualizar.html', {'preco': preco})
