---
title: 'Connecter une bibliothèque Seafile à SeaTable'
date: 2023-06-27
lastmod: '2023-06-27'
categories:
    - 'integrationen-innerhalb-von-seatable'
author: 'nsc2'
url: '/fr/aide/connecter-bibliotheque-seafile-a-seatable'
aliases:
    - '/fr/aide/eine-seafile-bibliothek-an-seatable-anbinden'
seo:
    title: 'Connecter une bibliothèque Seafile à SeaTable – guide'
    description: 'Intégrez Seafile dans SeaTable pour augmenter la capacité, gérer vos documents et synchroniser fichiers volumineux directement depuis vos bases.'
---

Si vous enregistrez beaucoup de fichiers volumineux (par exemple des images et des vidéos) dans une base, vous risquez d'une part d'atteindre un jour les [limites de stockage de votre abonnement]({{< relref "pages/prices" >}}) et d'autre part, au-delà de 100 Mo, il ne sera plus possible d'[exporter]({{< relref "help/startseite/import-von-daten/dtable-dateiformat" >}}) la base en tant que [fichier DTABLE]({{< relref "help/startseite/bases/speichern-einer-base-als-dtable-datei" >}}).

Une solution pour respecter les limites dans ce cas est d'externaliser vos fichiers dans un stockage en nuage comme **Seafile**, que vous pouvez ensuite connecter à SeaTable. Dans l'article suivant, vous apprendrez comment intégrer une bibliothèque Seafile dans une base.

{{< warning headline="Info" text="Seafile est la solution de partage de fichiers et de stockage en nuage des créateurs de SeaTable, ce qui vous permet de combiner les deux produits en une solution globale de gestion collaborative de l'information. Vous pouvez ainsi combiner les avantages de Seafile - capacité de stockage flexible et synchronisation des fichiers - avec les points forts de SeaTable." />}}

## Pour lier une bibliothèque Seafile à SeaTable, procédez comme suit

1. Ouvrez l'interface web Seafile et connectez-vous avec votre **compte Seafile**.
2. Cliquez sur l'**icône déroulante** pour ouvrir les options avancées d'une **bibliothèque Seafile** et cliquez sur **API Token**.

    ![Ouvrir les paramètres avancés d'une bibliothèque et cliquer sur API Token](images/click-api-token.png)

3. **Nommez** le **token**, attribuez une autorisation de lecture et d'écriture ou seulement une autorisation de lecture et créez le token en cliquant sur **Envoyer**.

    ![Création du jeton API](images/create-api-token.png)

4. **Copiez** le jeton API dans le cache.

    ![Copie du jeton de l'API dans le cache](images/copy-api-token.png)

5. Ouvrez ensuite l'**interface web de SeaTable** et allez dans la base dans laquelle vous souhaitez intégrer la **bibliothèque**.
6. Cliquez sur les **trois points** dans l'en-tête de la base pour ouvrir les options avancées de la base et sélectionnez l'option **Intégration de tiers**.

    ![Sélection de l'option Intégration de tiers](images/open-third-party-integration.png)

7. Dans la section Seafile, cliquez sur **Ajouter une bibliothèque Seafile.**

    ![Cliquez sur Ajouter une bibliothèque Seafile](images/add-seafile-library.png)

8. Saisissez le **nom de la bibliothèque**, l'**URL de votre serveur Seafile** et le **jeton API** de la bibliothèque que vous avez copié précédemment.

    ![Intégration de la bibliothèque Seafile](images/add-library-to-base.png)

9. Cliquez enfin sur **Vérifier**. Une fois le message de réussite affiché, confirmez l'intégration en cliquant sur **Envoyer**.

    ![Confirmer et terminer l'intégration de la bibliothèque Seafile](images/finish-integration.gif)

## Accéder aux fichiers dans Seafile

Une fois l'intégration dans la base réussie, la **bibliothèque Seafile** apparaît comme un dossier dans le [Gestionnaire de fichiers]({{< relref "help/base-editor/dateien/das-dateimanagement-einer-base" >}}) de votre base.

![Bibliothèque Seafile intégrée dans la gestion de fichiers de la base](images/library-in-file-management.png)

Cette intégration vous permet d'utiliser les fichiers stockés dans Seafile directement dans SeaTable.

## Possibilités d'intégration

En principe, vous pouvez connecter à SeaTable aussi bien des serveurs Seafile auto-hébergés que des serveurs hébergés. N ['hésitez pas à contacter notre équipe commerciale]({{< relref "pages/contact" >}}) si vous souhaitez héberger vous-même un serveur Seafile. Pour les clients SeaTable dédiés, nous proposons un co-hébergement Seafile.
