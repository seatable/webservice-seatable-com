---
title: 'Annuler les modifications via les journaux'
date: 2023-01-11
lastmod: '2023-06-22'
categories:
    - 'historie-und-versionen'
author: 'kgr'
url: '/fr/aide/annuler-changements-log-seatable'
aliases:
    - '/fr/aide/aenderungen-ueber-die-logs-rueckgaengig-machen'
seo:
    title: 'Annuler les modifications via logs dans SeaTable'
    description: 'Restaurez des cellules, lignes ou colonnes dans SeaTable directement depuis les logs : méthode, limite de l’historique et conseils pratiques.'

---

SeaTable consigne toutes les activités au sein d'une base dans un journal. Celui-ci permet de restaurer non seulement des valeurs individuelles, mais aussi des lignes, des colonnes et des tableaux. Les journaux permettent donc de voir les modifications de manière plus détaillée et d'en annuler davantage que la corbeille.

## Comment ouvrir le log d'une base

Vous ouvrez les logs comme la corbeille en cliquant sur l'icône des versions dans le coin supérieur droit.

![Ouvrir les logs dans la base](images/Logs-in-der-Base-oeffnen.png)

Dans le tableau de bord qui s'ouvre, vous trouverez, **dans l'ordre antichronologique**, les modifications les plus récentes qui ont été apportées à la base. Chaque entrée de journal contient les informations suivantes :

- Nom de l'agent
- Type de modification
- Tableau concerné
- Date de la modification
- Description de la modification

![Changements dans les logs](images/Aenderungen-in-den-Logs.png)

## Charger des entrées de journal plus anciennes

Si une base fait l'objet d'un travail intensif, le journal contient un grand nombre d'entrées et il peut être nécessaire de **faire défiler le journal vers le bas**. En faisant défiler le journal vers le bas, les anciennes entrées du journal sont successivement rechargées et vous pouvez alors les parcourir.

Pour chaque base, vous pouvez consulter **au maximum les 1.000 dernières entrées** du journal. La documentation des modifications encore plus anciennes est supprimée et n'est généralement plus nécessaire.

## Filtrer les entrées de journal

Si vous souhaitez suivre ou annuler certaines modifications dans une base avec de nombreux utilisateurs, cela devient vite confus. Pour savoir qui a fait des modifications, où et quand, vous pouvez filtrer les logs par **utilisateur**, **table** et **période**. Des filtres combinés sont également possibles.

## Annuler les modifications

Vous pouvez annuler une modification en cliquant sur **Rétablir** via l'**icône à trois points** sur le bord droit de l'entrée du journal. La restauration est immédiatement effectuée dans le tableau correspondant et confirmée par un bref message.

Une action annulée reste documentée dans le journal, mais ne peut pas être exécutée à nouveau. Une tentative correspondante est confirmée par un message d'erreur.

{{< warning  headline="Remarque"  text="Il y a des actions que vous ne pouvez **pas** annuler via les logs. Il s'agit par exemple des commentaires ou des nouvelles lignes et colonnes insérées. Si vous cliquez malgré tout sur l'icône à trois points, seul **Pas d'options** apparaît au lieu de l'option Rétablir." />}}
