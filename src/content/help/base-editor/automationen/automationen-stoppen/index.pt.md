---
title: 'Pausar as automatizações'
date: 2023-01-27
lastmod: '2025-11-05'
categories:
    - 'automationen'
author: 'kgr'
url: '/pt/ajuda/pausar-reativar-automacoes-seatable'
aliases:
    - '/pt/ajuda/automationen-stoppen'
seo:
    title: 'Pausar ou reativar automações no SeaTable: tutorial para times Enterprise'
    description: 'Saiba pausar e restaurar automações em SeaTable sem precisar excluir regras, garantir continuidade e flexibilidade em processos críticos do seu time.'
weight: 9
---

Se já não quiser executar as automatizações durante um determinado período de tempo, pode **suspendê-las** em vez de as [apagar]({{< relref "help/base-editor/automationen/automationen-loeschen" >}}). Isto tem a vantagem de poder simplesmente **reactivar** as automatizações pausadas, enquanto que tem de criar automatizações apagadas do zero.

## Parar temporariamente as automatizações

1. Abra uma **Base** na qual pretende colocar em pausa uma automatização ativa.
2. No cabeçalho da base, clique em {{< seatable-icon icon="dtable-icon-rule" >}} e depois em **Regras de automatização**.
3. Mova o ponteiro do rato sobre a regra de automatização correspondente, clique nos três pontos e depois em {{< seatable-icon icon="dtable-icon-paused" >}} **Pausar regra** .

![Pausa na regra de automatização](images/pause-automation-rule.gif)

A regra de automatização selecionada é então **pausada**. Pode reconhecer este facto pela nota **(parou)**, que é adicionada ao nome da automatização a vermelho.

{{< warning type="warning" headline="Nota importante" text="As automatizações em pausa já **não estão activas** até serem reiniciadas. Isto significa que os eventos de acionamento definidos **já não accionam** acções automatizadas." />}}

## Reiniciar a automatização

Para **ativar** novamente as automatizações em pausa, basta seguir os passos descritos acima e clicar em {{< seatable-icon icon="dtable-icon-implement" >}} **Reiniciar regra** .

![Reiniciar regra de automatização](images/start-automation-rule.gif)

O aviso **(parou)** à direita do nome da automatização desaparece novamente.