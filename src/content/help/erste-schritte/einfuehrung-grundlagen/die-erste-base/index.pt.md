---
title: 'A primeira base'
date: 2022-08-25
lastmod: '2023-05-15'
categories:
    - 'kurzanleitungen'
author: 'cdb'
url: '/pt/ajuda/criar-primeira-base-dados-seatable'
aliases:
    - '/pt/ajuda/die-erste-base'
seo:
    title: 'SeaTable: como criar sua primeira base de dados'
    description: 'Veja como iniciar sua primeira base no SeaTable, criar tabelas, definir campos e usar relações para organizar tudo com produtividade.'
---

No SeaTable, organiza os seus dados em [bases]({{< relref "help/startseite/bases/allgemeines-zu-bases" >}}). Uma base é um contentor para uma ou mais tabelas. As tabelas de uma base podem estar independentes umas das outras ou - como numa base de dados - estar ligadas entre si através de relações.

Também pode [partilhar]({{< relref "help/startseite/freigaben/base-und-ansichtsfreigaben-im-ueberblick" >}}) com outros membros da equipa ou [convidar]({{< relref "help/startseite/freigaben/unterschiede-zwischen-einladungs-links-und-externen-links" >}}) terceiros externos para trabalharem nelas em conjunto.

O SeaTable mantém um [histórico]({{< relref "help/base-editor/historie-und-versionen/historie-und-logs" >}}) para cada base em segundo plano, permitindo-lhe anular alterações e restaurar estados anteriores, se necessário.

## A página inicial

Depois de iniciar sessão, encontra-se na página **inicial**. Aqui pode gerir as suas bases. Se seleccionou [modelos]({{< relref "templates" >}}) durante o registo, estes serão apresentados aqui.

Ao clicar na **imagem do avatar** no canto superior direito, pode aceder às [definições pessoais]({{< relref "help/startseite/persoenliche-einstellungen" >}}) para ajustar a língua do sistema, por exemplo.

Clique em **Adicionar base** para criar a sua primeira base. Dê-lhe um **nome**, prima **Enter** e a base é colocada na página inicial. Se passar o ponteiro do rato sobre o nome da base, aparece um **símbolo de lápis** {{< seatable-icon icon="dtable-icon-rename" >}} e o símbolo de três pontos {{< seatable-icon icon="dtable-icon-more-vertical" >}} à direita para as funções alargadas.

Utilizando o ícone do lápis, pode mudar o nome da base e atribuir-lhe um ícone e uma cor diferentes. As funções avançadas incluem, por exemplo, a [partilha de]({{< relref "help/startseite/freigaben/base-und-ansichtsfreigaben-im-ueberblick" >}}) uma base ou a sua [exportação]({{< relref "help/startseite/import-von-daten/datenimport-und-export" >}}). Para abrir a base, clique no seu nome.

## Vista de tabela

A nova Base contém uma [tabela]({{< relref "help/erste-schritte/einfuehrung-funktionen/einfuehrung-in-die-arbeit-mit-bases-und-tabellen" >}}) desde o início. A vista de tabela é a vista central, mas não a única, do SeaTable. Na vista de tabela, pode gerir as tabelas da base, definir a sua estrutura de colunas e introduzir ou analisar os seus dados.

O SeaTable oferece um total de [mais de 20 tipos de colunas]({{< relref "help/base-editor/spalten/uebersicht-alle-spaltentypen" >}}). Provavelmente já está familiarizado com as colunas de texto, número e data das folhas de cálculo convencionais. Naturalmente, o SeaTable também as conhece. Além disso, o SeaTable oferece colunas para imagens e ficheiros, botões e caixas de verificação, bem como campos de seleção única e múltipla.

Quer adicionar fotografias a uma entrada? Basta arrastar a imagem para uma coluna de imagens e o SeaTable guarda-a directamente na tabela. Em SeaTable tem todos os seus dados no mesmo lugar!

Outro tipo de coluna com que não está familiarizado numa folha de cálculo é a [ligação a outras entradas]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}}). Com as ligações, criam-se relações entre linhas de diferentes tabelas. Este procedimento, que corresponde à forma como as bases de dados relacionais funcionam, evita entradas duplas, assegura a consistência dos dados e cria uma síntese.

Aqui está um exemplo de aplicação: Uma empresa de gestão de propriedade regista os objectos geridos numa tabela e liga-os a inquilinos que são geridos noutra tabela. Se algo mudar nas propriedades do objecto, o gestor só tem de alterar o ajustamento na tabela de objectos. Através da ligação, a informação alterada é automaticamente actualizada para todos os inquilinos atribuídos.

[Pode criar tabelas adicionais utilizando os separadores de tabelas]({{< relref "help/base-editor/tabellen/eine-tabelle-in-einer-base-hinzufuegen" >}}). Cada tabela tem uma disposição individual: desenhe as colunas de acordo com os seus próprios desejos e necessidades.
