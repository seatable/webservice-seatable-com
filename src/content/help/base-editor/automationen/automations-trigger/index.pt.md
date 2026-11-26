---
title: 'Acionadores de automatização'
date: 2023-01-27
lastmod: '2026-11-25'
categories:
    - 'automationen'
author: 'kgr'
url: '/pt/ajuda/automations-triggers-seatable'
aliases:
    - '/pt/ajuda/automations-trigger'
seo:
    title: 'Acionadores de automatização: SeaTable em resumo'
    description: 'Veja quais eventos (triggers) podem iniciar automatizações no SeaTable – condições, novos dados ou execuções programadas.'
weight: 5
---

Os **eventos de acionamento** são um dos dois componentes essenciais das automatizações. Os eventos desencadeiam diferentes tipos de [ações]({{< relref "help/base-editor/automationen/automations-aktionen" >}}), que pode definir individualmente para cada automatização. Este artigo fornece-lhe uma **visão geral** dos diferentes tipos de acionadores.

## Acionadores de automatização disponíveis

Na versão mais recente do SeaTable, há um total de **quatro** acionadores diferentes para escolher:

![Eventos de acionamento atualmente disponíveis](images/automation-triggers.jpg)

- Quando uma linha é alterada
- Quando uma linha é adicionada
- Numa hora programada
- Numa hora programada para entradas que preencham determinadas condições

## Definições de acionamento

Para criar ou editar um acionador, clique na caixa correspondente na área central do editor de automatização. As definições do acionador aparecem então à direita.

![Definições do acionador](images/automation-trigger-settings.jpg)

- Pode primeiro alterar o **acionador** utilizando o menu pendente. Para tal, selecione o evento de acionamento pretendido.
- De seguida, defina a **tabela** e a **vista** em que a automatização deve ter efeito.
- Dependendo do tipo de acionador, pode efetuar outras definições, por exemplo, **colunas monitorizadas**, **condições** para o acionamento ou a **hora** do acionamento.

![Definições de acionamento em pormenor](images/automation-trigger-settings.gif)

{{< warning headline="Guardar alterações" text="Não se esqueça de **guardar** as definições do acionador! Caso contrário, todas as alterações serão perdidas quando fechar a janela." />}}

## Acionador de automatização: Quando uma linha é alterada

Se selecionar este evento como um acionador, a automatização correspondente é acionada sempre que um valor é alterado numa das colunas monitorizadas e uma linha na vista selecionada preenche determinadas condições após a edição. Se pretender que o acionador seja ativado sempre que é feita uma alteração, não adicione quaisquer condições.

Nas **condições**, pode definir individualmente para cada coluna o aspeto que o valor correspondente deve ter após a edição para que a automatização seja iniciada. Como parte disto, pode decidir se todas ou apenas as colunas selecionadas na vista devem ser monitorizadas para detetar o evento de acionamento.

![Definições de acionamento quando uma linha é alterada](images/automation-trigger-when-a-row-is-updated.jpg)

Se selecionar este evento como o acionador de uma automatização, pode escolher entre as seguintes **ações automáticas**:

- Enviar notificação
- Enviar notificação de aplicação
- Enviar e-mail
- Adicionar registro
- Bloquear registro
- Modificar registro
- Adicionar ligações
- Adicionar uma nova entrada a outra tabela
- Adicionar entrada a uma tabela ligada
- Modificar entrada ligada noutra tabela
- Executar script Python
- Chamar a IA
- Gerir eventos no Google Calendar
- Converter página em PDF

## Acionador de automatização: Quando uma linha é adicionada

Se selecionar este evento como um acionador, a automatização correspondente será acionada sempre que uma **nova linha** for adicionada na vista selecionada. Além disso, pode restringir ainda mais a ocorrência do evento, definindo **condições** que a nova linha deve cumprir.

![Definições de acionamento quando é adicionada uma linha](images/automation-trigger-when-a-row-is-added.jpg)

Nas condições, pode especificar individualmente para cada coluna qual deve ser o valor correspondente para que a automatização seja iniciada. Se pretender que cada nova linha acione a automatização, não adicione quaisquer condições.

{{< warning headline="Sugestão" text="Este acionador é particularmente útil, por exemplo, quando importa novos registos de dados ou os introduz através de formulários." />}}

Se selecionar este evento como o acionador de uma automatização, pode escolher entre as seguintes **ações automáticas**:

- Enviar notificação
- Enviar notificação de aplicação
- Enviar e-mail
- Adicionar registro
- Bloquear registro
- Modificar registro
- Adicionar ligações
- Adicionar uma nova entrada a outra tabela
- Executar script Python
- Chamar a IA
- Gerir eventos no Google Calendar
- Converter página em PDF

## Acionador de automatização: Numa hora programada

Se selecionar este acionador, pode então definir uma **hora** em que a automatização é executada **diariamente**, **semanalmente** ou **mensalmente**.

![Opções de definição para um acionamento diário numa hora programada](images/automation-trigger-at-scheduled-time.jpg)

Enquanto só pode especificar a **hora** para uma automatização diária, também pode especificar o **dia da semana** para uma automatização semanal ou o **dia do calendário** para uma automatização mensal.

![Opções de definição para um acionamento semanal numa hora programada](images/automation-trigger-at-scheduled-time-weekly.jpg)

Se definir este acionador para uma automatização, pode escolher entre as seguintes **ações automáticas**:

- Enviar notificação
- Enviar notificação de aplicação
- Enviar e-mail
- Adicionar registro
- Adicionar ligações
- Executar script Python
- Executar processamento de dados
- Gerar PDF a partir do documento e enviar
- Arquivar

## Acionador de automatização: Numa hora programada para entradas que preencham determinadas condições

Com este acionador, especifica uma **hora**, tal como no acionador anterior, em que a automatização é acionada **diariamente**, **semanalmente** ou **mensalmente**. Também pode limitar as linhas que são afetadas por este evento de acionamento.

Para as **condições**, pode especificar individualmente para cada coluna qual deve ser o valor correspondente para que a automatização seja executada na hora especificada.

![Acionador numa hora programada para entradas que preencham determinadas condições](images/automation-trigger-at-scheduled-time-for-records-that-match-condition.jpg)

Se selecionar este acionador para uma automatização, pode escolher entre as seguintes **ações automáticas**:

- Enviar notificação
- Enviar notificação de aplicação
- Enviar e-mail
- Bloquear registro
- Modificar registro
- Converter página em PDF
- Arquivar
