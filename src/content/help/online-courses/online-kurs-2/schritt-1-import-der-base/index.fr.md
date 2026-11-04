---
title: 'Étape 1 : Importer la base'
date: 2024-09-19
lastmod: '2024-09-24'
categories:
    - 'online-kurs-2'
author: 'cdb'
url: '/fr/aide/etape1-import-base-seatable'
aliases:
    - '/fr/aide/schritt-1-import-der-base'
seo:
    title: 'Étape 1 du cours SeaTable 2 : importer et explorer la base'
    description: 'Démarrez le cours 2 : importez la base fournie, explorez champs et formules, et découvrez les vues clés pour vos prochains processus complexes.'
---

Pour créer un nouvel outil de gestion dans SeaTable, il faut d'abord la bonne structure de tableaux : c'est elle qui permet de saisir les données utiles au processus, puis de les exploiter efficacement. Les nombreux modèles proposés peuvent vous inspirer, mais il faut en général bien réfléchir au processus et définir clairement les données nécessaires et pertinentes.

Ce cours portant sur la gestion de prestations en ligne, il nous faut deux tableaux centraux :

- un tableau pour les cours proposés ;
- un tableau pour les participants.

Vous avez déjà appris à créer une base et ses colonnes lors du cours précédent. Nous sautons donc cette étape et partons d'une base toute prête.

Téléchargez le fichier suivant sur votre ordinateur, puis importez-le comme nouvelle base depuis la page d'accueil de SeaTable :

[SeaTable Course 2.dtable](/SeaTable-Course-2.dtable)

Vous n'avez pas à créer la base vous-même, mais prenez le temps de bien comprendre sa structure : elle utilise des types de colonnes que vous n'avez peut-être pas encore rencontrés dans le cours précédent.

## Ce que contient la base

À première vue, la base est plutôt simple. Elle comporte seulement :

- 2 tableaux ;
- 18 colonnes ;
- 3 vues ;
- 1 formulaire web.

Ne vous fiez pourtant pas à cette simplicité : cette structure est étonnamment puissante. Voyons pourquoi nous l'avons conçue ainsi.

### Vos cours en un coup d'œil

Le tableau `Courses` rassemble toutes les informations importantes sur vos cours. Chaque ligne correspond à un cours ou à une prestation que vous proposez, et les colonnes en donnent le détail, par exemple :

- le nom du cours ;
- sa date ;
- le nombre de participants inscrits ;
- son statut (complet ou places encore disponibles).

Vous gardez ainsi à tout moment une vue d'ensemble de vos cours et de leurs inscrits.

![Tableau « Courses » avec données de cours, nombre de participants et statut par cours](images/lvl2-table-courses.png)

{{< warning  headline="Des dates dans le passé"  text="Toutes les dates de cours sont passées : nous avons simplement choisi de ne pas les mettre à jour régulièrement. N'en tenez pas compte pendant le cours." />}}

### Tout sur vos participants

Le tableau `Registrations` rassemble les informations sur les personnes inscrites à vos cours. Chaque ligne correspond à une inscription :

- le nom du participant ;
- son adresse e-mail ;
- le cours auquel il s'est inscrit ;
- le statut de paiement de l'inscription (a-t-elle déjà été payée ?).

Ce tableau vous donne à tout moment une vision claire des inscriptions et des paiements.

![Tableau « Registrations » avec noms, e-mails et cours choisis par les participants](images/lvl2-table-registrations.png)

{{< warning  headline="Colonnes masquées"  text="Pour plus de lisibilité, deux colonnes sont masquées. Vous verrez plus loin qu'elles ne servent qu'au publipostage." />}}

## Autres particularités

Certaines fonctions de cette base ne sont compréhensibles qu'à la lecture de leur définition et/ou de leurs paramètres. Lisez attentivement les explications qui suivent : elles vous aideront pour la suite du cours.

### Colonnes de formule

Le tableau `Courses` contient deux colonnes de formule importantes, dont voici le rôle :

- `{{< seatable-icon icon="dtable-icon-formula" >}} Title and Date`
- `{{< seatable-icon icon="dtable-icon-formula" >}} Status`

`{{< seatable-icon icon="dtable-icon-formula" >}} Title and Date` est une colonne auxiliaire qui assemble les valeurs des colonnes `Title` et `Date` : sa formule, très simple, accole le titre et la date du cours.

![Colonne de formule « Title and Date » combinant titre du cours et date en un affichage unique](images/lvl2-formula-title-date.png)

À première vue, cette colonne semble superflue, puisqu'elle ne fait que combiner des données existantes. Croyez-nous : en examinant le formulaire d'inscription, vous comprendrez vite à quel point elle est utile.

---

La colonne de formule `{{< seatable-icon icon="dtable-icon-formula" >}} Status` indique automatiquement si un cours a encore des places disponibles ou s'il est complet. Sa logique est assez simple ; en situation réelle, elle pourrait aussi tenir compte de la date du cours.

![Colonne de formule « Status » calculant automatiquement places libres ou complet pour chaque cours](images/lvl2-formula-status.png)

{{< warning  headline="À quoi servent les colonnes de formule"  text="Les colonnes de formule jouent un rôle central dans les bases SeaTable bien conçues : elles combinent des informations ou déterminent un état. Tout leur intérêt apparaît souvent quand d'autres fonctions s'appuient sur elles." />}}

### Une vue pour ne proposer que les cours disponibles

Le tableau `Courses` comporte une vue spéciale, `{{< seatable-icon icon="dtable-icon-main-view" >}} Available Courses`. Elle utilise un filtre sur la colonne de formule `{{< seatable-icon icon="dtable-icon-formula" >}} Status` pour n'afficher que les cours qui ont encore des places. Les cours complets disparaissent ainsi automatiquement.

Cette vue est verrouillée {{< seatable-icon icon="dtable-icon-unlock" >}} pour que personne ne la modifie par erreur. Elle joue un rôle important : elle limite les choix proposés dans la colonne de lien `{{< seatable-icon icon="dtable-icon-link-other-record" >}} Registered for`.

Vous verrez pourquoi elle est si utile en examinant le formulaire d'inscription, à l'étape suivante.

![Paramètres de la colonne de lien « Registered for » limitée à la vue « Available Courses »](images/lvl2-link-column-limit-to-view.png)

### Des couleurs pour les lignes et les colonnes

SeaTable permet de mettre en couleur des lignes, des colonnes et des cellules. Deux exemples de coloration sont utilisés dans cette base :

- les lignes des cours prennent une couleur selon leur statut : en vert les cours qui ont encore des places, en rouge les cours complets ;
- les prix sont colorés selon leur montant : plus le cours est cher, plus la couleur est foncée.

## Prenez la base en main

Prenez le temps d'explorer la base en détail. Si certaines fonctions vous sont encore inconnues, consultez les articles d'aide ci-dessous.

## Article d'aide avec plus d'informations

- [Créer une base à partir d'un fichier DTABLE]({{< relref "help/startseite/import-von-daten/erstellen-einer-base-aus-einer-dtable-datei" >}})
- [La colonne des formules]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}})
- [Marquage des lignes par des couleurs]({{< relref "help/base-editor/ansichten/farbliche-markierung-von-zeilen" >}})
- [Verrouiller les vues]({{< relref "help/base-editor/ansichten/ansicht-sperren" >}})
