---
title: 'Validação de entrada para campos de texto com expressões regulares'
date: 2023-05-03
lastmod: '2024-03-11'
categories:
    - 'text-und-zahlen'
author: 'nsc2'
url: '/pt/ajuda/validacao-texto-regex-seatable'
aliases:
    - '/pt/ajuda/validierung-der-eingabe-bei-textfeldern'
seo:
    title: 'Validação de texto com regex em SeaTable: tutorial'
    description: 'Use expressões regulares para validar e realçar campos de texto SeaTable. Identifique erros de formato e fortaleça a consistência dos dados armazenados.'

---

Ao utilizar colunas de texto nas suas tabelas, tem a opção de validar entradas. Utilizando a validação, que suporta expressões regulares, é possível verificar os valores das células e destacar as células com conteúdo que se desvia do formato válido.

{{< warning  headline="Nota" >}}

Basicamente, existem duas formas diferentes de validar entradas em colunas de texto. A validação pode ser efectuada tanto ao **adicionar uma nova** [coluna]({{< relref "help/base-editor/spaltentypen/die-spalte-formatierter-text" >}}) **já criadas**.

{{< /warning >}}

## Validar entradas

![Activação da validação da entrada de colunas de texto](images/activate-validation-1.png)

1. Se pretender validar as entradas numa coluna de texto já criada, clique primeiro no **símbolo do triângulo** {{< seatable-icon icon="dtable-icon-drop-down" color="grey" >}} da coluna correspondente.
2. Seleccione **Personalizar tipo de coluna** no menu pendente.
3. Activar o cursor de **validação de entrada**
4. Definir um **formato de destino**.
5. Confirmar com **Submeter**.

![Definição do formato de destino](images/define-specific-format-2.png)

## Consequência da validação

Após uma validação bem sucedida, as **células** com **conteúdo que se desvia do** formato de destino são destacadas a vermelho.

![Células destacadas a vermelho com conteúdo diferente do formato de destino](images/marked-entries-which-not-match-the-format.png)

## Expressões regulares

O SeaTable suporta **expressões regulares** para validar as suas entradas em colunas de texto.  
Pode encontrar alguns exemplos na tabela seguinte:

| Expressão regular               | Função                                                                     |     |     |     |     |
| ------------------------------- | -------------------------------------------------------------------------- | --- | --- | --- | --- |
| \[123456\]                      | Verificar se uma entrada corresponde a um ano escolar de 1 a 6.            |     |     |     |     |
| \[1-9\]\[0-9\]?\[0-9\]?\[a-z\]? | Verificar o formato de um número de porta alemão (3 dígitos + 1 letra)     |     |     |     |     |
| \[0-9\]{5}                      | Verificar o formato dos códigos postais alemães (5x um número entre 0 e 9) |     |     |     |     |
| \[0-9/. \\-\]+                  | Verificar o formato de um número de telefone                               |     |     |     |     |
| Max Mustermann                  | Procurar um possível nome do meio de um autor                              |     |     |     |     |

{{< warning  headline="Dica"  text="Um **tutorial** detalhado sobre a utilização de expressões regulares para verificar cadeias de caracteres pode ser encontrado [aqui (alemão)](https://danielfett.de/2006/03/20/regulaere-ausdruecke-tutorial/) e [aqui (inglês](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285))." />}}
