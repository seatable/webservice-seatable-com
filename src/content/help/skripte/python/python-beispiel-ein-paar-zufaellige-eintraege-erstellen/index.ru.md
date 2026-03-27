---
title: 'Пример Python: создание нескольких случайных записей'
date: 2023-03-02
lastmod: '2023-03-22'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/ru/pomoshch/python-sluchaynye-zapisi-seatable'
aliases:
  - '/ru/pomoshch/python-beispiel-ein-paar-zufaellige-eintraege-erstellen'
seo:
    title: 'Python: быстро создавать случайные строки в SeaTable'
    description: 'Скрипт Python мгновенно генерирует примеры данных прямо в SeaTable—идеально для тестов, прототипирования и автозаполнения новых таблиц любым количеством.'
weight: 5
---


Иногда требуется сгенерировать несколько выборочных записей в базе. С помощью этого Python-скрипта вы можете сгенерировать от нескольких до многих тысяч записей в кратчайшие сроки.

Эта статья проведет вас через различные разделы скрипта, чтобы вы поняли, как он работает, и при необходимости смогли адаптировать его под свои нужды. Полный текст скрипта можно найти в конце этой статьи.

## 1) Загрузка модулей

Каждый скрипт Python начинается с загрузки используемых модулей Python, где мы будем использовать _base_ и _context_ из класса _seatable_api_. Модуль _random_ нужен только во второй строке, если вы хотите генерировать случайные числа.

```python
from seatable_api import Base, context
import random
```

## 2) Аутентификация

Следующие две строки необходимы для установления соединения с текущей базой. После этой аутентификации мы можем читать, удалять или манипулировать информацией через _объект базы_.

```python
base = Base(context.api_token, context.server_url)
base.auth()
```

## 3) Определите содержимое новой строки

Теперь, когда у нас есть доступ к текущей таблице, мы можем определить записи для создания. Следующий код предполагает, что у вас есть столбцы с именами _Name_, _single_, _random_, _rating_. Если ваши столбцы названы по-другому, вам нужно соответствующим образом изменить имена.

```python
# define the data for two new rows
rows_data = [
  {
    'Name': "I am new Row",
    'single': "new",
    'random': random.randint(0,100000000),
    'rating': random.randint(0,5)
  },
  {
    'Name': "I am second new row",
    'single': "other value",
    'random': random.randint(0,100000000),
    'rating': random.randint(0,5)
  },
]
```

## 4) Напишите новые строки

В последнем блоке кода содержимое новых _строк_ было определено и сохранено в переменной _rows_data_, но еще не записано в базу. Теперь мы сделаем это с помощью следующего вызова.

```python
# append the two rows
  base.batch_append_rows(context.current_table, rows_data)
```

## 5) Если вам нужно больше линий

Конечно, можно записать и более двух строк. Это можно сделать либо просто определив дополнительное содержимое строки, либо выполнив процесс записи несколько раз с помощью цикла.

```python
# execute batch append 10 times
for i in range(10):

  # define the data for two new rows
  ...

  # append the two rows
  ...
```

{{< warning  headline="Отступы для заметок в Python"  text="В Python отступы строк используются для структурирования кода. Это позволяет сделать код коротким и понятным, но в то же время вы должны обратить пристальное внимание на отступы, потому что они определяют, где заканчивается _цикл for_." />}}

## Полный сценарий

Полный сценарий должен быть готов к немедленному запуску без каких-либо серьезных изменений. Измените названия четырех столбцов, и сценарий сможет создавать новые строки в вашей таблице.

```python
from seatable_api import Base, context
import random

base = Base(context.api_token, context.server_url)
base.auth()

# execute batch append multiple times
for i in range(10):

  # define the data for two new rows
  rows_data = [
    {
      'Name': "I am new Row",
      'single': "new",
      'random': random.randint(0,100000000),
      'rating': random.randint(0,5)
    },
    {
      'Name': "I am second new row",
      'single': "more than new",
      'random': random.randint(0,100000000),
      'rating': random.randint(0,5)
    },
  ]

  # append the two rows
  base.batch_append_rows(context.current_table, rows_data)
```

Сценарий может быть запущен вручную или с помощью кнопки или автоматизации. Подробнее об этом можно узнать [здесь]({{< relref "help/skripte/allgemein/skript-manuell-per-schaltflaeche-oder-automation-ausfuehren" >}}).
