---
title: 'Passo 1: Criar uma nova base'
date: 2024-08-30
lastmod: '2024-09-04'
categories:
    - 'online-kurs'
author: 'cdb'
url: '/pt/ajuda/passo1-criar-base-despesas-seatable'
aliases:
    - '/pt/ajuda/schritt-1-anlegen-einer-neuen-base'
seo:
    title: 'Passo 1 Curso SeaTable 1: crie sua base de despesas agora'
    description: 'Início do curso: crie uma base do zero no SeaTable, defina colunas e categorias e prepare o rastreamento de despesas pessoais e profissionais.'
---

Neste curso, vamos criar uma ferramenta simples para registar e gerir as suas despesas pessoais ou profissionais. Quando estiver pronto, pode registar as despesas a qualquer momento, seja no seu computador ou no seu telemóvel. Sempre que puxar da carteira, deve documentar essa despesa. A recompensa por este esforço é o facto de poder ver rapidamente em que gastou quanto dinheiro.

Assim, vamos começar este curso online criando a estrutura necessária para poder guardar estes resultados. Para o fazer, vai criar uma base inicial e depois algumas colunas. Verá que os passos seguintes são quase auto-explicativos.

{{< warning  headline="Uma pequena dica para trabalhar eficazmente com este curso em linha"  text="Gostaria de recomendar que tivesse duas janelas do browser abertas no seu monitor e que as colocasse uma ao lado da outra. Abra este artigo numa janela do browser e abra o SeaTable na outra. Desta forma, será muito mais fácil seguir os passos deste curso sem ter de mudar constantemente de janela." />}}

![](images/level1-browser-window-setup.png)

## Criar uma nova base

Começamos na página inicial do SeaTable. Criar uma nova base com o nome `Expense Tracking` botão. Em seguida, clique nesta base para aceder ao Editor de bases.

## Alterar o nome da primeira tabela

Por defeito, cada base contém uma tabela com o nome `Table 1`que tem uma coluna com três linhas.

- Eliminar as três linhas
- Em seguida, altere o nome da tabela para `Expenses`

{{< warning  headline="Ajuda se ficar preso"  text="A utilização do SeaTable deve ser intuitiva na maioria dos casos. Por exemplo, pode eliminar linhas da mesma forma que está habituado a fazer em muitas outras soluções de software: Selecione as linhas e clique com o botão direito do rato. Se ainda precisar de ajuda, lembre-se dos artigos de ajuda que compilámos para si na parte inferior da página. Aí encontrará as instruções corretas para cada passo deste curso online." />}}

## Personalizar as colunas da tabela e adicionar novas colunas

Em seguida, passamos às colunas da tabela para que a nossa base possa registar os dados desejados.

- Alterar o nome da primeira coluna de `Name` sobre `Reason`
- Agora adicione mais três colunas

**Coluna 1:**

> Nome: `Date`
>
> Tipo de coluna: `{{< seatable-icon icon="dtable-icon-calendar-alt-solid" >}} Date`
>
> Formato: qualquer
>
> Ao minuto: `Yes`

**Nota:** Em vez do tipo de coluna `{{< seatable-icon icon="dtable-icon-calendar-alt-solid" >}} Date` o tipo de coluna `{{< seatable-icon icon="dtable-icon-creation-time" >}} Created time` pode ser utilizado. Enquanto a coluna da data tem de ser preenchida manualmente, esta seria preenchida automaticamente com a data atual. É claro que isso economiza tempo. No entanto, a desvantagem seria que não seria mais possível modificar o valor da data e, por exemplo, não seria mais possível entrar retroativamente despesas de outros dias.

---

**Coluna 2:**

> Nome: `Amount`
>
> Tipo de coluna: `{{< seatable-icon icon="dtable-icon-number" >}} Number`
>
> Formato: `Euro`

---

**Coluna 3:**

> Nome: `Category`
>
> Tipo de coluna: `{{< seatable-icon icon="dtable-icon-single-election" >}} Single select`

---

{{< warning  headline="26 tipos de colunas"  text="Até agora, só viu uma fração dos tipos de colunas possíveis. Um dos maiores pontos fortes do SeaTable é o facto de poder armazenar qualquer tipo de informação graças aos 26 tipos de colunas atualmente disponíveis." />}}

## Adicionar opções de seleção individuais

A seleção única não tem atualmente opções de seleção. Portanto, em seguida, criar uma nova seleção para a coluna `Category` as quatro opções seguintes:

- Vestuário
- Mercearia
- Lazer
- Viagens

## Breve controlo de qualidade

Fantástico. Se seguiu exatamente as instruções, a sua base deve agora ter o seguinte aspeto:

![](images/level1-expenses-table.png)

Vamos recapitular brevemente o que acabou de criar com apenas alguns cliques no rato: **Tem agora uma base na qual pode registar todas as suas despesas futuras.**

Ao mesmo tempo, ao selecionar os tipos de colunas, o utilizador garante que apenas as informações adequadas podem ser introduzidas nas colunas.

Este foi o passo 1 deste curso online. Desloque-se até ao fim deste artigo e salte para o **passo 2: Criar um formulário**.

## Artigo de ajuda com mais informações

- [Criar uma nova base]({{< relref "help/startseite/bases/eine-neue-base-erstellen" >}})
- [Como ajustar o tipo de coluna]({{< relref "help/base-editor/spalten/wie-man-den-spaltentyp-anpasst" >}})
- [Apagar uma linha]({{< relref "help/base-editor/zeilen/das-loeschen-von-zeilen" >}})
- [Adicionar uma coluna]({{< relref "help/base-editor/spalten/hinzufuegen-einer-spalte" >}})
- [Acrescentar opções a uma coluna de selecção única]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}})
- [Caraterísticas especiais da primeira coluna]({{< relref "help/base-editor/spalten/die-besonderheiten-der-ersten-spalte" >}})
- [Personalizar a aparência de uma base (ícone e cor)]({{< relref "help/startseite/bases/aussehen-einer-base-anpassen-icon-und-farbe" >}})
