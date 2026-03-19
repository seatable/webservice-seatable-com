---
title: 'Ejemplo Python: Enviar correos electrónicos'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/es/ayuda/python-enviar-emails'
seo:
    title: 'Python: Enviar correos desde SeaTable'
    description: 'Envíe correos electrónicos automatizados por SMTP directamente desde SeaTable con este script Python.'
---

Este script envía correos electrónicos por SMTP directamente desde un script Python de SeaTable. Puede usarlo para notificaciones, informes o cualquier correo automatizado basado en sus datos de SeaTable. El script soporta texto plano, contenido HTML y archivos adjuntos.

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
