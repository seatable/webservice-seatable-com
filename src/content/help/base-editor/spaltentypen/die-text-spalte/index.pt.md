---
title: 'A coluna de texto'
date: 2023-05-03
lastmod: '2024-03-11'
categories:
    - 'text-und-zahlen'
author: 'nsc2'
url: '/pt/ajuda/coluna-de-texto'
aliases:
    - '/pt/ajuda/validierung-der-eingabe-bei-textfeldern'
    - '/pt/ajuda/validacao-texto-regex-seatable'
seo:
    title: 'A coluna de texto: o tipo de coluna mais básico do SeaTable'
    description: 'Use a coluna de texto para registar cadeias alfanuméricas curtas, defina valores predefinidos e valide entradas com expressões regulares.'
weight: 1
---

A coluna de texto é um dos **tipos de coluna** mais elementares no SeaTable e é também apresentada em primeiro lugar no menu de seleção do tipo de coluna.

![A coluna de texto regular](images/select-regular-text-column.png)

Por predefinição, o SeaTable adiciona automaticamente uma **coluna de texto** como primeira coluna a cada tabela criada recentemente. Além disso, pode adicionar manualmente à sua tabela tantas colunas de texto quantas desejar. Saiba como o fazer [aqui]({{< relref "help/base-editor/spalten/hinzufuegen-einer-spalte" >}}).

![A coluna de texto](images/text-column-new.png)

A **primeira coluna** de uma tabela tem várias [características especiais]({{< relref "help/base-editor/spalten/die-besonderheiten-der-ersten-spalte" >}}), como pode ler no artigo ligado.

## Utilização da coluna de texto

A coluna de texto é particularmente adequada para registar e [ordenar]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}}) cadeias alfanuméricas curtas, por exemplo **termos**, **nomes**, **palavras-passe**, **matrículas de veículos** ou **IBAN**.

![Exemplo de aplicação da coluna de texto regular](images/regular-text-example.png)

{{< warning  headline="UTF-8"  text="O SeaTable suporta todos os caracteres de acordo com a norma UTF-8, uma vez que o UTF-8 é a codificação de caracteres mais difundida no mundo para a Internet." />}}

Ao utilizar a coluna, faz sentido manter as entradas o mais **curtas** possível, uma vez que apenas um **número limitado de caracteres** pode ser apresentado sem ter de aumentar a largura da coluna.

![As entradas demasiado longas não podem ser apresentadas na sua totalidade numa coluna de texto sem aumentar a largura da coluna](images/use-short-entries.png)

## Outros tipos de colunas baseadas em texto

Tenha em atenção que **não** estão disponíveis **opções de formatação** para as entradas na coluna de texto. Se pretender registar textos estruturados com quebras de linha, listas, imagens, etc., deve utilizar a coluna [Texto formatado]({{< relref "help/base-editor/spaltentypen/die-spalte-formatierter-text" >}}).

Existem no SeaTable três outros tipos de colunas baseadas em texto para casos de utilização especiais:
- a [coluna de correio eletrónico]({{< relref "help/base-editor/spaltentypen/die-e-mail-spalte" >}})
- a [coluna URL]({{< relref "help/base-editor/spaltentypen/die-url-spalte" >}})
- a [coluna de número de telefone]({{< relref "help/base-editor/spaltentypen/die-telefonnummer-spalte" >}})

{{< warning  headline="Nota" >}}
Existem inúmeras funções de texto para [colunas de fórmula]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}}), que se comportam como colunas de texto quando os resultados são **strings**.
{{< /warning >}}

## Definir valor predefinido

É possível definir um [valor predefinido]({{< relref "help/base-editor/spalten/standardwert-fuer-eine-spalte-festlegen" >}}) para cada coluna de texto. Este valor é automaticamente introduzido em cada nova linha da tabela.

Se especificar a referência **{creator.name}** ou **{creator.id}** como valor predefinido, o **nome** ou a **ID do utilizador** que adicionou a linha é automaticamente introduzido.

![Referência ao nome do utilizador com um valor predefinido](images/Set-creator-name-as-default-value.png)

## Validar entradas

Ao utilizar colunas de texto nas suas tabelas, tem a opção de validar entradas. Utilizando a validação, que suporta expressões regulares, é possível **verificar os valores das células** e destacar as células com conteúdo que se desvia do formato válido.

Pode configurar a verificação do formato logo ao criar uma coluna de texto, ativando o cursor.

![Ativação da validação da entrada de colunas de texto](images/activate-validation-1.png)

Se pretender validar as entradas numa coluna de texto já criada, clique primeiro no **símbolo do triângulo** {{< seatable-icon icon="dtable-icon-drop-down" color="grey" >}} da coluna correspondente e selecione **Personalizar tipo de coluna** no menu pendente.

1. Ative o cursor **Validar entrada**
2. Defina um **formato de destino**.
![Definição do formato de destino](images/define-specific-format-2.png)
3. Confirme com **Submeter**.

### Consequência da validação

Após uma validação bem sucedida, as **células** com **conteúdo que se desvia do** formato de destino são destacadas a vermelho.

![Células destacadas a vermelho com conteúdo diferente do formato de destino](images/marked-entries-which-not-match-the-format.png)

### Expressões regulares

O SeaTable suporta **expressões regulares** para validar as suas entradas em colunas de texto. Pode encontrar alguns exemplos na tabela seguinte:

| Expressão regular               | Função                                                                     |
| ------------------------------- | -------------------------------------------------------------------------- |
| \[123456\]                      | Verificar se uma entrada corresponde a uma nota escolar de 1 a 6.          |
| \[1-9\]\[0-9\]?\[0-9\]?\[a-z\]? | Verificar o formato de um número de porta alemão (3 dígitos + 1 letra)     |
| \[0-9\]{5}                      | Verificar o formato dos códigos postais alemães (5x um número entre 0 e 9) |
| \[0-9/. \\-\]+                  | Verificar o formato de um número de telefone                               |
| Max.\*Mustermann                | Procurar um possível nome do meio de um autor                              |

{{< warning  headline="Dica"  text="Um **tutorial** detalhado sobre a utilização de expressões regulares para verificar cadeias de caracteres pode ser encontrado [aqui (alemão)](https://danielfett.de/2006/03/20/regulaere-ausdruecke-tutorial/) e [aqui (inglês)](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)." />}}
