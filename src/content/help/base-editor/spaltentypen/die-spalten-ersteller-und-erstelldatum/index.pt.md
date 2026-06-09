---
title: 'As colunas Criador e Tempo criado'
date: 2023-01-20
lastmod: '2023-08-04'
categories:
    - 'datum-dauer-und-personen'
author: 'nsc2'
url: '/pt/ajuda/colunas-criador-criado-seatable'
aliases:
    - '/pt/ajuda/die-spalten-ersteller-und-erstelldatum'
seo:
    title: 'Colunas “criador” e “criado” no SeaTable: log automático e histórico detalhado'
    description: 'SeaTable usa "Criador" e "Criado" para registrar automaticamente usuários e datas. Ambas as colunas não podem ser editadas manualmente.'
weight: 21
---

As colunas **Criador** e **Tempo criado** são exclusivamente preenchidas **automaticamente** pelo SeaTable e, portanto, representam tipos de colunas especiais. Enquanto o SeaTable preenche a coluna Criador com o **nome do utilizador** que criou uma linha, a coluna Tempo criado regista a **data e hora** em que o utilizador criou a linha.

![As colunas "Criador e Criado" após a criação de um utilizador](images/column-creator-and-created-time.png)

## Características especiais dos dois tipos de colunas

- Os valores introduzidos automaticamente nas colunas Criador e Tempo criado **não podem** ser editados.
- Ao criar os dois tipos de coluna, **não** estão disponíveis **quaisquer** opções, para além do nome da coluna.
- Só pode ser criada **uma** coluna de Criador e Tempo criado por tabela. Se tentar criar outra coluna do mesmo tipo, aparece a mensagem "Outra coluna tem este tipo de coluna".

![Mensagem de erro para outra coluna criadora](images/Fehlermeldung-bei-weiterer-Ersteller-Spalte.png)

- Por este motivo, não é possível **duplicar** as colunas do Criador e da Tempo criado **ou personalizar o seu tipo de coluna**.
