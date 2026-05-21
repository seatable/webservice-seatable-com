---
title: 'Limitações da importação do CSV/Excel'
date: 2022-10-15
lastmod: '2024-05-10'
categories:
    - 'import-von-daten'
author: 'nsc2'
url: '/pt/ajuda/limitacoes-importacao-csv-excel'
aliases:
    - '/pt/ajuda/limitationen-beim-csv-excel-import'
seo:
    title: 'Limitações de importação CSV/Excel no SeaTable: guia completo'
    description: 'Saiba todos os limites para importar arquivos CSV ou Excel no SeaTable Cloud e Server. Tamanho, linhas suportadas e dicas importantes.'

---

O SeaTable possui uma poderosa função de importação para facilitar ao máximo a **importação de registos de dados de ficheiros XLSX ou CSV**. Na maioria dos casos, a importação funciona sem quaisquer dificuldades. Se tentar importar demasiados registos de uma só vez, o SeaTable avisa-o do limite. Embora possa escolher livremente os **limites para o tamanho do ficheiro e o número de linhas** nos servidores SeaTable auto-hospedados, o SeaTable Cloud impõe-lhe determinados limites.

## Tamanho máximo do ficheiro e número de linhas para o SeaTable Cloud

Se importar ficheiros Excel, o SeaTable suporta ficheiros até um tamanho máximo de **100 MB** e até **50.000 linhas**. Devido a estes limites generosos, nunca deverá ter problemas com o tamanho do ficheiro. Se tiver um ficheiro maior ou com mais linhas, terá de o dividir em dois **ficheiros Excel** e efetuar a importação em duas etapas.

{{< warning  headline="Limite de memória para linhas" >}}

O backend normal do SeaTable pode conter um máximo de 100.000 linhas por tabela. Se pretender importar um ficheiro Excel ou CSV que contenha mais de 100.000 linhas, tem de [ativar]({{< relref "help/base-editor/big-data/aktivieren-des-big-data-backends-in-einer-base" >}}) volumes de dados para poder [importar]({{< relref "help/base-editor/big-data/eine-excel-tabelle-ins-big-data-backend-importieren" >}}).

{{< /warning >}}

## Gráficos e ficheiros incorporados

**Não** é possível importar gráficos e ficheiros via ficheiro XLSX. Para uma tal importação é necessário utilizar o SeaTable API, com o qual se pode importar imagens e ficheiros sem dificuldade.

## Ligações a outros registos

Não é possível importar dados para o tipo de coluna **Ligação a outros registos**. Uma vez que o SeaTable é uma [base de dados relacional]({{< relref "posts/relationale-datenbank" >}}), as ligações funcionam ainda de forma diferente das referências cruzadas no Excel.

Saiba tudo sobre o manuseamento da coluna de ligação no SeaTable [aqui]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}).

{{< warning headline="Nota" >}}
Após a importação, pode também utilizar a operação de processamento de dados [Comparar e ligar]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-vergleichen-und-verknuepfen" >}}) para criar ligações entre registos específicos.
{{< /warning >}}

## Formatos de ficheiro desviantes

A função de importação do SeaTable foi testada com ficheiros do **LibreOffice**, bem como com ficheiros actuais do **Microsoft Excel**. Outros programas do Office (como o da empresa Softmaker) **não** são testados activamente, o que pode levar a resultados de importação desviantes. Em caso de dúvida, utilize o Microsoft Excel ou o LibreOffice gratuito para obter os melhores resultados.

{{< warning  headline="Utilizar o Excel ou o Libre Office" >}}

Se continuar a ter problemas com a importação de dados, recomendamos que consulte o artigo [Sugestões e truques para importar ficheiros CSV ou XLSX]({{< relref "help/startseite/import-von-daten/tipps-und-tricks-beim-import-von-csv-oder-xlsx-dateien" >}}). Ele descreve as armadilhas típicas.

{{< /warning >}}
