---
title: 'Conseils pour travailler avec des formules'
date: 2023-05-03
lastmod: '2023-09-21'
categories:
    - 'formeln'
author: 'nsc2'
url: '/fr/aide/conseils-formules-seatable'
aliases:
    - '/fr/aide/tipps-zum-arbeiten-mit-formeln'
seo:
    title: 'Conseils pour utiliser les formules dans SeaTable'
    description: 'Astuces pour les formules SeaTable : sauts de ligne, aide syntaxique, couleurs, parenthèses, planification et gestion des erreurs.'

---

Vous trouverez ici des aides et des conseils qui vous faciliteront le travail avec les formules de Seatable. Vous trouverez [ici]({{< relref "help/base-editor/formeln/formelreferenz" >}}) une liste de toutes les formules disponibles.

## Utiliser les espaces et les retours à la ligne

N'hésitez pas à utiliser des **espaces** et **des sauts de ligne** lorsque vous créez des formules. Ceux-ci vous aident à garder une vue d'ensemble des différentes fonctions et autres éléments, en particulier dans les formules complexes.

Vous pouvez placer des espaces et des sauts de ligne presque comme vous le souhaitez dans l'**éditeur de formules**. Seule l'utilisation de **fonctions** exige de la prudence. Il ne faut **pas** mettre d'espace juste **après** une fonction, par exemple _lower()_.

### Exemple d'application

![Les espaces et les retours à la ligne peuvent être placés presque n'importe où dans l'assistant de formules. La seule exception concerne les fonctions.](images/benutzen-Sie-leerzeichen-und-spaltenumbrueche.png)

## Utiliser la syntaxe dans l'éditeur de formules

Lorsque vous cliquez dans l'éditeur de formules sur un **élément** que vous souhaitez ajouter à votre formule, des informations utiles s'affichent. Juste sous le nom de l'élément sélectionné, vous voyez, outre une brève description de son **fonctionnement**, une **syntaxe** possible et un **exemple** concret de ce à quoi il pourrait ressembler dans une formule. Lors de l'écriture de formules plus complexes, ces **informations** peuvent être utiles pour éviter des erreurs ou des incertitudes.

![Informations sur un élément dans l'assistant de formules](images/Informationen-zu-einem-Element.png)

## Respecter les couleurs des différents éléments de la formule

Pour pouvoir distinguer les différents éléments de votre formule, ceux-ci sont marqués d'une **couleur** différente selon leur type. Vous pouvez lire [ici]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}}#klare-farbsprache-zur-orientierung) quels éléments sont représentés dans quelle couleur.

Aidez-vous des différentes **couleurs** afin d'avoir une meilleure vue d'ensemble de votre formule. En outre, dans deux cas, la mise en évidence des éléments de la formule par des couleurs peut également faire office d'**autocontrôle** :

- **Les éléments de texte** ne sont pas marqués en **rouge** dans votre formule tant qu'ils ne sont pas placés entre **guillemets**.
- **Les références aux colonnes** ne sont marquées en **violet** dans votre formule que lorsqu'elles sont entourées d'**accolades**.

Si les éléments de formule mentionnés **ne sont pas** marqués dans la **couleur** correspondante dans votre formule, vous les avez saisis **de manière erronée**. Pour les corriger, utilisez la syntaxe.

## Respecter la mise en évidence des parenthèses qui vont ensemble

**Les parenthèses associées** sont **mises en évidence** dans l'éditeur de formules dès que vous cliquez sur une parenthèse ouvrante ou fermante. Cela vous permet de repérer plus facilement les parenthèses **manquantes** ou **incorrectes**.

![Les parenthèses ouvrantes et fermantes sont toujours mises en évidence dans l'éditeur de formules.](images/example-brackets.png)

## Planifier des formules

La logique et la construction d'une formule peuvent parfois être un défi. Un exercice utile ici est d'écrire en langage simple quel objectif vous voulez concrètement atteindre.

Une manière optimale de planifier une formule pourrait par exemple ressembler à ceci :

1. Commencez par écrire avec vos propres mots l'**objectif** que vous souhaitez atteindre avec la formule (par exemple, calculer les jours restants avant un événement).
2. Cherchez une **fonction** appropriée dans l'éditeur de formules (par ex. dateDif).
3. Utilisez la **syntaxe** de la fonction pour vérifier qu'elle est correctement écrite – par exemple dateDif(date de début, date de fin, unité).
4. Écrivez la **formule** dans le champ de texte prévu à cet effet dans l'éditeur de formules. Utilisez **les sauts de ligne** et **les espaces** pour rendre la logique de votre formule plus visible. Il peut être utile, surtout au début, de n'écrire que des parties d'une formule et de la compléter ensuite au fur et à mesure avec d'autres éléments.
5. Prêtez attention aux éventuels **messages d'erreur**. S'il en apparaît, essayez d'abord de les corriger vous-même en contrôlant la formule à l'aide de la syntaxe. Si vous avez besoin d'aide supplémentaire, consultez notre article d'aide sur [les erreurs typiques lors de l'utilisation de formules]({{< relref "help/base-editor/formeln/typische-fehler-beim-arbeiten-mit-formeln" >}}).
