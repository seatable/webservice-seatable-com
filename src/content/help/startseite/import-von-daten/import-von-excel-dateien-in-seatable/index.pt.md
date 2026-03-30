---
title: 'Importação de ficheiros XLSX para o SeaTable'
date: 2022-09-28
lastmod: '2024-08-05'
categories:
    - 'import-von-daten'
author: 'nsc2'
url: '/pt/ajuda/importar-excel-xlsx-seatable'
aliases:
    - '/pt/ajuda/import-von-excel-dateien-in-seatable'
seo:
    title: 'Importar Excel XLSX para SeaTable: guia prático e rápido'
    description: 'Importe Excel como base ou tabela nova, insira em registros já existentes. Pré-visualização garante controle a cada etapa do processo de importação.'

---

O artigo seguinte fornece uma visão geral do tópico de **importação de dados de ficheiros XLSX** para o SeaTable. No artigo, encontrará **instruções** detalhadas sobre como importar exatamente tabelas do Excel para o SeaTable. Também apresentamos **características especiais** que devem ser tidas em conta aquando da importação de dados.

## Importar ficheiros XLSX para o SeaTable

Com a poderosa função de importação do SeaTable, pode transferir folhas de cálculo dos seus livros de trabalho Excel para as suas bases. Basta importar ficheiros com as extensões **.xls** ou **.xlsx**. Mesmo as folhas de cálculo do Excel com muitos milhares de linhas ficam disponíveis no SeaTable em apenas alguns instantes.

No total, tem à sua disposição **três** opções diferentes:

1. Importar um ficheiro XLSX como uma **nova tabela** para uma **nova base**.
2. Importar um ficheiro XLSX como uma **nova tabela** para uma **base existente**.
3. Importar um ficheiro XLSX para uma **tabela existente**.

## Opção 1: Importar como nova base

![Importação de um ficheiro Excel como uma nova base](images/Import-einer-Excel-Datei-als-neue-Base.gif)

1. Mudar para a página **inicial** da SeaTable.
2. No espaço de trabalho **My Bases** ou dentro de um **grupo**, clique em **Add a Base ou Folder**.
3. Clique em **Importar base de dados de um ficheiro (XLSX, CSV ou DTABLE)**.
4. Na vista geral do ficheiro que se abre, seleccione o **ficheiro** desejado do seu dispositivo que pretende importar.
5. Confirmar com **um duplo clique** no ficheiro seleccionado ou clicando em **Seleccionar** ou **Abrir**.
6. Será aberta uma **janela de pré-visualização** para que possa verificar o aspeto dos dados importados no SeaTable. Aqui pode selecionar exatamente **quais as colunas** e **tabelas que** pretende importar do livro de trabalho XLSX.
7. Clique em **Submeter** para finalizar a importação.

## Opção 2: Importar como uma nova tabela

![Importação de um ficheiro Excel como uma nova tabela](images/Import-einer-Excel-Datei-als-neue-Tabelle.gif)

1. Abrir qualquer **base** existente.
2. Clique no **símbolo \[+\]** localizado à direita do nome da última tabela.
3. Clique em **Importar ficheiro CSV ou XLSX**.
4. Na vista geral do ficheiro que se abre, seleccione o **ficheiro** desejado do seu dispositivo que pretende importar como uma nova tabela.
5. Confirmar com **um duplo clique** no ficheiro seleccionado ou clicando em **Seleccionar** ou **Abrir**.
6. Será aberta uma **janela de pré-visualização** para que possa verificar o aspeto dos dados importados no SeaTable. Aqui pode selecionar exatamente **quais as colunas** e **tabelas que** pretende importar do livro de trabalho XLSX.
7. Clique em **Submeter** para finalizar a importação.

## Opção 3: Importar para uma tabela existente

![Importar uma tabela do Excel para uma tabela existente](images/Import-einer-Excel-Tabelle-in-eine-bestehende-Tabelle.gif)

1. Clique no **símbolo triangular do menu pendente** à direita do nome da sua tabela.
2. Seleccionar **Importar novos dados do ficheiro CSV ou XLSX**.
3. Na vista geral do ficheiro que se abre, seleccione o **ficheiro** desejado do seu dispositivo que pretende importar para a tabela.
4. Confirmar com **um duplo clique** no ficheiro seleccionado ou clicando em **Seleccionar** ou **Abrir**.
5. Abre-se então uma **janela de pré-visualização** na qual pode verificar o aspeto dos dados importados no SeaTable. Clique em **Enviar** para finalizar a importação.

{{< warning  headline="Atenção"  text="Com esta opção, os nomes das colunas na tabela e **os nomes das colunas no ficheiro Excel** têm de ser **idênticos**. Todas as colunas com nomes diferentes não são importadas." />}}

## Perguntas mais frequentes

{{< faq "Porque é que a pré-visualização de importação não mostra todos os valores?" >}}A pré-visualização da importação mostra que estruturas de dados são importadas para o SeaTable. No entanto, um máximo de **201 filas** são exibidas na **pré-visualização**.
{{< /faq >}}
{{< faq "Podem ser importadas múltiplas folhas de trabalho do Excel?" >}}SeaTable pode manusear várias folhas de trabalho e tenta converter cada folha de trabalho numa tabela.
{{< /faq >}}
{{< faq "Porque é que a minha primeira linha não é importada?" >}}Os valores que se encontram na **primeira linha** de uma tabela Excel importada são sempre automaticamente utilizados como **nomes de colunas** pelo SeaTable e são, portanto, **removidos da** primeira linha durante a importação. Todos os outros dados na tabela são movidos para cima **numa linha**.
{{< /faq >}}
{{< faq "O SeaTable reconhece automaticamente o tipo de coluna?" >}}SeaTable tenta determinar o tipo de coluna automaticamente com base nos valores das primeiras filas. Certos **tipos de dados** são **automaticamente** reconhecidos pelo SeaTable. Por exemplo, se forem importados **números** ou **datas (ano-mês-dia)**, o programa adapta automaticamente o **tipo de coluna** aos dados importados.

{{< /faq >}}

## Importar um arquivo XLSX para o armazenamento de Big Data

Por defeito, o SeaTable permite o armazenamento de **até 100.000 linhas**, sendo que a função de importação suporta um máximo de 50.000 linhas numa folha de cálculo do Excel. Se pretender importar conjuntos de dados ainda maiores para o SeaTable, pode utilizar o **armazenamento de** grandes volumes de dados. [Aqui]({{< relref "help/base-editor/big-data/eine-excel-tabelle-ins-big-data-backend-importieren" >}}) pode descobrir como importar um **ficheiro XLSX para o** armazenamento de grandes volumes de dados.

## Artigos mais úteis sobre a importação de dados

Dependendo da forma do ficheiro de origem, pode encontrar dificuldades ao importar dados. Se algo não funcionar, os artigos seguintes podem ajudá-lo:

- [Dicas e truques para a importação de Excel]({{< relref "help/startseite/import-von-daten/tipps-und-tricks-beim-import-von-csv-oder-xlsx-dateien" >}})
- [Limitações da importação do Excel]({{< relref "help/startseite/import-von-daten/limitationen-beim-csv-excel-import" >}})
