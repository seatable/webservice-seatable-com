---
title: 'Criar uma nova tabela com um registo comum'
date: 2022-12-15
lastmod: '2024-06-12'
categories:
    - 'gemeinsame-datensaetze'
author: 'nsc2'
url: '/pt/ajuda/criar-tabela-conjunto-dados-comum'
aliases:
    - '/pt/ajuda/mit-einem-gemeinsamen-datensatz-eine-neue-tabelle-anlegen'
seo:
    title: 'Criar tabela com conjunto de dados comum SeaTable'
    description: 'Veja como criar uma nova tabela a partir de dados compartilhados no SeaTable, incluindo pré-requisitos, passos e sincronização de dados.'
---

Para utilizar um registo comum noutra base, pode importar a visualização da tabela correspondente do registo comum para a base desejada. Para tal, criar uma nova tabela na base com o conjunto de dados correspondente. Poderá então trabalhar com os dados do conjunto de dados comum ou a vista de tabela, incluindo condições específicas de filtragem e classificação, na base seleccionada.

## Requisitos

Para poder criar uma nova tabela numa base com um registo de dados partilhado, a base deve cumprir um dos dois requisitos seguintes:

1. A base deve pertencer ao **grupo** em que o registo de dados partilhados foi **criado**.
2. A base deve pertencer a um **grupo** para o qual o registo de dados partilhados tenha sido previamente **libertado**.

{{< warning  headline="Nota importante"  text="Uma base **deve** atender a um desses dois requisitos para que uma nova tabela possa ser criada nela com um registro de dados compartilhado. No entanto, **se** nenhum dos dois pré-requisitos se aplicar a uma base, **não** é possível criar uma nova tabela com um registo de dados partilhado." />}}

## Criar uma nova tabela com um registo comum

![Criar uma nova tabela com um registo comum](images/image-how-to-create-a-new-table-with-a-common-dataset.png)

1. Abrir uma **tabela** que se encontre numa base que cumpra um dos **requisitos** acima descritos.
2. Clique no **símbolo \[+\]** para criar uma nova tabela.
3. Clique em **Importar Registo Partilhado**.
4. Seleccionar um **registo comum**.
5. O conjunto de dados comum é então importado para a sua Base como uma **nova tabela**.

Se a **importação** do conjunto de dados comum for **bem sucedida**, aparece a seguinte mensagem:

![A seguinte mensagem aparece quando o Conjunto de Dados Comum é importado com sucesso](images/Erfolgsmeldung-beim-Import-eines-GD-.png)

## Características dos quadros criados com um conjunto de dados comum

As tabelas criadas com um registo de dados partilhados podem ser distinguidas das outras tabelas pelo **símbolo de pilha** à frente do nome da tabela. Se passar o ponteiro do rato sobre o ícone, um pequeno **texto informativo** também indica que a tabela foi criada com um registo de dados partilhado.

![Ícone em frente do nome de tabelas de um conjunto de dados comum.](images/icon-table-common-dataset-1.png)

Outra caraterística é o **carácter** no ícone das colunas que contêm dados de um conjunto de dados **partilhado**. As colunas da tabela que **não** contêm dados de um registo de dados partilhado **não** têm, por isso, esta etiqueta no ícone da coluna.

![Coluna de um conjunto de dados comum (esquerda) e coluna regular (direita)](images/icons-of-the-column-of-a-common-dataset-2.png)

## Consequências para o processamento de dados

A regra dominante que deve seguir ao trabalhar com registos partilhados é que a informação flui apenas **numa direcção**. Em termos concretos, isto significa que as alterações aos registos partilhados e às tabelas criadas com um registo partilhado só têm um efeito num sentido - nomeadamente em direcção às **tabelas**.

Se fizer alterações a uma visão de tabela que tenha publicado como um **conjunto de dados comum**, estas alterações são também adoptadas em todas as tabelas que foram criadas com o conjunto de dados comum correspondente. O pré-requisito para tal é uma **sincronização das respectivas tabelas com o conjunto de dados**, o que [pode ser feito automática ou manualmente]({{< relref "help/startseite/gemeinsame-datensaetze/synchronisation-eines-gemeinsamen-datensatzes" >}}).

Se, por outro lado, fizer alterações aos dados do conjunto de dados comum num quadro criado com um conjunto de dados comum, essas alterações **não** afectam a estrutura do conjunto de dados comum. As alterações serão então aplicadas **exclusivamente** à sua tabela e serão novamente **substituídas** da próxima vez que **se sincronizar** com o conjunto de dados.

No entanto, o que permanece na tabela durante a sincronização são **os nomes de colunas modificados**. Portanto, é possível renomear as colunas do registo de dados partilhados na tabela como se desejar.
