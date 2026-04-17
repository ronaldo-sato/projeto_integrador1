from django.shortcuts import render

# namespace home/ -> home/templates/home/ permite uso de arquivos com
# mesmo nome sem dar colisão de nomes


def index(request):
    # return HttpResponse('Retorno do app')
    return render(
        request,
        'home/index.html')
