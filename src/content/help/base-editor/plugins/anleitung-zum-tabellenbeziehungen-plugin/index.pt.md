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

## Gestão de um diagrama de relações

Por defeito, já é criado um diagrama com todas as relações de tabela quando o plugin de relações de tabela é aberto pela primeira vez. Se pretender criar outro diagrama de relações, clique em {{< seatable-icon icon="dtable-icon-add-table" >}} **Adicionar diagrama de relações**. Isto abre um campo de entrada no qual pode introduzir o **nome** pretendido.

![Opções de gestão de um diagrama de relações](images/table-relationship-plugin-management-options.png)

Quando passa o ponteiro do rato sobre o nome de um diagrama, aparecem três ícones. Para **alterar a ordem dos diagramas**, mantenha premido o botão esquerdo do rato na **superfície de aperto** {{< seatable-icon icon="dtable-icon-drag" >}} e **arraste e largue** um diagrama para a posição pretendida.

![Opções de um diagrama de relações](images/Options-of-Table-Relationship-Chart.png)

Além disso, pode clicar nos **três pontos** para gerir o diagrama. Estão disponíveis as seguintes opções:
- **renomear**
- **duplicar**
- **eliminar**
- **repor**
- **exportar como imagem**.

{{< warning  type="warning" headline="Nota"  text="Se apenas for criado um único diagrama no plugin, **não é possível** eliminá-lo." />}}

## Definições de um diagrama de relações

Através das **definições**, às quais se acede clicando no **símbolo da roda dentada** {{< seatable-icon icon="dtable-icon-set-up" >}}, é possível definir o seguinte para um diagrama, **(des)activando** os **cursores**:

- Deseja visualizar **ligações para outras tabelas** (ligações directas)?
- Deseja visualizar **ligações dentro de uma tabela** (ligações directas)?
- Deseja visualizar **fórmulas para ligações** (ligações indirectas)? Em caso afirmativo, que tipos de fórmulas de ligação?
- Deseja visualizar **todas as colunas independentemente das vistas**?
- Gostaria de apresentar **tabelas sem ligações**?
- Deseja **mostrar ou ocultar tabelas**?

![Opções de definição de um diagrama de relações](images/table-relationship-plugin-settings.png)

## Opções de design de um diagrama de relações

Vá para o separador **Design**, no canto superior direito, ao lado das definições, para alterar o estilo de determinados elementos num diagrama. Clique na **seta pendente** à frente de um elemento para expandir as definições disponíveis:

- **Tabelas**: cor do cabeçalho da tabela e tamanho do tipo de letra
- **Colunas de ligação** (ligações directas): largura de linha, estilo de linha e cor de linha
- **Fórmulas para ligações** (ligações indirectas de primeiro nível): largura de linha, estilo de linha e cor de linha
- **Fórmulas multinível para ligações** (ligações aninhadas de níveis superiores, por exemplo, uma fórmula de pesquisa que obtém valores através de outra coluna de ligação da tabela ligada): largura de linha, estilo de linha e cor de linha
- **Definir cor de fundo para exportação**

![Opções de design de um diagrama de relações](images/table-relationship-plugin-theme.png)

## Mover tabelas num diagrama

É possível mover as várias tabelas num diagrama, conforme necessário, **usando arrastar e largar**. Para isso, mantenha premido o botão esquerdo do rato, arraste a tabela para a posição desejada e largue-a.

![Mover tabelas num diagrama de relações usando arrastar e largar](images/Move-tables-in-a-Table-Relationship-Chart.gif)

## Adicionar uma nota num diagrama de relações

Pode também adicionar uma nota num diagrama de relações clicando no ícone de nota no canto inferior esquerdo. Em seguida, tem as seguintes opções:

- editar texto
- ocultar fundo
- alinhar o texto à esquerda, ao centro ou à direita
- eliminar nota

![Adicionar uma nota num diagrama de relações](images/add-note-on-table-relationship-chart.png)
