---
title: 'Exemple Python : Envoyer des e-mails'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/fr/aide/python-envoyer-emails'
seo:
    title: 'Python : Envoyer des e-mails depuis SeaTable'
    description: 'Envoyez des e-mails automatisés par SMTP directement depuis SeaTable avec ce script Python.'
---

Ce script envoie des e-mails par SMTP directement depuis un script Python SeaTable. Vous pouvez l'utiliser pour des notifications, des rapports ou tout e-mail automatisé basé sur vos données SeaTable. Le script supporte le texte brut, le contenu HTML et les pièces jointes.

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
