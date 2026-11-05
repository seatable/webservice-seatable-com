---
title: 'Создание и удаление webhook'
date: 2023-02-28
lastmod: '2023-02-28'
categories:
    - 'webhooks'
author: 'cdb'
url: '/ru/pomoshch/sozdanie-udaleniye-webhook-seatable'
aliases:
    - '/ru/pomoshch/anlegen-eines-webhooks'
seo:
    title: 'Создание и удаление webhooks в SeaTable: инструкция'
    description: 'Настройте webhook для вашей базы в SeaTable: введите URL-приемник, получайте обновления и управляйте уведомлениями простым удалением в пару шагов.'
---

Для базы всегда создается webhook. Как только webhook настроен, каждое изменение содержимого базы отправляется на целевой URL.

{{< info-box headline="POST-Request" text="Webhook всегда отправляется на целевой URL через POST-запрос." />}}

## Настройте webhook

1. На стартовой странице SeaTable наведите курсор на базу, для которой вы хотите установить webhook.
2. Нажмите на пункт _Webhooks_ в контекстном меню в разделе _Advanced_.
3. Введите URL-адрес назначения и подтвердите.
4. Webhook становится активным немедленно.

![Форма для создания webhook в SeaTable](images/seatable-webhook.png)
