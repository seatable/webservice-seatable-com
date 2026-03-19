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
    description: 'Отправляйте автоматические письма по SMTP прямо из SeaTable с помощью этого скрипта Python.'
---

Этот скрипт отправляет электронные письма через SMTP прямо из Python-скрипта SeaTable. Вы можете использовать его для уведомлений, отчётов или любой автоматической рассылки на основе данных SeaTable. Скрипт поддерживает простой текст, HTML и вложения.

## SMTP configuration

You need the SMTP credentials of your email provider. Common settings:

| Provider | Server | Port |
|---|---|---|
| Gmail | smtp.gmail.com | 587 |
| Outlook | smtp-mail.outlook.com | 587 |
| Custom | your SMTP server | 587 or 465 |

## The complete script

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
SMTP_PASSWORD = "your-password"

# Email settings
RECIPIENT = "recipient@example.com"
SUBJECT = "Automated email from SeaTable"
BODY = "This is an automated email sent from a SeaTable Python script."

msg = MIMEMultipart()
msg['From'] = SMTP_USER
msg['To'] = RECIPIENT
msg['Subject'] = SUBJECT
msg.attach(MIMEText(BODY, 'plain'))

with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
    server.starttls()
    server.login(SMTP_USER, SMTP_PASSWORD)
    server.send_message(msg)

print(f"Email sent to {RECIPIENT}")
```

{{< warning headline="Protect your credentials" text="Your SMTP password is visible to all users who have access to the base. Consider storing credentials in a separate configuration table with restricted access, or use environment variables on a self-hosted SeaTable server." />}}

You can extend this script to read recipients, subjects, or email content from your SeaTable tables using `base.list_rows()`. For HTML emails, replace `'plain'` with `'html'` in the `MIMEText` call.

For the complete function reference, visit the [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
