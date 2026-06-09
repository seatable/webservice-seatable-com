---
title: 'La colonne des formules'
date: 2023-01-28
lastmod: '2023-09-14'
categories:
    - 'formeln'
author: 'ssc'
url: '/fr/aide/colonne-formule-seatable'
aliases:
    - '/fr/aide/grundlagen-von-seatable-formeln'
    - '/fr/aide/die-formel-spalte'
seo:
    title: 'Colonne de formule SeaTable : fonctions et astuces'
    description: 'Utilisez la colonne de formule SeaTable pour calculs, texte ou logiques : tout savoir sur les opérations dans chaque ligne.'
weight: 17
---

SeaTable offre de nombreuses fonctions différentes que vous pouvez ajouter à votre tableau. L'une d'entre elles est la **colonne des formules**. Les formules vous permettent de combiner les valeurs de différentes colonnes et de créer différentes fonctions basées sur les types de données de ces colonnes. Vous pouvez, entre autres, calculer, fusionner ou mettre en relation les valeurs d'une ligne.

{{< warning  headline="SeaTable ne permet pas le référencement libre comme dans Excel"  text="Dans Excel, il est possible de faire référence à n'importe quelle cellule dans une formule. Dans SeaTable, cela n'est **pas** possible. Une formule ne peut toujours travailler qu'avec les **valeurs de la même ligne**." />}}

## Création d'une colonne de formules

Pour appliquer une formule, vous devez d'abord ajouter une nouvelle colonne de formule à votre tableau. Pour savoir comment faire, [cliquez ici]({{< relref "help/base-editor/spalten/hinzufuegen-einer-spalte" >}}).

![Sélection d'une colonne de formules](images/select-formula-column.png)

SeaTable propose un **éditeur de formules** pour faciliter la saisie des formules.

![Assistant de formule pour simplifier la saisie de formules, surtout complexes](images/Formula.wizard.png)

## Écrire une première formule

Dès que votre colonne de formules est créée, vous pouvez commencer à écrire la formule. L'illustration suivante montre une formule simple pour calculer la moyenne de cinq nombres.

![Saisie de n'importe quelle formule dans le champ de texte](images/input-formular.jpg)

Cette formule écrit toujours comme résultat la valeur statique _13.2_ dans la colonne de formule. La véritable force de la colonne de formules n'est toutefois mise en valeur que si vous utilisez les valeurs d'autres colonnes pour votre formule. Avec le **{nom de la colonne}** entre accolades, vous pouvez faire référence à des colonnes existantes dans votre tableau.

{{< warning headline="Ajouter des colonnes à la formule" text="Les noms de colonnes dans le tableau ouvert sont affichés à gauche dans l'éditeur de formules et peuvent être modifiés à l'aide d'un **Double clic** peut être inséré dans la formule." />}}

![Colonnes disponibles dans l'éditeur de formules](images/columns-in-the-formula-editor.jpg)

Vous pouvez ensuite insérer certaines **constantes**, **opérandes** et **fonctions** dans votre formule pour calculer, fusionner ou mettre en relation les valeurs des différentes colonnes.

## Un langage des couleurs clair

Pour pouvoir distinguer les différents éléments de votre formule, ceux-ci sont marqués d'une **couleur** différente selon leur type :

| Objet                   | Exemple                                                                                                                        |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| Fonctions               | ![Les fonctions sont toujours marquées en bleu dans une formule](images/example-function.png)                                  |
| Texte / Chaîne          | ![Les textes et les chaînes de caractères sont toujours marqués en rouge dans l'éditeur de formules.](images/example-text.png) |
| Chiffres                | ![Les nombres sont toujours marqués en vert dans l'éditeur de formules](images/example-number.png)                             |
| Références des colonnes | ![Les références de colonne sont toujours marquées en violet dans une formule ](images/example-reference-to-column.png)        |

{{< warning headline="Les parenthèses associées sont mises en évidence" text="Lorsque vous cliquez sur une parenthèse ouvrante ou fermante dans l'éditeur de formules, la parenthèse correspondante est également mise en évidence. Cela vous permet de repérer plus facilement les remplacements de parenthèses manquants ou incorrects." />}}

![Les parenthèses ouvrantes et fermantes sont toujours mises en évidence dans l'éditeur de formules.](images/example-brackets.png)

## Exemples de formules

Vous trouverez ci-dessous quelques exemples qui illustrent l'utilité et l'utilisation des formules.

- [Exemple de formule : multiplication simple par une formule]({{< relref "help/base-editor/formeln/formelbeispiel-einfache-multiplikation-mit-einer-formel" >}})
- [Exemple de formule : fusionner des colonnes de texte à l'aide d'une formule]({{< relref "help/base-editor/formeln/formelbeispiel-zusammenfuehren-von-text-spalten-mit-hilfe-einer-formel" >}})
- [Exemple de formule : opérateurs logiques If pour comparer des valeurs]({{< relref "help/base-editor/formeln/formelbeispiel-logische-if-operatoren-zum-vergleichen-von-werten" >}})
- [Exemple de formule : Calculer la durée d'un congé]({{< relref "help/base-editor/formeln/formelbeispiel-berechne-die-dauer-eines-urlaubs" >}})
- [Exemple de formule : calculer les jours jusqu'à un événement]({{< relref "help/base-editor/formeln/formelbeispiel-berechne-tage-bis-zu-einem-event" >}})
- [Exemple de formule : Rechercher un mot dans un texte]({{< relref "help/base-editor/formeln/formelbeispiel-nach-einem-wort-in-einem-text-suchen" >}})

## Les conventions mathématiques s'appliquent aussi à SeaTable

Vous pouvez bien sûr compter sur le fait que les conventions mathématiques sont également utilisées dans les formules de SeaTable. Voici les exemples les plus importants :

- **Les fonctions** peuvent être **imbriquées** les unes dans les autres à l'aide de parenthèses. Exemple : (( 1 + 2 ) \* 3)
- Le **point avant le tiret**, l'**ordre des parenthèses** et d'autres **règles mathématiques** sont pris en compte dans SeaTable.

## Mise en forme de la colonne de formules

Vous pouvez formater les résultats dans la colonne des formules. Chaque formule de SeaTable a pour résultat un **nombre**, une **date** ou un **texte/une chaîne de caractères**. Vous disposez donc de différents **paramètres de formatage** selon le cas.

![Mise en forme des résultats de formules](images/Formatierung-von-Formelergebnissen.jpg)
