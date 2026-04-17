---
title: 'Como personalizar o tipo de coluna'
date: 2022-10-10
lastmod: '2024-03-15'
categories:
    - 'arbeiten-mit-spalten'
author: 'nsc2'
url: '/pt/ajuda/alterar-tipo-coluna-seatable'
aliases:
    - '/pt/ajuda/wie-man-den-spaltentyp-anpasst'
seo:
    title: 'Alterar tipo de coluna no SeaTable: rápido e seguro'
    description: 'Ajuste o tipo de coluna via menu em SeaTable e veja um aviso se houver risco de perda de dados antes de salvar as alterações.'

---

Dependendo dos **valores** que pretende registar no SeaTable, pode atribuir-lhes diferentes **tipos de colunas**. Pode encontrar uma síntese de todos os 26 tipos de colunas no SeaTable [aqui]({{< relref "help/base-editor/spalten/uebersicht-alle-spaltentypen" >}}).

É possível modificar o tipo de coluna numa data posterior. Aqui pode descobrir como **alterar** o tipo de coluna **retrospetivamente**.

## Como ajustar o tipo de coluna

![Como ajustar o tipo de coluna](images/how-to-costumize-a-coloumn-type.gif)

1. Clique no **ícone** triangular {{< seatable-icon icon="dtable-icon-drop-down" color="grey" >}} à direita do nome da coluna cujo tipo pretende personalizar.
2. Seleccionar a opção **Personalizar tipo de coluna**.
3. Atribuir um novo **tipo de coluna** à coluna e fazer outras **configurações** específicas, se necessário.
4. Confirmar o processo clicando em **Submeter**.

{{< warning  headline="Nota"  text="Nem todos os tipos de colunas podem ser ajustados posteriormente. Por exemplo, os tipos de colunas automaticamente preenchidos **Created**, **Created by**, **Last** **edited** e **Last edited** são imutáveis." />}}

## Ajustar a primeira coluna

A **primeira coluna** de uma tabela suporta **apenas 6 dos 26 tipos de coluna**. Estes são

- [Texto]({{< relref "help/base-editor/spaltentypen/die-spalten-text-und-formatierter-text" >}})
- [Número]({{< relref "help/base-editor/spaltentypen/die-zahlen-spalte" >}})
- [Data]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}})
- [Seleção única]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}})
- [Número automático]({{< relref "help/base-editor/spaltentypen/der-spaltentyp-automatische-nummer" >}})
- [Fórmula]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}})

## Aviso de perda de dados

**A conversão de** certos tipos de colunas conduz normalmente a uma **perda** indesejada de **dados**. É o caso, por exemplo, das colunas [de ficheiros]({{< relref "help/base-editor/spaltentypen/die-bild-spalte" >}}) ou quando converte [colunas de texto]({{< relref "help/base-editor/spaltentypen/die-spalten-text-und-formatierter-text" >}}) em colunas numéricas. Nestes casos, o SeaTable apresenta uma **mensagem de aviso** a perguntar se pretende realmente alterar o tipo de coluna.
