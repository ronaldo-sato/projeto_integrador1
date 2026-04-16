# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# Funcionamento Protocolo HTTP:
# (cliente) HTTP Request <-> (servidor) HTTP Response

# Django funciona em MVT (Model View Template - variação de MVC)

# Functions Based Views - views usando função

def index(request):
    return HttpResponse('Retorno do app')
