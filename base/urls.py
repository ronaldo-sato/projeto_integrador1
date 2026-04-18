# Ao invés de usar urls.py do projeto/ podemos criar o mesmo arquivo
# no app (home) e incluí-lo no arquivo projeto/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
]

# OBS: com include se tivesse várias urls aninhadas

# home/farmacia
# home/produto
# home/preco

# com include fica subentendido o home/, ou seja os caminhos
# já começam com home/

# então nesse caso escrevemos apenas a parte da URL depois de home/:

# urlpatterns = [
#     path('', views.index)            # Aqui está havendo colisões de
#     path('farmacia/', views.index),  # nome, então é preciso usar
#     path('produto/', views.index),   # namespaces, porque senão será
#     path('preco/', views.index),     # buscado index e algum irá
# ]                                    # sobreescrever os outros
