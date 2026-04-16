---
title: 'La formule de recherche'
date: 2022-10-13
lastmod: '2023-04-06'
categories:
    - 'verknuepfungen'
author: 'vge'
url: '/fr/aide/colonne-lookup-seatable'
aliases:
    - '/fr/aide/die-lookup-funktion'
seo:
    title: 'Colonne lookup : valeurs multi-tables dans SeaTable'
    description: 'Affichez aisément des données provenant de tables liées avec la colonne lookup SeaTable – zéro redondance, tout est connecté.'

---

La fonction Lookup vous permet d'afficher des valeurs supplémentaires d'un tableau déjà liée dans votre tableau actuelle. Cela vous évite de devoir saisir les données deux fois et vous permet en même temps de mettre les données en relation les unes avec les autres. Dans Excel, cette fonction est connue sous le nom de _VLOOKUP_ ou _SVERWEIS_.

## Quand a-t-on besoin de la formule de recherche ?

La fonction de recherche devrait être utilisée chaque fois que vous souhaitez faire des références croisées à des informations stockées dans différents tableaux. Supposons que vous utilisiez SeaTable pour la [gestion de projets]({{< relref "pages/landing-pages/industry-solutions/project-management" >}}), les projets étant stockés dans un tableau et les tâches associées au projet dans un autre tableau. Chaque projet est alors lié à une série de tâches.

![Lien entre les tâches d'un projet](images/linked-tables-seatable.png)

En tant que chef de projet, vous souhaitez peut-être afficher des informations sur les tâches associées à chaque projet. La formule de recherche peut être utilisée pour sélectionner une colonne dans le tableau lié et afficher ses valeurs. Vous pouvez par exemple afficher automatiquement les collaborateurs du projet qui sont responsables de chaque tâche.

![Colonne de recherche](images/lookup-columns.png)

Cela peut être utile pour accéder facilement à des informations inter-tables, pour mettre en place des automatisations, des formules, etc. Vous trouverez ci-dessous plus d'informations sur l'utilisation de la fonction Lookup.

## Comment utiliser la colonne Lookup

### Ajouter un lien de tableau

La fonction Lookup ne peut être utilisée que s'il existe déjà une colonne de type _lien vers d'autres entrées_. Si vous ne disposez pas encore d'une telle colonne, commencez par en créer une. Pour savoir comment cela fonctionne, [cliquez ici]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}}).

### Ajouter une formule de recherche

Au début, la formule de recherche peut vous dérouter. Mais vous verrez qu'en peu de temps, vous adorerez cette fonction de colonne incroyablement polyvalente et puissante. Voici comment ajouter une colonne avec la formule de recherche :

![Configurer une colonne de recherche](images/setup-of-lookup-column.gif)

1. Créez une nouvelle colonne de type **Formule pour les liens**.
2. Définissez l'option **Lookup** comme formule.
3. Sélectionnez une **colonne de liens**. Ce champ est automatiquement rempli correctement si vous n'avez qu'une seule colonne de liens.
4. Avec la **colonne de référence dans le tableau lié**, vous déterminez de quelle colonne de l'autre tableau les valeurs doivent être reprises.
5. Cliquez sur **Envoyer**.

## Questions fréquentes sur la colonne de recherche

{{< faq "Est-il possible de récupérer plusieurs valeurs dans un tableau par lookup ?" >}}Sans aucun doute. Créez simplement une autre colonne et utilisez à nouveau la fonction Lookup. Vous pouvez ainsi lire et afficher autant d'informations que vous le souhaitez à partir du tableau lié.
{{< /faq >}}
{{< faq "Les lookups peuvent-ils être modifiés ultérieurement ?" >}}C'est bien sûr possible. Cliquez sur l'**icône en forme de triangle** à droite du nom de la colonne, puis sur **Personnaliser le type de colonne**. Adaptez les paramètres de la colonne et les informations souhaitées s'affichent immédiatement.
{{< /faq >}}
{{< faq "Les lookups fonctionnent-ils en cas de liens multiples ?" >}}Chaque formule de recherche ne peut récupérer que les informations d **'une seule** colonne de vos tableaux liés. Mais vous pouvez bien sûr utiliser des colonnes de liaison pour lier plusieurs tableaux et créer d'autres colonnes de lookup pour extraire et afficher encore plus d'informations.
{{< /faq >}}
{{< faq "Les entrées consultées par lookup peuvent-elles être filtrées ?" >}}Oui, vous pouvez filtrer les entrées comme vous le souhaitez. Pour ce faire, activez le **Régulateur** dans les _Paramètres des colonnes_ et sélectionnez la **Colonne(s)** dont les entrées doivent être recherchées. Vous pouvez sélectionner autant de **Conditions de filtrage** définir.

{{< /faq >}}
