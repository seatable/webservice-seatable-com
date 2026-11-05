---
title: 'O que são os webhooks e para que são utilizados?'
date: 2023-02-28
lastmod: '2026-11-05'
categories:
    - 'webhooks'
author: 'cdb'
url: '/pt/ajuda/o-que-sao-webhooks-e-como-usar'
aliases:
    - '/pt/ajuda/was-sind-webhooks-und-wofuer-setzt-man-diese-ein'
seo:
    title: 'O que são webhooks – guia completo e aplicações'
    description: 'Entenda o que são webhooks no SeaTable: notificações automáticas, conexões com outros softwares e automação de processos.'
---

{{< required-version "Grátis" "Mais" "Empresa" >}}

SeaTable oferece a possibilidade de montar um ou até mais webhooks para uma base. Uma vez criado um webhook, qualquer alteração ao conteúdo de uma base desencadeia um impulso sob a forma de um pedido de correio HTTP para qualquer URL.

Simplificado, pode pensar num webhook como um sistema de notificação. Sempre que algo muda numa base, um registo é enviado para um URL que se define.

- Adiciona uma nova fila: SeaTable envia-lhe uma mensagem.
- Coloca-se uma marca numa caixa de verificação, que é também uma mensagem.
- Suprime-se uma linha, quem teria pensado, que também cria uma mensagem.

Cada alteração, por menor que seja, ao conteúdo de uma base, faz com que seja enviado um webhook. É por isso que os webhooks são frequentemente referidos como notificações em tempo real. Se uma operação alterar várias linhas ao mesmo tempo, é enviado [apenas um webhook]({{< relref "help/integrationen/webhooks/webhook-bei-mehreren-gleichzeitigen-aenderungen" >}}).

{{< warning headline="Importante" text="Se forem feitas alterações à estrutura da base, tais como a criação de uma nova coluna, não é enviado nenhum webhook." />}}

## Possíveis usos dos webhooks

Juntamente com as APIs REST, os webhooks são um método popular de permitir que os sistemas informáticos falem uns com os outros. De certa forma, um webhook é uma espécie de pedido API invertido. Com o API, a SeaTable espera por um pedido para entrar, que é respondido pelo API. Com um webhook, por outro lado, uma notificação é automaticamente enviada quando algo acontece.

Desta forma, é possível utilizar webhooks para assegurar que certas alterações sejam processadas noutro software. O SeaTable envia o evento para o URL alvo em formato JSON. O URL é chamado de webhook endpoint.

Portanto, os webhooks funcionam basicamente apenas numa direcção. O SeaTable informa outra aplicação de que algo aconteceu. Por conseguinte, é da responsabilidade da aplicação alvo decidir se esta mudança é relevante e que actividades de seguimento devem ser desencadeadas. Os usos populares dos webhooks são, por exemplo:

- Notificação por e-mail ou chat assim que uma nova fila é criada numa base.
- Publicação automática de um artigo assim que o estado é alterado para "publicar agora".
- Actualização de uma subscrição assim que um pagamento é registado.

Em termos de automatização, os webhooks são sempre, portanto, o gatilho que conduz a uma actividade de seguimento desejada.

## Vantagens dos webhooks

Há duas formas de sistemas diferentes poderem comunicar entre si para trocar informações:

- Sondagem (uma consulta cíclica para obter informações, eventos e alterações de valor).
- Webhook.

Com as sondagens, são solicitadas informações, o que leva a uma troca constante, mesmo que não ocorram quaisquer eventos.

![Webhook vs Sondagem](images/webhooks-vs-polling.png)

Por outro lado, os webhooks só precisam de comunicar quando um evento tiver ocorrido.

## Limites dos webhooks

Os webhooks funcionam bem como acionador, mas não como registo completo de todas as alterações. As entregas falhadas não são repetidas e um webhook pode ser [desativado após erros]({{< relref "help/integrationen/webhooks/deaktivierung-eines-webhooks-bei-fehlern" >}}). Se pretender manter os dados sincronizados com outro sistema, deve por isso também [sincronizar os dados regularmente]({{< relref "help/integrationen/webhooks/webhook-bei-mehreren-gleichzeitigen-aenderungen" >}}).
