---
title: 'Processamento de dados: Comparar e copiar'
date: 2023-03-17
lastmod: '2023-11-27'
categories:
    - 'datenverarbeitung'
author: 'nsc2'
url: '/pt/ajuda/comparar-copiar-dados-seatable'
aliases:
    - '/pt/ajuda/datenverarbeitung-vergleichen-und-kopieren'
seo:
    title: 'Compare e copie dados facilmente no SeaTable'
    description: 'Transfira valores entre tabelas SeaTable de modo prático quando existir coincidência de valores em campos definidos.'
---

É possível utilizar a função de processamento de dados para executar várias operações em uma coluna. **Comparar e copiar** é uma operação com a qual é possível copiar os valores de uma coluna de uma tabela para a coluna de outra tabela, desde que um determinado valor de comparação seja idêntico em ambos os registos de dados.

## Pôr em prática a operação

![Criar uma acção de tratamento de dados](images/create-an-data-processing-action-1.jpg)

1. Abrir qualquer **tabela** e clicar nos **três pontos** das opções de visualização.
2. Clique em **Data Processing** e depois em **Add Data Processing Operation**.
3. Dar um **nome** à operação e seleccionar **Comparar e Copiar**.

![Nomear a acção de tratamento de dados e seleccionar o tipo de operação](images/name-operation-and-select-operation-type-exmaple-copy.jpg)

5. Definir de **que tabela** provêm os dados e **em que tabela** pretende copiar os dados.
6. Definir uma ou mais **condições** em que duas colunas das tabelas comparadas devem ter um valor idêntico para a operação a ser realizada.
7. Seleccionar uma ou mais **colunas de origem** das quais os valores serão copiados para **colunas de resultados** que também precisam de ser definidas, desde que as condições de correspondência que definir sejam cumpridas.

![Definição da acção de tratamento de dados](images/name-operation-and-define-columns-example-copy-1.png)

{{< warning  headline="Nota"  text="Com um clique em **Adicionar**, pode seleccionar quantas colunas quiser para outras **condições** ou **processos de cópia**." />}}

11. Clique em **Guardar para** guardar a acção e executá-la mais tarde, ou em **Executar** para executar a acção directamente.

A primeira vez que é executado com sucesso, um pequeno **carrapato verde**.  
![Se a acção de processamento de dados for executada com sucesso pela primeira vez, aparece uma marca verde](images/gruener-haken-zur-bestaetigung-der-ersten-ausfuehrung.jpg)

## Estojo de utilização

Um caso concreto de utilização para esta operação de processamento de dados pode ocorrer, por exemplo, se mantiver os **dados dos funcionários** da sua equipa numa tabela e quiser criar as **tarefas da sua equipa** que ainda precisam de ser completadas numa nova tabela. Ao adicionar uma coluna com os **nomes dos** funcionários responsáveis pelas respectivas tarefas, pretende criar uma correspondência entre as tabelas.

Subsequentemente, pretende que certos dados dos empregados, que já existem na tabela de empregados, sejam copiados para a tabela de tarefas. Por exemplo, poderá também precisar do **endereço de correio electrónico** para poder contactar directamente a pessoa responsável.

Para implementar esta operação de processamento de dados, são necessárias **duas tabelas na mesma base**. Na primeira tabela, os **dados do pessoal** são mantidos, o que inclui, entre outras coisas, os **endereços de correio electrónico** do pessoal.

![Tabela de exemplo para a manutenção dos dados pessoais dos empregados](images/example-table-employees-and-personal-data-1.png)

Na segunda tabela são introduzidas as **tarefas em aberto**, para as quais o respectivo funcionário responsável é introduzido noutra coluna. Além disso, cria-se uma nova coluna do tipo [e-mail]({{< relref "help/base-editor/spaltentypen/die-e-mail-spalte" >}}), para a qual os endereços de e-mail devem ser copiados mais tarde.

![Tabela de destino incluindo a coluna de resultados antes da execução da acção de processamento de dados](images/table-open-tasks-before-data-processing-operation-1.png)

Para criar a operação de processamento de dados, seguir os passos descritos acima. Para o caso de utilização específica, seleccionar como **condição** que o **nome** de um funcionário na coluna do nome da tabela de **funcionários** deve corresponder ao nome na coluna **responsável** da tabela de **tarefas em aberto**. Esta etapa é essencial para que os dados correctos dos funcionários correspondentes sejam copiados durante a operação de processamento de dados.

![Definição da condição de correspondência para a acção de processamento de dados](images/define-condition-for-data-operation-compare-and-copy.png)

{{< warning  headline="Nota importante"  text="Nesta operação de processamento de dados, as colunas a serem comparadas devem ter **o mesmo tipo de coluna** para que o SeaTable possa reconhecer de forma fiável valores idênticos." />}}

No passo seguinte, pode seleccionar qualquer número de colunas de origem da tabela de **funcionários**, cujo conteúdo será copiado para as colunas de resultados seleccionados da tabela de **tarefas em aberto** quando a operação for executada e a justa condição de correspondência definida for verdadeira.

![Selecção das colunas da tabela de origem cujo conteúdo é copiado para a tabela de destino, se a condição de correspondência for cumprida.](images/select-columns-to-copy.png)

{{< warning  headline="Cuidado com a perda de dados" >}}

As colunas de origem e resultado devem ter **o mesmo tipo de coluna** para que não se percam dados quando se copia. Pode-se, por exemplo, copiar dados de uma [coluna de data]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}) para uma [coluna de texto]({{< relref "help/base-editor/spaltentypen/die-spalten-text-und-formatierter-text" >}}), mas estes já não são adequados para [calendários]({{< relref "help/base-editor/ansichten/die-kalender-ansicht" >}}). Portanto, antes de realizar a operação, crie uma coluna de **resultados** do mesmo tipo na tabela de destino para cada coluna de **origem** que pretende copiar.

{{< /warning >}}

Se a operação for executada com sucesso, as tabelas de **funcionários** e **tarefas em aberto** são verificadas quanto à correspondência no **nome das** colunas definidas e **responsáveis**. Se os **nomes** nas colunas de ambas as tabelas corresponderem, o **endereço de e-mail do** funcionário correspondente é automaticamente copiado do **e-mail** da coluna definida para o **contacto da** coluna de resultados.

![Conteúdo copiado para a tabela de destino após a acção de processamento de dados ter sido desencadeada.](images/table-after-data-processing-operation-2.png)

{{< warning  headline="Nota"  text="Para facilidade de compreensão, decidimos no caso de utilização copiar apenas **uma coluna** utilizando a operação de processamento de dados. Para aumentar o efeito, é claro que também se pode seleccionar um maior número de colunas de origem e de resultados." />}}

## Tipos de colunas não suportados

Os seguintes tipos de colunas **não podem** ser copiados através da operação _Comparar e copiar_ e, portanto, **não** estão disponíveis ao definir as colunas de origem e de resultado.

- [Coluna de selecção múltipla]({{< relref "help/base-editor/spaltentypen/die-mehrfachauswahl-spalte" >}})
- [A coluna do Criador]({{< relref "help/base-editor/spaltentypen/die-spalten-ersteller-und-erstelldatum" >}})
- [A coluna do último editor]({{< relref "help/base-editor/spaltentypen/die-spalten-letzter-bearbeiter-und-bearbeitungsdatum" >}})
- [Botão]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}})
