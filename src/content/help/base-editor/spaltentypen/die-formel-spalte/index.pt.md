---
title: 'A coluna de fórmulas'
date: 2023-01-28
lastmod: '2023-09-14'
categories:
    - 'formeln'
author: 'ssc'
url: '/pt/ajuda/coluna-formula-seatable'
aliases:
    - '/pt/ajuda/grundlagen-von-seatable-formeln'
    - '/pt/ajuda/die-formel-spalte'
seo:
    title: 'Coluna de fórmula em SeaTable: como usar e exemplos'
    description: 'Saiba como calcular, combinar e manipular valores por linha usando a coluna de fórmula no SeaTable – para todos os usos.'

---

O SeaTable oferece-lhe muitas funções diferentes que pode adicionar à sua tabela. Uma delas é a chamada **coluna de fórmulas**. Com a ajuda das fórmulas, pode ligar valores de diferentes colunas e criar diferentes funções com base nos tipos de dados dessas colunas. Entre outras coisas, pode calcular com valores numa linha, fundi-los ou relacioná-los entre si.

{{< warning  headline="SeaTable não permite referências gratuitas como no Excel"  text="No Excel, é possível endereçar qualquer célula numa fórmula. Isto **não** é possível no SeaTable. Uma fórmula só pode funcionar com os **valores da mesma linha**." />}}

## Criar uma coluna de fórmulas

Para aplicar uma fórmula, deve primeiro adicionar uma nova coluna de fórmula à sua tabela. Pode saber como o fazer [aqui]({{< relref "help/base-editor/spalten/hinzufuegen-einer-spalte" >}}).

![Selecção de uma coluna de fórmula](images/select-formula-column.png)

O SeaTable fornece-lhe um **editor de** fórmulas para o ajudar a introduzir fórmulas.

![Assistente de fórmulas para simplificar a introdução de fórmulas especialmente complexas](images/Formula.wizard.png)

## Escreva uma primeira fórmula

Quando a coluna de fórmulas estiver criada, pode começar a escrever a fórmula. A ilustração seguinte mostra uma fórmula simples para calcular a média de cinco números.

![Introduzir qualquer fórmula no campo de texto](images/input-formular.jpg)

Esta fórmula escreve sempre o valor estático _13,2_ na coluna de fórmula como resultado. No entanto, a verdadeira força da coluna de fórmulas só se manifesta quando utiliza os valores de outras colunas para a sua fórmula. Com o **{nome da coluna}** entre parênteses rectos, pode fazer referência a colunas existentes na sua tabela.

{{< warning headline="Acrescentar colunas à fórmula" text="Os nomes das colunas na tabela aberta são apresentados à esquerda no editor de fórmulas e podem ser alterados com um **Fazer duplo clique** deve ser inserido na fórmula." />}}

![Colunas disponíveis para selecção no editor de fórmulas](images/columns-in-the-formula-editor.jpg)

Pode então inserir certas **constantes**, **operandos** e **funções** na sua fórmula para calcular, fundir ou relacionar os valores das diferentes colunas.

## Linguagem de cor clara

Para poder distinguir os diferentes elementos da sua fórmula, estes são marcados com uma **cor** diferente consoante o seu tipo:

| Objecto                 | Exemplo                                                                                                         |
| ----------------------- | --------------------------------------------------------------------------------------------------------------- |
| Funções                 | ![As funções são sempre marcadas a azul numa fórmula](images/example-function.png)                              |
| Texto / Corda           | ![Os textos e as cordas são sempre marcados a vermelho no editor de fórmulas](images/example-text.png)          |
| Números                 | ![Os números são sempre marcados a verde no editor de fórmula](images/example-number.png)                       |
| Referências das colunas | ![As referências das colunas são sempre marcadas com uma fórmula roxa ](images/example-reference-to-column.png) |

{{< warning headline="Os parênteses que pertencem juntos são destacados" text="Quando clica num parêntesis de abertura ou de fecho no editor de fórmulas, o parêntesis correspondente também é realçado. Isto facilita a deteção de substituições de parênteses em falta ou incorrectas." />}}

![Abertura e fecho de parênteses são sempre realçados no editor de fórmulas](images/example-brackets.png)

## Exemplos de fórmulas

Seguem-se alguns exemplos que ilustram a utilidade e a utilização de fórmulas.

- [Exemplo de fórmula: Multiplicação simples com uma fórmula]({{< relref "help/base-editor/formeln/formelbeispiel-einfache-multiplikation-mit-einer-formel" >}})
- [Exemplo de fórmula: Fórmula de fusão de colunas de texto com a ajuda de uma fórmula]({{< relref "help/base-editor/formeln/formelbeispiel-zusammenfuehren-von-text-spalten-mit-hilfe-einer-formel" >}})
- [Exemplo de fórmula: Lógico se operadores para comparar valores]({{< relref "help/base-editor/formeln/formelbeispiel-logische-if-operatoren-zum-vergleichen-von-werten" >}})
- [Exemplo de fórmula: Calcular a duração de umas férias]({{< relref "help/base-editor/formeln/formelbeispiel-berechne-die-dauer-eines-urlaubs" >}})
- [Exemplo de fórmula: Calcular dias para um evento]({{< relref "help/base-editor/formeln/formelbeispiel-berechne-tage-bis-zu-einem-event" >}})
- [Exemplo de fórmula: Procura de uma palavra num texto]({{< relref "help/base-editor/formeln/formelbeispiel-nach-einem-wort-in-einem-text-suchen" >}})

## As convenções matemáticas também se aplicam em SeaTable

Evidentemente, pode confiar no facto de que as convenções matemáticas também são aplicadas nas fórmulas de SeaTable. Aqui estão os exemplos mais importantes:

- Pode **aninhar funções** umas dentro das outras com parênteses. Exemplo: (( 1 + 2 ) \* 3)
- **O ponto antes do traço**, a **ordem dos parêntesis** e outras **regras matemáticas** são tidas em conta no SeaTable.

## Formatação da coluna de fórmulas

Pode formatar os resultados na coluna da fórmula. Cada fórmula no SeaTable tem como resultado um **número**, uma **data** ou um **texto/corda**. Dependendo disso, estão disponíveis diferentes **definições de formato**.

![Resultados da fórmula de formatação](images/Formatierung-von-Formelergebnissen.jpg)
