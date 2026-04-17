---
title: 'Páginas de calendário em aplicações de SeaTable'
date: 2023-12-04
lastmod: '2025-02-26'
categories:
    - 'seitentypen-in-universellen-apps'
author: 'kgr'
url: '/pt/ajuda/paginas-de-calendario-em-apps-seatable'
aliases:
    - '/pt/ajuda/kalenderseiten-in-universellen-apps'
    - '/pt/ajuda/paginas-de-calendario-em-apps-universais'
seo:
    title: 'Páginas de calendário em SeaTable Apps'
    description: 'Use calendário nas SeaTable Apps para planejar eventos, filtrar, editar compromissos e tarefas fácil.'
weight: 5
---

Este tipo de página permite-lhe apresentar as entradas de uma ou duas [colunas de data]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}) da sua tabela num **calendário**. Um caso de utilização específico poderia ser, por exemplo, a apresentação do calendário das próximas **reuniões**.

![Próximas reuniões numa vista de calendário da página de calendário](images/calendar-page-example.png)

## Definições da página

Se pretender alterar as definições de uma página, clique no **símbolo da roda dentada** {{< seatable-icon icon="dtable-icon-set-up" >}} correspondente na barra de navegação.

![Alterar as definições da página de calendário](images/Einstellungen-auf-der-Kalenderseite-aendern.png)

Nas **definições da página**, pode selecionar o **título**, a **data de início** e a **cor** das **entradas** apresentadas no calendário, bem como o **dia em que a semana começa**, entre outras coisas.

![Definições de página do tipo de página: Calendário ](images/page-settings-calendar-page.png)

## Filtros predefinidos e colunas ocultas

É possível definir **filtros predefinidos** e **colunas ocultas** para limitar os dados apresentados aos utilizadores.

![Adicionar filtro nas páginas de calendário](images/Add-filter-on-calendar-pages-in-Universal-Apps.png)

Para tal, clique em **Adicionar filtro**, seleccione a **coluna** e a **condição** pretendidas e confirme com **Enviar**.

Os utilizadores podem ver mais informações sobre um compromisso clicando numa entrada de calendário.

![Abrir entradas de calendário numa aplicação](images/Kalendereintraege-in-der-Universellen-App-oeffnen.gif)

Por conseguinte, decida quais os dados que devem ser **visíveis** e mostre ou oculte as colunas correspondentes utilizando os **cursores**.

![Ocultar colunas em páginas de calendário](images/Hide-columns-on-calendar-pages-in-Universal-Apps.png)

{{< warning  headline="Nota importante"  text="Os utilizadores da aplicação **não podem alterar os filtros predefinidos** e **as colunas ocultas**. Por conseguinte, o utilizador só verá os dados filtrados que desejar." />}}

## Adicionar entrada de calendário

Se tiver a autorização adequada, pode **adicionar novas entradas** diretamente numa página do calendário. Na vista mensal, clique no pequeno **símbolo de mais** no canto superior direito de um mosaico. A **data** desse dia já está pré-preenchida.

Independentemente da data, pode também clicar no grande **símbolo circular de mais** no canto inferior direito da página. Abre-se então uma janela com os **pormenores da linha**. Introduza aí todos os dados necessários e grave a entrada clicando em **Enviar**.

![Adicionar uma entrada de calendário numa aplicação](images/Kalendereintrag-hinzufuegen.gif)

## Editar e mover entradas de calendário

Pode editar facilmente as entradas do calendário clicando **numa entrada** e efectuando as alterações pretendidas nos **detalhes da linha** que se abrem. Também pode mover convenientemente entradas no calendário **utilizando a função arrastar e largar**. O SeaTable ajusta automaticamente os valores nas respectivas [colunas de datas]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}).

![Mover e editar entradas nas páginas do calendário](images/Eintraege-auf-Kalenderseiten-verschieben-und-bearbeiten.gif)

## Definições da coluna de ligações

Nas **opções da coluna de ligação**, é possível especificar quais os dados visíveis e quais as operações permitidas para cada tabela ligada.

![Ligar definições de coluna em páginas de calendário nas aplicações](images/Link-column-settings-on-table-pages-in-Universal-Apps.png)

- **Definições de campo**: Aqui pode definir exatamente a que colunas se aplicam as seguintes autorizações.
- **Adicionar e ligar novos registos**: Se ativar este seletor, os utilizadores podem adicionar novas entradas à tabela ligada. Pode utilizar as definições de campo para definir as colunas que são **visíveis** e as que são **obrigatórias**, ou seja, que têm de ser preenchidas.
- **Ligar registos existentes**: Se ativar esta barra deslizante, os utilizadores podem ligar entradas existentes na tabela ligada. Pode utilizar as definições de campo para definir as colunas que são **visíveis**.
- **Limitar as ligações a um registro máximo**: Se ativar esta barra deslizante, os utilizadores só podem ligar uma linha da tabela ligada nas células da coluna de ligação.
- **Filtros predefinidos**: Se adicionar um filtro aqui, apenas as opções que satisfazem as condições do filtro serão apresentadas ao ligar as entradas.
- **Ativar** a função de grandes volumes de dados: Se a função de grandes volumes de dados estiver activada, os utilizadores podem pesquisar mais de 20.000 registos de dados, desde que existam este número de entradas na tabela ligada.
- **Modificar registos ligados**: Se ativar esta barra deslizante, os utilizadores podem editar as entradas existentes na tabela ligada. Pode utilizar as definições de campo para definir quais as colunas que são **editáveis**.

## Autorizações de páginas

Na parte inferior das definições da página, pode restringir exatamente quais os utilizadores autorizados a interagir com a página. Especifique quem está autorizado a ver a página, adicionar linhas ou alterar entradas.

![Autorizações de página em páginas de calendário](images/Seitenberechtigungen-auf-Kalenderseiten.png)
