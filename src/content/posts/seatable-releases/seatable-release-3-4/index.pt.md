---
title: 'SeaTable 3.4: Concepção dinâmica da página, mais funções de pesquisa e formulários web melhorados'
description: 'Layout de documentos adaptável, campos editáveis nas webforms, preenchimento por URL, busca avançada em colunas e listas, app de consulta cruzada de dados, filtros e novos menus elevam a personalização e automação dos processos para outro patamar no seu time de dados.'
date: 2023-03-01
lastmod: '2023-03-01'
author: 'rdb'
url: '/pt/seatable-release-3-4'
color: '#f36f22'
categories:
    - 'product-features'
seo:
    title: 'SeaTable 3.4: layout dinâmico e busca potente'
    description: 'Layout dinâmico no plugin de design, buscas melhores, formulários flexíveis e múltiplos filtros chegam ao SeaTable 3.4.'
---

Despertar da Primavera no SeaTable! Enquanto as primeiras flores estão a brotar no exterior, estamos a sair das férias de Inverno com o SeaTable 3.4. Aqueça-se para uma melhor experiência de utilização e ainda mais liberdade de desenho! O plugin de design da página desdobra agora todo o seu potencial, tal como o editor de formulários web - com funções alargadas para posicionamento dinâmico de elementos e outras opções úteis. Descubra a nova função de pesquisa ao filtrar, ordenar e agrupar nas definições de visualização e ao criar opções nas colunas de selecção. Foram também feitas inovações notáveis na Data Query App, que permite agora pesquisas refinadas em múltiplos campos. O menu de contexto de linha também tem mais opções e as entradas no registo de linha brilham em novo esplendor.

Curioso agora? Então, põe-te a andar! Esta manhã actualizámos a SeaTable Cloud para a versão 3.4. Todos os auto-hospedeiros podem fazer o mesmo - e agora até mesmo soltar o limite da linha por base. A imagem do SeaTable 3.4 está disponível para download [no bem conhecido repositório Docker](https://hub.docker.com/r/seatable/seatable-enterprise) . Como sempre, é possível encontrar a lista completa de alterações no [changelog]({{< relref "posts/seatable-releases/seatable-release-3-4" >}}).

## Posicionamento dinâmico de elementos no desenho da página

Com o plug-in de concepção de página, pode converter dados das suas bases em documentos descritivos. Com o toque de um botão, é criada uma carta de formulário, um certificado ou uma lista de stock. Até agora, o plug-in de desenho de página era menos adequado para criar documentos com conteúdo de comprimento variável, tais como ofertas ou facturas. Levantámos esta restrição com o SeaTable 3.4.

O plug-in de design da página no SeaTable 3.4 permite o posicionamento dinâmico de elementos na página pela primeira vez. Dependendo da extensão dos elementos precedentes, os elementos subsequentes deslocam-se para baixo de uma página. Isto permite utilizar o mesmo modelo, quer uma oferta contenha um ou uma dúzia de elementos. As quebras de página e as novas páginas são inseridas automaticamente. É possível definir as margens superior e inferior individualmente.

![SeaTable 3.4 - Posicionamento dinâmico de elementos no plugin de design da página](SeaTable-3.4-DynamicPositioningElements.png)

A nova função "Adaptar automaticamente a tabela ao conteúdo" está disponível para o elemento de vista "Todas as entradas da vista", bem como para a representação tabular de ligações em "Campos de tabela". Quando a função é activada, o marcador de posição para o elemento de tabela (elemento com moldura verde na imagem) define o comprimento mínimo da tabela a inserir. Se a tabela for maior do que o marcador de posição, este último é automaticamente alargado.

A função anterior "Adicionar mais páginas se o tamanho do espaço reservado não for suficiente para todas as entradas", que foi introduzida na [versão 3.1]({{< relref "posts/seatable-releases/seatable-release-3-1" >}}), já não existe no SeaTable 3.4 e foi substituída por uma função mais poderosa. Se tiver sido activada num modelo para um elemento de tabela, a nova função é automaticamente activada.

## Pesquisa em múltiplos campos com o Data Query App

As aplicações externas do SeaTable tornam os dados de tabela facilmente acessíveis ao público. Em particular, a aplicação Data Query App é utilizada para consultar rápida e especificamente conjuntos de dados com muitas centenas ou mesmo milhares de linhas (por exemplo, um catálogo de produtos ou uma lista de membros). Com o SeaTable 3.4 eliminámos a lacuna de que as consultas só podiam ser feitas através de um único campo.

Agora podem ser feitas consultas em qualquer número de campos. Para cada campo, pode especificar se é um campo obrigatório ou se a entrada é opcional. Para campos baseados em texto, pode também activar uma pesquisa difusa e forçar a consideração de maiúsculas e minúsculas. Ao combinar as opções, é possível controlar a pesquisa em grande medida. O menu para ocultar colunas individuais nos resultados da pesquisa e as opções de ordenação permanecem inalteradas.

![SeaTable 3.4 - Aplicação de consulta de dados melhorada](SeaTable-3.4-DataQueryApp.png)

No caso de campos de consulta múltiplos, aplica-se sempre uma operação Booleana E, ou seja, todos os valores introduzidos devem aparecer nos resultados da pesquisa. Evidentemente, a aplicação Data Query App continua a não ser adequada para informações confidenciais, porque não requer autenticação do utilizador. Vamos colmatar esta lacuna funcional com outra aplicação externa, que vamos introduzir em breve.

## Formulários web melhorados

No [SeaTable 3.3]({{< relref "posts/seatable-releases/seatable-release-3-3" >}}) alterámos o editor de formulários para bloquear o desenho. Isto tornou possível a disposição dos campos em qualquer ordem. Introduzimos também as anotações dos elementos estáticos e a linha separadora. Na verdade, houve outras melhorias no desenvolvimento, mas não chegaram à versão de Natal. Estamos agora a compensar isto!

O editor de formulários do SeaTable 3.4 oferece a opção de definir um nome de exibição para cada elemento do formulário, que é então exibido no formulário web em vez do nome da coluna. Desta forma, torna-se possível nomear as colunas na tabela destacadas do formulário web: Os nomes das colunas podem ser curtos e concisos, enquanto que os nomes dos campos do formulário podem ser um pouco mais verbais, por uma questão de facilidade de utilização. Isto dá-lhe ainda mais liberdade na concepção dos seus formulários da web.

![SeaTable 3.4 - Novo editor para ligações de formulários personalizados](SeaTable-3.4-FormLinkEditor.png)

Duas melhorias dizem respeito à capacidade do SeaTable de pré-preencher formulários web através de parâmetros URL. Embora esta funcionalidade já exista há algum tempo, faltava-lhe uma forma amigável de criar e gerir ligações personalizadas de formulários, bem como a opção de proteger um valor pré-preenchido contra alterações por parte do utilizador do formulário. Abordámos e resolvemos ambos no SeaTable 3.4.

Atrás do botão "... Mais" no editor de formulários está uma nova janela para criar qualquer número de ligações de formulários. Cada ligação pode conter um ou mais valores de formulário pré-preenchidos. Além disso, pode especificar para cada valor se este deve ser sobregravável ou protegido contra escrita. Uma ligação criada é identificada por um nome livremente selecionável. Isto facilita a chamada de ligações de formulários existentes e a sua modificação, se necessário.

## Função de pesquisa e filtragem nas definições de visualização

Para tabelas com muitas colunas, as listas de selecção nas definições de visualização podem tornar-se bastante longas e confusas. Para reduzir ao mínimo o esforço de pesquisa, existe agora uma função de pesquisa e filtragem em todos os menus principais das definições de visualização (filtrar, ordenar, agrupar, ocultar e formatar linhas). É muito fácil de usar: introduza o nome da coluna que procura e apenas a coluna desejada será exibida. Claro, isto também funciona se introduzir apenas parte do nome, por exemplo, se não tiver bem a certeza do nome da coluna que procura. Poderá então seleccionar a coluna de que necessita a partir da lista filtrada de resultados sem grande esforço.

![SeaTable 3.4 - Filtros em configurações de visualização](SeaTable-3.4-FilterInViewSettings.png)

Uma vez que esta função de pesquisa prática também estava ausente em colunas de selecção simples e múltiplas com muitas opções, integrámo-la também aí. Desta forma, ao criar novas opções, nunca mais terá de verificar laboriosamente se já existe ou não uma opção.

## E muito mais

Se der uma vista de olhos no changelog, encontrará muitas mais melhorias que não podemos explicar aqui individualmente. Apenas três outros melhoramentos devem ser mencionados aqui muito brevemente.

![SeaTable 3.4 - Nova funcionalidade adicionar/duplicar múltiplas filas](SeaTable-3.4-AddMultipleRows.png)

Usando o menu de contexto de linhas, que se obtém nas tabelas clicando com o botão direito do rato, pode-se agora inserir várias linhas em branco e também duplicar várias linhas seleccionadas.

Os troncos na linha são mais compactos no SeaTable 3.4 do que antes. Todas as alterações que um utilizador fez a uma fila num determinado momento são exibidas numa entrada colectiva. Anteriormente, uma entrada de registo separada era mostrada para cada alteração.

Até agora, o limite de linha por base permaneceu inalterado em 100.000 linhas. Se o limite fosse excedido, a base só poderia ser aberta em modo de leitura. Com o SeaTable 3.4, os auto-hospedeiros obtêm mais controlo sobre o limite da linha. Em certos casos de utilização, o limite pode ser aumentado através dos ficheiros de configuração. Mais informações sobre isto podem ser encontradas no [manual SeaTable](https://admin.seatable.com/configuration/base-rows-limit/).

## Duas limitações funcionais

Bases e pontos de vista partilhados a grupos já não podem ser movidos para pastas com a nova versão. As bases e visões partilhadas que foram movidas para uma pasta no passado são agora exibidas fora da pasta.

A permissão de acesso "Grupos específicos" para formulários Web foi removida. Se for um dos poucos utilizadores que a utilizaram, terá de repor a permissão de partilha.

## Anúncio de uma mudança significativa na função

SeaTable 3.5 introduz um limite de 100.000 caracteres para células individuais do tipo Texto Formatado. 100.000 caracteres correspondem a aproximadamente 25 páginas A4 de texto. O limite de caracteres deve, portanto, ter um impacto em muito poucos utilizadores.

Créditos de imagem: weestock no Freepik
