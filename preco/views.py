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

    preco.nome = request.POST.get('nome_medicamento')
    preco.preco = request.POST.get('preco')
    preco.data = request.POST.get('data')
    preco.hora = request.POST.get('hora')

    preco.save()

    return redirect('index')


def select(nome, data, hora):
    preco = get_object_or_404(Preco, nome=nome)

    selecionado_por_data = Preco.objects.filter(data=data)

    selecionado_por_exclusao = Preco.objects.exclude(data=data)

    objects = []

    for obj in selecionado_por_data:

        objects.append(obj)
