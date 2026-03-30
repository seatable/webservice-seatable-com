---
title: 'Guardar um documento PDF por botão numa coluna'
date: 2023-01-23
lastmod: '2023-05-04'
categories:
    - 'andere-spalten'
author: 'nsc2'
url: '/pt/ajuda/salvar-pdf-em-coluna-por-botao'
aliases:
    - '/pt/ajuda/ein-pdf-dokument-per-schaltflaeche-in-einer-spalte-speichern'
seo:
    title: 'Salvar PDF em coluna via botão – tutorial SeaTable'
    description: 'Veja como gravar PDFs na coluna de arquivos usando botões no SeaTable, configurando também condições para modelos em diferentes idiomas.'
---

Com a ajuda de um **botão**, pode guardar documentos PDF em colunas de ficheiro. O pré-requisito para tal é a configuração do **plug-in de design da página** através das opções de base.

## Guardar documentos PDF através de um botão numa coluna

Os botões permitem-lhe guardar documentos PDF nas [colunas de arquivo das]({{< relref "help/base-editor/spaltentypen/die-datei-spalte" >}}) suas tabelas. A acção está disponível quando se cria um botão, logo que se tenha configurado o [plug-in de desenho de página]({{< relref "help/base-editor/plugins/anleitung-zum-seitendesign-plugin" >}}) na tabela correspondente.

No primeiro passo, nomeia a **coluna** e define o **rótulo** e a **cor do** botão que deseja adicionar às suas linhas.

![Nomear a linha, etiquetar e seleccionar a cor do botão](images/name-button-and-select-colour.png)

Em seguida, defina a ação para **"Guardar ficheiro PDF na coluna"**.

![Seleccionar a acção: Guardar ficheiro PDF na coluna](images/create-pdf-design-and-save-to-column.png)

Depois seleccionar uma **página** do plug-in de concepção de página para ser guardada como um ficheiro PDF. Pode escolher a partir de páginas existentes ou [adicionar]({{< relref "help/base-editor/plugins/anleitung-zum-seitendesign-plugin" >}}) uma nova página primeiro.

![Selecção da página a partir do plug-in de concepção de página que deve ser guardado como PDF na coluna.](images/select-file-to-create-PDF-with.png)

{{< warning  headline="Nota importante"  text="Também pode utilizar páginas para visualizar **informações de uma tabela** sob a forma de cartas, cartões de visita e boletins informativos, entre outras coisas." />}}

Agora seleccione a **coluna de ficheiro** em que a página deve ser guardada como PDF.

![Seleccionar a coluna do ficheiro em que o ficheiro PDF deve ser guardado.](images/select-column-to-put-PDF.png)

Finalmente, **nomeie** os ficheiros PDF que serão adicionados à sua tabela. Utilizar **{nome da coluna}**, ou seja, o nome de uma coluna entre parênteses rectos, para dar ao ficheiro o nome do valor dessa coluna.

![Nomear os ficheiros](images/PDF-file-name.png)

Depois de clicar no botão, o **ficheiro PDF** seleccionado é adicionado à linha correspondente.

![Desencadear a acção activando o botão](images/pdf-example.gif)

## Execução condicional de acções de botão

Tem a opção de definir a acção **Guardar ficheiro PDF na coluna** **várias vezes** num botão. Para cada acção individual, pode definir uma **condição** específica que deve ser cumprida para que um ficheiro PDF seja guardado na coluna quando o botão é clicado. Além disso, pode seleccionar uma **página** diferente do plug-in de design de página para guardar como PDF para cada acção.

![Definição de múltiplas acções para um botão e adição de condições específicas para executar a acção](images/add-several-actions-and-conditions-to-button.jpg)

Esta função permite-lhe, por exemplo, guardar um documento em diferentes línguas com um único botão. Crie várias acções, para cada uma das quais seleccione um modelo em diferentes **línguas**, e defina a condição de que, dependendo da língua do cliente, o **modelo adequado** seja guardado como PDF na coluna.

Esta seria a acção para anexar um documento alemão:

![Definição de diferentes modelos em diferentes línguas para cada acção, de modo a que o modelo apropriado seja guardado na coluna, dependendo da origem do cliente e se a condição do filtro se aplica](images/create-pdf-via-button-condition-1.png)

E esta é a acção para anexar um documento inglês:

![Definição de diferentes modelos em diferentes línguas para cada acção, de modo a que o modelo apropriado seja guardado na coluna, dependendo da origem do cliente e se a condição do filtro se aplica](images/create-pdf-via-button-condition-2.png)
