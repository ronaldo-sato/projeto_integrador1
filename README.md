Esta aplicação foi desenvolvida no contexto da disciplica **DRP03 - Projeto Integrador em Computação 1 da Univesp**, cujo tema **"Desenvolvimento de um software com framework web que utilize noções de banco de dados, praticando controle de versão"**, visa promover uma solução para algum problema na comunidade.

Os envolvidos no desenvolvimento desta aplicação estão elencados na tela **Sobre**:

<img src="app_images/sobre.png" width="1000">

A partir da identificação de necessidade econômica em relação a compra de medicamentos, devido a variação e diferença de preços entre estabelecimentos e marcas, o grupo se propôs a desenvolver um protótipo de aplicação com o intuito de fornecer subsídios para os consumidores quanto a escolha do local conveniente para a compra de medicamento por meio de comparação de preços:

<img src="app_images/home.png" width="1000">

Assim, a aplicação tem a finalidade de pesquisar os preços de um medicamento e para isso é preciso que a farmácia, o medicamento e o preço estejam cadastrados.

A aplicação é uma página simples no estilo _Simple Landing Page_, ou seja, é uma página única contendo todas as telas, cuja navegação acontece pelo _Menu_ de Navegação no topo da página de forma intuitiva.

A aplicação foi feita com [Django](https://www.djangoproject.com/), [HTML5](https://developer.mozilla.org/pt-BR/docs/Web/HTML) e [CSS3](https://developer.mozilla.org/pt-BR/docs/Web/CSS). 

Como o preço faz o relacionamento de um medicamento com uma farmácia (entidade Preco tem relacionamento associativo entre as entidades Farmacia e Medicamento), para o cadastro do preço, é preciso que o medicamento e a farmácia estejam cadastrados. O Diagrama de Entidade-Relacionamento da aplicação:

<img src="app_images/der.png" width="800">

Assim, para cadastrar uma farmácia, isso é feito pela tela **Farmácia**, como mostrado abaixo:

<img src="app_images/farmacia.png" width="1000">

E para cadastrar um medicamento, tela **Medicamento**:

<img src="app_images/medicamento.png" width="1000">

Estando a farmácia e o medicamento cadastrados é possível cadastrar o preço de um medicamento, já que o preço faz o relacionamento de medicamento e de farmácia (entidade Preço é associativa com relacionamento N:N entre a entidade Farmácia e entidade Medicamento).

Para o cadastro do preço na tela **Preço**, é preciso selecionar o medicamento e filtrar os fabricantes (pelo botão "Filtrar"), para então selecionar o fabricante, informar o preço e selecionar a farmácia:

<img src="app_images/preco.png" width="1000">

Logo, havendo algum preço cadastrado para um medicamento, a pesquisa de preço é feita pela tela **Pesquisa**:

<img src="app_images/pesquisa.png" width="1000">

Se o medicamento não aparecer como opção na tela de pesquisa, isso significa que ele não está cadastrado.

Havendo algum preço cadastrado, ao realizar a pesquisa o medicamento deve aparecer em nova página (url relativa: "/pesquisa/precos/") contendo a tabela com a lista de preços, onde a linha com menor preço fica em destaque:

<img src="app_images/lista_pesquisa.png" width="1000">

Caso contrário, se não houver preço cadastrado essa nova tela de tabela dos preços aparece vazia com a mensagem "Nenhum resultado encontrado".

Em relação ao funcionamento do _backend_, está implementado um CRUD (_Create_, _Read_, _Update_ e _Delete_ - respectivamente, Criar, Ler, Atualizar e Apagar) básico para cada entidade (Farmacia, Medicamento e Preco).

Assim, o estado de cada entidade pode ser visualizado por uma "página escondida" (não está no **_Menu_ de Navegação**) que contém a listagem dos respectivos atributos, por meio das URLs no padrão "/entidade/listar/".

Entidade Farmacia listada em /farmacia/listar/:

<img src="app_images/lista_farmacias.png" width="1000">

Entidade Medicamento listada (a seguir, apenas início e final da listagem) em /medicamento/listar/:

<img src="app_images/lista_medicamentos_inicio.png" width="1000">

<img src="app_images/lista_medicamentos_final.png" width="1000">

Entidade Preco listada (apenas início e final da listagem) em /precos/listar/:

<img src="app_images/lista_precos_inicio.png" width="1000">

<img src="app_images/lista_precos_final.png" width="1000">

Note que ao final de cada registro há os botões "Alterar" e "Excluir", os quais permitem que os atributos Farmacia(nome, endereco), Medicamento(nome, fabricante) e Preco(preco, data_hora, fabricante_id, medicamento_id), possam ser alterados ou apagados (também em "telas escondidas" - apenas para mostar o funcionamento do CRUD). 
