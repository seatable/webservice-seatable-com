---
title: 'A coluna de texto longo'
date: 2023-02-21
lastmod: '2023-11-08'
categories:
    - 'text-und-zahlen'
author: 'kgr'
url: '/pt/ajuda/coluna-de-texto-longo'
aliases:
    - '/pt/ajuda/die-spalten-text-und-formatierter-text'
    - '/pt/ajuda/texto-vs-texto-formatado-seatable'
seo:
    title: 'A coluna de texto longo: tipo de coluna SeaTable'
    description: 'Registe textos estruturados de qualquer dimensão com a coluna de texto longo do SeaTable: listas, imagens, links e muito mais no editor.'
weight: 2
---

Para o **registo de textos estruturados de qualquer dimensão**, o SeaTable disponibiliza o tipo de coluna *Texto longo*. Saiba neste artigo quais são as diferenças relativamente à coluna de texto e em que casos faz sentido recorrer à coluna de texto longo.

## Utilização da coluna de texto longo

Ao contrário da coluna de texto, o tipo de coluna **Texto longo** não regista cadeias de caracteres não estruturadas, mas sim textos formatados com quebras de linha, listas, imagens, etc.

![A coluna de texto longo](images/formatted-text-column.png)

As colunas de texto longo são particularmente adequadas para guardar **textos mais longos**, por exemplo descrições de produtos, listas de verificação ou publicações nas redes sociais.

{{< warning  headline="UTF-8"  text="O SeaTable suporta todos os caracteres de acordo com a norma UTF-8, uma vez que o UTF-8 é a codificação de caracteres mais difundida no mundo para a Internet." />}}

**Não** escreve as suas entradas diretamente na célula, mas num **editor** que pode ser chamado com um clique, o qual oferece várias **opções de formatação**. Assim, ao contrário da coluna de texto, também pode estruturar textos mais longos.

![Exemplo de aplicação de uma coluna de texto longo](images/long-text-example.png)

Entre outras coisas, pode escolher um **formato de parágrafo**, definir a **fonte** para itálico ou negrito, bem como inserir **links**, **citações**, **listas**, **tabelas** e **imagens**.

{{< warning  type="warning" headline="Limite de caracteres"  text="Aplica-se um limite de 100.000 caracteres às células individuais do tipo Texto longo. Isto corresponde a aproximadamente 25 páginas A4 de texto. O limite de caracteres só deverá, portanto, ter um impacto no seu trabalho em casos excecionais." />}}

## Outros tipos de colunas baseadas em texto

Se pretender registar **cadeias de caracteres curtas sem formatação** (por exemplo nomes, palavras-passe, matrículas de veículos), deve utilizar a [coluna de texto]({{< relref "help/base-editor/spaltentypen/die-text-spalte" >}}).

Para além da coluna de texto longo, existem no SeaTable três outros tipos de colunas baseadas em texto para casos de utilização especiais:
- a [coluna de correio eletrónico]({{< relref "help/base-editor/spaltentypen/die-e-mail-spalte" >}})
- a [coluna URL]({{< relref "help/base-editor/spaltentypen/die-url-spalte" >}})
- a [coluna de número de telefone]({{< relref "help/base-editor/spaltentypen/die-telefonnummer-spalte" >}})

## Definir valor predefinido

É possível definir um [valor predefinido]({{< relref "help/base-editor/spalten/standardwert-fuer-eine-spalte-festlegen" >}}) para cada coluna de texto longo. Este texto é automaticamente introduzido na célula em cada linha criada recentemente.

1. Clique na **seta do menu pendente** à direita do nome da coluna.
2. Vá a **Definir valor predefinido**.
3. Ao clicar em **Editar texto**, abre-se o editor, onde pode redigir o texto que servirá de valor predefinido.

## Restrições nos filtros, na ordenação e no agrupamento

Não é possível ordenar nem agrupar as entradas de uma tabela por colunas de texto longo. Nos filtros, apenas tem as opções "está vazio" e "não está vazio" à disposição.
