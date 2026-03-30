---
title: 'Adicionar uma tabela numa base'
date: 2022-09-28
lastmod: '2025-02-28'
categories:
    - 'arbeiten-in-tabellen'
author: 'nsc2'
url: '/pt/ajuda/adicionar-tabela-base-seatable'
aliases:
    - '/pt/ajuda/eine-tabelle-in-einer-base-hinzufuegen'
seo:
    title: 'Adicionar nova tabela à base SeaTable: passo-a-passo'
    description: 'Inclua ou importe uma tabela em base já existente. Clique ou importação por arquivo – integração e vinculação ágil para conjuntos de dados grandes.'

---

As bases consistem em uma ou mais tabelas, que por sua vez podem conter dados muito diferentes e ligar-se umas às outras. Uma base pode conter **até 200 tabelas**. No entanto, por uma questão de clareza, deve considerar dividir as tabelas em várias bases e sincronizar os dados com a função de [Conjuntos de Dados Partilhados]({{< relref "help/startseite/gemeinsame-datensaetze/funktionsweise-von-gemeinsamen-datensaetzen" >}}), se tiver mais de 20 tabelas.

## Acrescentar uma tabela numa base

1. No **Base aberta** No canto superior esquerdo verá as abas com todos os **Tabelas** da base.

    ![tabelas numa base de SeaTable](images/Tabellen-in-seatable.png)

2. Clique no **símbolo \[+\]** à direita do separador da última tabela.
3. Agora selecione **Adicionar tabela**.
4. Dê um **nome** à nova tabela e confirme com **Enviar**.

## Importar tabela de um ficheiro

Em alternativa, também pode importar tabelas de **ficheiros** para a sua Base. A importação é feita como um [ficheiro CSV]({{< relref "help/startseite/import-von-daten/datenimport-und-export" >}}#tabelle_importieren).

![Importar tabela de um ficheiro](images/import-data-in-table.jpg)

## Importar tabela de outra base

No SeaTable, [as bases]({{< relref "help/startseite/bases/allgemeines-zu-bases" >}}) são basicamente unidades separadas, mas não é raro precisar de dados noutra base. Em vez de ter de exportar uma tabela de uma base e importá-la para a base desejada, o SeaTable oferece a opção conveniente de **importar** tabelas **directamente** de outras bases e, assim, transferir dados para além das fronteiras da base.

![Importar uma tabela de outra base](images/import-table-from-other-base.gif)

Com [conjuntos de dados partilhados]({{< relref "help/startseite/gemeinsame-datensaetze/funktionsweise-von-gemeinsamen-datensaetzen" >}}), pode também partilhar uma tabela principal num grupo e utilizar e sincronizar as ramificações da tabela em bases diferentes. Pode obter mais informações sobre este assunto [aqui]({{< relref "help/startseite/gemeinsame-datensaetze/mit-einem-gemeinsamen-datensatz-eine-neue-tabelle-anlegen" >}}).

## Manter a visão geral

Por vezes uma imagem vale mais do que mil palavras. SeaTable também lhe permite utilizar emojis no nome da tabela, tornando as abas da tabela mais curtas.

![Emojis no nome da tabela](images/emojis-seatable-table-name.png)

Pode encontrar instruções pormenorizadas no artigo [Utilizar emojis em nomes de tabelas]({{< relref "help/base-editor/tabellen/verwendung-von-emojis-im-tabellennamen" >}}).
