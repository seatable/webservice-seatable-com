---
title: 'Importação e exportação de dados'
date: 2022-08-25
lastmod: '2024-03-11'
categories:
    - 'import-von-daten'
author: 'cdb'
url: '/pt/ajuda/importacao-exportacao-dados-seatable'
aliases:
    - '/pt/ajuda/datenimport-und-export'
seo:
    title: 'Importação e exportação de dados no SeaTable: bases, Excel, CSV'
    description: 'Veja como importar e exportar bases e tabelas no SeaTable usando DTABLE, Excel e CSV—guia completo com dicas e solução de problemas.'
star: true
weight: 1
---

As funções de importação do SeaTable permitem passar de outras soluções para o SeaTable com pouco esforço. O mesmo se aplica à mudança de um sistema SeaTable para outro, por exemplo, ao migrar de um sistema SeaTable Cloud para um sistema auto-hospedado. Pode continuar a trabalhar sem problemas sobre uma base que tenha importado de outra instância SeaTable.

Como exportar bases e tabelas do SeaTable e importá-las para o SeaTable é o tema deste artigo.

## Exportar bases

Pode exportar o estado atual das suas bases, incluindo todas as tabelas, [vistas]({{< relref "help/base-editor/ansichten/was-ist-eine-ansicht" >}}), [formulários Web]({{< relref "help/base-editor/webformulare/webformulare" >}}) e plugins. Os [comentarios]({{< relref "help/base-editor/zeilen/zeilen-kommentieren" >}}), [automatizações]({{< relref "help/base-editor/automationen/uebersicht-ueber-automationen" >}}) e o [histórico de alterações]({{< relref "help/base-editor/historie-und-versionen/historie-und-logs" >}}), bem como [os dados no backend de big data]({{< relref "help/base-editor/big-data/potenzial-big-data" >}}), **não** são **exportados**.

![Bases de exportação](images/export-bases.png)

SeaTable utiliza o [formato de ficheiro DTABLE]({{< relref "help/startseite/import-von-daten/dtable-dateiformat" >}}) para exportar bases. Para mais informações, ver o artigo [Salvando uma Base como um ficheiro DTABLE]({{< relref "help/startseite/bases/speichern-einer-base-als-dtable-datei" >}}).

## Exportar tabelas

Pode **exportar tabelas** individuais a partir de cada base a que tem acesso **para ficheiros Excel**. O conteúdo das colunas baseadas em texto e números são copiadas como valores para o ficheiro de destino. Os [comentarios]({{< relref "help/base-editor/zeilen/zeilen-kommentieren" >}}), [automatizações]({{< relref "help/base-editor/automationen/uebersicht-ueber-automationen" >}}) e o [histórico de alterações]({{< relref "help/base-editor/historie-und-versionen/historie-und-logs" >}}) **não** são **exportados**.

![Exportação de tabela](images/export-tables.jpg)

Inicia-se a exportação de uma tabela a partir da Base. Clique na seta para a direita do nome da tabela a ser exportada. Agora seleccione **Exportar tabela para Excel** para iniciar o download. Quando a exportação estiver concluída, encontrará o ficheiro XLSX no local seleccionado no seu dispositivo.

## Importar bases

SeaTable suporta a importação de bases a partir do seu próprio [formato DTABLE]({{< relref "help/startseite/import-von-daten/dtable-dateiformat" >}}), de **ficheiros Excel** e do **formato** genérico **CSV**. Quando se importa um **ficheiro DTABLE**, a base é restaurada exactamente como se apresentava no momento da exportação. Ao importar um ficheiro CSV ou Excel, os valores do ficheiro CSV/XLSX são copiados para colunas de tabela de uma nova base, e o SeaTable tenta interpretar os tipos de colunas com base nos dados.

![Importação de dados para uma base](images/import-data-into-your-base.png)

O que tem de considerar ao importar uma base depende do tipo de ficheiro de importação. Contudo, o procedimento é o mesmo para todos os tipos de ficheiro: Vá à página **inicial** e clique em **Adicionar uma base ou pasta** na área ou grupo onde pretende ter a nova base. Pode encontrar informações mais detalhadas nos artigos seguintes:

- [Criação de uma Base a partir de um ficheiro DTABLE]({{< relref "help/startseite/import-von-daten/erstellen-einer-base-aus-einer-dtable-datei" >}})
- [Importar ficheiros Excel para o SeaTable]({{< relref "help/startseite/import-von-daten/import-von-excel-dateien-in-seatable" >}})
- [Importação de dados usando CSV em SeaTable]({{< relref "help/startseite/import-von-daten/daten-import-mithilfe-von-csv-in-seatable" >}})

## Importar tabelas

Nas bases existentes, pode **preencher tabelas** individuais **via CSV ou importação Excel**. Tem as seguintes opções: Pode importar os dados para uma **tabela existente**

![Importar dados para uma tabela existente](images/Daten-in-eine-bestehende-Tabelle-importieren.png)

ou importar os dados para uma **nova tabela**.

![Preenchimento de tabelas existentes através de importação de dados](images/import-data-in-table.jpg)

A importação tem lugar como [ficheiro CSV]({{< relref "help/startseite/import-von-daten/daten-import-mithilfe-von-csv-in-seatable" >}}) ou [ficheiro Excel]({{< relref "help/startseite/import-von-daten/import-von-excel-dateien-in-seatable" >}}) na tabela. Para mais informações, ver os artigos ligados.

Se já tiver criado uma tabela no **SeaTable** e precisar dela **noutra base**, pode simplesmente copiá-la. Pode descobrir [aqui]({{< relref "help/base-editor/tabellen/eine-tabelle-in-einer-base-hinzufuegen" >}}) como importar tabelas de outra base.

{{< warning  headline="Limite de memória para linhas" >}}

O backend normal do SeaTable pode conter um máximo de 100.000 linhas por tabela. Se pretender importar um ficheiro Excel ou CSV que contenha mais de 100 000 linhas, tem de [ativar]({{< relref "help/base-editor/big-data/aktivieren-des-big-data-backends-in-einer-base" >}}) para o poder importar.

{{< /warning >}}

## Outros artigos úteis sobre o tema da importação de dados

- [Dicas e truques para a importação de ficheiros CSV ou XLSX]({{< relref "help/startseite/import-von-daten/tipps-und-tricks-beim-import-von-csv-oder-xlsx-dateien" >}})
- [Limitações da importação de CSV/Excel]({{< relref "help/startseite/import-von-daten/limitationen-beim-csv-excel-import" >}})
- [Importação de conjuntos de dados CSV para uma base existente]({{< relref "help/startseite/import-von-daten/daten-import-mithilfe-von-csv-in-seatable" >}})
