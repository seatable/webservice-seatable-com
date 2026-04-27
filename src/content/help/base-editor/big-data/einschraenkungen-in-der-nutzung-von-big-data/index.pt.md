---
title: 'Limitações na utilização de Big Data'
date: 2023-05-11
lastmod: '2024-12-16'
categories:
    - 'big-data'
author: 'nsc2'
url: '/pt/ajuda/limitacoes-big-data-seatable'
aliases:
    - '/pt/ajuda/einschraenkungen-in-der-nutzung-von-big-data'
seo:
    title: 'SeaTable Big Data: principais limitações e dicas'
    description: 'Veja as limitações da função Big Data do SeaTable: sincronia, edição, compartilhamento, operações e recomendações práticas para o gerenciamento eficiente.'

---

Uma vista normal no SeaTable permite o trabalho **colaborativo** **em tempo real** **até 100.000 linhas**. O Big Data permite-lhe **armazenar** linhas **ilimitadas**, mas reduz a sua capacidade de colaboração. Antes de utilizar o Big Data, não se esqueça de consultar este artigo de ajuda para saber quais as limitações que deve esperar ao utilizar o Big Data.

## Limitações do Big Data

O armazenamento de grandes volumes de dados oferece-lhe um **armazenamento** amplamente **ilimitado de linhas**, mas também tem algumas limitações. Pode encontrar uma visão geral das **restrições** abaixo:

- As alterações a uma entrada de Big Data **não** são **sincronizadas** em **tempo real** no browser de outro utilizador. As alterações só são visíveis para outros utilizadores após um **recarregamento** da página.
- **Não é possível partilhar** visualizações de Big Data - nem individualmente nem com [autorizações de partilha definidas pelo utilizador]({{< relref "help/startseite/freigaben/benutzerdefinierte-freigabe-erstellen" >}}).
- **Não é possível** criar **novas linhas** numa vista de megadados. Isto deve ser sempre feito numa [vista normal]({{< relref "help/base-editor/zeilen/zeilen-kommentieren" >}}).
- Numa vista de grandes volumes de dados, não é possível [ajustar]({{< relref "help/base-editor/spalten/spaltenberechtigungen-festlegen" >}}).
- **Não é possível modificar**[entradas ligadas]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}}) em entradas de grandes volumes de dados. As ligações a linhas na memória de grandes volumes de dados **não** são apresentadas em vistas normais - mas são apresentadas numa vista de grandes volumes de dados.
- A formatação condicional[(realçar linhas com cores]({{< relref "help/base-editor/ansichten/einfaerben-von-zellen" >}}).
- [As operações de processamento de dados]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitungsoperationen-in-seatable" >}}) **não** estão disponíveis para grandes volumes de dados. A única exceção é [comparar e juntar]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-vergleichen-und-verknuepfen" >}}). Esta operação pode ligar entradas na memória de grandes volumes de dados com linhas em qualquer outra tabela, independentemente de as linhas estarem armazenadas na base ou na memória de grandes volumes de dados.
- A função de [pesquisa e substituição]({{< relref "help/base-editor/tabellen/suchen-und-ersetzen-von-werten-in-seatable" >}}) **não** está disponível.

{{< warning  headline="Muitas destas limitações dos grandes volumes de dados não se aplicam à aplicação" >}}

A maioria dos utilizadores de armazenamento de grandes volumes de dados não sente que o seu trabalho seja afetado por estas restrições. No entanto, se for afetado, pode dar uma vista de olhos à [aplicação]({{< relref "help/app-builder/app-verwaltung/universelle-app" >}}). Algumas das restrições mencionadas não se aplicam aí.

{{< /warning >}}
