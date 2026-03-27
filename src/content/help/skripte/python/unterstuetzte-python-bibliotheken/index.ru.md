---
title: 'Поддерживаемые библиотеки Python'
date: 2023-05-12
lastmod: '2026-03-27'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/ru/pomoshch/podderzhivaemye-python-biblioteki'
aliases:
    - '/ru/pomoshch/unterstuetzte-python-bibliotheken'
seo:
    title: 'Поддерживаемые Python библиотеки в SeaTable – обзор'
    description: 'Полный список всех предустановленных библиотек Python в SeaTable Cloud и Server — с инструкциями по добавлению пользовательских библиотек.'
weight: 1
star: true
---

Среда Python в SeaTable использует **Python 3.12** и включает полную [стандартную библиотеку Python](https://docs.python.org/3.12/library/index.html) (например, os, sys, datetime, math, random, json, re, io, smtplib). Вы можете импортировать эти модули непосредственно в свои скрипты.

## Предустановленные библиотеки

Помимо стандартной библиотеки, в SeaTable Cloud и в стандартной установке SeaTable Server доступны следующие пакеты:

Для некоторых из этих библиотек мы предоставляем [примеры Python]({{< relref "help/skripte/python" >}}) с готовыми скриптами и примерами баз для скачивания.

| Библиотека | Описание | Пример |
|---|---|---|
| [seatable-api](https://pypi.org/project/seatable-api/) | API-клиент SeaTable | все примеры |
| [requests](https://pypi.org/project/requests/) | HTTP-запросы | [Курсы акций]({{< relref "help/skripte/python/aktienkurs-abfragen" >}}) |
| [pandas](https://pypi.org/project/pandas/) | Анализ и обработка данных | |
| [scipy](https://pypi.org/project/scipy/) | Научные вычисления | |
| [openai](https://pypi.org/project/openai/) | API-клиент OpenAI | |
| [qrcode](https://pypi.org/project/qrcode/) | Генерация QR-кодов | [Генерация QR-кодов]({{< relref "help/skripte/python/qr-code-generieren" >}}) |
| [python-barcode](https://pypi.org/project/python-barcode/) | Генерация штрих-кодов | [Генерация штрих-кодов]({{< relref "help/skripte/python/barcode-generieren" >}}) |
| [pillow-heif](https://pypi.org/project/pillow-heif/) | Поддержка HEIC/HEIF для Pillow | [Конвертация HEIC в PNG]({{< relref "help/skripte/python/heic-zu-png-konvertieren" >}}) |
| [pdfmerge](https://pypi.org/project/pdfmerge/) | Объединение PDF | [Объединение PDF-файлов]({{< relref "help/skripte/python/pdf-zusammenfuehren" >}}) |
| [rapidfuzz](https://pypi.org/project/rapidfuzz/) | Нечёткое сравнение строк | |
| [markdown](https://pypi.org/project/Markdown/) | Конвертация Markdown в HTML | |
| [ldap3](https://pypi.org/project/ldap3/) | Операции LDAP | |
| [dateutils](https://pypi.org/project/dateutils/) | Вспомогательные функции для дат | |
| [pyOpenSSL](https://pypi.org/project/pyOpenSSL/) | Функции TLS/SSL | |
| [PyJWT](https://pypi.org/project/PyJWT/) | Обработка JSON Web Tokens | |

Благодаря зависимостям вышеуказанных пакетов также доступны **Pillow** (обработка изображений) и **numpy** (численные вычисления).

{{< warning headline="Этот список может измениться" text="Актуальный список предустановленных библиотек можно найти в файле [requirements.txt Python Runner](https://github.com/seatable/python-pipeline/blob/main/runner/requirements.txt) на GitHub." />}}

## Установка пользовательских библиотек

В **SeaTable Cloud** вы ограничены библиотеками, перечисленными выше. Установить дополнительные пакеты невозможно.

На **самостоятельно размещённом сервере SeaTable** вы можете добавить дополнительные библиотеки, создав пользовательский Python Runner. Инструкции можно найти в [руководстве администратора SeaTable](https://admin.seatable.com/installation/advanced/python-pipeline-custom-python-runner/).
