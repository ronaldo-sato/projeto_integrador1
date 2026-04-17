# Ao invés de usar urls.py de farmacia/ podemos criar o mesmo arquivo
# no app (home) e incluí-lo no arquivo farmacia/urls.py
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

# então nesse caso seria:

# urlpatterns = [
#     path('', views.index)
#     path('farmacia/', views.index),
#     path('produto/', views.index),
#     path('preco/', views.index),
# ]
