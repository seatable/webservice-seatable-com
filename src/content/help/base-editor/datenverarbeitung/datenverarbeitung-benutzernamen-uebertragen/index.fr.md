---
title: "Traitement des données : transfert du nom d'utilisateur"
date: 2023-03-17
lastmod: '2023-03-17'
categories:
    - 'datenverarbeitung'
author: 'nsc2'
url: '/fr/aide/transfert-noms-utilisateurs-seatable'
aliases:
    - '/fr/aide/datenverarbeitung-benutzernamen-uebertragen'
seo:
    title: 'Transfert des noms d’utilisateurs avec SeaTable'
    description: 'Transférez automatiquement des noms d’utilisateurs dans des champs texte pour rapports, listes et intégration de processus.'
---

La fonction de traitement des données permet d'effectuer diverses opérations sur une colonne. Le **transfert de noms d'utilisateurs** est une opération qui permet de copier des données de colonnes de type [Collaborateur]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}}), [Créateur]({{< relref "help/base-editor/spaltentypen/die-spalten-ersteller-und-erstelldatum" >}}) ou [Dernier éditeur]({{< relref "help/base-editor/spaltentypen/die-spalten-letzter-bearbeiter-und-bearbeitungsdatum" >}}) dans une [colonne de texte]({{< relref "help/base-editor/spaltentypen/die-text-spalte" >}}).

## Mise en place de l'opération

![Création d'une action de traitement des données](images/create-an-data-processing-action-1.jpg)

1. Ouvrez n'importe quel **tableau** et cliquez sur les **trois points** dans les options d'affichage.
2. Cliquez sur **Traitement des données**, puis sur **Ajouter une opération de traitement des données**.
3. Donnez un **nom** à l'opération et sélectionnez **Transférer le nom d'utilisateur**.

![Désignation de l'action de traitement des données et sélection du type d'opération](images/select-operation-and-name-example-name.jpg)

5. Définir le **tableau**, la **vue**, la **colonne source** et **la colonne résultat**.

![Définition du tableau, de la vue, de la colonne source et de la colonne résultat de l'opération](images/define-table-view-and-columns-example-name.png)

7. Cliquez sur **Enregistrer** pour sauvegarder l'action et l'exécuter plus tard, ou sur **Exécuter** pour l'exécuter directement.

Lors de la première exécution réussie, une petite icône apparaît dans la marge inférieure gauche. **crochet vert**.  
![Si la première exécution de l'action de traitement des données est réussie, une coche verte apparaît.](images/gruener-haken-zur-bestaetigung-der-ersten-ausfuehrung.jpg)

## Exécution de l'opération

Par exemple, si vous gérez un tableau de tâches à effectuer dans lequel les **membres de votre équipe** sont saisis en tant que personnes de contact responsables dans une [colonne de collaborateurs]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}}), vous pouvez simplement copier les noms d'utilisateur dans une [colonne de texte]({{< relref "help/base-editor/spaltentypen/die-text-spalte" >}}), par exemple pour les utiliser dans une liste de collaborateurs.

Pour ce faire, suivez les étapes décrites ci-dessus et sélectionnez la colonne des collaborateurs comme **colonne source** et la colonne de texte comme **colonne de résultats**.

![Définition de l'action de traitement des données](images/name-operation-and-define-columns-example-name-1.png)

Si l'opération est effectuée avec succès, les **noms d'utilisateur sélectionnés** sont extraits de la colonne des collaborateurs et transférés dans la colonne de texte, séparés par une virgule.

![Transfert des noms d'utilisateur dans une colonne de texte ou de résultats](images/table-after-operation-example-user-name.png)

{{< warning  headline="Remarque importante"  text="Veuillez noter qu'à chaque nouvelle exécution de cette opération, les entrées existantes dans la colonne des résultats seront **écrasées** si les noms d'utilisateur dans la colonne source ont changé." />}}
