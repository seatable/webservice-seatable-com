---
title: 'La clave secreta de un webhook'
date: 2023-02-28
lastmod: '2026-11-05'
categories:
    - 'webhooks'
author: 'cdb'
url: '/es/ayuda/seguridad-webhook-clave-secreta-seatable'
aliases:
  - '/es/ayuda/der-geheime-schluessel-eines-webhooks'
seo:
    title: 'Seguridad de webhook: clave secreta y firma SeaTable'
    description: 'Así protege una clave secreta sus webhooks: valide la firma de SeaTable, confirme el origen y evite accesos no autorizados a su endpoint con shared secret.'

---

Si el destino de un webhook es de acceso público, debe garantizarse para las solicitudes entrantes que proceden del sistema de origen deseado. Con la ayuda de una clave secreta, se puede garantizar el origen de un webhook.

## La idea de una clave secreta

Para crear un nuevo webhook, basta con introducir cualquier URL. La clave secreta también puede permanecer vacía. Sin embargo, si su URL de destino está disponible públicamente, debe establecer una clave secreta y validar este valor al procesar los webhooks. De lo contrario, cualquiera puede enviarle las peticiones correspondientes a esta URL de webhook, que serán procesadas por usted. Sin la clave secreta, el sistema de destino no tiene forma fiable de reconocer si el evento procede realmente de SeaTable.

Si especifica una clave secreta, el webhook tiene una clave adicional _X-SeaTable-Signature-Header_que puede utilizarse para garantizar el origen del webhook. Mientras otra persona no conozca la clave secreta, no podrá enviarte eventos a través de webhook y encontrar la clave coincidente. \_X-SeaTable-Signature-Header_ para producir.

Si se establece una clave secreta, una solicitud de webhook tendrá, por ejemplo, el siguiente aspecto:

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

## Cálculo de la firma

La clave secreta es un [secreto compartido](https://en.wikipedia.org/wiki/Shared_secret) entre SeaTable y el sistema receptor. SeaTable utiliza la clave secreta para calcular un valor hash a partir del evento, la firma. El sistema receptor utiliza la misma clave para calcular el valor hash a partir del contenido recibido y lo compara con la firma. Si los dos valores no coinciden, el webhook no debe procesarse.

## Validación de la firma

En cada lenguaje de programación, deberían existir las funciones correspondientes para poder validar dicha firma como corresponde. Puedes averiguar cómo sería esta comprobación en PHP en [este artículo]({{< relref "help/integrationen/webhooks/verarbeitung-eines-webhooks-mit-hilfe-von-php" >}}).

En el caso de Python, un examen podría tener este aspecto:

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
