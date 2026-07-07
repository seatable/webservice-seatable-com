---
title: 'Étape 7 : orchestrer avec n8n'
date: 2026-07-02
lastmod: '2026-07-02'
categories:
    - 'online-kurs-4'
author: 'bha'
url: '/fr/aide/etape-7-orchestrer-avec-n8n'
aliases:
    - '/fr/aide/schritt-7-n8n'
seo:
    title: 'Étape 7 du cours SeaTable 4 : orchestrer un workflow avec n8n'
    description: 'Enchaînez SeaTable et Seafile avec n8n : archivez automatiquement chaque bon de livraison et récupérez son lien dans la base. Une étape à suivre en démonstration ou à rejouer.'
---

Un webhook envoie un message ; un script en envoie un sur mesure. Mais quand il faut **enchaîner plusieurs services** — prendre un fichier ici, le déposer là, en récupérer un lien, le réécrire ailleurs — on gagne à sortir un outil dédié : un orchestrateur. Le nôtre s'appelle n8n.

Cette étape est une démonstration : vous pouvez simplement la suivre pour voir comment ces briques s'assemblent. Si vous voulez la rejouer vous-même, un compte n8n et un compte Seafile suffisent, et nous vous fournissons le workflow tout prêt.

## Un orchestrateur de workflow

Ce type d'outil porte un nom : un **orchestrateur de workflow**. Le principe est toujours le même — vous reliez des applications entre elles sous forme d'une suite d'actions, sans écrire de code : vous configurez chaque étape, un nœud, et l'outil fait circuler les données de l'une à l'autre. Plusieurs solutions se partagent ce terrain et se ressemblent beaucoup à l'usage ; vous avez peut-être déjà croisé *Zapier* ou *Make*, qui rendent des services comparables.

Nous mettons n8n en avant pour deux raisons précises. D'abord, il est **open source** et vous pouvez l'héberger vous-même : vos données ne transitent pas forcément par un service tiers. Ensuite et surtout, c'est SeaTable qui **développe et maintient** le nœud n8n officiel — vous restez dans un écosystème que l'éditeur contrôle et documente, plutôt qu'à la merci d'un connecteur bâti par quelqu'un d'autre. Les autres outils savent aussi dialoguer avec SeaTable, le plus souvent via son API ; mais avec n8n, vous êtes en terrain maîtrisé de bout en bout.

## Le scénario : archiver le bon de livraison

Vos bons de livraison sont précieux : en cas de litige, il faut pouvoir remettre la main sur l'original. Plutôt que de les laisser dormir dans la base, archivons-les dans un espace de stockage dédié — **Seafile**.

Seafile est de la même famille que SeaTable : mêmes interfaces, jeton d'API au même endroit. Vous ne serez pas dépaysé, et c'est un choix cohérent — là encore, on reste dans ce que l'on maîtrise. Un essai gratuit, sans carte bancaire, suffit largement pour cette étape.

## Le workflow, étape par étape

Voici le workflow, tel qu'il apparaît dans n8n :

{{< image-hotspots image="images/lvl4-n8n-workflow.png" alt="Le workflow n8n : du déclencheur SeaTable jusqu'à l'écriture du lien Seafile dans la base" >}}
[
  {"x":1,"y":2,"w":9,"h":45,"img":"images/lvl4-n8n-node-trigger.png","label":"Déclencheur : un nouveau document avec fichier"},
  {"x":16,"y":2,"w":10,"h":45,"img":"images/lvl4-n8n-node-geturl.png","label":"Récupérer l'adresse du fichier dans SeaTable"},
  {"x":32,"y":2,"w":10,"h":45,"img":"images/lvl4-n8n-node-download.png","label":"Télécharger le fichier"},
  {"x":49,"y":2,"w":10,"h":45,"img":"images/lvl4-n8n-node-upload.png","label":"Envoyer le fichier dans Seafile"},
  {"x":65,"y":2,"w":10,"h":45,"img":"images/lvl4-n8n-node-getlink.png","label":"Demander un lien à Seafile"},
  {"x":81,"y":2,"w":10,"h":45,"img":"images/lvl4-n8n-node-update.png","label":"Écrire le lien dans Backup URL du document"}
]
{{< /image-hotspots >}}

Cliquez sur un nœud pour ouvrir sa configuration en détail.

Il forme un aller-retour complet entre les deux services :

1. **Le déclencheur** surveille la table `Documents` : dès qu'un document disposant d'un fichier apparaît, le workflow démarre.
2. n8n **récupère l'adresse du fichier** dans SeaTable, puis le **télécharge**.
3. Il **l'envoie dans Seafile**, dans un dossier d'archives (`/Delivery notes/2026/`).
4. Il **demande à Seafile un lien** vers le fichier ainsi archivé.
5. Il **réécrit ce lien** dans la colonne `Backup URL` du document, côté SeaTable.

En clair : le fichier part de SeaTable, se range dans Seafile, et son adresse d'archive revient se poser dans la base. La force de n8n n'est pas un nœud spectaculaire — c'est cette **composition** de gestes simples entre deux outils.

## Le rejouer vous-même

Si vous voulez le voir tourner pour de bon, pas besoin de le reconstruire nœud par nœud : importez-le tout prêt.

<!-- TODO: verifier que le fichier est bien servi a cette URL apres build. -->
[Télécharger le workflow n8n](/n8n/lvl4-seafile-archive.json)

Dans votre n8n, créez un nouveau workflow et importez ce fichier. Il vous restera à installer le nœud communautaire `n8n-nodes-seafile`, puis à renseigner vos propres accès — vos comptes SeaTable et Seafile, et l'identifiant de votre bibliothèque Seafile à la place de la valeur `YOUR_SEAFILE_LIBRARY`. Lancez ensuite le workflow, et déposez un bon de livraison dans votre base.

{{< warning headline="Une sauvegarde n'est pas une vitrine" text="Le lien que le workflow enregistre pointe vers une archive privée, pas vers une page à diffuser. C'est voulu : sauvegarder un document et le présenter au public sont deux besoins distincts. Ici, l'objectif est de conserver l'original en lieu sûr et de garder sa trace dans la base, rien de plus." />}}

## Essayez par vous-même

Rendez-vous dans votre bibliothèque Seafile après avoir traité un bon : le PDF s'y trouve, rangé dans son dossier d'archives. Revenez ensuite dans la base et ouvrez le document : sa colonne `Backup URL` contient désormais le lien qui y mène. Vous venez de faire dialoguer deux applications sans écrire une ligne de code — c'est tout l'intérêt d'un orchestrateur.

## Article d'aide avec plus d'informations

- [L'intégration n8n de SeaTable]({{< relref "help/integrationen/n8n/" >}})
- [n8n — automatisation de workflows](https://n8n.io/)
- [Seafile — stockage de fichiers](https://www.seafile.com/en/home/)
