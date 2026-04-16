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
    description: 'Envíe correos electrónicos por botón directamente desde SeaTable con este script Python. Lee el destinatario, el asunto y el texto de la fila actual.'
---


Este script envía un correo electrónico por SMTP basado en los datos de la fila actual. Está diseñado como un **script de botón**: se hace clic en un botón en una fila y el script lee el destinatario, el asunto y el texto de las columnas correspondientes. El estado de envío se escribe en una columna de selección simple.

![Send Email in SeaTable](send-email.png)

{{< dtable-download name="Send Email" file="/downloads/python-examples/send-email.dtable" text="Base con datos de ejemplo y script listo para probar directamente." />}}

{{< warning headline="Activar el acceso SMTP" >}}

La mayoría de los proveedores de correo bloquean el acceso de aplicaciones de terceros por defecto. Primero debe activar el acceso SMTP:

- **Gmail**: [Crear una contraseña de aplicación](https://myaccount.google.com/apppasswords) (la autenticación en dos pasos debe estar activada)
- **Microsoft 365 / Outlook**: Crear una contraseña de aplicación en la configuración de seguridad
- **Otros proveedores**: Consulte la configuración en «Seguridad» o «Aplicaciones de terceros»

Utilice siempre una contraseña de aplicación, no su contraseña habitual.

{{< /warning >}}

## Requisitos

La tabla necesita las siguientes columnas:

- **Recipient** (Correo electrónico) — dirección del destinatario
- **Subject** (Texto) — asunto del correo
- **Body** (Texto largo) — contenido del correo
- **Status** (Selección simple) — el script lo establece en «Success» o «Error»

También se debe configurar una **columna de botón** para ejecutar el script.

## El script

Adapte las credenciales SMTP y los nombres de las columnas a su configuración. El script utiliza `context.current_row` para leer los datos de la fila donde se hizo clic en el botón.

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

## Servidores SMTP

Configuraciones SMTP comunes:

| Proveedor | Servidor | Puerto |
|---|---|---|
| Gmail | smtp.gmail.com | 587 |
| Outlook / Microsoft 365 | smtp-mail.outlook.com | 587 |
| Servidor propio | Su servidor SMTP | 587 o 465 |

{{< warning headline="Proteger sus credenciales" text="Su contraseña SMTP es visible para todos los usuarios que tienen acceso a la base. Almacene las credenciales en una tabla de configuración separada con acceso restringido." />}}

Para correos HTML, reemplace `'plain'` por `'html'` en la llamada `MIMEText`.

Para la referencia completa de funciones, visite el [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
