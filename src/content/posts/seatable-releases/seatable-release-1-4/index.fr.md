---
title: 'SeaTable 1.4 : Nouvelles options pour la gestion des données et la collaboration en ligne - SeaTable'
description: 'Colonne URL : accédez à des ressources en 2 clics ; assistant de liens contextuel ; requêtes sur chaînes de tables liées ; chat temps réel sur les lignes ; webhooks, scripts Python et navigation réorganisée offrent gain de temps et meilleure collaboration pour toutes les équipes.'
date: 2020-10-29
lastmod: '2023-07-11'
author: 'rdb'
url: '/fr/seatable-release-1-4'
color: '#396afc'
categories:
    - 'product-features'
seo:
    title: 'SeaTable 1.4 : URL, liaisons et chat intégré'
    description: 'Colonne URL, liaison facilitée, requêtes multi-tables, chat d’équipe et scripts Python : SeaTable 1.4 s’enrichit !'
---

Nous sommes heureux d'annoncer la sortie de SeaTable 1.4 ! Nous avons intégré un nouveau type de colonne, des fonctions de base de données améliorées, un chat en temps réel et de nombreuses autres améliorations dans cette nouvelle version. Organiser des données et collaborer en équipe n'a jamais été aussi facile et pratique ! Et surtout, chaque utilisateur bénéficie des nouvelles fonctionnalités, y compris l'abonnement gratuit.

Pour une liste complète des changements, veuillez consulter le [SeaTable Changelog]({{< relref "pages/changelog" >}}). Cette note de version représente les changements les plus importants et les plus passionnants de SeaTable 1.4. Allons-y !

## Bienvenue dans l'équipe de type Colonne #18

SeaTable 1.4 contient un autre type de colonne : la [colonne URL]({{< relref "help/base-editor/spalten/uebersicht-alle-spaltentypen" >}}#url). Cette colonne se comporte comme une colonne de texte, mais le contenu de la cellule est interprété comme une référence à une ressource réseau. Les adresses Internet et IP telles que https://seatable.com, [www.seafile.com](https://www.seafile.com/en/home/), 192.168.178.1 et localhost:8000 sont en de bonnes mains dans la colonne URL.

L'adresse d'une ressource du réseau peut être appelée à partir d'une colonne URL en deux clics. Au premier clic, une icône de lien apparaît sur le bord droit de la cellule. En cliquant une deuxième fois sur cette icône, l'adresse est appelée dans un nouvel onglet du navigateur ; http(s) est automatiquement ajouté comme préfixe. Si vous vous demandez maintenant pourquoi deux clics sont nécessaires, en voici la raison : les deux clics protègent contre les appels de page web erronés lors de la navigation dans le tableau, ce qui peut facilement arriver, surtout sur les appareils mobiles.

## Des fonctions de base de données plus puissantes et plus simples

Le nouvel assistant pour la colonne de liens et les options de requête étendues raviront en particulier les amateurs de bases de données, mais pas seulement ! SeaTable rend les bases de données aussi simples qu'elles devraient l'être !

### Liens très simples

La liaison des entrées était encore quelque peu fastidieuse dans la version 1.3. Un menu déroulant listait les entrées des premières colonnes du tableau lié. Compact, mais peu pratique si le tableau lié comporte deux ou plusieurs lignes avec les mêmes valeurs dans la colonne 1. Ce problème est résolu dans SeaTable 1.4 !

La liste déroulante a fait place à un nouvel assistant, riche en détails et sensible au contexte. Un double-clic sur une cellule l'ouvre. Si la cellule est vide, l'assistant affiche les premières colonnes du tableau lié. La confusion quant à l'entrée correcte dans le tableau cible fait désormais partie du passé. En double-cliquant sur une cellule contenant déjà des entrées liées, l'assistant affiche les détails des entrées liées. D'autres entrées peuvent être liées en cliquant sur le bouton "Ajouter un nouveau lien" dans le coin supérieur droit.

![Nouvel assistant pour les colonnes de liens vers d'autres enregistrements](linking-dialog.png)

Le nouvel assistant simplifie la liaison des tableaux, mais ce n'est pas la seule chose qu'il peut faire. De nouvelles entrées peuvent également être créées dans la table liée directement à partir de l'assistant. Sans tables à langer, sans orgies de clics et sans perte de temps. Avec le nouvel assistant, vous travaillez sur deux tables différentes en même temps.

### Puissance totale de la base de données

Les requêtes de base de données portant sur plusieurs tables ont quelque chose de magique. Dans les versions précédentes de SeaTable, les requêtes n'étaient possibles que sur des tables directement liées. Cette restriction a été supprimée dans SeaTable 1.4 ! Tant que les entrées sont liées, SeaTable peut les suivre et produire la valeur cible - quel que soit le nombre de liens que SeaTable doit suivre. L'implémentation intuitive de cette fonctionnalité dans SeaTable garantit que les experts en bases de données ne sont pas les seuls à pouvoir profiter de cette touche de magie.

Imaginez que vous gérez vos actifs informatiques avec SeaTable. Dans le tableau 1, vous gérez les utilisateurs, le tableau 2 contient les salles et le tableau 3 énumère le matériel. Chaque utilisateur est lié à une salle par une relation 1:1 et aux actifs informatiques par une relation 1:n. L'utilisateur représente donc le lien entre la pièce et le bien. Avec SeaTable 1.4, la création d'une liste des actifs informatiques par pièce est une question de quelques clics.

## Chattez avec vos collègues en temps réel

Une collaboration en ligne efficace n'est pas possible sans une bonne communication au sein de l'équipe. La version 1.4 présente maintenant la solution qui vous permet de rester en contact étroit avec les membres de votre équipe ! Discuter des idées, commenter les nouveaux enregistrements et discuter des changements, tout cela est facilement possible et se produit là où cela doit se produire : directement dans les données.

![Discussion en temps réel dans les commentaires](comment-chat.png)

Si vous ne connaissez pas encore la fonction de commentaire, sélectionnez une ligne et appuyez sur la barre d'espacement pour afficher les détails de la ligne. Dans les coins supérieurs droits, vous trouverez la colonne des commentaires. Le backend amélioré de SeaTable informe les utilisateurs des nouveaux commentaires sans délai. Si les utilisateurs sont en ligne, le chat de groupe peut alors commencer. Dans le cas contraire, les utilisateurs sont informés par [notification]({{< relref "help/startseite/benachrichtigungen" >}}). Échangez vos idées et vos impressions avec vos collègues lorsqu'elles sont fraîches.

## Des Webhooks pour une meilleure automatisation

Qu'y a-t-il de mieux que SeaTable ? SeaTable en interaction avec vos autres applications préférées ! C'est pourquoi nous nous sommes efforcés d'offrir une option d'intégration pratique avec [Zapier](https://zapier.com/apps/seatable/integrations) aussi rapidement que possible.

Mais Zapier n'était que la première étape. Les Webhooks, introduits avec cette version, sont la seconde. Les webhooks de SeaTable permettent de déclencher facilement des actions basées sur des événements dans des applications externes. Voici deux exemples simples : Un compteur est incrémenté d'une unité lorsqu'une nouvelle entrée est créée ou un courriel est envoyé lorsqu'une valeur dépasse un seuil critique.

## Scripts SeaTable maintenant aussi en Python

![Support de Python dans les scripts SeaTable](python.png)

Enfin, SeaTable 1.4 offre également une innovation pour les développeurs. Cette fois, ce sont de bonnes nouvelles pour les amateurs de python.

SeaTable 1.3 a introduit le moteur de script de SeaTable. JavaScript était le langage de script pris en charge. Avec SeaTable 1.4, les scripts peuvent désormais être développés et exécutés en Python. Importez votre script Python ou développez-le directement dans l'éditeur de script SeaTables pour automatiser le traitement des données et construire votre application personnalisée. Pour plus d'informations sur les scripts SeaTables, consultez le [manuel de programmation des scripts SeaTable](https://developer.seatable.com/scripts/).

Spoiler : Dans l'une des prochaines versions, nous ajouterons la possibilité d'exécuter des scripts en temps contrôlé.

## De nombreuses autres améliorations

Tous les membres de l'équipe de développement de SeaTable, qui compte environ 30 personnes, ne travaillent pas sur ces développements majeurs. Beaucoup de travail et de passion sont également consacrés aux innombrables petites améliorations incrémentales que nous apportons à SeaTable à chaque version, rendant SeaTable meilleur petit à petit. Voici les améliorations les plus importantes parmi ces petites améliorations.

Nous avons réorganisé la navigation sur le côté gauche de la bibliothèque de base. La nouvelle navigation contient deux catégories : L'espace de travail contient les bases, les formulaires web et l'aperçu des activités. Aide et ressources propose des liens directs vers notre collection croissante de templates ainsi que vers le manuel d'utilisation.

Au sujet de l'aperçu des activités : ce menu lui-même est à peine reconnaissable avec son nouveau design. Dans le passé, toutes les activités étaient listées ici par ordre chronologique, sans autre structure. Lorsque l'intensité d'utilisation augmentait, cela devenait rapidement confus. La nouvelle vue d'ensemble des activités conserve la structure chronologique de base, mais regroupe les activités base par base et offre ainsi une bien meilleure vue d'ensemble. Un clic sur une base ouvre les détails des modifications du jour sélectionné.

De petites mais fines améliorations ont également été apportées à la vue des tableaux. Lorsque vous ouvrez une base pour la première fois, la description de la base est automatiquement appelée. Ceci est très utile lorsque vous partagez des bases avec d'autres personnes. De cette façon, vos collègues reçoivent les informations que vous voulez qu'ils voient avant de se plonger dans les données.

Êtes-vous intéressé ou même inspiré ? Alors qu'attendez-vous ? L'inscription se fait en un rien de temps et SeaTable est définitivement gratuit ! Si vous avez des questions ou des doutes, des idées ou des commentaires, veuillez nous écrire ou laisser un commentaire dans le [forum](https://forum.seatable.com).
