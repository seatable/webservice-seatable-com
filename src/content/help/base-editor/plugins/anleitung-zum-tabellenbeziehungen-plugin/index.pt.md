---
title: 'Instruções para o plugin de relações de tabela'
date: 2024-07-29
lastmod: '2024-08-01'
categories:
    - 'plugins'
author: 'kgr'
url: '/pt/ajuda/guia-plugin-relacoes-tabelas'
aliases:
    - '/pt/ajuda/anleitung-zum-tabellenbeziehungen-plugin'
seo:
    title: 'Guia do plugin de relações entre tabelas SeaTable'
    description: 'Aprenda a usar o plugin de relações entre tabelas no SeaTable para visualizar e gerenciar ligações entre tabelas das suas bases.'

---

Especialmente quando existem muitas tabelas com dezenas de colunas numa base, é fácil perder a noção de como estão relacionadas umas com as outras. Pode utilizar o plugin de relações entre tabelas para visualizar as tabelas que estão ligadas entre si através de que colunas.

Pode descobrir como ativar o plugin numa base [aqui]({{< relref "help/base-editor/plugins/aktivieren-eines-plugins-in-einer-base" >}}).

![Plugin de relações de tabela](images/Table-Relationships-Plugin.png)

## Como funciona o plugin

Depois de ter configurado e aberto o plugin de relações de tabela, começa por ver **todas as tabelas** da base. **Todas as colunas** que são criadas nas respectivas tabelas são listadas sob os nomes de tabela coloridos.

Para visualizar as relações de tabela, verá não só **linhas sólidas** para ligações _directas_ através de [colunas de ligação]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}), mas também **linhas tracejadas** para ligações _indirectas_ através de colunas de fórmula de ligação (por exemplo, [pesquisas]({{< relref "help/base-editor/formeln/die-lookup-funktion" >}}).

## Definir opções para um gráfico de relações de tabela

Por defeito, já é criado um gráfico com todas as relações de tabela quando o plug-in de relações de tabela é aberto pela primeira vez. {{< seatable-icon icon="dtable-icon-add-table" >}} Se pretender criar outro gráfico, clique em **Adicionar nova relação de tabela**. Isto abre um campo de entrada no qual pode introduzir o **nome** pretendido.

![Opções de um gráfico de relações de tabela](images/Options-of-Table-Relationship-Chart.png)

{{< seatable-icon icon="dtable-icon-drag" >}} Para **alterar a ordem dos gráficos**, mantenha premido o botão esquerdo do rato na **superfície de aperto** e arraste **e largue** um gráfico para a posição pretendida. Também é possível **renomear**, **duplicar** ou **eliminar** os gráficos.

{{< warning  headline="Nota"  text="Se apenas for criado um único gráfico no plugin, **não é possível** eliminá-lo." />}}

{{< seatable-icon icon="dtable-icon-set-up" >}} Através das **definições**, às quais se acede clicando no **símbolo da roda dentada**, é possível definir o seguinte para o gráfico, **(des)activando** os **cursores**:

- Deseja visualizar **ligações para outras entradas** (ligações directas)?
- Deseja visualizar **fórmulas para ligações** (ligações indirectas)?
- Pretende apresentar **fórmulas de dois níveis para ligações** (por exemplo, uma fórmula de pesquisa que obtém valores da coluna de pesquisa de outra tabela)?
- Gostaria de apresentar **tabelas sem ligações**?

![Definir opções para um gráfico de relações de tabela](images/Settings-of-Table-Relationship-Chart.png)

## Mover tabelas num gráfico

É possível mover as várias tabelas no gráfico, conforme necessário, **usando arrastar e soltar**. Para isso, manter pressionado o botão esquerdo do mouse, arrastar a tabela para a posição desejada e soltá-la.

![Mover tabelas em um gráfico de relações de tabela usando arrastar e soltar](images/Move-tables-in-a-Table-Relationship-Chart.gif)
