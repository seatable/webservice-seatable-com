---
title: "Mise en forme à l'aide de Markdown / texte enrichi"
date: 2023-05-11
lastmod: '2023-08-21'
categories:
    - 'text-und-zahlen'
author: 'nsc2'
url: '/fr/aide/markdown-texte-enrichi'
aliases:
    - '/fr/aide/formatierungen-mithilfe-von-markdown-rich-text'
seo:
    title: 'Markdown et texte enrichi : Misez sur la mise en forme SeaTable'
    description: 'Découvrez comment utiliser Markdown et le texte enrichi dans SeaTable : titres, listes, code et bonnes pratiques pour structurer au mieux vos informations.'
---

[Markdown](https://en.wikipedia.org/wiki/Markdown) est un langage de balisage très simplifié utilisé pour **mettre en forme des textes**. SeaTable utilise Markdown à différents endroits pour mettre en forme des textes longs de manière visuellement attrayante.

Vous n'êtes pas obligé de vous familiariser avec la syntaxe de Markdown. Mais que vous utilisiez Markdown pour la première fois ou que vous ayez déjà de l'expérience, cet article vous aidera à mieux comprendre où et comment utiliser la version SeaTable de Markdown.

## SeaTable Markdown

Actuellement, il existe cinq domaines dans lesquels vous pouvez utiliser la syntaxe Markdown dans SeaTable. Il s'agit de :

- Colonnes de type [Texte formaté]({{< relref "help/base-editor/spaltentypen/die-spalten-text-und-formatierter-text" >}})
- [Descriptions de la base]({{< relref "help/base-editor/weitere-optionen/wie-man-einer-base-eine-beschreibung-hinzufuegt" >}})
- Textes d'e-mails lors de l'envoi via [des automatisations]({{< relref "help/base-editor/schaltflaechen/eine-e-mail-per-schaltflaeche-verschicken" >}})
- [Formulaires web]({{< relref "help/base-editor/webformulare/webformulare" >}})
- [Apps]({{< relref "help/app-builder/app-verwaltung/universelle-app" >}})

Dès que Markdown est utilisé dans SeaTable, le masque de saisie suivant vous est proposé. Vous pouvez bien sûr sélectionner des mots ou des blocs de texte comme d'habitude, puis choisir la mise en forme souhaitée.

![Markdown dans SeaTable](images/markdown-seatable.png)

Vous pouvez également déclencher directement le formatage Markdown en saisissant certains caractères spéciaux. Il suffit de taper dans un champ de saisie Markdown un {{< key "#" >}} suivi d'un mot. Vous verrez que dans la syntaxe Markdown, le dièse correspond à un premier titre. Ainsi, si vous savez quel caractère spécial déclenche quel formatage, vous pouvez saisir et formater vos textes beaucoup plus rapidement.

Actuellement, vous ne pouvez déclencher qu'une partie du formatage par un caractère spécial. Vous découvrirez dans cet article quels sont ces caractères.

{{< warning  headline="Qu'est-ce que SeaTable Markdown"  text="Même si l'on parle volontiers d'une syntaxe Markdown _unique_, il en existe en fait plusieurs variantes. SeaTable prend en charge les principales mises en forme permettant de créer des textes visuellement attrayants." />}}

## Déclencher le formatage syntaxique dans SeaTable par des caractères spéciaux

Actuellement, SeaTable permet d'activer les options de syntaxe suivantes par des caractères spéciaux.

### Titres

Une ligne commençant par un à trois {{< key "#" >}}\-suivi d'un espace, donne un **Titre** du premier au troisième niveau.

**Syntaxe Markdown**

\# En-tête de premier niveau  
\## Second level header  
\### En-tête de troisième niveau

**Résultat**

![Résultat de la syntaxe Markdown Titres](images/syntax-headings-richtext-markdown-1.png)

### Gras et italique

Texte rédigé par un {{< key "\*" >}} ou {{< key "\_" >}} couple est entouré **en italique** formaté (ce qui, en Markdown, signifie une emphase) ; le texte qui est accompagné d'un double {{< key "\*\*" >}} ou {{< key "\_ \_" >}} couple est entouré **gras** (ce qui signifie une forte accentuation en Markdown). Les mises en forme peuvent également être combinées avec d'autres formats en ligne.

**Syntaxe Markdown**

\*Ce texte sera en italique\*  
\_Ce sera aussi en italique

\*\*This text will be bold\*\*.  
\_\_This will also be bold\_\_

\_\*\*Combine them for bold italic\*\*\_

**Résultat**

_Ce texte sera en italique_  
_Ce sera aussi en italique_

**Ce texte sera en gras**  
**Ce texte sera également en gras**

_**Combinez-les pour obtenir un italique gras**_

### Liste non triée

Vous pouvez soit {{< key "\-" >}} ou {{< key "\*" >}} comme marqueur d'une **liste non triée** utiliser.

![Résultat de la syntaxe Markdown Liste non triée](images/result-unordered-list-syntax-1.png)

### Liste triée

Si une ligne commence par un {{< key "1." >}}elle est automatiquement transformée en une **liste triée** transformé.

1\. item 1  
2ème item 2

### Citations en bloc

Un **Citation en bloc** est une ligne qui commence par {{< key "\>" >}} suivie du contenu de la citation. Les citations sont signalées par une indentation et un cadre dans la marge de gauche.

![Citation de Markdown](images/markdown-cite.png)

### Code en ligne

Texte rédigé par un {{< key "FIXME: backtick" >}} couple est représenté sous forme de code en ligne. Ainsi, de **apiKey est votre jeton secret API** le formatage suivant :

![Résultat de la syntaxe Markdown Code en ligne](images/result-inline-code.png)

### Blocs de code

Un **Bloc de code** est déterminé par trois successives **Bâtons de cuisson** {{< key "```" >}} a été introduit. La particularité du bloc de code est que son contenu est présenté sous forme de **Code en ligne** est affiché avec une police monospace. Les indentations sont également conservées telles qu'elles sont saisies.

![Bloc de code Markdown](images/markdown-codeblock.png)

### Sauts de ligne

Chaque retour à la ligne {{< key "↵" >}} est traité comme un saut de ligne dur avec un espace entre les deux lignes. Un saut de ligne sans espace entre les différentes lignes n'est pas possible. Aussi **plusieurs retours à la ligne** à la suite sont supprimés et réduits à un simple retour à la ligne.

## Formatages que vous ne pouvez pas activer par des caractères spéciaux

**Cases à cocher** sont typiquement remplacés en Markdown par un {{< key "\[ \]" >}} ou un {{< key "\[x\]" >}} est saisie. Toutefois, cette saisie n'est pas automatiquement convertie en case à cocher. Au lieu de cela, vous devez utiliser la petite icône de case à cocher {{< seatable-icon icon="dtable-icon-check-square" >}} cliquer.

**Les hyperliens** sont également pris en charge dans SeaTable Markdown, mais ne peuvent être insérés que via l'icône {{< seatable-icon icon="icon-link" >}}.

## Formats non pris en charge

{{< key "~~strikethrough~~" >}} n'est pas pris en charge par SeaTable. Les doubles retours à la ligne sont également supprimés et un {{< key "<br>" >}} n'est pas interprété comme un saut de ligne supplémentaire.
