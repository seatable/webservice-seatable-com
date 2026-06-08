---
title: 'Criar operações de processamento de dados'
date: 2023-03-03
lastmod: '2023-03-13'
categories:
    - 'datenverarbeitung'
author: 'nsc2'
url: '/pt/ajuda/criar-operacoes-processamento-dados'
aliases:
    - '/pt/ajuda/datenverarbeitungsoperationen-anlegen'
seo:
    title: 'Criar operações de processamento de dados no SeaTable'
    description: 'Passo a passo para criar operações matemáticas, comparar dados e vincular colunas entre tabelas no SeaTable: automação avançada fácil.'

---

Com a ajuda da função de processamento de dados, é possível realizar várias **operações**. Pode efectuar cálculos matemáticos em todos os valores de uma coluna, bem como correlacionar valores quando as entradas em duas tabelas diferentes são idênticas.

Pode criar operações de processamento de dados nas suas tabelas em qualquer altura, utilizando as opções de visualização. Simplesmente armazena os resultados de uma operação numa coluna adicional.

## Criar uma operação de tratamento de dados

![Criar uma acção de tratamento de dados](images/create-an-data-processing-action-1.jpg)

1. Abra qualquer **tabela** para a qual deseje criar uma operação de processamento de dados.
2. Clique nos **três pontos** nas opções de visualização.
3. Clique em **Data Processing** e depois em **Add Data Processing Operation**.
4. Dar um **nome** à operação.
5. Seleccionar uma **operação**.
6. Dependendo da operação, definir a **tabela**, **vista**, **coluna de origem** e **coluna de resultados** ou as tabelas e colunas a serem comparadas.
7. Clique em **Guardar para** guardar a operação e executá-la mais tarde, ou em **Executar** para iniciar directamente a operação.

![Definição da acção de tratamento de dados](images/define-data-processing-action.jpg)

## Operações de tratamento de dados

Estão actualmente disponíveis as seguintes operações:

- Calcular valores acumulados
- Calcular a classificação
- Calcular alterações
- Calcular a percentagem
- Comparar e ligar
- Comparar e copiar
- Transferir nomes de utilizadores

## Requisitos

Existem **diferentes requisitos para a** criação de uma operação de processamento de dados, dependendo da operação.

Para cálculos matemáticos, ou seja, para as operações **Calcular Valores Cumulados**, Calcular **Classificação**, Calcular **Alterações** e Calcular **Percentagem**, são necessárias pelo menos **duas** [colunas de números]({{< relref "help/base-editor/spaltentypen/die-zahlen-spalte" >}}) na vista da tabela seleccionada. Normalmente, a **coluna de origem** já existe e é preenchida com dados, enquanto que a **coluna de resultados** é criada e preenchida com valores através da operação.

Para as outras operações, é necessário em parte [ligar colunas]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}})**(comparar e ligar** & **comparar e copiar**) ou [colunas de texto]({{< relref "help/base-editor/spaltentypen/die-text-spalte" >}})**(transferir nome de utilizador**).
