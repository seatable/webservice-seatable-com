---
title: 'Colorir células nas vistas de tabela'
date: 2022-10-26
lastmod: '2025-02-25'
categories:
    - 'ansichtsoptionen'
author: 'vge'
url: '/pt/ajuda/colorir-celulas'
aliases:
    - '/pt/ajuda/einfaerben-von-zellen'
seo:
    title: 'Colorir células nas vistas de tabela do SeaTable com regras e valores personaliz.'
    description: 'Aprenda como colorir células no SeaTable usando regras ou valores próprios e destaque dados para melhor análise. Instruções passo a passo.'
weight: 28
---

Ao contrário do Excel, não pode simplesmente colorir células nas vistas de tabela do SeaTable como quiser, mas deve colori-las ou por **regras** definidas por si ou com base nos **valores** numa **coluna**. Parece complicado? Mas não é.

{{< warning  headline="Nota" >}}

Para além da opção de **colorir células**, existe também a possibilidade de [marcação de linhas por cor]({{< relref "help/base-editor/ansichten/farbliche-markierung-von-zeilen" >}}) . Neste caso, porém, as células não são coloridas, mas as marcas coloridas são colocadas no início das filas.

{{< /warning >}}

## Coloração por regras ou por valores

Cada coluna numa vista de tabela oferece a opção **Células colunas coloridas**:  
![Opção de formatação de coluna no SeaTable](images/color-cells.png)

SeaTable comportar-se-á de forma diferente consoante o **tipo de coluna** para o qual chamar esta opção. Para [colunas numéricas]({{< relref "help/base-editor/spaltentypen/die-zahlen-spalte" >}}), pode utilizar tanto regras como valores para colorir. Para todos os outros tipos de colunas, apenas as regras de coloração estão disponíveis.

![Visão geral de coloração de células por regras ou valores](images/color-cells-rules-values.png)

## Para colorir células por uma regra

![Exemplo: colorir células com base em uma regra](images/einfaerben-von-zellen-beispiel-1-1.gif)

1. Clique no **símbolo do triângulo** no cabeçalho da tabela de uma coluna.
2. Seleccionar a opção **Células colunas coloridas**.
3. Ir para **Regras de Utilização**.
4. Clique em **Add Rule (Adicionar regra)**.
5. Clique na nova linha que aparece para definir a regra.
6. Selecione uma **coluna** e escolha uma **condição** no campo central.
7. Introduzir o **valor** a que a condição está ligada.
8. Clique no **ícone do triângulo colorido** na frente da regra para abrir o selector de cores e mudar a cor das células às quais se aplica a sua regra.

Ao utilizar uma regra, colore **todas as células** de uma coluna à qual **se aplica** uma regra. Por exemplo, tal regra poderia ser: "Colorir todas as células com uma classificação de três ou mais estrelas amarelas".

![Resultado: uma regra colore células correspondentes de amarelo](images/Einfaerben-von-Zellen-mit-einer-Regel.png)

É possível criar **várias regras com cores diferentes** por coluna.

![Várias regras com cores diferentes em uma coluna](images/Einfaerben-von-Zellen-mit-mehreren-Regeln.png)

Também pode definir **várias condições** por regra, que podem estar relacionadas com todas as colunas da tabela. Por exemplo, colorir a [coluna de texto]({{< relref "help/base-editor/spaltentypen/die-spalten-text-und-formatierter-text" >}}) com o título de um artigo se o **estado** não for "terminado", a **data de publicação** estiver no futuro e já existir uma **imagem** disponível.

![Regra com várias condições para colorir células](images/Regel-mit-mehreren-Bedingungen-fuer-die-farbliche-Zeilenmarkierung.png)

{{< warning  headline="Diferentes opções dependendo do tipo de coluna"  text="A **seleção** das condições possíveis adapta-se dinamicamente ao tipo de coluna." />}}

## Para colorir células por valores

![Exemplo: colorir células com base em valores no SeaTable](images/einfaerben-von-zellen-beispiel-2-1.gif)

1. Clique no **símbolo do triângulo** no cabeçalho da tabela de uma coluna.
2. Seleccionar a opção **Células colunas coloridas**.
3. Ir para **Valores de Utilização**.
4. Clique na **selecção de cor** para escolher entre mais cores
5. Decidir de qual e até que **valor** deseja formatar as células.
6. Clique em **Submeter**.

Com a opção **Utilizar valores**, colore a coluna inteira. Quanto maior for um valor em todo o espectro, mais escura ou mais clara é a cor da célula.

![Gradiente de claro a escuro conforme valores das células](images/einfaerben-von-zellen-2.png)

Este tipo de coloração ajuda-o a tornar rápida e facilmente visíveis os valores **aberrantes** (isto é, particularmente pequenos ou particularmente grandes) numa coluna.

## Localizar duplicados

![Exemplo: destacar valores duplicados em uma coluna](images/einfaerben-von-zellen-beispiel-3.gif)

1. Clique no **símbolo do triângulo** no cabeçalho da tabela de uma coluna.
2. Seleccionar a opção **Células colunas coloridas**.
3. Ir para **Destacar Duplicações**.

Com a ajuda da opção de **Duplicatas em Destaque**, valores idênticos numa coluna podem ser encontrados rapidamente.

## Perguntas mais frequentes

### Preencher todas as células com a mesma cor

Para o fazer, definir uma regra que se aplique a todas as células desejadas. Por exemplo, é possível colorir todas as células **preenchidas** numa coluna, seleccionando a condição **não está vazia**.

![Exemplo FAQ: colorir todas as células preenchidas](images/einfaerben-von-zellen-6.png)

### Cor nas próximas nomeações

Tem aqui duas opções para colorir as respectivas células de uma coluna de datas. Ou selecciona a condição **em ou depois** e uma **data exacta** - ou selecciona a opção **dentro de um** prazo e um período no futuro.

![Exemplo: destacar datas próximas com cores](images/einfaerben-von-zellen-7.png)

### Colorir uma data específica

Seleccionar a opção **é igual a** e introduzir a respectiva data.

![Exemplo: colorir uma data específica](images/einfaerben-von-zellen-8.png)
