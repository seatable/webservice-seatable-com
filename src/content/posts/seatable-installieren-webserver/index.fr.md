---
title: Installer SeaTable Server sur son propre serveur
description: "Grâce à Docker, SeaTable s'installe en quelques minutes sur n'importe quel serveur Linux. Découvrez les prérequis, le déroulement de l'installation et pourquoi l'auto-hébergement avec SeaTable est si simple."
date: 2021-05-15
lastmod: 2025-03-27
categories:
    - product-features
url: /fr/installation-seatable-enterprise-serveur-web
aliases:
    - /fr/seatable-enterprise-auf-dem-eigenen-server-hinter-einem-webserver-installieren
    - /fr/installation-seatable-enterprise-ubuntu-20-04
    - /fr/seatable-enterprise-edition-unter-ubuntu-20-04-lts-installieren
color: '#265697'
seo:
    title: "Installer SeaTable Server : auto-hébergement simplifié"
    description: "Installez SeaTable Server sur votre propre serveur Linux en quelques minutes avec Docker et Caddy. Tout sur les prérequis et le processus."
---

Si vous préférez conserver vos données sur votre propre serveur, SeaTable Server est la solution idéale. Grâce à Docker, l'installation est simple et se termine en quelques minutes, quelle que soit la distribution Linux que vous utilisez.

Le guide d'installation complet étape par étape se trouve dans le SeaTable Admin Manual : **[Accéder au guide d'installation sur admin.seatable.com](https://admin.seatable.com/installation/basic-setup/)**

Dans la suite, vous découvrirez ce dont vous avez besoin pour l'installation, comment se déroule le processus et tout ce que SeaTable en tant que plateforme peut vous offrir.

## Pourquoi héberger SeaTable soi-même ?

SeaTable est disponible en tant que solution cloud sur [cloud.seatable.io](https://cloud.seatable.io). Cependant, de nombreuses entreprises et organisations préfèrent exploiter leurs données sur leur propre infrastructure, que ce soit pour des raisons de protection des données, des exigences de conformité internes ou simplement pour garder le contrôle total. SeaTable Enterprise Edition rend exactement cela possible : vous installez SeaTable sur votre propre serveur et le configurez et l'exploitez selon vos besoins.

## Ce dont vous avez besoin

Les prérequis pour une installation de SeaTable sont raisonnables :

- **Un serveur Linux** avec au moins 4 cœurs CPU, 8 Go de RAM et 10 Go d'espace libre (plus de l'espace pour vos données)
- **Un accès root** au serveur, par SSH ou console
- **Un (sous-)domaine** avec DNS pointant vers l'adresse IP de votre serveur
- **Accessibilité sur les ports 80 et 443** via ce domaine

Peu importe la distribution Linux que vous utilisez : Ubuntu, Debian, Rocky Linux ou une autre variante. Tant que Docker fonctionne dessus, SeaTable fonctionnera. Une adresse IPv4 statique est utile mais pas indispensable. Elle maximise l'accessibilité de votre serveur, car certains réseaux mobiles ne prennent toujours pas en charge IPv6.

## Ce qui se cache sous le capot

SeaTable utilise Docker pour exécuter ses services via plusieurs conteneurs. En plus du serveur SeaTable lui-même, on trouve une base de données MariaDB pour le stockage des données, Redis pour la mise en cache rapide et un proxy inverse qui reçoit les requêtes entrantes et les transmet à SeaTable. Tous ces composants sont gérés ensemble via Docker Compose : vous n'avez pas à vous occuper de chacun individuellement.

Par défaut, SeaTable est livré avec Caddy comme proxy inverse. Le grand avantage de Caddy est qu'il demande et renouvelle automatiquement les certificats HTTPS via Let's Encrypt. Si vous pointez votre domaine vers le serveur et ouvrez les ports 80 et 443, vous obtenez des connexions chiffrées sans aucune configuration manuelle.

## Comment se déroule l'installation

L'installation complète se divise en cinq étapes :

1. **Installer Docker** – Si ce n'est pas déjà fait, Docker est configuré sur le serveur.
2. **Télécharger les fichiers Compose** – SeaTable fournit des fichiers de configuration YAML prêts à l'emploi qui définissent tous les composants nécessaires.
3. **Ajuster la configuration** – Dans un fichier central `.env`, vous entrez votre domaine, vos mots de passe et vos paramètres de base.
4. **Demander une licence** – SeaTable Enterprise est gratuit pour jusqu'à trois utilisateurs. Vous recevez un fichier de licence simplement par e-mail.
5. **Démarrer le serveur** – Une seule commande `docker compose up` lance tous les conteneurs et SeaTable est prêt à l'emploi.

L'ensemble du processus ne prend généralement pas plus de 10 minutes.

## SeaTable derrière son propre serveur web

Caddy est la solution recommandée et la plus simple, mais pas la seule. Si vous avez déjà un serveur web comme nginx, Apache ou Traefik sur votre serveur, vous pouvez également faire fonctionner SeaTable derrière celui-ci. Dans ce cas, vous désactivez le proxy Caddy inclus et configurez votre serveur web existant comme proxy inverse pour SeaTable. Le serveur web transmet alors les requêtes entrantes sur le domaine SeaTable au conteneur SeaTable, une procédure courante que la plupart des administrateurs connaissent déjà.

Dans ce scénario, vous gérez les certificats HTTPS vous-même, par exemple via Let's Encrypt et Certbot ou un certificat SSL existant de votre organisation. La documentation officielle décrit également ce scénario en détail.

## Mises à jour faciles

L'architecture Docker reste avantageuse après l'installation : les mises à jour vers une nouvelle version de SeaTable se font en quelques commandes. Vous téléchargez la dernière image Docker, redémarrez les conteneurs, et c'est fait. Vos données et configurations restent intactes.

## Ce que vous pouvez réaliser avec SeaTable

SeaTable est bien plus qu'une base de données. C'est une plateforme qui permet même aux utilisateurs sans expérience informatique de créer des solutions sur mesure en un temps record.

Un exemple concret : une administration universitaire souhaite gérer numériquement les demandes de subvention entrantes. Avec SeaTable, un collaborateur crée une base, génère un formulaire web pour le dépôt des demandes et met en place une automatisation IA qui extrait automatiquement les informations pertinentes des documents soumis. Les notifications informent l'équipe des changements de statut, et via une application personnalisée, les demandeurs peuvent consulter l'état de leur dossier à tout moment. Tout cela est possible sans compétences en programmation et se met en place en quelques heures.

Qu'il s'agisse de gestion de projet, d'inventaire, de CRM ou de planification d'événements, les possibilités sont aussi variées que les besoins de votre organisation.

![CRM et ventes dans SeaTable : opportunités groupées par propriétaire avec statut, clients et valeur estimée](seatable-crm-example.png)

## Commencez gratuitement

Vous pouvez utiliser SeaTable Enterprise Edition avec jusqu'à trois utilisateurs de manière permanente et gratuite, aussi bien pour un usage privé que commercial. La licence gratuite vous est envoyée simplement par e-mail.

Si vous avez besoin de plus d'utilisateurs, vous pouvez acheter des licences pour 10, 25 ou 50 utilisateurs directement sur la [page de tarifs SeaTable]({{< relref "pages/prices" >}}). Pour des installations plus importantes, veuillez nous contacter via le [formulaire de contact]({{< relref "pages/contact" >}}).
