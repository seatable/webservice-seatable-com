---
title: 'A Fórmula Findmin'
date: 2023-02-13
lastmod: '2023-02-13'
categories:
    - 'verknuepfungen'
author: 'vge'
url: '/pt/ajuda/formula-findmin'
aliases:
    - '/pt/ajuda/die-findmin-formel'
seo:
    title: 'Fórmula Findmin no SeaTable – menor valor automático'
    description: 'Saiba como aplicar a fórmula Findmin no SeaTable para localizar o valor mínimo em registros vinculados e colunas numéricas.'
---

A **fórmula Findmin** procura o **valor mínimo** entre as entradas de uma coluna ligada e devolve-o. Isto é útil se houver **várias entradas** na tabela ligada que se referem ao mesmo registo (por exemplo, de uma pessoa) noutra tabela.

A fórmula Findmin só funciona com **valores numéricos**, razão pela qual o conteúdo da coluna ligada deve também consistir em valores numéricos. Além disso, a utilização da fórmula Findmin só faz sentido se o selector **Permitir a ligação a várias linhas** for activado ao criar a coluna **Ligação a outras entradas**. Se a opção estivesse desligada, a fórmula Findmin conteria sempre o mesmo número que na coluna ligada.

## Para que precisa da fórmula Findmin

A **função Findmin** deve ser utilizada quando se pretende **cruzar os** valores numéricos armazenados em diferentes tabelas. Digamos que utiliza o SeaTable para recolher as **horas de trabalho dos** seus empregados, onde uma tabela armazena os empregados e outra tabela armazena a actividade diária. Pode então ligar cada registo de empregado às horas de trabalho introduzidas.

![fórmula de minas finas](images/findmax-1.png)

Para determinar quando um membro da equipa iniciou sessão pela primeira vez, pode usar a **fórmula Findmin** para mostrar o **menor valor** - neste caso o primeiro login - a partir dos tempos totais de login numa coluna.

![fórmula de minas finas](images/findmin.png)

Pode usar a fórmula Findmin para todos os valores numéricos para representar o **valor mínimo**.

## Para usar a fórmula Findmin

### Acrescentar uma ligação de tabela

Descubra como criar uma coluna do tipo **Ligar a outras entradas** [no]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}}). Este é um requisito básico para se poder utilizar a fórmula Findmin.

### Adicionar uma coluna com fórmula Findmin

![fórmula de minas finas](images/findmin.gif)

1. Criar uma nova coluna do tipo **Fórmula para links**.
2. Defina a opção **Findmin** como a fórmula.
3. Seleccione a coluna previamente criada do tipo **Link para outras entradas** nesta tabela.
4. No campo **Selecionar coluna de pesquisa** na **tabela ligada "...", seleccione** a coluna da outra tabela que pretende ligar à coluna aqui.
5. Clique em **Submeter**.

{{< warning  headline="Atenção"  text="A fórmula Findmin funciona exclusivamente com **valores numéricos**e é por isso que a coluna ligada deve conter valores numéricos." />}}
