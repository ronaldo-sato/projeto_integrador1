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
    context = {
        'farmacias': Farmacia.objects.all(),
        'medicamentos': Medicamento.objects.all(),
    }
    return render(request, 'base/index.html', context)
