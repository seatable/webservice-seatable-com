---
title: 'Python example: Send emails'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/help/python-send-emails'
seo:
    title: 'Python: Send emails from SeaTable'
    description: 'Send emails by button directly from SeaTable using this Python script. Reads recipient, subject and body from the current row.'
---


This script sends an email via SMTP based on the data of the current row. It is designed as a **button script**: you click a button in a row and the script reads the recipient, subject and body from the corresponding columns. The send status is written back to a single-select column.

![Send Email in SeaTable](send-email.png)

{{< dtable-download name="Send Email" file="/downloads/python-examples/send-email.dtable" text="Base with sample data and ready-made script to try out directly." />}}

{{< warning headline="Enable SMTP access" >}}

Most email providers block access by third-party applications by default. You need to enable SMTP access first:

- **Gmail**: [Create an app password](https://myaccount.google.com/apppasswords) (2FA must be enabled)
- **Microsoft 365 / Outlook**: Create an app password in the security settings
- **Other providers**: Check the settings under "Security" or "Third-party apps"

Always use an app password, not your regular password.

{{< /warning >}}

## Prerequisites

The table requires the following columns:

- **Recipient** (Email) — recipient address
- **Subject** (Text) — email subject
- **Body** (Long text) — email content
- **Status** (Single select) — set by the script to "Success" or "Error"

A **button column** must also be set up to execute the script.

## The script

Adjust the SMTP credentials and column names to your configuration. The script uses `context.current_row` to read the data from the row where the button was clicked.

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

## SMTP servers

Common SMTP settings:

| Provider | Server | Port |
|---|---|---|
| Gmail | smtp.gmail.com | 587 |
| Outlook / Microsoft 365 | smtp-mail.outlook.com | 587 |
| Custom server | Your SMTP server | 587 or 465 |

{{< warning headline="Protect your credentials" text="Your SMTP password is visible to all users who have access to the base. Store credentials in a separate configuration table with restricted access." />}}

For HTML emails, replace `'plain'` with `'html'` in the `MIMEText` call.

For the complete function reference, visit the [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
