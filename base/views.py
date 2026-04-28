from django.shortcuts import render

from farmacia.models import Farmacia
from medicamento.models import Medicamento

# Create your views here.


# def index(request):
#     return render(
#         request,
#         'base/index.html')

# Ter as farmácias e medicamentos cadastrados para usá-los nos selects
# do forms de cadastro de preço
def index(request):

    farmacias = Farmacia.objects.all()
    medicamentos = Medicamento.objects.all()
    medicamentos_unicos = Medicamento.objects.values('nome') \
        .distinct().order_by('nome')

    fabricantes_filtrados = None
    medicamento_selecionado = request.GET.get('medicamento_nome')

    # Incluindo medicamentos_unicos: nome de medicamentos sem repetição
    context = {
        'farmacias': farmacias,
        'medicamentos': medicamentos,
        'medicamentos_unicos': medicamentos_unicos,
        'medicamento_selecionado': medicamento_selecionado,
    }
    return render(request, 'base/index.html', context)
