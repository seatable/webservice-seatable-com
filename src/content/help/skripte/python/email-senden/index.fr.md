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
    description: "Envoyez des e-mails par bouton directement depuis SeaTable avec ce script Python. Lit le destinataire, l'objet et le texte de la ligne actuelle."
---


Ce script envoie un e-mail par SMTP en se basant sur les données de la ligne actuelle. Il est conçu comme un **script de bouton** : vous cliquez sur un bouton dans une ligne et le script lit le destinataire, l'objet et le texte dans les colonnes correspondantes. Le statut d'envoi est écrit dans une colonne de sélection simple.

![Send Email in SeaTable](send-email.png)

{{< dtable-download name="Send Email" file="/downloads/python-examples/send-email.dtable" text="Base avec données d'exemple et script prêt à l'emploi pour essayer directement." />}}

{{< warning headline="Activer l'accès SMTP" >}}

La plupart des fournisseurs de messagerie bloquent l'accès par des applications tierces par défaut. Vous devez d'abord activer l'accès SMTP :

- **Gmail** : [Créer un mot de passe d'application](https://myaccount.google.com/apppasswords) (l'authentification à deux facteurs doit être activée)
- **Microsoft 365 / Outlook** : Créer un mot de passe d'application dans les paramètres de sécurité
- **Autres fournisseurs** : Vérifiez les paramètres sous « Sécurité » ou « Applications tierces »

Utilisez toujours un mot de passe d'application, pas votre mot de passe habituel.

{{< /warning >}}

## Prérequis

La table nécessite les colonnes suivantes :

- **Recipient** (E-mail) — adresse du destinataire
- **Subject** (Texte) — objet de l'e-mail
- **Body** (Texte long) — contenu de l'e-mail
- **Status** (Sélection simple) — défini par le script sur « Success » ou « Error »

Une **colonne de bouton** doit également être configurée pour exécuter le script.

## Le script

Adaptez les identifiants SMTP et les noms de colonnes à votre configuration. Le script utilise `context.current_row` pour lire les données de la ligne où le bouton a été cliqué.

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

## Serveurs SMTP

Paramètres SMTP courants :

| Fournisseur | Serveur | Port |
|---|---|---|
| Gmail | smtp.gmail.com | 587 |
| Outlook / Microsoft 365 | smtp-mail.outlook.com | 587 |
| Serveur propre | Votre serveur SMTP | 587 ou 465 |

{{< warning headline="Protéger vos identifiants" text="Votre mot de passe SMTP est visible par tous les utilisateurs ayant accès à la base. Stockez les identifiants dans une table de configuration séparée avec un accès restreint." />}}

Pour les e-mails HTML, remplacez `'plain'` par `'html'` dans l'appel `MIMEText`.

Pour la référence complète des fonctions, consultez le [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
