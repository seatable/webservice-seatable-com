---
title: 'A coluna de seleção múltipla'
date: 2023-03-28
lastmod: '2025-07-15'
categories:
    - 'spalten'
author: 'kgr'
url: '/pt/ajuda/coluna-selecao-multipla'
aliases:
    - '/pt/ajuda/die-mehrfachauswahl-spalte'
seo:
    title: 'Coluna de seleção múltipla no SeaTable: opções e cores'
    description: 'Aprenda a usar seleção múltipla – etiquetas coloridas, ordenação, exportação, cores personalizadas e diferenças para seleção única.'
weight: 8
---

Uma coluna de seleção múltipla é ideal se quiser atribuir as suas linhas numa coluna **várias opções** de uma lista de opções a serem definidas. As opções são dadas etiquetas coloridas que pode utilizar para rotular os seus registos e tornar as tabelas claras, por exemplo, através [de filtragem]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}}) para opções específicas.

![Tabela de exemplo com uma coluna de seleção múltipla](images/example-table-multiple-select.png)

## Criar uma coluna de seleção múltipla

A criação de uma coluna de seleção múltipla é uma brincadeira de criança e feita com apenas alguns cliques. Para informações detalhadas, ver [Adicionar uma coluna]({{< relref "help/base-editor/spalten/hinzufuegen-einer-spalte" >}}).

1. Clique no **símbolo \[+\]** à direita da última coluna de qualquer tabela.
2. Dê um **nome** à nova coluna.
3. Selecione **Seleção múltipla** como tipo de coluna.
4. Confirme com **Enviar**.

## Semelhanças com a coluna de seleção única

### Adicione várias opções de seleção

Adicionar opções a uma coluna de seleção múltipla funciona **exatamente da mesma forma que com uma coluna de seleção única**. Pode adicionar novas opções de várias formas. Saiba tudo sobre isto no artigo [sobre a coluna de seleção única]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}}).

### Exportar e importar opções de seleção múltipla

Pode **exportar** e **importar** as opções de uma coluna de seleção múltipla da mesma forma que uma coluna de seleção única. Pode encontrar mais informações sobre isto no artigo sobre a coluna de seleção única.

### Cores das opções

Tal como na coluna de seleção única, estão atualmente disponíveis **24 cores** para realçar visualmente as respectivas opções.

![Cores da coluna de seleção única](images/farben-einfachauswahl.png)

Com uma [subscrição Enterprise]({{< relref "help/teamverwaltung/abonnement/abo-pakete" >}}), também tem a opção de criar as suas [próprias cores]({{< relref "help/base-editor/weitere-optionen/eigene-farben-in-einer-base-hinzufuegen" >}}) para as suas múltiplas opções de seleção.

### Altere a ordem das opções de seleção múltipla

A ordem das opções pode ser ajustada da mesma forma que para uma única coluna de seleção. É de importância crucial se quiser [ordenar]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}}) ou [agrupar]({{< relref "help/base-editor/ansichten/gruppieren-von-eintraegen-in-einer-ansicht" >}}) pela coluna de seleção múltipla. Isto deve-se ao facto de o SeaTable **não organizar as opções por ordem alfabética**, mas sim de forma flexível, de acordo com a **ordem das opções** que especificar utilizando a função arrastar e largar.

### Defina o valor padrão

Ao contrário da coluna de seleção única, você **não pode** especificar um valor padrão para uma coluna de seleção múltipla.

## Seleção múltipla ou ligação a outras entradas?

Se pretender guardar **informação adicional** para cada opção de seleção, deve considerar a utilização de uma [coluna de ligação]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}) em vez de uma coluna de seleção múltipla. Para tal, crie registos de dados completos para todas as opções numa tabela separada, que pode ligar a qualquer número de linhas noutras tabelas.
