---
title: 'Секретный ключ веб-крючка'
date: 2023-02-28
lastmod: '2026-11-05'
categories:
    - 'webhooks'
author: 'cdb'
url: '/ru/pomoshch/bezopasnost-webhook-sekret-seatable'
aliases:
  - '/ru/pomoshch/der-geheime-schluessel-eines-webhooks'
seo:
    title: 'Безопасность вебхуков: секрет и подпись в SeaTable'
    description: 'Как секретный ключ защищает вебхук SeaTable: проверяйте подпись, подтверждайте источник событий и блокируйте несанкционированный доступ. Практическая настройка.'

---

Если назначение веб-крючка общедоступно, то для входящих запросов необходимо убедиться, что они исходят от нужной системы-исходника. С помощью секретного ключа можно гарантировать происхождение веб-крючка.

## Идея секретного ключа

Чтобы создать новый webhook, просто введите любой URL. Секретный ключ также может оставаться пустым. Однако если ваш целевой URL-адрес общедоступен, вам следует установить секретный ключ и подтвердить это значение при обработке веб-крючков. В противном случае любой может отправить вам соответствующие запросы на этот URL webhook, которые затем будут обработаны вами. Без секретного ключа у целевой системы не будет надежного способа распознать, действительно ли событие пришло от SeaTable.

Если вы укажете секретный ключ, веб-крючок будет иметь дополнительный *X-SeaTable-Signature-Header*который может быть использован для обеспечения происхождения webhook. Пока кто-то другой не знает секретный ключ, он не сможет отправить вам события через webhook и найти подходящий ключ. _X-SeaTable-Signature-Header_ производить.

Если установлен секретный ключ, запрос webhook выглядит, например, так:

```
-- HEADER --
Content-Type: application/json
Content-Length: 625
X-Seatable-Signature: sha256=598b55485e7875def064746867ff220e79d7c75512fdb931a39e313af5abfe60
Connection: keep-alive
Accept: */*
Accept-Encoding: gzip, deflate
User-Agent: python-requests/2.28.1
Host: example.com

-- CONTENT --
{
  event:update
  data: {
    dtable_uuid: 6c17f178ee724c109c68ecee364027fc
    row_id: Y_aYcE6wTo-IzGWb-oDmaQ
    op_user: 92d8f9b243f8437db0131c2536398403@auth.local
    op_type: insert_row
    op_time: 1677595743.088
    table_id: 0000
    table_name: Table1
    row_name: ""
    row_data: []
  }
}

```

## Вычисление подписи

Секретный ключ - это [общий секрет](https://en.wikipedia.org/wiki/Shared_secret) между SeaTable и принимающей системой. SeaTable использует секретный ключ для вычисления хэш-значения события, то есть подписи. Принимающая система с помощью того же ключа вычисляет хэш-значение полученного содержимого и сравнивает его с подписью. Если значения не совпадают, вебхук не следует обрабатывать.

## Проверка подлинности подписи

В каждом языке программирования должны существовать соответствующие функции для проверки такой подписи. Как выглядит такая проверка в PHP, вы можете узнать из [этой статьи]({{< relref "help/integrationen/webhooks/verarbeitung-eines-webhooks-mit-hilfe-von-php" >}}).

Для Python экзамен может выглядеть следующим образом:

```
import hmac
from flask import Flask, request

app = Flask(__name__)

@app.route('/receive-seatable-webhook', methods=['POST'])
def receive_seatable_webhook():
    secret = 'secret'
    seatable_signature = request.headers.get('X-Seatable-Signature', '').replace('sha256=', '')

    signature = hmac.new(
        secret.encode('utf-8'), request.data, digestmod='sha256').hexdigest()

    signature_compare = hmac.compare_digest(signature, seatable_signature)

    if signature_compare:
        # do something
        pass

    return {'success': signature_compare}

```
