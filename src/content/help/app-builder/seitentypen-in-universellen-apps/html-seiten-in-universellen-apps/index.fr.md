---
title: 'Pages HTML dans les applications de SeaTable'
date: 2026-08-11
lastmod: '2026-11-20'
categories:
    - 'seitentypen-in-universellen-apps'
author: 'kgr'
url: '/fr/aide/pages-html-apps-seatable'
seo:
    title: 'Ajouter des pages HTML dans SeaTable Apps'
    description: 'Ajoutez à votre application des pages entièrement personnalisées basées sur HTML, JavaScript et CSS pour concevoir vous-même l’interface.'
weight: 12
---

Les autres [types de pages d'une application]({{< relref "help/app-builder/seitentypen-in-universellen-apps/ueberblick" >}}) offrent certes de nombreuses possibilités de configuration, mais ils imposent la structure et le comportement d'une page. Grâce aux **pages HTML**, vous pouvez ajouter à votre application des pages entièrement personnalisées basées sur HTML, JavaScript et CSS. Vous pouvez ainsi concevoir des applications exactement selon vos idées et réaliser sans problème des interactions même complexes. Les **cas d'application typiques** sont :
- Des formulaires, des listes et des pages d'information au design individuel
- Des types de graphiques ou de schémas personnalisés avec des éléments cliquables
- Des vues combinées, p. ex. un tableau et un enregistrement individuel sur une même page

![Exemple d'une page HTML](images/html-page.png)

Les pages HTML peuvent afficher des **contenus statiques**, mais elles déploient leur véritable potentiel en combinaison avec les **données d'une base**. Tout comme les autres types de pages de l'App Builder, elles peuvent récupérer des données d'une base et modifier des enregistrements dans une base. En ce qui concerne la **conception de l'interface utilisateur**, il n'y a pratiquement aucune limite. Tout ce qui peut être réalisé avec HTML, CSS et JavaScript peut également être intégré dans votre application sous forme de page HTML.

{{< warning headline="Pas une approche no-code" >}}

Notez que ce type de page s'adresse aux **utilisateurs ayant une expérience en programmation**. L'ensemble du code de la page doit être créé en dehors de SeaTable, puis téléchargé dans l'application sous forme de paquet. Si vous n'avez pas de connaissances en programmation, créez plutôt une **page générée par l'IA**, qui vous permet de faire générer des pages HTML par une IA en langage naturel.

{{< /warning >}}

**Regardez notre vidéo explicative sous-titrée en français.**
{{< youtube pPdRwUx_Io8 >}}

## Comment créer une page HTML

1. Ouvrez une application en **mode d'édition**. Pour ce faire, passez la souris sur l'application et cliquez sur l'**icône en forme de crayon** {{< seatable-icon icon="dtable-icon-rename" >}}.
   ![Modifier les applications](images/edit-apps.png)
2. Cliquez en haut à gauche sur **le cercle orange avec l'icône plus**, puis sélectionnez **Ajouter une page HTML**.
   ![Ajouter une page HTML](images/add-html-page.png)
3. Donnez un **nom** à la page et définissez éventuellement une **icône** pour la page.
   ![Créer une page HTML](images/create-html-page.png)
4. Confirmez avec **Envoyer**.
5. Créez sur votre appareil un **fichier zip** contenant les fichiers HTML, JavaScript et CSS.
6. **Téléchargez le fichier** en cliquant dans la zone prévue à cet effet ou en y glissant le fichier.
   ![Télécharger le fichier zip](images/upload-zip-file.png)
7. SeaTable affiche ensuite le fichier sous forme de **page dans l'application**.

{{< warning headline="Attention" >}}

Le fichier zip ne doit pas dépasser **10 Mo** et doit contenir un fichier HTML nommé **index.html**.

{{< /warning >}}

## Comment créer les fichiers nécessaires

Il existe **deux moyens** de créer une page HTML et de la mettre à disposition sous forme de fichier zip :
- L'**approche low-code** : Concevez la page dans un **éditeur HTML visuel**, reliez-la à votre base à l'aide d'**extraits de code** prédéfinis, ajoutez éventuellement des **images et des graphiques** et regroupez le tout dans un **fichier zip**. Cette méthode est idéale pour les formulaires, les tableaux de bord et les pages au design individuel avec des opérations de lecture et d'écriture simples.
- L'**approche développeur** : Dès que vous souhaitez créer des pages HTML plus importantes avec une logique plus complexe, p. ex. lorsque les éléments de la page doivent interagir entre eux, vous avez besoin de la **chaîne d'outils JavaScript complète**. Le développement nécessite **Node.js** et **npm**, un **serveur de développement** avec rechargement en direct ainsi qu'un **jeton API** généré dans la base.

Vous trouverez de plus amples informations, des exemples et des modèles dans notre [manuel du développeur](https://developer.seatable.com/html-pages/).
