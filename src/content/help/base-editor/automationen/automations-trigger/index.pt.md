---
title: 'Acionadores de automatização'
date: 2023-01-27
lastmod: '2025-11-11'
categories:
    - 'automationen'
author: 'kgr'
url: '/pt/ajuda/automations-triggers-seatable'
aliases:
    - '/pt/ajuda/automations-trigger'
seo:
    title: 'Disparadores de automação: SeaTable em resumo'
    description: 'Veja quais eventos (triggers) podem iniciar automações no SeaTable – condições, novos dados ou execuções programadas.'
weight: 5
---

**Os eventos de acionamento** são um dos dois componentes essenciais das automatizações. Os eventos desencadeiam diferentes tipos de [acções]({{< relref "help/base-editor/automationen/automations-aktionen" >}}), que pode definir individualmente para cada automatização. Este artigo fornece-lhe uma **visão geral** dos diferentes tipos de acionadores.

## Acionadores de automação disponíveis

Na versão mais recente do SeaTable, há um total de **quatro** acionadores diferentes para escolher:

![Eventos de acionamento atualmente disponíveis](images/automation-triggers.jpg)

- Quando uma linha é alterada
- Quando uma linha é adicionada
- Numa hora programada
- Numa hora programada para entradas que preencham determinadas condições

## Definições de acionamento

Para criar ou editar um acionador, clique na caixa correspondente na área central do editor de automação. As definições do acionador aparecem então à direita.

![Definições do acionador](images/automation-trigger-settings.jpg)

- Pode primeiro alterar o **acionador** utilizando o menu pendente. Para tal, selecione o evento de disparo pretendido.
- De seguida, defina a **tabela** e a **vista** em que a automatização deve ter efeito.
- Dependendo do tipo de acionador, pode fazer outras definições, por exemplo, **colunas monitorizadas**, **condições** para o acionamento ou a **hora** do acionamento.

![definições de acionamento em pormenor](images/automation-trigger-settings.gif)

{{< warning headline="Guardar alterações" text="Não se esqueça de **guardar** as definições do acionador! Caso contrário, todas as alterações serão perdidas quando fechar a janela." />}}

## Acionador de automação: Quando uma linha é alterada

Se selecionar este evento como um acionador, a automatização correspondente é acionada sempre que um valor é alterado numa das colunas monitorizadas e uma linha na vista selecionada preenche determinadas condições após a edição. Se pretender que o acionador seja disparado sempre que é feita uma alteração, não adicione quaisquer condições.

Nas **Condições**, pode definir individualmente para cada coluna o aspeto que o valor correspondente deve ter após a edição para que a automatização seja iniciada. Como parte disto, pode decidir se todas ou apenas as colunas selecionadas na vista devem ser monitorizadas para a ocorrência do evento de acionamento.

![definições de acionamento quando uma linha é alterada](images/automation-trigger-when-a-row-is-updated.jpg)

Se selecionar este evento como o acionador de uma automatização, pode escolher entre as seguintes **acções automáticas**:

- Enviar notificação
- Enviar notificação de aplicação
- Enviar e-mail
- Adicionar registro
- Bloquear registro
- Modificar registro
- Adicionar ligações
- Adicionar uma nova entrada a outra tabela
- Executar o script Python
- Chamar a IA

## Acionador de automação: Quando uma linha é adicionada

Se selecionar este evento como um acionador, a automatização correspondente será acionada sempre que uma **nova linha** for adicionada na vista selecionada. Além disso, pode restringir ainda mais a ocorrência do evento, definindo **condições** que a nova linha deve cumprir.

![Definições de acionamento quando é adicionada uma linha](images/automation-trigger-when-a-row-is-added.jpg)

Nas condições, pode especificar individualmente para cada coluna qual deve ser o valor correspondente para que a automatização seja iniciada. Se pretender que cada nova linha accione a automatização, não adicione quaisquer condições.

{{< warning headline="Sugestão" text="Este acionador é particularmente útil, por exemplo, quando importa novos registos de dados ou os introduz através de formulários." />}}

Se selecionar este evento como o acionador de uma automatização, pode escolher entre as seguintes **acções automáticas**:

- Enviar notificação
- Enviar notificação de aplicação
- Enviar e-mail
- Adicionar registro
- Bloquear registro
- Modificar registro
- Adicionar ligações
- Adicionar uma nova entrada a outra tabela
- Executar o script Python
- Chamar a IA

## Acionador de automação: Numa hora programada

Se selecionar este acionador, pode então definir uma **hora** em que a automatização é executada **diariamente**, **semanalmente** ou **mensalmente**.

![Opções de definição para um acionamento diário numa hora programada](images/automation-trigger-at-scheduled-time.jpg)

Embora só possa especificar a **hora** para uma automatização diária, também pode especificar o **dia da semana** para uma automatização semanal ou o **dia do calendário** para uma automatização mensal.

![Definir opções para um acionamento semanal a uma hora programada](images/automation-trigger-at-scheduled-time-weekly.jpg)

Se definir este acionador para uma automatização, pode escolher entre as seguintes **acções automáticas**:

- Enviar notificação
- Enviar notificação de aplicação
- Enviar e-mail
- Adicionar registro
- Adicionar ligações
- Executar script Python
- Chamar a IA
- Executar processamento de dados
- Gerar PDF a partir do documento e enviar

## Acionador de automação: Numa hora programada para entradas que preencham determinadas condições

Com este acionador, especifica uma **hora** congruente com o acionador anteriormente mencionado em que a automatização é acionada **diariamente**, **semanalmente** ou **mensalmente**. Também pode limitar as linhas que são afectadas por este evento de acionamento.

Para as **condições**, pode especificar individualmente para cada coluna qual deve ser o valor correspondente para que a automatização seja executada na hora especificada.

![acionar numa hora programada para registos que satisfazem determinadas condições](images/automation-trigger-at-scheduled-time-for-records-that-match-condition.jpg)

Se selecionar este acionador para uma automatização, pode escolher entre as seguintes **acções automáticas**:

- Enviar notificação
- Enviar notificação de aplicação
- Enviar e-mail
- Bloquear registro
- Modificar registro
- Converter página em PDF
