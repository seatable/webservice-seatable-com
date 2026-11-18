---
title: 'Обработка webhook с помощью PHP'
date: 2023-02-28
lastmod: '2023-02-28'
categories:
    - 'webhooks'
author: 'cdb'
url: '/ru/pomoshch/obrabotka-webhook-php-seatable'
aliases:
    - '/ru/pomoshch/verarbeitung-eines-webhooks-mit-hilfe-von-php'
seo:
    title: 'Обработка webhooks SeaTable с помощью PHP: пример'
    description: 'Обрабатывайте webhooks SeaTable с помощью PHP: получайте, проверяйте и анализируйте события – с готовыми примерами кода.'

---

Обработка события webhooks может быть выполнена с помощью любого языка программирования и зависит от языка программирования. В следующем примере показана простая обработка с помощью PHP, которая может послужить основой для всех дальнейших разработок.

## Сценарий

Следующий PHP-код служит лишь иллюстрацией того, как реагировать, например, на определенное событие, такое как удаленная строка.

```
// get the webhook
$raw_payload = file_get_contents('php://input', true);
$payload = json_decode($raw_payload, true);

if($payload['event'] === "update"){

    // check for a deleted row
    if($payload['data']['op_type'] === "delete_row"){
        // ...
    }

    // check if a checkbox was checked in the column with the name "checkbox"
    if($payload['data']['row_data'][0]['column_name'] === "checkbox" AND $payload['data']['row_data'][0]['value'] === true){
        // ...
    }

    // save content to file (for debugging)
    $file = 'webhook_payload.txt';
    $current = file_get_contents($file);
    $current .= $raw_payload;
    $output = file_put_contents($file, $current);
}

```

Если webhook отправляет секретный ключ, вы можете проверить содержимое webhook с помощью следующего кода. Конечно, вы должны заменить переменную _$secret_ на выбранный вами секретный ключ.

```
// verify the signature
function verifySignature($body){
  $secret = "your-webhook-secret";
  $headers = getallheaders();
  return hash_equals('sha256='.hash_hmac('sha256', $body, $secret), $headers['X-Seatable-Signature']);
}

if (verifySignature($raw_payload) !== false) {
    // verified
    // ...
} else {
    // not verified
}

```

## Структура, лежащая в основе сценария

Первые две строки считывают входящее событие webhook и создают массив in из входящей структуры JSON.

При первом запросе "if" далее обрабатываются только те события, для которых "op_type" имеет значение "delete_row".

Второй запрос "if" принимает только те события, в которых активирован флажок в столбце с именем "checkbox".

Последние строки являются необязательными и сохраняют полезную нагрузку в текстовом файле. В качестве альтернативы можно также сохранять отдельные запросы в базе данных и, например, документировать успешную обработку запросов.
