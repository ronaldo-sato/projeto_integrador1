"""
URL configuration for comparador_preco project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
# from django.http import HttpResponse
# from base import views as 

# Padrão MVT do Django:
# Navegador ->    URLS   -> Views -> Models -> Banco
#     --------------------------                 |
#     |                        |                 |
#     V                        |                 V
# Navegador <- Templates <- Views <- Models <- Banco

# HTTP Request <-> HTTP Response

# MVT é uma variação do padrão de Projeto MVC

# Function Based Views (Views Baseadas em Funções)


# def my_view(request):
#     print('Podemos fazer coisas aqui nesta função baseada em função')
#     return HttpResponse('Isto aqui é enviado ao navegador')


# def home(request):
#     print('Home')
#     return HttpResponse('Home')


urlpatterns = [
    # nenhuma URL pode começar com /
    # path('', home),                 # Porém Django trabalha com apps e
    # path('minha_view/', my_views),  # essas views devem ficar em
    # path('', base.index),           # views.py do respectivo app
    path('', include('base.urls')),
    path('admin/', admin.site.urls),
]
