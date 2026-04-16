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
    description: 'Envie e-mails por botão diretamente do SeaTable com este script Python. Lê o destinatário, o assunto e o texto da linha atual.'
---


Este script envia um e-mail por SMTP com base nos dados da linha atual. Foi concebido como um **script de botão**: clica-se num botão numa linha e o script lê o destinatário, o assunto e o texto das colunas correspondentes. O estado de envio é escrito numa coluna de seleção simples.

![Send Email in SeaTable](send-email.png)

{{< dtable-download name="Send Email" file="/downloads/python-examples/send-email.dtable" text="Base com dados de exemplo e script pronto para experimentar diretamente." />}}

{{< warning headline="Ativar o acesso SMTP" >}}

A maioria dos fornecedores de e-mail bloqueia o acesso por aplicações de terceiros por defeito. É necessário ativar primeiro o acesso SMTP:

- **Gmail**: [Criar uma palavra-passe de aplicação](https://myaccount.google.com/apppasswords) (a autenticação de dois fatores deve estar ativada)
- **Microsoft 365 / Outlook**: Criar uma palavra-passe de aplicação nas definições de segurança
- **Outros fornecedores**: Verifique as definições em «Segurança» ou «Aplicações de terceiros»

Utilize sempre uma palavra-passe de aplicação, não a sua palavra-passe habitual.

{{< /warning >}}

## Pré-requisitos

A tabela necessita das seguintes colunas:

- **Recipient** (E-mail) — endereço do destinatário
- **Subject** (Texto) — assunto do e-mail
- **Body** (Texto longo) — conteúdo do e-mail
- **Status** (Seleção simples) — definido pelo script como «Success» ou «Error»

Também deve ser configurada uma **coluna de botão** para executar o script.

## O script

Adapte as credenciais SMTP e os nomes das colunas à sua configuração. O script utiliza `context.current_row` para ler os dados da linha onde o botão foi clicado.

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

Configurações SMTP comuns:

| Fornecedor | Servidor | Porta |
|---|---|---|
| Gmail | smtp.gmail.com | 587 |
| Outlook / Microsoft 365 | smtp-mail.outlook.com | 587 |
| Servidor próprio | O seu servidor SMTP | 587 ou 465 |

{{< warning headline="Proteger as suas credenciais" text="A sua palavra-passe SMTP é visível para todos os utilizadores que têm acesso à base. Armazene as credenciais numa tabela de configuração separada com acesso restrito." />}}

Para e-mails HTML, substitua `'plain'` por `'html'` na chamada `MIMEText`.

Para a referência completa das funções, visite o [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
