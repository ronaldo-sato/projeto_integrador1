from django.contrib import messages

from django.shortcuts import redirect, render, get_object_or_404

from .models import Preco, Farmacia, Medicamento

# Create your views here.


def cadastrar(request):

    farmacias = Farmacia.objects.all()

    # Pegar medicamentos únicos (para listar no select)
    medicamentos_unicos = Medicamento.objects.values('nome') \
        .distinct().order_by('nome')

    # Para selecionar fabricantes de determinado medicamento, é preciso
    # manter o estado das interações com o formulário
    # Primeira interação: selecionar medicamento
    # Segunda interação: selecionar fabricante (a partird de filtrados)
    fabricantes_filtrados = None
    medicamento_selecionado = None

    filtrar = False

    if request.method == 'POST':
        # Do formulário vem os ids de farmacia e medicamento (são
        # selecionados a partir de listagem)
        farmacia_id = request.POST.get('farmacia_id')
        medicamento_id = request.POST.get('medicamento_id')
        preco_entrada = request.POST.get('valor_preco')
        # data_hora = request.POST.get('data_hora')

        medicamento_selecionado = request.POST.get('medicamento_nome')
        filtrar = request.POST.get('acao_botao') == 'filtrar'

        # Quando o botão de filtrar é acionado, os fabricantes de
        # determinado medicamento serão passados
        if filtrar and medicamento_selecionado:

            fabricantes_filtrados = Medicamento.objects.filter(
                nome=medicamento_selecionado)

            return render(request, 'base/index.html', {
                'farmacias': farmacias,
                'medicamentos_unicos': medicamentos_unicos,
                'fabricantes_filtrados': fabricantes_filtrados,
                'medicamento_selecionado': medicamento_selecionado,
                'farmacia_selecionada_id': farmacia_id,
                'preco_digitado': preco_entrada,
            })

    if not filtrar:

        if not farmacia_id or not medicamento_id or not preco_entrada:

            messages.error(
                request,
                'Por favor, selecione a farmácia, o medicamento e' +
                ' informe o valor (todos os campos são obrigatórios).')

            # retornando com valores selecionados
            return render(request, 'base/index.html', {
                'farmacias': farmacias,
                'medicamentos_unicos': medicamentos_unicos,
                'fabricantes_filtrados': fabricantes_filtrados,
                'medicamento_selecionado': medicamento_selecionado,
                'farmacia_selecionada_id': farmacia_id,
                'preco_digitado': preco_entrada,
            })

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

            messages.success(request, 'Preço cadastrado com sucesso!')

        except Exception:

            messages.error(
                request, 'Erro ao cadastrar preço. Verifique os dados.')

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
