---
title: 'Copiar linhas para outra tabela utilizando um botão'
date: 2024-02-20
lastmod: '2024-02-20'
categories:
    - 'andere-spalten'
author: 'kgr'
url: '/pt/ajuda/copiar-linhas-outra-tabela-botao'
alaises:
    - '/pt/ajuda/zeilen-per-schaltflaeche-in-eine-andere-tabelle-kopieren'
seo:
    title: 'Copiar linhas para outra tabela via botão SeaTable'
    description: 'Copie registros para outras tabelas com um botão no SeaTable: use filtros, condições e automações fáceis por clique ou regras.'

---

É possível utilizar um **botão** para **copiar linhas para outras tabelas**. Isto é útil se precisar de determinados registos de dados em tabelas diferentes, mas não quiser utilizar [uma ligação]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}}). As instruções seguintes ilustram o caso de utilização através de um exemplo.

## Exemplo de aplicação

Está a planear uma **receção de casamento** e já elaborou uma lista de convidados.

![Exemplo de lista de convidados](images/Beispiel-Gaesteliste.png)

Agora também quer organizar a próxima despedida de **solteira** da noiva e a despedida de **solteiro** do noivo. Por conseguinte, pretende copiar os dados dos convidados para duas tabelas adicionais depois de estes terem confirmado a sua presença - consoante o sexo do convidado.

## Criar tabelas adequadas

Criar duas novas tabelas para as respectivas listas de convidados da festa.

{{< warning  headline="Atenção"  text="Os **tipos** e **nomes das colunas** nas tabelas de destino devem ser **idênticos** aos da tabela de origem, caso contrário a ação não funcionará. Todos os valores de coluna que o SeaTable não pode atribuir **não** são copiados e permanecem vazios nas tabelas de destino." />}}

**Sugestão:** Um método simples de adotar a estrutura da tabela original é **duplicar a tabela sem as entradas existentes**.

![Estrutura de tabela duplicada](images/Tabellenstruktur-duplizieren.png)

Nas tabelas vazias, é claro que pode eliminar as colunas que não são necessárias ou adicionar novas colunas numa data posterior.

![Esvaziar tabelas duplicadas](images/Leere-duplizierte-Tabellen.png)

## Criar o botão

![Botão Criar](images/Schaltflaeche-anlegen.gif)

1. Clique no **símbolo de mais** grande na extremidade direita do cabeçalho da tabela.
2. Dê um **nome** à coluna e seleccione _Botão_ como o **tipo de coluna**.
3. Em seguida, defina a **etiqueta** e a **cor do botão**.
4. No passo seguinte, defina o número de **acções** que devem ser desencadeadas pela ativação do botão. No nosso caso, seleccione **Copiar linha para outra tabela**.

![Ação do botão Copiar linha para outra tabela](images/Schaltflaechen-Aktion-Zeile-in-andere-Tabelle-kopieren.gif)

6. Seleccione a **tabela** para a qual as linhas devem ser copiadas.
7. Pode definir **filtros** para ligar a execução de acções de botões a **condições**.
8. Confirmar a criação do botão com **Enviar**.

## Execução condicional de acções de botão

No nosso exemplo de aplicação, os convidados do sexo feminino devem ser copiados para a tabela "Convidados da festa da galinha" e os convidados do sexo masculino para a tabela "Convidados da festa do veado" quando o botão é premido. Para tal, cria-se **duas vezes a mesma ação**, que é equipada com **condições de fil** tragem opostas. Isto permite-lhe copiar os convidados para tabelas diferentes, consoante o sexo, com um único botão.

![Linhas copiadas por botão](images/Per-Schaltflaeche-kopierte-Zeilen.gif)

{{< warning  headline="Nota" >}}

Esta ação de botão não é suportada em [páginas de tabela em aplicações]({{< relref "help/app-builder/seitentypen-in-universellen-apps/tabellenseiten-in-universellen-apps" >}}). É apresentada uma mensagem de erro correspondente quando o botão é premido.

{{< /warning >}}

## A automatização como opção adicional

Se tiver uma subscrição SeaTable Enterprise, também pode automatizar totalmente esta etapa do processo. Para tal, configure uma [automatização]({{< relref "help/base-editor/automationen/beispiel-eintraege-in-andere-tabellen-per-automation-hinzufuegen" >}}).
