---
title: 'Python-Beispiel: E-Mails versenden'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/de/hilfe/python-emails-versenden'
seo:
    title: 'Python: E-Mails aus SeaTable versenden'
    description: 'Versenden Sie automatisierte E-Mails per SMTP direkt aus SeaTable mit diesem Python-Skript. Unterstützt Text, HTML und Dateianhänge.'
---


Dieses Skript versendet E-Mails per SMTP direkt aus einem SeaTable Python-Skript. Sie können es für Benachrichtigungen, Berichte oder andere automatisierte E-Mails auf Basis Ihrer SeaTable-Daten verwenden. Das Skript unterstützt Klartext, HTML-Inhalte und Dateianhänge.

## SMTP-Konfiguration

Sie benötigen die SMTP-Zugangsdaten Ihres E-Mail-Anbieters. Gängige Einstellungen:

| Anbieter | Server | Port |
|---|---|---|
| Gmail | smtp.gmail.com | 587 |
| Outlook | smtp-mail.outlook.com | 587 |
| Eigener Server | Ihr SMTP-Server | 587 oder 465 |

## Das vollständige Skript

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

{{< warning headline="Zugangsdaten schützen" text="Ihr SMTP-Passwort ist für alle Benutzer sichtbar, die Zugriff auf die Base haben. Speichern Sie Zugangsdaten in einer separaten Konfigurationstabelle mit eingeschränktem Zugriff oder verwenden Sie Umgebungsvariablen auf einem selbst gehosteten SeaTable-Server." />}}

Sie können dieses Skript erweitern, um Empfänger, Betreff oder E-Mail-Inhalt aus Ihren SeaTable-Tabellen mit `base.list_rows()` zu lesen. Für HTML-E-Mails ersetzen Sie `'plain'` durch `'html'` im `MIMEText`-Aufruf.

Die vollständige Funktionsreferenz finden Sie im [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
