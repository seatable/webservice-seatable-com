---
title: 'Configurer GMX ou WEB.DE pour envoyer des e-mails par SMTP'
date: 2023-03-10
lastmod: '2025-02-14'
categories:
    - 'integrationen-innerhalb-von-seatable'
author: 'cdb'
url: '/fr/aide/configurer-gmx-ou-web-de-pour-envoi-smtp'
aliases:
    - '/fr/aide/gmx-oder-web-de-fuer-den-versand-von-e-mails-per-smtp-einrichten'
seo:
    title: 'Configurer GMX ou WEB.DE pour envoi SMTP avec SeaTable'
    description: 'Guide complet pour configurer GMX ou WEB.DE sur SeaTable afin d’envoyer des emails via SMTP en toute sécurité et simplicité.'
---

Les services de messagerie GMX et WEB.DE jouissent d'une grande popularité dans les pays germanophones. Vous pouvez utiliser les comptes GMX et WEB.DE pour envoyer des e-mails à partir d'une base SeaTable.

Cet article explique comment configurer un compte de messagerie **GMX** ou **WEB.DE** dans une base SeaTable et quelles sont les mesures préparatoires nécessaires.

{{< warning headline="Procédure identique pour GMX et WEB.DE" text="**GMX** et **WEB.DE** sont des offres du fournisseur de télécommunications allemand 1&1. La procédure d'intégration d'un compte e-mail dans une SeaTable Base est démontrée dans cet article d'aide en prenant l'exemple de GMX. Si vous souhaitez utiliser un compte WEB.DE, suivez les instructions de la même manière. L'étape préparatoire doit être effectuée dans les paramètres du compte WEB.DE." />}}

**Dans ce tutoriel vidéo, nous vous montrons comment configurer votre compte de messagerie dans SeaTable (avec des sous-titres en français).**

{{< youtube 5AcQzZiwCx0 >}}

## Autoriser la récupération POP3/IMAP

Par défaut, les comptes GMX et WEB.DE ne peuvent être utilisés que via les webmails ou les applications des deux fournisseurs. La consultation et l'envoi d'e-mails avec un programme tiers comme Outlook, Thunderbird et aussi SeaTable doivent être explicitement autorisés. Vous faites cela dans les paramètres de votre compte.

1. Connectez-vous à votre **compte de messagerie GMX**.
2. Accédez aux **paramètres** de votre compte.

![Paramètres au sein de GMX](images/gmx-free-email-smtp-versand-mit-seatable.jpg)

4. Cliquez sur **Récupération POP3/IMAP** dans les paramètres de messagerie.
5. Activez **Autoriser l'accès POP3 et IMAP**.

![Autoriser SMTP pour GMX et WEB.De.](images/activate_smtp_for_gmx.png)

7. **Enregistrez** votre modification.

Vous avez ainsi fait tous les préparatifs nécessaires pour pouvoir utiliser ce compte e-mail dans SeaTable pour l'envoi d'e-mails.

## Création d'un compte e-mail dans SeaTable

Ajoutez maintenant votre compte e-mail en tant que **tiers** dans votre base SeaTable. Pour cela, il faut suivre les étapes suivantes :

![Intégration de fournisseurs tiers via les options de base étendues](images/Integration-von-Drittanbietern-ueber-die-erweiterten-Base-Optionen.png)

1. Ouvrez les options avancées de la base en cliquant sur l'**icône à trois points** {{< seatable-icon icon="dtable-icon-more-level" >}}.
2. Sélectionnez l'option **Intégration de tiers**.
3. Cliquez sur **Ajouter un compte de messagerie**.

4. Saisissez les informations suivantes :
    - **Nom du compte**: un nom quelconque pour le compte, par exemple 'GMX'.
    - **Expéditeur**: votre adresse GMX, par exemple 'seatable@gmx.de'.
    - **Serveur SMTP**: 'mail.gmx.net
    - **Port SMTP**: '587
    - **Nom d'utilisateur**: votre adresse GMX, par exemple 'seatable@gmx.de'.
    - **Mot de passe**: le mot de passe de votre compte GMX

Les champs Hôte IMAP et Port IMAP peuvent rester vides. Vous trouverez les données du serveur SMTP pour WEB.DE dans [la zone d'aide de WEB.DE](https://hilfe.web.de/pop-imap/imap/imap-serverdaten.html).

Voici un exemple de configuration pour un compte GMX :  
![Paramètres SMTP de GMX](images/smtp-settings-gmx.jpg)

## Envoyer des e-mails par automatisation

Ensuite, vous pouvez utiliser le compte e-mail créé dans votre SeaTable Base pour envoyer des e-mails par automatisation ou [par bouton]({{< relref "help/base-editor/schaltflaechen/eine-e-mail-per-schaltflaeche-verschicken" >}}).

Si vous souhaitez en savoir plus sur cette automatisation utile, lisez l'article [Envoi d'e-mails par automatisation]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}}).
