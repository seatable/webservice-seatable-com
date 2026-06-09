---
title: 'As características especiais da primeira coluna'
date: 2022-10-13
lastmod: '2024-03-15'
categories:
    - 'arbeiten-mit-spalten'
author: 'nsc2'
url: '/pt/ajuda/particularidades-primeira-coluna'
aliases:
  - '/pt/ajuda/die-besonderheiten-der-ersten-spalte'
seo:
    title: 'Particularidades da primeira coluna no SeaTable explicadas'
    description: 'Veja tudo sobre a primeira coluna no SeaTable: limitações, tipos permitidos e como ajustar suas configurações de forma segura e fácil.'
---

A **primeira coluna** de uma tabela no SeaTable tem várias características e restrições especiais em comparação com as outras colunas. Aqui pode descobrir como personalizar a primeira coluna no SeaTable.

## As características especiais da primeira coluna em SeaTable

- Ao contrário das outras colunas, **não é possível ocultar** a primeira coluna de uma tabela.
- Ao contrário das outras colunas, **não é possível deslocar** a primeira coluna de uma tabela.
- Ao contrário das outras colunas, **não é possível eliminar** a primeira coluna de uma tabela.
- No entanto, ao contrário das outras colunas, é possível **fixar** a primeira coluna individualmente.
- Para a **primeira coluna**, existem apenas **seis tipos de colunas** à escolha:
  - [Texto]({{< relref "help/base-editor/spaltentypen/die-text-spalte" >}})
  - [Número]({{< relref "help/base-editor/spaltentypen/die-zahlen-spalte" >}})
  - [Data]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}})
  - [Seleção única]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}})
  - [Número automático]({{< relref "help/base-editor/spaltentypen/der-spaltentyp-automatische-nummer" >}})
  - [Fórmula]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}})

## Como personalizar o tipo da primeira coluna

![Ajustar a primeira coluna](images/change-the-first-column.gif)

1. Clique no **símbolo** triangular **suspenso** à direita do nome da primeira coluna.
2. Ir para **Personalizar tipo de coluna**.
3. Clique no **campo do** tipo de coluna actual.
4. Seleccionar um **novo tipo de coluna** para a primeira coluna.
5. Fazer **configurações de formato**, se necessário.
6. Clique em **Submeter**.
7. Confirmar o ajustamento clicando em **Convert**.

## Fórmulas na primeira coluna

Se definir uma **fórmula** como a **primeira coluna** de uma tabela, pode utilizar a fórmula simples **{nome da coluna}**, por exemplo, para **citar** as entradas de quase todas as outras colunas da sua tabela. Isto funciona mesmo que o outro tipo de coluna **não** seja suportado na primeira coluna.

![Possibilidades com o tipo de coluna Fórmula na primeira coluna de uma tabela](images/formular-in-the-first-column-1.png)

## Perguntas mais frequentes

{{< faq "Quais são as limitações da primeira coluna?" >}}A primeira coluna não pode ser **escondida**, nem **deslocada** ou **apagada**.
{{< /faq >}}
{{< faq "É possível mudar depois o tipo da primeira coluna?" >}}Sim, isto é possível. Em alguns casos, contudo, pode acontecer que a informação **se perca** quando se [muda o tipo de coluna]({{< relref "help/base-editor/spalten/wie-man-den-spaltentyp-anpasst" >}}), por exemplo, de texto para número. Por conseguinte, após uma conversão, verificar se toda a informação foi transferida correcta e completamente.
{{< /faq >}}
{{< faq "O que é um número automático?" >}}Se pretender que as suas linhas tenham um **número de identificação único**, o tipo de coluna [Número automático]({{< relref "help/base-editor/spaltentypen/der-spaltentyp-automatische-nummer" >}}) pode ser-lhe útil. Os exemplos incluem números de facturas, casos de teste ou IDs de empregados. O número também pode ser complementado com qualquer prefixo.

{{< /faq >}}
