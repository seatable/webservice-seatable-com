---
title: "Erreurs typiques lors de l'utilisation de formules"
date: 2023-05-03
lastmod: '2023-05-03'
categories:
    - 'formeln'
author: 'nsc2'
url: '/fr/aide/erreurs-formules-seatable'
aliases:
    - '/fr/aide/typische-fehler-beim-arbeiten-mit-formeln'
seo:
    title: 'Erreurs fréquentes avec les formules dans SeaTable'
    description: 'Identifiez et corrigez les erreurs fréquentes dans les formules SeaTable : placez correctement guillemets, parenthèses, virgules et références.'

---

La [colonne de formules]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}}) vous ouvre de nombreuses possibilités pour travailler avec vos données. Les formules vous permettent par exemple de mettre en relation les valeurs de différentes colonnes et d'effectuer des calculs avec celles-ci. Toutefois, comme le travail avec des formules complexes peut s'avérer difficile, surtout au début, nous vous proposons dans cet article des **solutions aux problèmes les plus connus**.

## Absence de guillemets autour des éléments de texte

Chaque élément de texte de vos formules **doit** impérativement être placé entre guillemets pour être reconnu par l'éditeur de formules. Si un texte **n'est pas** placé entre guillemets, le **message d'erreur** suivant peut apparaître :

![Message d'erreur qui apparaît lorsque des guillemets manquent autour d'éléments de texte](images/Fehlermeldung-fehlende-Anfuehrungszeichen-bei-Textelementen.png)

#### Saisie incorrecte :

![Saisie incorrecte d'éléments de texte](images/fehlerhafte-eingabe-anfuehrungszeichen.png)

#### Saisie correcte :

![Saisie correcte d'éléments de texte](images/richtige-eingabe-anfuehrungszeichen.png)

{{< warning  headline="Conseil"  text="Les éléments de texte sont toujours marqués en **rouge** dans une formule et peuvent ainsi être distingués des autres éléments. Si un élément de texte **n'est pas** marqué en **rouge** dans l'éditeur de formules, cela signifie qu'il a été saisi **de manière incorrecte**." />}}

## Les parenthèses des fonctions sont manquantes ou mal placées

Dans l'éditeur de formules, **chaque fonction** doit d'abord être suivie d'une **parenthèse ouvrante** avant que vous n'ajoutiez d'autres éléments. Une fois que vous avez ajouté tous les éléments d'une fonction à la formule, celle-ci doit en outre se terminer par une **parenthèse fermante**. Si **aucune** parenthèse n'est placée, l'éditeur de formules ne peut **pas** reconnaître la fonction et les messages d'erreur suivants peuvent apparaître :

![Message d'erreur qui apparaît lorsqu'aucune parenthèse ouvrante n'est placée après une fonction](images/Fehlermeldung-bei-fehlender-Klammer-nach-einer-Funktion.png)

![Message d'erreur qui apparaît lorsque les parenthèses d'une fonction sont mal placées](images/fehlermeldung-klammern-bei-funktion-falsch-gesetzt.png)

#### Saisie incorrecte :

![Saisie incorrecte d'une fonction](images/fehlerhafte-eingabe-funktion-1.png)

#### Saisie correcte :

![Saisie correcte d'une fonction](images/korrekte-eingabe-funktion-1.png)

{{< warning  headline="Conseil"  text="Les fonctions sont toujours marquées en **bleu** dans une formule. Si vous cliquez sur une parenthèse ouvrante ou fermante dans l'éditeur de formules, **la parenthèse correspondante est mise en évidence**. Cela vous permet de repérer plus facilement les parenthèses manquantes ou incorrectes lors de la saisie de fonctions." />}}

## Placement incorrect des parenthèses et accolades en général

Le placement correct des parenthèses et des accolades est l'un des plus grands défis lors de la saisie de formules. Qu'il s'agisse de **parenthèses ou d'accolades**, elles doivent toujours être placées au **bon endroit** dans une formule pour que celle-ci soit reconnue par l'éditeur de formules.

### Parenthèses

La **section précédente** de cet article vous explique comment placer correctement les parenthèses lors de la saisie de fonctions.

### Accolades

Vous utilisez les accolades lorsque vous souhaitez faire référence à certaines **colonnes du tableau**. Le **nom** de la colonne souhaitée doit toujours être entouré de **deux accolades**. Si **aucune** accolade n'est placée ou si les accolades sont **incorrectes**, l'éditeur de formules ne peut **pas** reconnaître la référence à la colonne et les messages d'erreur suivants peuvent apparaître :

![Message d'erreur qui apparaît si aucune accolade n'est placée lors de la référence à des noms de colonnes](images/fehlermeldung-keine-geschweiften-klammern.png)

![Message d'erreur qui apparaît lorsque les accolades sont mal placées lors de la référence à des noms de colonnes](images/fehlermeldung-geschweifte-klammern-falsch-gesetzt-1.png)

#### Saisie incorrecte :

![Saisie incorrecte des accolades lors de la référence à des noms de colonnes](images/fehlerhafte-eingabe-geschweifte-klammern-1.png)

#### Saisie correcte :

![Saisie correcte des accolades lors de la référence à des noms de colonnes](images/korrekte-eingabe.geschweifte-klammern.png)

### Références à des colonnes dans les fonctions

Si vous souhaitez faire référence à des noms de colonnes au sein d'une fonction, vous devez faire particulièrement attention au placement correct des parenthèses et des accolades. Respectez les règles propres aux fonctions et aux références de colonnes. Si vous n'êtes pas sûr qu'une paire de parenthèses ou d'accolades soit complète, n'oubliez pas que le second signe est toujours mis en évidence lorsque vous cliquez sur l'un des deux dans l'éditeur de formules.

#### Saisie incorrecte :

![Saisie incorrecte d'une fonction avec une référence de colonne](images/fehlerhafte-eingabe-einer-funktion-mit-spaltenverweis.png)

#### Saisie correcte :

![Saisie correcte d'une fonction avec une référence de colonne](images/korrekte-eingabe-einer-funktion-mit-spaltenverweis.png)

## Enchaîner plusieurs fonctions

Si vous souhaitez intégrer **plusieurs fonctions** dans votre formule, vous devez veiller à toujours séparer les différentes fonctions par une **virgule**.

De plus, vous devez terminer les formules qui contiennent plusieurs fonctions par **plusieurs parenthèses fermantes**. Si votre formule contient par exemple trois fonctions, elle doit également se terminer par trois parenthèses fermantes dans l'éditeur de formules.

Si ces points ne sont **pas** respectés, l'éditeur de formules ne peut **pas** reconnaître la formule saisie et les messages d'erreur suivants peuvent apparaître :

![Message d'erreur qui apparaît lorsqu'une formule contenant plusieurs fonctions ne se termine pas par le nombre requis de parenthèses fermantes](images/fehlermeldung-zu-weinge-klammern-am-ende-der-formel.png)

![Message d'erreur qui apparaît lorsqu'aucune virgule n'est placée entre les différentes fonctions d'une formule ou lorsque les virgules sont mal placées](images/fehlermeldung-falsche-kommasetzung.png)

#### Saisie incorrecte :

![Saisie incorrecte d'une formule dans laquelle plusieurs fonctions ont été enchaînées](images/fehlerhafte-eingabe-einer-formel-mit-mehreren-funktionen.png)

#### Saisie correcte :

![Saisie correcte d'une formule dans laquelle plusieurs fonctions ont été enchaînées](images/korrekte-eingabe-formel-mit-mehreren-funktionen.png)

{{< warning  headline="Conseil"  text="Pour les formules plus complexes, travaillez toujours avec **des espaces et des retours à la ligne**, afin de pouvoir examiner séparément les différentes fonctions de votre formule et de repérer plus facilement les erreurs." />}}

## Concaténer plusieurs éléments de texte dans une formule

Pour concaténer plusieurs éléments de texte dans votre formule, vous devez séparer les différents éléments de texte par un **symbole &**. Si **aucun symbole &** n'est ajouté entre les éléments de texte, l'éditeur de formules ne peut **pas** reconnaître la formule saisie et le message d'erreur suivant apparaît :

![Message d'erreur qui apparaît lorsque plusieurs éléments de texte dans une formule ne sont pas séparés par &.](images/Fehlermeldung-bei-fehlendenen-zwischen-Textelementen.png)

#### Saisie incorrecte :

![Saisie incorrecte de plusieurs éléments de texte dans une formule](images/fehlerhafte-Eingabe-mehrere-Textelemente.png)

#### Saisie correcte :

![Saisie correcte de plusieurs éléments de texte dans une formule](images/korrekte-Eingabe-mehrere-Textelemente.png)

{{< warning headline="Conseil" text="Pour que les différents éléments de texte soient séparés par une espace, insérez **deux symboles &** et **deux guillemets (en haut)** entre chacun des éléments de texte." />}}

![Modification de la formule afin que les éléments de texte soient séparés par une espace](images/Leerzeichen-zwischen-Textelementen.png)
