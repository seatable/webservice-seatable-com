---
title: 'Definir o valor predefinido para uma coluna'
date: 2023-11-07
lastmod: '2024-06-11'
categories:
    - 'arbeiten-mit-spalten'
author: 'kgr'
url: '/pt/ajuda/definir-valor-padrao-coluna'
aliases:
    - '/pt/ajuda/standardwert-fuer-eine-spalte-festlegen'
seo:
    title: 'Definir valor padrão para uma coluna no SeaTable'
    description: 'Saiba como definir valores padrão em colunas do SeaTable para preencher novas linhas automaticamente e ganhar tempo na inserção de dados.'
---

Se definir um **valor prede** finido para uma coluna, este é **automaticamente introduzido em cada nova linha** da tabela. Com valores predefinidos, pode poupar alguns cliques ao [adicionar novas linhas]({{< relref "help/base-editor/zeilen/hinzufuegen-einer-zeile" >}}). É claro que pode ajustar manualmente os valores introduzidos automaticamente mais tarde.

## Como definir valores por defeito

![Definir o valor predefinido para uma coluna](images/Standardwert-festlegen.gif)

1. Clique no **ícone** triangular do menu **pendente** {{< seatable-icon icon="dtable-icon-drop-down" color="grey" >}} à direita do nome da coluna para a qual pretende definir um valor predefinido.
2. Seleccione a opção **Definir valor por defeito**.
3. Introduzir o **valor proposto** desejado. Dependendo do tipo de coluna, existem várias opções para selecionar.
4. Confirmar o processo com o **botão Enter** ou **clicando** fora da janela de diálogo.
5. Se **criar** agora uma **nova linha**, o SeaTable introduz automaticamente os valores correspondentes. Pode então **ajustar** os dados como habitualmente.

{{< warning  headline="Atenção"  text="Os valores por defeito são utilizados **universalmente** na criação de novas linhas, ou seja, as linhas criadas através de uma ação automática ou de um botão também contêm os valores por defeito." />}}

Também é possível definir um valor por defeito diretamente ao [criar uma nova coluna]({{< relref "help/base-editor/spalten/hinzufuegen-einer-spalte" >}}).

## Para que tipos de colunas é possível definir valores por defeito

Os valores predefinidos podem ser definidos para muitos, mas não todos, os [tipos de colunas no SeaTable]({{< relref "help/base-editor/spalten/uebersicht-alle-spaltentypen" >}}). As colunas cujo conteúdo é gerado automaticamente pelo SeaTable[(fórmulas]({{< relref "help/base-editor/spaltentypen/die-bild-spalte" >}}), [ficheiros]({{< relref "help/base-editor/spaltentypen/die-datei-spalte" >}}) e [assinaturas]({{< relref "help/base-editor/spaltentypen/die-signatur-spalte" >}}).

**Segue-se uma síntese dos tipos de colunas para os quais é possível definir valores propostos:**

| Tipo de coluna       | Suporta valores por defeito                                   |
| -------------------- | ------------------------------------------------------------- |
| Número automático    | {{< icon "circle-xmark" >}}                                   |
| Imagem               | {{< icon "circle-xmark" >}}                                   |
| Caixa de verificação | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Ficheiro             | {{< icon "circle-xmark" >}}                                   |
| Data                 | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Duração              | {{< icon "circle-xmark" >}}                                   |
| Selecção única       | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Correio electrónico  | {{< icon "circle-xmark" >}}                                   |
| Criador              | {{< icon "circle-xmark" >}}                                   |
| Criado em            | {{< icon "circle-xmark" >}}                                   |
| Texto formatado      | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Fórmula              | {{< icon "circle-xmark" >}}                                   |
| Fórmula para links   | {{< icon "circle-xmark" >}}                                   |
| Geoposição           | {{< icon "circle-xmark" >}}                                   |
| Último editor        | {{< icon "circle-xmark" >}}                                   |
| Selecção múltipla    | {{< icon "circle-xmark" >}}                                   |
| Empregados           | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Classificação        | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Botão                | {{< icon "circle-xmark" >}}                                   |
| Assinatura           | {{< icon "circle-xmark" >}}                                   |
| Texto                | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| URL                  | {{< icon "circle-xmark" >}}                                   |
| Número               | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Última edição        | {{< icon "circle-xmark" >}}                                   |

## Valores por defeito referenciados em colunas de texto

Se especificar a referência **{creator.name}** ou **{creator.id}** como valor predefinido numa [coluna de texto]({{< relref "help/base-editor/spaltentypen/die-spalten-text-und-formatierter-text" >}}), o **nome** ou **ID do utilizador** que adicionou a linha é automaticamente introduzido.

![Referência ao nome do utilizador com um valor predefinido](images/Set-creator-name-as-default-value.png)

## O âmbito dos valores por defeito

Os valores predefinidos aplicam-se **sempre que** é possível criar novas linhas:

- num [quadro]({{< relref "help/base-editor/zeilen/hinzufuegen-einer-zeile" >}})
- numa [coluna de ligação]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}})
- via [botão]({{< relref "help/base-editor/schaltflaechen/zeilen-per-schaltflaeche-in-eine-andere-tabelle-kopieren" >}}) (ação: "Copiar linha para outra tabela")
- através da [automatização]({{< relref "help/base-editor/automationen/automations-aktionen" >}}) (acções: "Adicionar linha" e "Adicionar nova entrada noutra tabela")
- no [calendário]({{< relref "help/base-editor/plugins/anleitung-zum-kanban-plugin" >}})
- através de [formulários Web]({{< relref "help/base-editor/webformulare/webformulare" >}})
- nas [páginas]({{< relref "help/app-builder/seitentypen-in-universellen-apps/tabellenseiten-in-universellen-apps" >}}), [formulário]({{< relref "help/app-builder/seitentypen-in-universellen-apps/formularseiten-in-universellen-apps" >}}) e [Kanban]({{< relref "help/app-builder/seitentypen-in-universellen-apps/kanbanseiten-in-universellen-apps" >}}) das aplicações

![O valor por defeito aplica-se a todas as novas linhas](images/Standardwert-greift-ueberall-bei-neuen-Zeilen.gif)

## Valores por defeito em formulários Web

Para além dos valores por defeito definidos na tabela, [os formulários Web]({{< relref "help/base-editor/webformulare/webformulare" >}}) também permitem definir valores por defeito para os campos de formulário ligados às colunas. Também é possível definir se os utilizadores podem **alterar** estes valores por defeito ao preencherem o formulário.

![Definir valores predefinidos em formulários Web](images/Set-default-values-in-web-forms.png)

{{< warning  headline="Nota importante"  text="Se for definido um valor predefinido na tabela e no formulário Web, o valor do formulário aplica-se a todas as linhas que são criadas através do formulário Web. Os valores por defeito definidos na tabela **só têm efeito** se não forem definidos quaisquer valores por defeito no editor de formulários." />}}

## Valores por defeito nas aplicações

Os valores predefinidos definidos na base também afectam as linhas que são introduzidas nas **páginas de tabela, formulário e Kanban** das [aplicações]({{< relref "help/app-builder/app-verwaltung/universelle-app" >}}). O único [tipo de página]({{< relref "help/app-builder/seitentypen-in-universellen-apps/ueberblick" >}}) para o qual ainda é possível definir valores predefinidos na aplicação é a [página de formulário]({{< relref "help/app-builder/seitentypen-in-universellen-apps/formularseiten-in-universellen-apps" >}}). As definições funcionam exatamente da mesma forma que para os formulários Web: Para tal, active os cursores, como mostra a imagem acima.
