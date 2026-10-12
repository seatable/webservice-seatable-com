---
title: 'Étape 4 : Réception du paiement'
date: 2024-09-19
lastmod: '2024-09-24'
categories:
    - 'online-kurs-2'
author: 'cdb'
url: '/fr/aide/etape4-reception-paiement-seatable'
aliases:
    - '/fr/aide/schritt-4-geldeingang'
seo:
    title: 'Étape 4 SeaTable Cours 2 : réception de paiement – email'
    description: 'À la quatrième étape, créez un bouton SeaTable pour enregistrer les paiements et envoyer une confirmation automatique par e-mail aux participants.'
---

Après avoir reçu la demande de paiement par e-mail, les participants virent le prix du cours sur votre compte bancaire. Nous n'allons pas automatiser davantage le suivi des paiements à ce stade. Il serait toutefois utile d'ajouter à votre base un second bouton, qui remplirait deux fonctions :

1. confirmer au participant que son paiement est bien arrivé, et donc que son inscription est complète ;
2. garder une trace du paiement dans la base.

## Plusieurs actions dans un seul bouton

SeaTable le permet facilement. Dans le tableau `Registrations`, ajoutez un nouveau bouton qui enchaîne deux actions :

- envoyer au participant un e-mail de confirmation de paiement ;
- passer `Payment Status` à `Paid`.

Avec ce que vous avez appris, cela ne devrait pas vous poser de difficulté. Pour l'e-mail, vous pouvez reprendre ce texte :

> Subject: Payment Confirmation and Online Meeting Details
>
> Hey,
>
> Thank you for your payment! We’re excited to confirm that we’ve successfully received it.
>
> You can join the online meeting using the link below:  
> – https://meet.jit.si/{Course-ID}
>
> We look forward to seeing you there!  
> Best regards

## Article d'aide avec plus d'informations

- [Configurer un compte de messagerie dans une base]({{< relref "help/base-editor/weitere-optionen/einrichtung-eines-e-mail-kontos-in-einer-base" >}})
- [Configurer Gmail pour l'envoi d'e-mails via SMTP]({{< relref "help/integrationen/integrationen-innerhalb-von-seatable/gmail-fuer-den-versand-von-e-mails-per-smtp-einrichten" >}})
- [Le bouton]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}})
- [Envoyer un e-mail via un bouton]({{< relref "help/base-editor/schaltflaechen/eine-e-mail-per-schaltflaeche-verschicken" >}})
- [E-mail par automatisation]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}})
