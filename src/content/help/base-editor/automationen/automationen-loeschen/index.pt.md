---
title: 'Eliminar automatizações'
date: 2022-12-06
lastmod: '2025-11-05'
categories:
    - 'automationen'
author: 'kgr'
url: '/pt/ajuda/excluir-automacoes-seatable'
aliases:
    - '/pt/ajuda/automationen-loeschen'
seo:
    title: 'Excluir automações em SeaTable: guia e consequências'
    description: 'Descubra como excluir automações em SeaTable, os efeitos em cada ação e o passo a passo para remoção definitiva das regras.'
weight: 10
---

É possível **eliminar regras de automatização** que já tenham sido criadas em qualquer altura. É favor notar os efeitos que a eliminação tem sobre as várias **acções automatizadas**.

## Para eliminar uma automatização

![Eliminar uma automatização](images/delete-automation-rule.gif)

1. Abra uma **Base** na qual pretende eliminar uma automatização que já tenha sido criada.
2. No cabeçalho da base, clique em {{< seatable-icon icon="dtable-icon-rule" >}} e depois em **Regras de automatização**.
3. Mova o ponteiro do rato sobre a regra de automatização correspondente, clique nos três pontos e depois em {{< seatable-icon icon="dtable-icon-delete" >}} **Eliminar regra** .
4. Confirme com **Eliminar**.

{{< warning type="warning" headline="A eliminação é definitiva" text="A regra de automatização eliminada é então **finalmente eliminada e não pode ser restaurada**." />}}

## Efeitos

Dependendo das acções que definiu para uma automatização, a eliminação de uma regra de automatização pode ter **diferentes consequências**. Em princípio, no entanto, o evento de disparo definido **já não irá desencadear quaisquer acções** após a eliminação - a menos que ainda seja utilizado como um disparador para outra automatização existente.

Particularmente no caso de acções complexas, como o envio de e-mails, scripts Python ou funções de IA, deve considerar apenas [pausar a automação]({{< relref "help/base-editor/automationen/automationen-stoppen" >}}) em vez de a eliminar permanentemente.