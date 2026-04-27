---
title: 'Пример Python: Отправка электронной почты'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/ru/pomoshch/python-otpravka-email'
seo:
    title: 'Python: Отправка e-mail из SeaTable'
    description: 'Отправляйте письма по кнопке прямо из SeaTable с помощью этого скрипта Python. Читает получателя, тему и текст из текущей строки.'
---


Этот скрипт отправляет электронное письмо через SMTP на основе данных текущей строки. Он разработан как **скрипт-кнопка**: вы нажимаете кнопку в строке, и скрипт читает получателя, тему и текст из соответствующих столбцов. Статус отправки записывается в столбец одиночного выбора.

![Send Email in SeaTable](send-email.png)

{{< dtable-download name="Send Email" file="/downloads/python-examples/send-email.dtable" text="База с примерами данных и готовым скриптом для непосредственного тестирования." />}}

{{< warning headline="Активировать доступ SMTP" >}}

Большинство почтовых провайдеров блокируют доступ сторонних приложений по умолчанию. Сначала необходимо активировать доступ SMTP:

- **Gmail**: [Создать пароль приложения](https://myaccount.google.com/apppasswords) (должна быть включена двухфакторная аутентификация)
- **Microsoft 365 / Outlook**: Создать пароль приложения в настройках безопасности
- **Другие провайдеры**: Проверьте настройки в разделе «Безопасность» или «Сторонние приложения»

Всегда используйте пароль приложения, а не обычный пароль.

{{< /warning >}}

## Предварительные требования

Таблица должна содержать следующие столбцы:

- **Recipient** (Электронная почта) — адрес получателя
- **Subject** (Текст) — тема письма
- **Body** (Длинный текст) — содержание письма
- **Status** (Одиночный выбор) — устанавливается скриптом на «Success» или «Error»

Также необходимо настроить **столбец-кнопку** для запуска скрипта.

## Скрипт

Адаптируйте учётные данные SMTP и названия столбцов под вашу конфигурацию. Скрипт использует `context.current_row` для чтения данных из строки, в которой была нажата кнопка.

```python
from seatable_api import Base, context
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

base = Base(context.api_token, context.server_url)
base.auth()

# SMTP configuration
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SMTP_USER = "your-email@example.com"
SMTP_PASSWORD = "your-app-password"

TABLE_NAME = "Table1"

# Read data from current row
row = context.current_row
if not row:
    print("ERROR: This script must be run via a button.")
else:
    recipient = row.get('Recipient', '')
    subject = row.get('Subject', '')
    body = row.get('Body', '')

    if not recipient:
        print("ERROR: No recipient specified.")
    elif not subject:
        print("ERROR: No subject specified.")
    else:
        msg = MIMEMultipart()
        msg['From'] = SMTP_USER
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(body or '', 'plain'))

        try:
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(SMTP_USER, SMTP_PASSWORD)
                server.send_message(msg)
            base.update_row(TABLE_NAME, row['_id'], {'Status': 'Success'})
            print(f"Email sent to {recipient}")
        except Exception as e:
            base.update_row(TABLE_NAME, row['_id'], {'Status': 'Error'})
            print(f"Failed: {e}")
```

## SMTP-серверы

Распространённые настройки SMTP:

| Провайдер | Сервер | Порт |
|---|---|---|
| Gmail | smtp.gmail.com | 587 |
| Outlook / Microsoft 365 | smtp-mail.outlook.com | 587 |
| Собственный сервер | Ваш SMTP-сервер | 587 или 465 |

{{< warning headline="Защита учётных данных" text="Ваш пароль SMTP виден всем пользователям, имеющим доступ к базе. Храните учётные данные в отдельной таблице конфигурации с ограниченным доступом." />}}

Для HTML-писем замените `'plain'` на `'html'` в вызове `MIMEText`.

Полный справочник функций доступен в [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
