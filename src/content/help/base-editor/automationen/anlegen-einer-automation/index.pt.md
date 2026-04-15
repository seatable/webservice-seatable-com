---
title: 'Criar uma automatização'
date: 2022-12-06
lastmod: '2025-11-04'
categories:
    - 'automationen'
author: 'kgr'
url: '/pt/ajuda/criar-automacao'
aliases:
    - '/pt/ajuda/anlegen-einer-automation'
seo:
    title: 'Criar automação no SeaTable – tutorial prático'
    description: 'Veja como criar automações no SeaTable – gatilhos, ações e regras para automatizar e facilitar processos na sua base.'
weight: 2
---

Com a ajuda de automatizações, pode **automatizar processos** de modo a não só poupar tempo, mas também minimizar o número de erros humanos. O primeiro passo para fluxos de trabalho automatizados é a criação de uma automatização.

## Criar uma automatização

1. Abra a **Base** na qual pretende criar uma automatização.

![Criar automações](images/how-to-use-automations.jpg)

2. No cabeçalho da base, clique em {{< seatable-icon icon="dtable-icon-rule" >}} e depois em **Regras de automatização**.

3. Clique em **Adicionar regra ou pasta** e depois em **Regra**.

![Criar uma automatização](images/add-automation.jpg)

4. Atribua um **nome** à regra de automatização.

5. Crie a automatização pretendida, definindo um **acionador** e várias **acções**.

{{< warning headline="Dica" text="Se ainda não existirem regras na base, também pode selecionar um acionador diretamente **para a primeira automatização** – e SeaTable criará automaticamente uma regra." />}}

![Atalho para a primeira automatização](images/shortcut-add-first-automation.gif)

### Crie uma regra de automatização numa pasta

Se já tiver criado uma pasta para regras de automatização, também pode criar uma regra diretamente na pasta. Para o fazer, mova o ponteiro do rato sobre a pasta, clique nos **três pontos** e em **Adicionar regra**.

![Criar regra de automatização numa pasta](images/add-automation-in-folder.jpg)

## Outras etapas de automatização

### Administração

Em primeiro lugar, pode gerir a nova regra de automatização, por exemplo, **renomear**, **eliminar** ou **mover para uma pasta**.

{{< button label="Mais sobre a gestão de regras de automatização" link="help/base-editor/automationen/automationen-verwalten-und-gruppieren" >}}

### Accionadores

No passo seguinte, define um evento que serve de acionador e inicia a automatização. Aqui também especifica em que **tabela** e em que **vista** a automatização deve ter efeito. O **acionador** pode ser a adição de uma linha ou o cumprimento de determinadas condições após uma alteração. Também pode definir a automatização para ser acionada diariamente, semanalmente ou mensalmente numa hora específica.

![definições de acionamento](images/trigger-settings.jpg)

{{< button label="Mais sobre accionadores de automatização" link="help/base-editor/automationen/automations-trigger" >}}

### Acções

Por fim, defina uma ou mais **acções** que são acionadas pelo evento de acionamento definido anteriormente. Dependendo do tipo de acionador, as acções possíveis podem incluir o envio de notificações e e-mails, a adição ou o bloqueio de entradas ou a execução de uma função de IA.

![Outras etapas de automatização](images/steps-for-automation.jpg)

{{< button label="Mais sobre acções de automatização" link="help/base-editor/automationen/automations-aktionen" >}}
