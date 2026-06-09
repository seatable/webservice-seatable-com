---
title: 'Filtrar entradas numa vista'
date: 2022-11-16
lastmod: '2025-02-25'
categories:
    - 'ansichtsoptionen'
author: 'kgr'
url: '/pt/ajuda/filtrar-registros-visualizacao-seatable'
aliases:
    - '/pt/ajuda/filtern-von-eintraegen-in-einer-ansicht'
seo:
    title: 'Filtrar registros em uma vista SeaTable: dicas, exemplos e métodos'
    description: 'Veja como mostrar apenas os dados relevantes de sua tabela SeaTable criando filtros personalizados, agrupados e tipos de campo flexíveis para análise eficiente.'
weight: 21
---

Com a função de filtro do SeaTable, é possível utilizar **regras de filtragem** para filtrar as entradas desejadas de uma tabela e exibir apenas as entradas que satisfazem determinados critérios. O conjunto de filtros refere-se apenas à **vista activa**.

{{< warning headline="Nota importante" text="A filtragem apenas altera o número de registos de dados apresentados na sua vista! A base de dados permanece inalterada pela filtragem e as linhas invisíveis não são eliminadas. Assim, se os registos de dados tiverem desaparecido, verifique se está na vista correta ou se ocultou registos de dados com um filtro." />}}

## Filtrar entradas numa vista

![Filtrar entradas](images/Filtern-von-Eintraegen-1.gif)

1. Seleccione a **vista** na qual pretende definir um filtro.
2. Clique em **Filtrar** nas opções de visualização acima da tabela.
3. Ir para **Adicionar filtro** ou **Adicionar grupo de filtros**.
4. No primeiro campo, seleccione a **coluna** para a qual pretende definir uma regra de filtragem.
5. No campo do meio, definir a **condição** segundo a qual as entradas devem ser filtradas.
6. No último campo, decida qual a **opção** ou **valor** a que a condição se deve referir.

## As diferentes condições ao filtrar

SeaTable suporta a filtragem por todos os [tipos de colunas]({{< relref "help/base-editor/spalten/uebersicht-alle-spaltentypen" >}}) exceto botões.

Dependendo do **tipo de coluna** que se pretende filtrar, as condições que se podem seleccionar também se adaptam.

### Aqui estão alguns exemplos

Tem estas opções de condição com um [Coluna de texto]({{< relref "help/base-editor/spaltentypen/die-text-spalte" >}}): 

![Filtrar coluna de texto](images/filtern-von-eintraegen-5.png)

Tem estas opções de condição com um [Coluna de seleção única]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}}): 

![Coluna de selecção única com filtro](images/filtern-von-eintraegen-6.png)

Tem estas opções de condição com um [Coluna de imagem]({{< relref "help/base-editor/spaltentypen/die-bild-spalte" >}}): 

![Filtrar coluna de imagem](images/filtern-von-eintraegen-7.png)

As linhas **com células vazias** na coluna de filtro não são geralmente apresentadas, a menos que "está vazio" seja explicitamente procurado.

## Retirar um filtro

Pode **eliminar** filtros que tenha criado clicando no **símbolo x**. 

![Remoção de um filtro de uma vista](images/filtern-von-eintraegen.png)

## Aplicar vários filtros

Pode criar um ou mais filtros que restringem ainda mais a primeira condição. Leia mais sobre isto no artigo [Ligar as regras de filtragem com AND e OR]({{< relref "help/base-editor/ansichten/filter-regeln-mit-und-und-oder-verknuepfen" >}}).

## Filtros de rearranjo

É possível mover e reorganizar os filtros movendo o rato sobre o **superfície de agarrar**, premir e manter, puxar e soltar.  

![Filtrar Entradas de Ordenação](images/Filtern-von-Eintraegen-2.gif)
