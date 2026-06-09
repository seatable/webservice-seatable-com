---
title: 'As colunas Último modificador y Último tempo modificado'
date: 2023-01-20
lastmod: '2023-08-04'
categories:
    - 'datum-dauer-und-personen'
author: 'nsc2'
url: '/pt/ajuda/ultimo-editor-data-alteracao-seatable'
aliases:
    - '/pt/ajuda/die-spalten-letzter-bearbeiter-und-bearbeitungsdatum'
seo:
    title: 'Último editor e data de alteração em SeaTable'
    description: 'As colunas especiais do SeaTable informam que usuário alterou cada linha e quando, proporcionando rastreio, automações e controle de versões.'
weight: 23
---

As colunas **Último modificador** y **Último tempo modificado** são exclusivamente preenchidas **automaticamente** pelo SeaTable e são, portanto, tipos de colunas especiais. Revelam-se extremamente úteis se pretender registar **quando** e **por quem** uma entrada foi **editada pela última vez**.

Uma vez que as duas colunas registam automaticamente as alterações às entradas, elas são bem adequadas, por exemplo, como gatilhos para [automatismos]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}}) e [triagem]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}}).

## As colunas Último modificador y Último tempo modificado

Enquanto o SeaTable preenche a coluna **Último modificador** com o nome do utilizador que editou uma linha pela última vez, a coluna **Último tempo modificado** regista a data e hora exacta em que ocorreu a última edição.

![As colunas Último modificador y Último tempo modificado após criação por um utilizador](images/last-modifiere-and-last-modified-time.png)

## Características especiais dos dois tipos de colunas

- **Não é possível** modificar manualmente os valores inseridos automaticamente nas colunas Último modificador y Último tempo modificado. Os valores são actualizados assim que é feita uma modificação numa linha.
- Ao criar os dois tipos de coluna, **não** existem opções disponíveis, para além do nome da coluna.
- Só pode ser criada **uma** coluna do respetivo tipo por tabela. Se tentar criar outra coluna do mesmo tipo, aparece a mensagem "Outra coluna tem este tipo de coluna".

![Mensagem de erro para outra coluna do Último modificador](images/Fehlermeldung-bei-weiterer-Letzter-Bearbeiter-Spalte.png)

- Por este motivo, não é possível **duplicar** as colunas Último modificador y Último tempo modificado ou **personalizar o seu tipo de coluna**.
