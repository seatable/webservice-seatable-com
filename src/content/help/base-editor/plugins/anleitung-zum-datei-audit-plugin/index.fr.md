---
title: "Instructions pour le plugin d'audit des fichiers"
date: 2026-11-26
lastmod: '2026-11-26'
categories:
    - 'plugins'
author: 'bha'
url: '/fr/aide/guide-plugin-audit-fichiers'
aliases:
    - '/fr/aide/anleitung-zum-datei-audit-plugin'
seo:
    title: "Guide du plugin d'audit des fichiers SeaTable"
    description: "Le plugin d'audit des fichiers de SeaTable repère les fichiers qu'une base n'utilise plus, les références à des fichiers manquants et ce qui occupe son stockage."
---

Le **plugin d'audit des fichiers** examine les **fichiers stockés dans votre base** : tout ce qui y a été déposé — dans les colonnes de fichiers, d'images et de signature, dans le texte mis en forme, dans les commentaires, les formulaires et les apps —, ainsi que les fichiers de vos propres dossiers personnalisés de la [gestion des fichiers]({{< relref "help/base-editor/dateien/das-dateimanagement-einer-base" >}}). Il compare ce qui se trouve dans le stockage avec ce que votre base référence réellement, et signale l'écart dans les deux sens : les **fichiers que plus personne n'utilise**, et les **références à des fichiers qui n'existent plus**. Il vous montre aussi ce qui occupe l'espace.

Dans SeaTable, le stockage se remplit naturellement, car retirer un fichier d'une cellule **ne le supprime pas** : le fichier reste dans la gestion des fichiers de la base, pour pouvoir être [restauré]({{< relref "help/haeufig-gestellte-fragen/wissen-und-tipps/zugriff-auf-geloeschte-anhaenge" >}}). Avec le temps, une base peut finir par stocker bien plus que ce que montrent ses lignes.

Le plugin ne demande aucune configuration : la première fois que vous l'ouvrez, l'audit se lance tout seul. L'audit lui-même ne modifie rien — les fichiers ne sont supprimés, et les références retirées, que lorsque vous le demandez, élément par élément ou groupe par groupe.

{{< zoom image="images/file-audit-plugin.png" alt="Le plugin d'audit des fichiers affichant le stockage d'une base par dossier et ses ressources orphelines" >}}

Pour savoir comment activer un plugin dans une base, [cliquez ici]({{< relref "help/base-editor/plugins/aktivieren-eines-plugins-in-einer-base" >}}).

## Comment fonctionne l'audit {#how-the-audit-works}

Un audit fait trois choses :

1. Il **fait l'inventaire du stockage de la base** : chaque fichier, avec son dossier et sa taille.
2. Il rassemble tous les fichiers que la base **référence**, où qu'ils soient utilisés :
    - les **colonnes de fichiers et d'images** de chaque tableau, ainsi que les **signatures** des colonnes de signature,
    - les images insérées dans les cellules de **texte mis en forme**,
    - les images de la **description de la base** et des **commentaires des lignes**,
    - les images des **formulaires web** de la base et des formulaires de ses **apps**,
    - les **lignes archivées**, qui sont lues comme les autres.
3. Il examine les **autres bases auxquelles vous avez accès**, pour y trouver des lignes qui affichent des fichiers stockés dans cette base (voir [Fichiers partagés entre bases](#files-shared-between-bases) ci-dessous).

Il compare ensuite ces listes et affiche le résultat. L'audit s'exécute avec **vos propres droits** — aucun jeton à créer — et le rapport est enregistré avec la base : quand vous rouvrez le plugin, vous retrouvez le dernier résultat, avec sa date, au lieu d'un nouvel audit. Le bouton **Relancer l'audit** en lance un nouveau, ce qu'il faut faire après chaque modification.

{{< warning type="warning" headline="Les scripts ne sont pas audités" text="Les **scripts** de la base sont stockés comme des fichiers à part entière, mais le plugin ne les voit pas du tout : comme dans la gestion des fichiers, ils n'apparaissent pas dans l'arborescence des ressources de la base, leur taille n'est pas comptée, et **leur contenu n'est pas lu** — un fichier utilisé par un script n'est pas considéré comme référencé. Les scripts font pourtant bien partie des ressources de la base : lors d'un export, **ils ne sont conservés que si l'option *Inclure les pièces jointes* est activée**." />}}

## Ce que le plugin signale

### Synthèse et stockage par dossier

Le haut du rapport fait la synthèse : le **total des ressources en stockage**, combien sont **référencées dans la base**, combien sont **orphelines** et la part du stockage qu'elles représentent, puis le nombre de **références manquantes** et d'**URL externes**.

**Stockage par dossier** montre ce qui occupe l'espace. Cliquez sur un dossier pour l'explorer. Vos propres dossiers (**dossiers personnalisés**) sont présentés séparément des **dossiers système**, que SeaTable crée pour les colonnes de fichiers et d'images, les signatures, les formulaires et les apps. Certains dossiers système contiennent des fichiers dont SeaTable a besoin pour faire fonctionner la base, et qu'aucune ligne ne référence par nature — les fichiers des plugins, les pages et les paramètres de chaque app, les logos et images d'arrière-plan des formulaires, et les modèles du plugin de conception de pages : ils portent la mention **Dossier système — NE PAS SUPPRIMER**, et ne sont jamais listés comme orphelins. Les fichiers que les utilisateurs déposent via une app sont en revanche audités comme n'importe quel autre fichier.

### Ressources orphelines {#orphaned-assets}

Une **ressource orpheline** est un fichier du stockage qu'aucune ligne ne référence plus — en général un fichier dont la référence a été retirée d'une cellule, ou un fichier conservé après la suppression d'une ligne. La liste est regroupée par dossier : vous pouvez supprimer un seul fichier, ou tous les fichiers orphelins d'un dossier à la fois.

Si l'un des emplacements listés [plus haut](#how-the-audit-works) **n'a pas pu être lu** lors d'un audit — les commentaires ou les lignes archivées, par exemple —, la section l'indique et **la suppression est désactivée** pour cet audit : sans cela, tous les fichiers utilisés uniquement à cet endroit vous seraient proposés à la suppression. Relancez l'audit pour réessayer.

Avant de supprimer quoi que ce soit, lisez les avertissements de cette section et les [limites](#limitations) ci-dessous : un fichier orphelin est un fichier *pour lequel le plugin n'a trouvé aucune référence*, ce qui n'est pas tout à fait la même chose qu'un fichier dont personne n'a besoin.

{{< warning type="warning" headline="Les fichiers supprimés vont dans la corbeille" text="Les fichiers que le plugin supprime vont dans la **corbeille** de la gestion des fichiers, où ils restent **60 jours** et peuvent être restaurés. Passé ce délai, ou une fois la corbeille vidée, ils sont définitivement perdus : les snapshots n'incluent pas les fichiers. Pour conserver une sauvegarde complète, **exportez la base avec l'option *Inclure les pièces jointes* activée** avant de supprimer quoi que ce soit." />}}

### Références manquantes

Une **référence manquante**, c'est l'inverse : une ligne dont la colonne de fichiers ou d'images pointe vers un fichier qui **n'existe plus** dans le stockage. La cellule affiche encore une entrée, mais il n'y a plus rien derrière. Vous pouvez retirer la référence obsolète d'une ligne, de toutes les lignes d'une colonne, ou de partout à la fois. Le reste de la cellule n'est pas modifié.

### URL externes

Les colonnes d'images peuvent aussi contenir des liens vers des fichiers **hébergés en dehors de SeaTable**. Le plugin les liste, regroupés par tableau et par colonne. Ils ne sont pas vérifiés pendant l'audit, ce qui le ralentirait : lancez vous-même la vérification avec **Vérifier les URL externes**. Chaque lien est alors classé **OK**, **invalide** ou **invérifiable** — beaucoup de sites ne permettent pas à un navigateur de vérifier leurs fichiers depuis un autre site, donc *invérifiable* ne veut pas dire que le lien est cassé. Vous pouvez ensuite retirer les liens invalides.

### Fichiers partagés entre bases {#files-shared-between-bases}

Les deux dernières sections concernent les **fichiers qui passent d'une base à une autre** — un cas qui passe facilement inaperçu, et la raison pour laquelle le plugin examine vos autres bases à chaque audit.

Quand vous **copiez une cellule ou une ligne** d'une base vers une autre, SeaTable copie la référence au fichier, **pas le fichier lui-même**. Le fichier reste stocké dans la base d'origine, et l'autre base l'affiche depuis celle-ci — même si elle se trouve dans un autre espace de travail. Rien, dans aucune des deux bases, n'indique qu'elles sont désormais liées. **Importer un tableau** depuis une autre base fonctionne autrement : les fichiers sont copiés eux aussi, et les deux bases sont ensuite indépendantes. **Privilégiez cette méthode** chaque fois que vous avez besoin des fichiers dans les deux bases.

- **Fichiers utilisés par d'autres bases** liste les fichiers stockés dans *cette* base qu'affichent des lignes d'une *autre* base. Ils sont exclus de la liste des orphelins, même si plus rien dans cette base ne les référence : en supprimer un casserait l'autre base.
- **Références vers des fichiers d'autres bases** est le cas inverse : les lignes de *cette* base qui affichent un fichier stocké dans une *autre* base. Elles ne comptent ici ni comme orphelines ni comme références manquantes, et le plugin ne peut pas vérifier si ces fichiers existent encore.

Un fichier affiché de cette façon conserve les **permissions de la base qui le stocke**. Les personnes qui n'ont pas accès à cette base voient une **cellule vide** là où vous voyez le fichier — une même ligne peut donc s'afficher différemment pour deux personnes.

## Permissions et sécurité

- Avec un accès en **lecture seule** à la base, vous pouvez consulter tout le rapport, mais les boutons de suppression ne sont pas disponibles.
- Dans un **groupe** que vous n'administrez pas, vous pouvez quand même supprimer des fichiers, mais le plugin vous avertit qu'ils ont pu être déposés par d'autres membres, et vous demande une confirmation explicite.
- Avant de modifier une ligne pour la première fois — en supprimant une référence manquante ou un lien invalide —, le plugin crée un **snapshot** de la base. Il vous permet de récupérer le **contenu des cellules** que le plugin a retiré : les noms de fichiers et les liens, pas les fichiers eux-mêmes. La suppression de fichiers ne modifie aucune ligne et n'est pas couverte : les snapshots n'incluent pas les fichiers (voir l'avertissement [plus haut](#orphaned-assets)).

## Limites {#limitations}

{{< warning type="warning" headline="Seules les bases auxquelles vous avez accès sont examinées" text="La recherche de références dans d'autres bases porte sur les bases que vous voyez : celles de vos espaces de travail et de vos groupes, et celles qui sont partagées avec vous. La base d'un collègue à laquelle vous n'avez pas accès peut très bien afficher un fichier de la vôtre, sans que le plugin puisse le savoir. **Qu'un fichier apparaisse comme orphelin dans le rapport ne prouve donc jamais qu'il est inutilisé.** Les bases auxquelles vous n'avez pas accès n'apparaissent jamais dans le rapport, puisque le plugin ignore leur existence. Seules les bases que vous voyez mais que le plugin n'a pas réussi à lire lors d'un audit — à la suite d'une erreur, par exemple — sont citées dans le rapport, avec la raison." />}}

L'audit a quelques autres angles morts, à connaître avant de supprimer :

- **Seuls les emplacements listés [plus haut](#how-the-audit-works) sont lus.** Un fichier appelé d'une autre manière n'est pas reconnu comme référencé, et peut donc être listé comme orphelin — par exemple un fichier dont l'adresse est enregistrée dans une colonne de texte ou d'URL, ou utilisée dans un script ou via un outil externe (orchestrateur, etc.).
- **Vos propres dossiers sont traités comme les autres.** Un fichier que vous avez déposé dans un dossier personnalisé de la gestion des fichiers, pour l'y conserver, est listé comme orphelin tant qu'aucune ligne ne le référence.
- **Les fichiers des dossiers personnalisés ne sont pas suivis d'une base à l'autre.** Une ligne les référence par un identifiant qui n'indique pas dans quelle base ils sont stockés : le plugin ne peut donc pas savoir si une autre base en utilise un.
- **Une base créée par import ou par copie peut encore utiliser des fichiers de la base d'origine.** Quand vous importez une base depuis un fichier `.dtable` ou que vous la copiez, ses fichiers sont copiés eux aussi, mais certains emplacements gardent leurs liens vers la base d'origine — selon la façon dont la base a été créée, les images de la description de la base, des formulaires web et des formulaires d'apps, ou les fichiers des lignes archivées. Le plugin liste ces liens sous **Références vers des fichiers d'autres bases**, et les copies qu'ils laissent inutilisées dans cette base apparaissent comme orphelines. Leurs images sont chargées depuis la base d'origine, et certaines peuvent ne pas s'afficher pour d'autres personnes, même si elles ont accès à cette base. Les commentaires des lignes ne font pas non plus partie d'un export ni d'une copie : les images qui y sont insérées deviennent donc elles aussi orphelines dans la nouvelle base.
- **Le rapport décrit le moment où l'audit a été lancé.** N'importe qui peut ajouter ou retirer une référence ensuite, dans cette base ou dans une autre : relancez l'audit avant de supprimer.
- Si vous avez accès à beaucoup de bases, les examiner toutes **prend un certain temps**.

## Autres articles utiles

- [Aperçu de tous les plugins]({{< relref "help/base-editor/plugins/alle-plugins-in-der-uebersicht" >}})
- [La gestion des fichiers d'une base]({{< relref "help/base-editor/dateien/das-dateimanagement-einer-base" >}})
- [Accès aux fichiers et images supprimés]({{< relref "help/haeufig-gestellte-fragen/wissen-und-tipps/zugriff-auf-geloeschte-anhaenge" >}})
- [Comment supprimer des fichiers de façon permanente]({{< relref "help/base-editor/dateien/wie-man-dateien-dauerhaft-entfernt" >}})
- [Activer un plugin dans une base]({{< relref "help/base-editor/plugins/aktivieren-eines-plugins-in-einer-base" >}})
