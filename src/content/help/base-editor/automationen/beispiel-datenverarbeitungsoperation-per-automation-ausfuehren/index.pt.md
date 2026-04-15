---
title: 'Efectuar a operação de tratamento de dados por automatização'
date: 2023-04-28
lastmod: '2023-05-03'
categories:
    - 'beispiel-automationen'
author: 'nsc2'
url: '/pt/ajuda/automatizar-operacao-dados-seatable'
aliases:
    - '/pt/ajuda/datenverarbeitungsoperation-per-automation-ausfuehren'
seo:
    title: 'Automatize operações de dados em SeaTable'
    description: 'Execute operações de processamento de dados por automações e poupe tempo: cálculos, ligações e mais, de forma recorrente e segura.'

---

Com a ajuda da automatização, já não é necessário executar uma operação de processamento de dados manualmente, mas sim automaticamente. A variedade de [operações de processamento de dados]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitungsoperationen-in-seatable" >}}) disponíveis - desde cálculos matemáticos até à criação de ligações entre valores em diferentes tabelas - abre novas possibilidades para automatizar os seus processos de trabalho.

## Efectuar uma operação de tratamento de dados por automatização

![Efectuar operações de tratamento de dados por automatização](images/how-to-use-automations-for-locking-rows-3.png)

1. Clique em {{< seatable-icon icon="dtable-icon-rule" >}} no cabeçalho da Base e depois nas **Regras de Automatização**.
2. Clique em **Add Rule (Adicionar regra)**.
3. Dê um **nome** à automatização e defina a **tabela** e a **vista em** que esta deve ser accionada.
4. Definir um **evento de disparo que desencadeia** a automatização.
5. Clique em **Adicionar acção** e seleccione **Executar operação de processamento de dados** como a acção automatizada.
6. Seleccionar qualquer **operação de processamento de dados**.
7. Efectuar as **opções** necessárias (por exemplo, tabela, coluna de origem, coluna de resultados) na **operação de processamento de dados**.
8. Confirmar com **Submeter**.

## Criar a automatização

Depois de determinar em que **tabela** e **visão a** automatização deve ser accionada, definir o [evento de accionamento]({{< relref "help/base-editor/automationen/automations-trigger" >}}). Atualmente, apenas um **acionador periódico** pode resultar em uma operação de processamento de dados. Portanto, é necessário definir um **momento** em que a automação deve ser acionada diariamente, semanalmente ou mensalmente.

![Selecção do accionador de automatização para a acção: Executar operação de processamento de dados](images/select-trigger-for-data-operation-per-automation.png)

{{< warning  headline="Nota importante"  text="A ação automatizada **Executar operação de tratamento de dados** está disponível para si **exclusivamente** disponível no seguinte acto gerador:" />}}

!["Acionador periódico]({{< relref "help/base-editor/automationen/automations-trigger" >}}#automations-trigger_periodischer_trigger)

Em seguida, seleccione **Executar operação de tratamento de dados** como acção automatizada e escolha a [operação de tratamento de dados]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitungsoperationen-in-seatable" >}}) pretendida.

![Adicionar a acção automatizada](images/add-an-action.png)

![Selecção da operação de tratamento de dados a executar como acção automatizada da automatização](images/select-data-operation-for-automation.png)

As seguintes **operações de tratamento de dados** estão à sua disposição:

- [Calcular valores acumulados]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-kumulierte-werte-berechnen" >}})
- [Calcular variações]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-veraenderungen-berechnen" >}})
- [Calcular percentagem]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-prozentualen-anteil-berechnen" >}})
- [Calcular ranking]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-rangliste-berechnen" >}})
- [Transferir nomes de utilizador]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-benutzernamen-uebertragen" >}})
- [Comparar e copiar]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-vergleichen-und-kopieren" >}})

No passo seguinte, efectue **definições** específicas na **operação de tratamento de dados** que deve ser desencadeada pela automatização. Dependendo da operação seleccionada, ser-lhe-á pedido que defina **tabelas** e/ou **colunas** (por exemplo, coluna de origem e de resultados) que pretende utilizar para os cálculos matemáticos ou para estabelecer relações entre valores em diferentes tabelas.

![Definições específicas a efectuar na operação de tratamento de dados](images/specific-settings-for-data-processing-operation.png)

Por fim, confirme a automatização com **Submeter** para a guardar e a fazer executar no momento definido pelo acionador, ou clique em **Executar agora** para que a automatização seja executada **imediatamente**.

![Guardar a automatização ou executá-la directamente](images/cancel-run-now-or-submit-automation.png)

## Exemplo de aplicação

Um caso de utilização concreto deste tipo de automatização poderia surgir, por exemplo, se pretendesse registar na sua tabela o número de acessos diários a um sítio Web. Para o efeito, pretende **somar** linha a linha, numa nova coluna, os **números de acessos** de cada dia, registados numa [coluna numérica]({{< relref "help/base-editor/spaltentypen/die-zahlen-spalte" >}}) existente.

Até agora, [o cálculo dos números de acessos acumulados com uma operação de tratamento de dados]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-kumulierte-werte-berechnen" >}}) só era possível **manualmente**. Com uma automatização correspondente, é agora possível ter os números de acessos acumulados calculados **automaticamente**, **todos os dias**, a uma hora fixa.

Para a implementação, necessita primeiro de uma tabela na qual os vários **dias** estão registados numa [coluna de data]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}) e os **números de acessos** ao sítio Web numa [coluna numérica]({{< relref "help/base-editor/spaltentypen/die-zahlen-spalte" >}}).

![Tabela de exemplo para o caso de utilização da automatização: Calcular valores acumulados](images/Beispiel-Tabelle-automation-data-processing-kumulierte-werte-berechnen.png)

Em seguida, adicione à tabela uma **segunda coluna numérica** na qual, após cada execução da automatização, os valores acumulados serão calculados. A nova coluna _Cumulated Visitors_, inicialmente vazia, actua na operação de tratamento de dados como **coluna de resultados**, enquanto a coluna _Unique Visitors_ constitui a **coluna de origem**.

![Adicionar uma segunda coluna numérica](images/Beispiel-Tabelle-automation-data-processing-kumulierte-werte-berechnen-2.png)

Para criar a automatização, siga os passos descritos na secção [Criar a automatização]({{< relref "help/base-editor/automationen/anlegen-einer-automation" >}}). Seleccione igualmente a coluna _Unique Visitors_ como **coluna de origem** e a coluna recém-adicionada _Cumulated Visitors_ como **coluna de resultados**.

![Selecção da coluna de origem e da coluna de resultados](images/auswahl-quell-und-ergebnisspalte-im-anwendungsfall.png)

Após a confirmação da automatização, o SeaTable calcula diariamente, à hora seleccionada, o **número acumulado de visitantes do sítio Web** e escreve-o automaticamente na coluna de resultados. O cálculo automático dos valores acumulados pressupõe naturalmente que o **número de visitantes do sítio Web do dia anterior** seja escrito diariamente, **antes** da execução da automatização, na coluna _Unique Visitors_.

Tabela **antes** do disparo da automatização:

![Tabela de exemplo antes do disparo da automatização](images/Beispiel-Tabelle-vor-Ausloesung-der-Auomation-Kumulierte-Werte-Berechnen.png)

Tabela **depois** do disparo da automatização:

![Tabela de exemplo depois do disparo da automatização](images/Beispiel-Tabelle-nach-Ausloesung-der-Automation-Kumulierte-Werte-berechnen.png)
