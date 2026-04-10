---
title: 'Páginas de consulta em aplicações de SeaTable'
date: 2023-12-08
lastmod: '2025-02-27'
categories:
    - 'seitentypen-in-universellen-apps'
author: 'kgr'
url: '/pt/ajuda/paginas-consulta-apps-seatable'
aliases:
    - '/pt/ajuda/abfrageseiten-in-universellen-apps'
    - '/pt/ajuda/paginas-consulta-apps-universais'
seo:
    title: 'Páginas de consulta em SeaTable Apps'
    description: 'Pesquise e filtre grandes conjuntos de dados em aplicações de SeaTable: defina filtros, ordenações e campos de consulta para resultados personalizados.'
weight: 9
---

Utilizando este tipo de página, pode procurar nos seus registos de dados valores específicos em determinados campos. O tipo de página é particularmente útil para **registos de dados extensos**, como catálogos de produtos ou bibliotecas. Um caso de utilização específico poderia ser, por exemplo, a consulta de um diretório de empregados.

![Páginas de consulta em aplicações](images/Abfrageseiten-in-Universellen-Apps.png)

## Definições da página

Se pretender alterar as definições de uma página, clique no **símbolo da roda dentada** {{< seatable-icon icon="dtable-icon-set-up" >}} correspondente na barra de navegação.

![Alterar as definições da página de consulta](images/Einstellungen-der-Abfrageseite-aendern.png)

## Filtros predefinidos, ordenação e colunas ocultas

Nas **definições da página**, comece por definir a **tabela** a pesquisar.

Pode então definir **filtros** predefinidos, **ordenação** e **colunas ocultas** para limitar e organizar os dados apresentados aos utilizadores. Para filtrar ou ordenar, clique em **Adicionar filtro** ou **Adicionar ordenação**, seleccione a **coluna** e a **condição** pretendidas e confirme com **Enviar**.

![Adicionar filtro nas páginas de consulta nas aplicações](images/Add-filter-on-query-pages-in-Universal-Apps.png)

Os utilizadores podem ver todas as informações dos registos de dados aplicáveis nos **resultados da consulta** se não os restringir. Por conseguinte, decida quais os dados que devem ser **visíveis** e mostre ou oculte as colunas correspondentes utilizando os **cursores**.

![Ocultar colunas em páginas de consulta nas aplicações](images/Hide-columns-on-query-pages-in-Universal-Apps.png)

{{< warning  headline="Nota importante"  text="Os utilizadores da aplicação **não podem alterar os filtros predefinidos** e **as colunas ocultas**. Por conseguinte, o utilizador só verá as entradas filtradas, como desejar. No entanto, os utilizadores podem personalizar a **altura das linhas** e a **ordenação** dos registos de dados consultados." />}}

## Adicionar campos de consulta

**Os campos de consulta** são de importância central para este tipo de página. Os utilizadores podem utilizá-los para procurar valores específicos nas colunas da tabela selecionada e, assim, **encontrar registos de dados**. Clique em {{< seatable-icon icon="dtable-icon-enlarge" >}} **Adicionar campo** nas definições da página para definir um campo de consulta.

![Adicionar campos às páginas de consulta](images/Felder-auf-Abfrageseiten-hinzufuegen.png)

Em seguida, pode selecionar a **coluna** pretendida e definir se o campo de consulta deve ser **obrigatório**, se é possível uma **pesquisa difusa** e se as maiúsculas **e min** úsculas são tidas em conta ao efetuar entradas.

## Adicionar nota

Pode adicionar uma **nota** introdutória à sua página de consulta, que pode conter explicações sobre como preencher os campos de consulta, por exemplo. Para tal, basta ativar a **barra deslizante** nas definições da página e escrever a nota na caixa de texto que aparece.

![Adicionar nota às páginas de consulta](images/Hinweis-auf-Abfrageseiten-der-Universellen-App-hinzufuegen.png)

## Editar resultados da consulta

Para poder utilizar esta função, deve **ativar** a barra deslizante nas definições da página em **É o resultado da consulta editável**.

![Tornar o resultado da consulta editável](images/Abfrageergebnis-bearbeitbar-machen.png)

Todos os utilizadores com acesso à página de consulta podem então **editar** os **registos de dados** pesquisados.

![Editar os resultados da consulta nas páginas de consulta da aplicação](images/Abfrageergebnisse-bearbeiten-auf-Abfrageseiten-der-App.gif)

- Efetuar uma **consulta de dados bem sucedida**.
- Desloque o rato para a **numeração das linhas** da lista de acertos e clique no **símbolo da seta dupla** em frente do registo de dados que pretende editar.
- Efetuar as alterações desejadas nos **detalhes da linha** aberta.
- Clique no **símbolo x** para fechar a janela e guardar as suas alterações.

{{< warning  type="warning" headline="Colunas só de leitura" text="Pode definir antecipadamente colunas que não podem ser editadas. Para o fazer, vá às definições da página e marque as caixas das colunas que devem ser **apenas de leitura** para os utilizadores. Pode reconhecer as colunas só de leitura pelo facto de os campos nos detalhes da linha estarem realçados a cinzento." />}}

## Autorizações de páginas

Na parte inferior das definições da página, pode restringir quem pode ver a página de consulta.

![Autorização para páginas da consulta](images/Berechtigung-fuer-individuelle-Seiten-der-Universellen-App.png)

Esta é a única [autorização de página]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}) que pode selecionar aqui. Não é possível adicionar ou eliminar linhas na tabela através de páginas de consulta.

No entanto, após uma consulta de dados bem sucedida, os utilizadores da aplicação podem clicar nos [botões]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}}) da lista de ocorrências apresentada para **executar** determinadas **acções**.

![Botões de execução nas páginas de consulta](images/Schaltflaechen-auf-Abfrageseiten-ausfuehren.gif)

Um exemplo de aplicação é um quadro de empregos interno: a página de consulta permite-lhe procurar rapidamente posições relevantes. Se for encontrada uma posição interessante, basta clicar no botão nos resultados da pesquisa para se candidatar diretamente à posição.

{{< warning  headline="Atenção com os botões" >}}

[Os botões]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}}) podem ser **sempre** premidos, independentemente das autorizações da página. Isto significa que todos os utilizadores da aplicação podem fazer determinadas alterações aos registos de dados que definiu previamente, mesmo que as colunas afectadas estejam bloqueadas para eles ou que o utilizador não esteja autorizado a editar os resultados da consulta.

{{< /warning >}}
