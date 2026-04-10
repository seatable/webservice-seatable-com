---
title: 'Formatação com Markdown / Rich text'
date: 2023-05-11
lastmod: '2023-08-21'
categories:
    - 'text-und-zahlen'
author: 'nsc2'
url: '/pt/ajuda/markdown-texto-rico'
aliases:
    - '/pt/ajuda/formatierungen-mithilfe-von-markdown-rich-text'
seo:
    title: 'Markdown e texto rico: Formate seus dados no SeaTable em detalhes'
    description: 'Saiba como aproveitar Markdown e rich text no SeaTable, usando listas, cabeçalhos, blocos de código e dicas para otimizar o conteúdo visual.'
---

[Markdown](https://en.wikipedia.org/wiki/Markdown) é uma linguagem de marcação altamente simplificada utilizada para **formatar texto**. O SeaTable utiliza Markdown em vários sítios para formatar textos mais longos de uma forma visualmente apelativa.

Não precisa necessariamente de estar familiarizado com a sintaxe do Markdown. Mas quer esteja a utilizar o Markdown pela primeira vez ou já tenha experiência com ele, este artigo irá ajudá-lo a compreender melhor onde e como utilizar a versão SeaTable do Markdown.

## SeaTable Markdown

Existem actualmente cinco áreas onde pode utilizar a sintaxe Markdown no SeaTable. São elas:

- Colunas do tipo de [texto formatado]({{< relref "help/base-editor/spaltentypen/die-spalten-text-und-formatierter-text" >}})
- [Descrições de base]({{< relref "help/base-editor/weitere-optionen/wie-man-einer-base-eine-beschreibung-hinzufuegt" >}})
- Textos de correio electrónico ao enviar através de [automações]({{< relref "help/base-editor/schaltflaechen/eine-e-mail-per-schaltflaeche-verschicken" >}})
- [Formulários Web]({{< relref "help/base-editor/webformulare/webformulare" >}})
- [Aplicações]({{< relref "help/app-builder/app-verwaltung/universelle-app" >}})

Assim que o Markdown for utilizado no SeaTable, ser-lhe-á apresentada a seguinte máscara de entrada. Naturalmente, pode marcar palavras ou blocos de texto como habitualmente e, em seguida, seleccionar a formatação pretendida.

![Markdown no SeaTable](images/markdown-seatable.png)

Em alternativa, também pode activar a formatação Markdown directamente, introduzindo determinados caracteres especiais. Basta digitar um caractere especial num campo de entrada do Markdown. {{< key "#" >}} seguido de uma palavra. Verá que o hash na sintaxe Markdown representa um primeiro título. Assim, se souber que carácter especial desencadeia que formatação, pode capturar e formatar os seus textos muito mais rapidamente.

Actualmente, só é possível activar parte da formatação com um carácter especial. Pode descobrir quais são estes caracteres neste artigo.

{{< warning  headline="O que é o SeaTable Markdown"  text="Apesar de as pessoas gostarem de falar de _uma_ sintaxe Markdown, existem de facto várias formas da mesma. O SeaTable suporta a formatação mais importante para criar textos visualmente apelativos." />}}

## Activar a formatação da sintaxe no SeaTable através de caracteres especiais

Actualmente, é possível activar as seguintes opções de sintaxe no SeaTable através de caracteres especiais.

### Manchetes

Uma linha que começa com um a três {{< key "#" >}}O carácter -, seguido de um espaço, resulta num **Título** do primeiro ao terceiro nível.

**Sintaxe Markdown**

\## Cabeçalho de primeiro nível  
\## Cabeçalho de segundo nível  
\### Cabeçalho de terceiro nível

**Resultado**

![Resultado dos cabeçalhos da sintaxe Markdown](images/syntax-headings-richtext-markdown-1.png)

### Negrito e itálico

Texto escrito por um {{< key "\*" >}} ou {{< key "\_" >}} O casal está rodeado **itálico** formatado (que em Markdown significa uma ênfase); texto que é acompanhado por um duplo {{< key "\*\*" >}} ou {{< key "\_ \_" >}} O casal está rodeado **ousado** formatado (o que significa grande ênfase em Markdown). A formatação também pode ser combinada com outros formatos em linha.

**Sintaxe Markdown**

\*Este texto será colocado em itálico  
Este também será em itálico

\*\*Este texto será apresentado a negrito\*\*  
\_\_Isto também será negrito\_\_

\_\*\*Combiná-los para negrito e itálico\*\*\_

**Resultado**

_Este texto ficará em itálico_  
_Este também será em itálico_

**Este texto será apresentado a negrito**  
**Isto também será negrito**

_**Combine-os para obter negrito e itálico**_

### Lista não ordenada

Pode {{< key "\-" >}} ou {{< key "\*" >}} como um marcador para um **lista não ordenada** utilização.

![Resultado da sintaxe Markdown Lista não ordenada](images/result-unordered-list-syntax-1.png)

### Lista ordenada

Se uma linha começar com um {{< key "1." >}}é automaticamente convertido num **lista ordenada** convertido.

Número 1  
2\. Ponto 2

### Citações em bloco

A **Citação de bloco** é uma linha que começa com {{< key "\>" >}} e, em seguida, o conteúdo da citação. As citações são assinaladas por um travessão e uma moldura na margem esquerda.

![Citação Markdown](images/markdown-cite.png)

### Código em linha

Texto escrito por um {{< key "FIXME:backtick" >}} é rodeado é representado como código em linha. Assim, de **apiKey é o seu token secreto da API** a seguinte formatação:

![Resultado do código em linha da sintaxe Markdown](images/result-inline-code.png)

### Blocos de código

A **Bloco de códigos** é obtida através de três **Retrocessos** {{< key "```" >}} introduzido. A característica especial do bloco de código é o facto de o conteúdo ser **Código em linha** é apresentado com tipo de letra monospace. Os recuos também são mantidos exactamente como foram introduzidos.

![Bloco de código Markdown](images/markdown-codeblock.png)

### Quebras de linha

Cada quebra de linha {{< key "↵" >}} é tratada como uma quebra de linha rígida com espaçamento entre as duas linhas. Uma quebra de linha sem espaçamento entre as linhas individuais não é possível. Também **quebras de linha múltiplas** são removidas e reduzidas a uma simples quebra de linha.

## Formatação que não pode ser activada com caracteres especiais

**Caixas de verificação** são normalmente representados em Markdown por um {{< key "\[ \]" >}} ou um {{< key "\[x\]" >}} é introduzido. No entanto, esta entrada não é automaticamente convertida numa caixa de verificação. Em vez disso, é necessário clicar no pequeno ícone da caixa de verificação {{< seatable-icon icon="dtable-icon-check-square" >}} clique.

**As hiperligações** também são suportadas no SeaTable Markdown, mas só podem ser inseridas através do ícone {{< seatable-icon icon="icon-link" >}}.

## Formatação não suportada

{{< key "~~passado~~" >}} não é suportado pelo SeaTable. As quebras de linha duplicadas também são removidas e um {{< key "<br>" >}} não é interpretado como uma quebra de linha adicional.
