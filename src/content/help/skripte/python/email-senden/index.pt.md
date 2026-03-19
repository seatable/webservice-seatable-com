---
title: 'Exemplo Python: Enviar e-mails'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/pt/ajuda/python-enviar-emails'
seo:
    title: 'Python: Enviar e-mails do SeaTable'
    description: 'Envie e-mails automatizados via SMTP diretamente do SeaTable com este script Python.'
---

Este script envia e-mails via SMTP diretamente de um script Python do SeaTable. Pode usá-lo para notificações, relatórios ou qualquer e-mail automatizado baseado nos seus dados do SeaTable. O script suporta texto simples, conteúdo HTML e anexos.

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
