---
title: 'La colonne des liens'
date: 2022-10-11
lastmod: '2026-10-08'
categories:
    - 'verknuepfungen'
author: 'kgr'
url: '/fr/aide/colonne-des-liens'
aliases:
    - '/fr/aide/wie-man-tabellen-in-seatable-miteinander-verknuepft'
    - '/fr/aide/comment-lier-tables-seatable'
seo:
    title: 'Enregistrements liés dans SeaTable : la colonne des liens'
    description: 'Des enregistrements liés sans programmation : reliez des tableaux, utilisez lookup et rollup et visualisez les relations sous forme de diagramme.'
weight: 20
---

Avec la colonne des liens, vous créez des relations entre tableaux dans SeaTable, sans SQL ni programmation. Un enregistrement d'un tableau renvoie à un ou plusieurs enregistrements d'un autre tableau, par exemple une commande à son client et aux produits commandés. Ces **enregistrements liés** (en anglais : _linked records_) sont la base des fonctions de [base de données relationnelle]({{< relref "posts/relationale-datenbank" >}}) de SeaTable. Le type de colonne s'appelle **Lien vers d'autres enregistrements**.

## Quelles relations vous pouvez représenter

| Relation | Exemple | Comment faire dans SeaTable |
|---|---|---|
| **1:1** (un à un) | Une facture correspond à exactement une commande. | Colonne des liens avec le réglage [Limiter les liens à une seule ligne maximum](#limiter-les-liens-à-une-seule-ligne-maximum) |
| **1:n** (un à plusieurs) | Un client a plusieurs commandes, chaque commande appartient à un client. | Colonne des liens limitée à une ligne dans le tableau des commandes et sans limite dans le tableau des clients |
| **n:m** (plusieurs à plusieurs) | Une commande contient plusieurs produits, un produit figure dans de nombreuses commandes. | Colonne des liens sans limite, aucune table intermédiaire nécessaire |
| **Dans un même tableau** | Tâches et sous-tâches, collaborateurs et leurs responsables | [Liens dans un tableau]({{< relref "help/base-editor/tabellen/verknuepfungen-innerhalb-einer-tabelle" >}}) |

Un lien est visible dans les deux tableaux. Lors de la création de la colonne des liens, vous choisissez si le lien est affiché dans une **colonne existante** de l'autre tableau ou si une **nouvelle colonne** y est créée.

{{< warning  headline="Conseil : données par combinaison"  text="Vous avez besoin, dans une relation n:m, de données propres à la combinaison, comme la **quantité** et le **prix** d'un produit dans une commande donnée ? Créez alors un tableau dédié, par ex. **Lignes de commande**, et reliez-le aux commandes et aux produits." />}}

### Exemple : clients, commandes et produits

![Base avec les tableaux Clients, Commandes, Lignes de commande, Produits et leurs liens](images/verknuepfungsspalten.png)

- Le tableau **Clients** contient le nom, l'interlocuteur et l'adresse.
- Chaque enregistrement de **Commandes** est lié à un client.
- Les **Lignes de commande** relient une commande à un produit et contiennent la quantité et le prix.
- Le tableau **Produits** contient la référence, la désignation et le prix catalogue.

Avec une [formule pour les liens](#utiliser-les-données-des-enregistrements-liés--lookup-rollup-et-plus), vous affichez le nom du client dans chaque commande et calculez le chiffre d'affaires par client dans le tableau des clients. Le [plugin de relations entre les tableaux](#visualiser-les-relations--le-diagramme-de-relations) affiche toute la structure sous forme de diagramme.

## Voici comment lier deux tableaux

![Créer un lien entre deux tableaux](images/how-to-link-different-tables.gif)

1. Créez une nouvelle colonne et sélectionnez le type de colonne **Lien vers d'autres enregistrements**.
2. Donnez un **nom** à la colonne.
3. Sous **Sélectionner un tableau pour le lien**, sélectionnez le tableau dont vous souhaitez lier les enregistrements au tableau actuel.
4. Cliquez sur **Envoyer**.
5. Le contenu de la nouvelle colonne est encore vide. Pour la remplir, vous pouvez **relier des enregistrements existants** ou **ajouter un enregistrement**.

Dès que les tableaux sont liés entre eux, vous pouvez utiliser la **boîte de dialogue des liens** pour accéder aux informations des enregistrements liés. Pour ce faire, cliquez sur le **symbole de la double flèche** dans une **cellule** de la colonne de liaison ou faites un **double clic**. Les **enregistrements liés** sont listés dans la boîte de dialogue de lien qui s'ouvre. Cliquez sur une entrée pour voir les **détails de la ligne** dans une fenêtre supplémentaire.

![Vue détaillée des lignes pour les enregistrements liés](images/Zeilendetailansicht-bei-verknuepften-Eintraegen-711x225.png)

## Lier des enregistrements existants

![Lier des enregistrements existants](images/link-existing-entries.gif)

1. Cliquez dans une **cellule** de la **colonne des liens**, puis sur le **symbole plus** qui apparaît.
2. Une liste des **lignes** disponibles **du tableau lié** s'affiche alors. Sélectionnez la ou les lignes que vous souhaitez lier à la ligne de votre tableau actuel.
3. Dans la colonne des liens, chaque ligne s'affiche immédiatement **comme un enregistrement lié**.

{{< warning  headline="Détour par la boîte de dialogue des liens"  text="Vous pouvez également ouvrir d'abord la boîte de dialogue des liens. Cliquez sur une **cellule dans la colonne des liens**, puis sur l'**icône** bleue **à double flèche** ou faites un **double clic**. Cliquez ensuite sur **Relier les enregistrements existants** et sélectionnez la ou les lignes comme ci-dessus." />}}

La **fonction de recherche intégrée** dans la boîte de dialogue du lien permet de parcourir les enregistrements du tableau lié afin de trouver rapidement la ligne souhaitée.

{{< warning  headline="Plusieurs liens par cellule"  text="Vous pouvez lier **plusieurs enregistrements** du tableau lié dans **une cellule** de la colonne de liaison. Pour ce faire, répétez les instructions décrites ci-dessus." />}}

## Ajouter un enregistrement

Vous pouvez même ajouter une **nouvelle ligne** à un **tableau lié** à l 'aide de la boîte de dialogue de lien, sans devoir passer dans ce tableau. La ligne est ensuite ajoutée dans le tableau lié parmi les enregistrements existants et s'affiche en tant qu'entrée liée dans la colonne de lien du tableau ouvert.

1. **Double-cliquez** sur la **cellule** d'une **colonne de lien** ou cliquez sur l'**icône bleue à double flèche** pour ouvrir la boîte de dialogue de lien.
    ![Double-clic dans une colonne de raccourcis](images/click-in-linked-column.png)
2. Cliquez sur **Ajouter un enregistrement**.
    ![Clique sur Ajouter une ligne](images/click-add-record.jpg)
3. Dans la fenêtre qui s'ouvre, remplissez les différentes **colonnes du tableau**.
    ![Remplir les colonnes du tableau](images/fill-columns.png)
4. Cliquez sur **Envoyer** pour créer la nouvelle ligne.
    ![Cliquez sur Envoyer](images/click-submit.png)
5. La **nouvelle ligne** est automatiquement ajoutée au **tableau lié** et s'affiche dans le tableau actuellement ouvert en tant qu'**entrée liée** dans la colonne de lien.

## Modifier les enregistrements existants d'un tableau lié

![Modifier les enregistrements existants d'un tableau lié](images/edit-linked-entries.gif)

1. Cliquez dans une **cellule** de la colonne des liens.
2. Cliquez sur l'**enregistrement lié** que vous souhaitez modifier.
3. Les **détails de la ligne** s'ouvrent. Effectuez-y les **modifications** souhaitées.
4. **Fermez** la fenêtre pour **enregistrer** les modifications.

## Supprimer les liens

Vous pouvez supprimer les entrées liées dans une colonne de liens en quelques clics seulement. Pour ce faire, il vous suffit d'ouvrir la **boîte de dialogue des liens** de la colonne de liens correspondante et de cliquer sur le **symbole X** à droite de l'entrée souhaitée.

![Supprimer les liens](images/delete-links.png)

{{< warning  headline="Remarque importante"  text="Seule l'**entrée liée** est **supprimée** de la colonne de liaison correspondante. Par contre, la **ligne dans le tableau lié** est toujours **conservée**." />}}

## Paramètres de la colonne des liens

Une colonne de liens vous permet d'effectuer et de modifier facilement différents réglages. Pour ce faire, cliquez dans l'en-tête du tableau sur l'**icône** triangulaire **déroulante** de la colonne de liens, puis sur **Paramètres**.

![Ouvrir les paramètres d'une colonne de liens](images/Einstellungen-einer-Link-Spalte-oeffnen-350x200.png)

### Sélection de la colonne à afficher du tableau relié

Dans le menu déroulant, vous pouvez d'abord sélectionner la **colonne du tableau lié** dont les **entrées** doivent être affichées dans la colonne de lien.

![Sélection de la colonne liée dans le tableau lié](images/select-column-of-linked-table-to-display.png)

### Limiter les liens à une seule ligne maximum

En activant le curseur correspondant, vous pouvez limiter le lien à **une ligne au maximum**. Si ce paramètre est activé, **une seule entrée liée** peut être ajoutée dans chaque cellule de la colonne de lien.

![Limiter les liens](images/limit-linking-to-max-one-row.png)

Si vous avez déjà ajouté une enregistrement lié à une cellule, les options permettant d'ajouter d'autres enregistrements ne sont **plus** affichées.

![Si le lien est limité à une ligne maximum, les options d'ajout de liens dans la boîte de dialogue des liens ne sont plus disponibles dès qu'un lien a été ajouté.](images/not-visibble-options-to-add-linked-records.png)

Ce paramètre peut par exemple être utile lorsqu'une facture doit être liée à la commande correspondante d'un autre tableau - lorsque les enregistrements liés forment donc des **paires** logiques. Dans ce cas, l'ajout d'autres liens pourrait entraîner une certaine confusion et nuire aux processus de travail.

### Limiter la sélection des liens à une seule vue

En activant ce paramètre, vous pouvez limiter les liens à **une vue** du tableau lié. Pour ce faire, vous devez définir une **vue** du tableau lié. Dans la colonne des liens, vous pouvez ensuite lier **uniquement** les entrées de cette vue. Il n'est alors **plus** possible de lier des entrées d'autres vues.

![Limiter les raccourcis à une seule vue](images/Verknuepfungen-auf-eine-Ansicht-einschraenken.png)

Ce paramètre est particulièrement utile pour les **vues filtrés** et peut vous aider si vous souhaitez lier des **enregistrements spécifiques** dans vos tableaux.

### Empêcher de relier des enregistrements existants

Dans les paramètres d'une colonne de liens, vous pouvez également empêcher la création de liens vers des enregistrements existants en activant le curseur correspondant. Si le curseur **est activé**, la colonne de liens correspondante ne prend en charge **que** l'ajout de **nouvelles lignes**.

Les enregistrements déjà existants dans le tableau lié ne peuvent alors **plus** être liés dans la colonne. Les enregistrements qui ont déjà été liés dans la colonne ne sont cependant **pas affectés** par ce réglage.

![Réglage pour empêcher la création de liens vers des entrées existantes](images/setting-avoid-linking-existing-records.png)

### Limiter la sélection des lignes avec un filtre

Si vous activez cette option, vous pouvez restreindre la sélection des lignes pouvant être liées en fonction de règles de filtrage. Les filtres eux-mêmes peuvent être statiques ou dynamiques :
- Dans le cas d'un **filtre statique**, vous utilisez une valeur uniforme pour filtrer les lignes dans la table liée (par exemple, seules les lignes qui n'ont pas la valeur "archivé" peuvent être liées). L'effet est donc similaire à celui de l'option **Limiter la sélection des liens à une seule vue**.
- Dans le cas d'un **filtre dynamique**, la valeur utilisée pour filtrer les lignes dans le tableau lié est une valeur de colonne de la ligne active (par exemple, seules les lignes dont l'état est identique à l'état de la ligne active peuvent être liées). Les **lignes avec des valeurs de filtre différentes** ont donc des lignes liées différentes.

![Limiter les liens avec une règle de filtrage](images/limit-row-selection-using-a-filter-rule.png)

## Options d'affichage de la boîte de dialogue des liens

Dans la boîte de dialogue de lien d'une colonne de lien, vous disposez en outre de différentes options d'affichage.

### Ajuster la taille de la fenêtre

Pour avoir une vue d'ensemble de toutes les enregistrements liés, vous pouvez adapter la **taille** de la fenêtre de dialogue des liens. Pour ce faire, il suffit de passer la souris sur l'un des bords extérieurs jusqu'à ce que le curseur se transforme en **double flèche**, puis de faire glisser le bord dans la direction souhaitée en maintenant le bouton de la souris enfoncé.

![Adapter la taille de la fenêtre de la boîte de dialogue des liens](images/adjust-size-of-the-link-dialogue.gif)

### Adapter la largeur des colonnes

Pour que davantage d'entrées de colonnes des lignes liées tiennent dans la fenêtre, vous pouvez également adapter la **largeur** des **colonnes** affichées dans la boîte de dialogue des liens. Pour ce faire, passez la souris sur la **zone entre deux noms de colonnes** jusqu'à ce que le curseur se transforme en **double flèche** et faites glisser la ligne de délimitation invisible vers la gauche ou la droite en maintenant le bouton de la souris enfoncé jusqu'à ce que vous obteniez la **largeur de colonne** souhaitée.

![Adapter la largeur des colonnes](images/adjust-size-of-columns-in-link-dialog.gif)

### Masquer les colonnes

Pour rendre la boîte de dialogue des liens encore plus claire, vous pouvez masquer autant de colonnes que vous le souhaitez des enregistrements liés en cliquant sur le **symbole de l'œil**. Une fenêtre s'ouvre alors, dans laquelle vous pouvez **(dé)activer** les différentes colonnes à l'aide de régulateurs. En conséquence, les colonnes sont masquées ou affichées dans l'aperçu des enregistrements liés.

![Masquage de certaines colonnes dans la vue des enregistrements liés dans la boîte de dialogue d'une colonne de liaison](images/hide-columns.in-link-dialog.jpg)

### Trier les entrées

En cliquant sur les **symboles fléchés**, vous pouvez **trier** les entrées liées dans la boîte de dialogue des liens. Utilisez cette fonction, par exemple, pour afficher les entrées liées dans l'ordre alphabétique à l'aide d'une colonne de texte ou pour les classer selon une autre colonne.

![Tri des entrées dans la boîte de dialogue d'une colonne de liens](images/sort-entries-link-dialog.jpg)

{{< warning  headline="Conseil"  text="**Combinées**, les **options d'affichage** ont encore plus d'impact et peuvent vous aider à trouver certaines entrées liées encore plus rapidement et plus facilement." />}}

## Utiliser les données des enregistrements liés : lookup, rollup et plus

Les enregistrements liés n'affichent d'abord qu'une seule valeur de l'autre tableau, par ex. le nom. Pour récupérer, compter ou résumer d'autres valeurs, utilisez une colonne de type [Formule pour les liens]({{< relref "help/base-editor/spaltentypen/die-spalte-formel-fuer-verknuepfungen" >}}). Cinq formules sont disponibles :

| Formule | Ce qu'elle fait | Exemple |
|---|---|---|
| [Lookup]({{< relref "help/base-editor/formeln/die-lookup-funktion" >}}) | récupère les valeurs d'une colonne des enregistrements liés | afficher le numéro de téléphone du client dans la commande |
| [Rollup]({{< relref "help/base-editor/formeln/die-rollup-formel" >}}) | résume les valeurs des enregistrements liés, par ex. en somme ou en moyenne | chiffre d'affaires par client sur toutes ses commandes |
| [Countlinks]({{< relref "help/base-editor/formeln/die-countlinks-formel" >}}) | compte les enregistrements liés | nombre de commandes par client |
| [Findmax]({{< relref "help/base-editor/formeln/die-findmax-formel" >}}) | trouve l'enregistrement lié ayant la valeur la plus élevée | dernière commande d'un client |
| [Findmin]({{< relref "help/base-editor/formeln/die-findmin-formel" >}}) | trouve l'enregistrement lié ayant la valeur la plus faible | première commande d'un client |

Les formules pour les liens fonctionnent aussi sur plusieurs niveaux : un lookup peut accéder à une colonne lookup ou rollup du tableau lié. Ainsi, une ligne de commande affiche le nom du client : la commande le récupère par lookup dans le tableau des clients, et la ligne de commande accède par lookup à cette colonne de la commande.

## Visualiser les relations : le diagramme de relations

Avec de nombreux tableaux liés, on perd vite la vue d'ensemble. Le [plugin de relations entre les tableaux]({{< relref "help/base-editor/plugins/anleitung-zum-tabellenbeziehungen-plugin" >}}) affiche tous les tableaux d'une base avec leurs colonnes sous forme de **diagramme de relations**. Les lignes continues représentent des liens directs via des colonnes des liens, les lignes en pointillés des connexions indirectes via des formules pour les liens comme lookup ou rollup. Vous pouvez exporter le diagramme en tant qu'image.

![Diagramme de relations de la base d'exemple Clients, Commandes, Lignes de commande, Produits](images/Beziehungsdarstellung.png)

## Limites

- **Modifier le type de colonne ultérieurement :** Une colonne existante ne peut pas être convertie en colonne des liens. Créez plutôt une nouvelle colonne (voir [Questions fréquentes](#questions-fréquentes)).
- **Une colonne par lookup :** Chaque colonne lookup récupère les valeurs d'exactement une colonne du tableau lié. Pour d'autres valeurs, créez d'autres colonnes lookup.

## Questions fréquentes

{{< faq "SeaTable peut-il représenter des relations n:m (plusieurs à plusieurs) ?" >}}Oui. Une colonne des liens sans limite permet un nombre quelconque d'enregistrements liés dans chaque cellule, et un enregistrement peut être lié à un nombre quelconque de lignes de l'autre tableau. Vous n'avez besoin d'une table intermédiaire que si vous souhaitez enregistrer des données sur la combinaison, par ex. la quantité et le prix par ligne de commande.
{{< /faq >}}

{{< faq "Faut-il connaître SQL pour relier des tableaux ?" >}}Non. Vous configurez les liens, lookups et rollups entièrement dans l'interface. Si vous le souhaitez, vous pouvez aussi travailler avec les enregistrements liés via l'[API](https://developer.seatable.com) ou avec des scripts Python et JavaScript.
{{< /faq >}}

{{< faq "Les liens sont-ils conservés lors d'une importation depuis Airtable ?" >}}Oui. Lors de la [migration de bases Airtable]({{< relref "help/startseite/import-von-daten/migration-von-airtable-bases-zu-seatable" >}}), vous indiquez les colonnes de liens dans le script de migration, et elles arrivent dans SeaTable sous forme de liens. Toutes les colonnes sont importées sauf **Button**, **Count**, **Lookup** et **Rollup**. Après l'importation, recréez les colonnes lookup et rollup en tant que formules pour les liens.
{{< /faq >}}

{{< faq "Je ne trouve pas ce type de colonne. Ne puis-je pas créer de lien ?" >}}La colonne de liens est disponible dans chaque abonnement SeaTable. Cependant, vous essayez probablement de modifier le type de colonne d'une colonne existante. Lorsque vous [modifiez le]({{< relref "help/base-editor/spalten/wie-man-den-spaltentyp-anpasst" >}}) type de colonne, le type de colonne **Lien vers d'autres entrées** n'est en effet _pas_ disponible. Créez plutôt une **nouvelle colonne** et le type de colonne souhaité vous sera proposé.

{{< /faq >}}
