---
title: 'Importação de dados usando CSV em SeaTable'
date: 2022-10-11
lastmod: '2024-08-07'
categories:
    - 'import-von-daten'
author: 'nsc2'
url: '/pt/ajuda/importar-csv-no-seatable'
aliases:
    - '/pt/ajuda/daten-import-mithilfe-von-csv-in-seatable'
seo:
    title: 'Como importar CSV no SeaTable: tutorial completo'
    description: 'Saiba importar arquivos CSV para tabelas novas ou já existentes no SeaTable; dicas sobre preview, erros e exigências de campos.'

---

O artigo seguinte serve como uma visão geral do tópico da **importação de dados** utilizando o **CSV** no SeaTable. No artigo encontrará **instruções** detalhadas **sobre** como exactamente pode importar ficheiros CSV para o SeaTable. Além disso, introduzimos-lhe **características especiais** que deve ter em conta ao importar dados.

## Três opções de importação diferentes

Com a função de importação do SeaTable, pode transferir ficheiros CSV para as suas bases. No total, há um total de **três** opções diferentes à sua disposição:

1. Importar um ficheiro CSV como uma **nova tabela** para uma **nova base**.
2. Importar um ficheiro CSV como uma **nova tabela** para uma **base existente**.
3. Importar um ficheiro CSV para uma **tabela** existente.

{{< warning  headline="Atenção"  text="Para que o SeaTable reconheça corretamente um ficheiro CSV, este deve ser formatado de acordo com a [norma UTF-8](https://de.wikipedia.org/wiki/UTF-8)." />}}

## Opção 1: Importar como nova base

![Importar um ficheiro CSV como uma nova base](images/Import-einer-CSV-Datei-als-neue-Base.gif)

1. Mudar para a página **inicial** da SeaTable.
2. No espaço de trabalho **My Bases** ou dentro de um **grupo**, clique em **Add a Base ou Folder**.
3. Clique em **Importar base de ficheiro (XLSX, CSV ou DTABLE)**.
4. Na vista geral do ficheiro que se abre, seleccione o **ficheiro CSV** desejado do seu dispositivo que pretende importar.
5. Confirmar com **um duplo clique** no ficheiro seleccionado ou clicando em **Seleccionar** ou **Abrir**.
6. Abre-se então uma **janela de pré-visualização** para que possa verificar o aspeto dos dados importados no SeaTable. Aqui pode selecionar exatamente **quais as colunas** do ficheiro CSV que pretende importar.
7. Clique em **Submeter** para finalizar a importação.

## Opção 2: Importar como nova tabela

![Importar um ficheiro CSV como uma nova tabela](images/Import-einer-CSV-Datei-als-neue-Tabelle.gif)

1. Abrir qualquer **base existente**.
2. Clique no **símbolo \[+\]** localizado à direita do nome da última tabela.
3. Clique em **Importar ficheiro CSV ou XLSX**.
4. Na síntese de ficheiros que se abre, seleccione o **ficheiro CSV** desejado do seu dispositivo que pretende importar como uma nova tabela.
5. Confirmar com **um duplo clique** no ficheiro seleccionado ou clicando em **Seleccionar** ou **Abrir**.
6. Abre-se então uma **janela de pré-visualização** para que possa verificar o aspeto dos dados importados no SeaTable. Aqui pode selecionar exatamente **quais as colunas** do ficheiro CSV que pretende importar.
7. Clique em **Submeter** para finalizar a importação.

## Opção 3: Importar para uma tabela existente

![Importar um ficheiro CSV para uma tabela existente](images/Import-einer-CSV-Datei-in-eine-bestehende-Tabelle.gif)

1. Clique no **símbolo** triangular do **menu pendente** à direita do nome da sua tabela.
2. Seleccionar **Importar novos dados do ficheiro CSV ou XLSX**.
3. Na vista geral do ficheiro que se abre, seleccione o **ficheiro CSV** desejado do seu dispositivo que pretende importar para a tabela.
4. Confirmar com **um duplo clique** no ficheiro seleccionado ou clicando em **Seleccionar** ou **Abrir**.
5. Uma **janela de pré-visualização** será então aberta para que possa verificar como ficarão os dados importados no SeaTable. Clique em **Submeter** para completar a importação.

{{< warning  headline="Atenção"  text="Com esta opção, os nomes das colunas na tabela e **os nomes das colunas no ficheiro CSV** têm de ser **idênticos**. Todas as colunas com nomes diferentes não são importadas." />}}

## Notas sobre a importação do CSV

Com a importação do CSV pode importar praticamente todos os seus dados para o SeaTable. Aqui estão mais algumas dicas a ter em mente ao importar ficheiros CSV:

- Ao importar ficheiros CSV, a pré-visualização pode **não** mostrar todos os dados que são importados para a tabela, já que um máximo de **201 linhas** pode ser exibido na **pré-visualização**.
- Os valores que estão na **primeira linha** de uma tabela importada com CSV são sempre utilizados automaticamente pela SeaTable como **nomes de colunas** e são por isso **removidos da** primeira linha durante a importação. Todos os outros dados da tabela serão movidos para **uma linha** superior em conformidade.
- Ao importar ficheiros CSV, o **tipo de dados** **não** é automaticamente reconhecido pelo SeaTable. Consequentemente, o tipo de coluna **não** se adapta aos dados individuais (ao contrário do que acontece com a importação do Excel).

## Que mensagens de erro podem aparecer se a importação dos dados falhar?

Se a importação de dados **falhar,** podem aparecer as seguintes mensagens de erro:

![Conteúdo do ficheiro inválido](images/Bildschirmfoto-2022-10-28-um-11.39.36.png)

Esta mensagem de erro aparece se o conteúdo do ficheiro que se pretende importar for **inválido**. Uma razão para esta mensagem de erro pode ser, por exemplo, que o ficheiro que seleccionou **não** é **um** ficheiro CSV. É melhor procurar novamente no **primeiro ponto** destas **FAQ** o que deve ser exactamente um ficheiro CSV para a importação.

![rede de verificação](images/Bildschirmfoto-2022-10-28-um-11.44.06.png)

Esta mensagem de erro aparece quando a importação do ficheiro falha devido a problemas com a **ligação à Internet**. Certifique-se de que o seu dispositivo está **ligado à Internet** e tente novamente.

## Perguntas mais frequentes

{{< faq "Que aspecto deve ter o ficheiro CSV para ser importado para a tabela?" >}}O ficheiro CSV deve ser formatado de acordo com a [norma UTF-8](https://de.wikipedia.org/wiki/UTF-8) e conter o sufixo **.csv** no **final do nome do ficheiro**.
{{< /faq >}}
{{< faq "Será que os dados existentes serão substituídos durante a importação?" >}}**Não**, **nenhum** dado é substituído durante a importação.
{{< /faq >}}
{{< faq "Os dados importados são simplesmente inseridos sob as linhas existentes?" >}}**Sim**, os dados importados serão inseridos nas colunas correspondentes do quadro sob as linhas já existentes.

{{< /faq >}}

## Outros artigos úteis sobre a importação de ficheiros CSV para o SeaTable

- [Dicas e truques para a importação de ficheiros CSV]({{< relref "help/startseite/import-von-daten/tipps-und-tricks-beim-import-von-csv-oder-xlsx-dateien" >}})
- [Limitações da importação do CSV]({{< relref "help/startseite/import-von-daten/limitationen-beim-csv-excel-import" >}})
