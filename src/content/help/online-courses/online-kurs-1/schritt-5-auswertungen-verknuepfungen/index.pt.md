---
title: 'Etapa 5: Análises utilizando as ligações'
date: 2024-08-30
lastmod: '2024-09-05'
categories:
    - 'online-kurs'
author: 'cdb'
url: '/pt/ajuda/passo-5-analises-com-links'
aliases:
    - '/pt/ajuda/schritt-5-auswertungen-verknuepfungen'
seo:
    title: 'Passo 5: análise de dados com links no SeaTable'
    description: 'Aprenda a usar links no SeaTable para criar análises estatísticas dinâmicas e rápidas, agregando dados vinculados com fórmulas rollup.'

---

Ligámos agora os registos de dados de ambas as tabelas. É importante que esta ligação não seja unilateral. Se ligar à tabela `Categories` verá que também foi adicionada uma nova coluna, que mostra as ligações. No nosso caso, isto significa que um problema está ligado a uma categoria e que uma categoria pode estar ligada a muitos problemas.

Ainda não obtivemos quaisquer benefícios diretos da ligação, mas isso está prestes a mudar: Com a ajuda das ligações, podemos criar análises estatísticas numa questão de segundos. Por exemplo, podemos determinar facilmente qual o valor total de todas as despesas na categoria `Travel` é.

## Aumentar a altura da linha

Em primeiro lugar, aumentar a altura da linha na tabela `Categories`para ver mais ligações. Encontrará a opção correspondente `{{< seatable-icon icon="dtable-icon-row-height-default" >}}` na linha acima do nome da coluna. Também pode arrastar colunas individuais para ver mais conteúdo.

![Vista de tabela com altura de linha ajustada para melhor visualização das ligações](images/level1-row-height.png)

## Análise das categorias

Agora crie uma nova coluna na tabela `Categories` para.

> Nome: `Sum`
>
> Tipo de coluna: `{{< seatable-icon icon="dtable-icon-link-formulas" >}} Fórmula de link`
>
> Fórmula: `rollup`
>
> Coluna Link nesta tabela: `Expenses`
>
> Coluna a resumir: `{{< seatable-icon icon="dtable-icon-number" >}} Amount`
>
> Método de resumo: `Soma`

![Coluna de fórmula de ligação «Sum» com rollup para somar valores ligados](images/lvl1-rollup.png)

Em seguida, é possível alterar o formato da coluna `Sum` para euros, para que os totais apresentados sejam formatados em euros.

## Cálculo automático em cada alteração

Não é fantástico? Na coluna `Sum` o total das despesas de cada categoria é sempre apresentado automaticamente. Mesmo que se clique noutras despesas no `Expenses` o total é atualizado imediatamente.

É claro que isto não é tudo. Pode limitar a análise a anos individuais ou acrescentar condições adicionais. À medida que for ganhando mais experiência com o SeaTable, será capaz de criar tais análises com apenas alguns cliques.

Chegamos assim ao fim desta secção. Desloque-se até ao fim e passe para o sexto e penúltimo tópico deste curso online.

{{< warning  headline="Análises estatísticas como um profissional"  text="O SeaTable oferece muitas mais opções para analisar estatisticamente os seus dados. Por isso, pode aguardar o segundo curso em linha, no qual iremos certamente analisar este tópico com mais pormenor." />}}

## Artigo de ajuda com mais informações

- [Ajustar a altura da linha nas vistas de tabela]({{< relref "help/base-editor/ansichten/zeilenhoehe-anpassen" >}})
- [A Fórmula Rollup]({{< relref "help/base-editor/formeln/die-rollup-formel" >}})
