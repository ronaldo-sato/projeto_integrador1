from django.shortcuts import render

# namespace para app home/ -> home/templates/home/
# permite uso de arquivos com mesmo nome sem colisão de nomes


def index(request):
    # return HttpResponse('Retorno do app')
    return render(
        request,
        'base/index.html')
