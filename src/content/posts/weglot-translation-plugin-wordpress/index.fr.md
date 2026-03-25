---
title: 'Comment traduire automatiquement votre site web avec Weglot.'
description: "Weglot est un plug-in WordPress permettant de traduire automatiquement son propre site web. L'idée est simple et rapidement expliquée. On rédige comme d'habitude tous les textes de son propre site web dans sa langue maternelle et on laisse Weglot traduire tous les contenus dans une ou plusieurs autres langues. Le visiteur du site web est automatiquement redirigé vers la version linguistique qui lui convient le mieux et Weglot se charge de tous les travaux nécessaires au référencement international."
date: 2022-03-21
categories:
    - 'best-practice'
tags:
    - 'Outils & plugins'
color: '#07bfff'
url: '/fr/weglot-plugin-traduction-wordpress'
aliases:
    - /fr/weglot-translation-plugin-wordpress
seo:
    title: 'Comment traduire automatiquement votre site avec Weglot'
    description: 'Weglot est un plugin WordPress qui traduit automatiquement votre site dans d’autres langues, vous aidant à toucher de nouveaux publics'
---

Weglot est un plug-in WordPress permettant de traduire automatiquement son propre site web. L'idée est simple et rapidement expliquée. On rédige comme d'habitude tous les textes de son propre site web dans sa langue maternelle et on laisse Weglot traduire tous les contenus dans une ou plusieurs autres langues. Le visiteur du site web est automatiquement redirigé vers la version linguistique qui lui convient le mieux et [Weglot](https://www.weglot.com/) se charge de tous les travaux nécessaires au référencement international. 

![Traduction automatique de la page web avec Weglot](automatische-uebersetzung-der-webseite-mit-weglot-1.gif)

Traduction automatique de la page web avec Weglot

Avec Weglot, le souhait d'avoir un site web multilingue devient réalité. On obtient un prix client plus élevé avec un minimum d'efforts et, grâce aux textes supplémentaires, le site web devient plus pertinent aux yeux de Google et le classement s'améliore automatiquement. 

Cet article est mon rapport d'expérience personnel après un an et demi d'utilisation active de [Weglot](https://www.weglot.com/). Si vous ne connaissez pas encore Weglot, ce texte vous donnera une idée de la raison pour laquelle nous avons choisi Weglot chez SeaTable. Bien sûr, il y a eu des problèmes, qui ont tous pu être résolus, mais qu'il convient de mentionner ici.

Sur Medium, j'ai publié un autre article décrivant nos scripts individuels, nos solutions aux problèmes et nos adaptations. Cet article s'adresse à ceux qui ont déjà opté pour Weglot et qui [souhaitent](https://christophdb.medium.com/common-pitfalls-and-challenges-with-the-translation-plugin-weglot-on-the-way-to-more-traffic-and-1f51e8c607f4) maintenant [en savoir](https://christophdb.medium.com/common-pitfalls-and-challenges-with-the-translation-plugin-weglot-on-the-way-to-more-traffic-and-1f51e8c607f4) plus sur la [technique derrière Weglot](https://christophdb.medium.com/common-pitfalls-and-challenges-with-the-translation-plugin-weglot-on-the-way-to-more-traffic-and-1f51e8c607f4). 

## Avec Weglot, le référencement international devient un jeu d'enfant

Le logiciel SeaTable est utilisé dans le monde entier et existe dans de nombreuses langues. Par conséquent, notre site web doit également être multilingue. Comme vous pouvez le constater, le site est actuellement disponible en allemand, en anglais, en français, en espagnol et en russe. Au début, je pensais que je devrais traduire moi-même tous les textes du site dans les autres langues, mais je suis tombé par hasard sur Weglot.  
La perspective de voir Weglot se charger de l'ensemble du travail de traduction m'a d'abord paru séduisante, mais en même temps, j'étais sceptique quant à la qualité d'une traduction automatique. Entre-temps, nous utilisons Weglot depuis fin 2020 et sommes devenus des fans absolus. Néanmoins, je souhaite vous faire part de toutes les expériences positives et négatives que j'ai vécues.

Mais assez parlé. Si vous ne connaissez pas encore Weglot, je vous invite à regarder brièvement la vidéo suivante de Weglot, qui décrit brièvement son fonctionnement.

[![Weglot expliqué en 63 secondes](weglot-youtube-video.png)](https://www.youtube.com/watch?v=frzdb79qTrU)

Weglot expliqué en 64 secondes.

## Avec Weglot, on obtient un site web multilingue en quelques secondes

Permettez-moi de vous décrire brièvement les premiers pas avec Weglot. Tout d'abord, vous vous inscrivez sur le site weglot.com pour bénéficier de l'abonnement gratuit. _Free_\-version de l'application. Ne vous inquiétez pas : Weglot écrit quelque chose de 10 jours d'essai, mais Weglot est gratuit en permanence pour une autre langue et un maximum de 2.000 mots.

![Créer le premier projet dans Weglot](weglot-erstes-projekt-anlegen.png)

Créer le premier projet dans Weglot.

Après avoir confirmé votre adresse e-mail, vous créez votre premier projet et choisissez votre technologie web. Outre WordPress, Weglot prend en charge de nombreuses autres technologies web comme Wix, Shopify, Magento, Webflow ou Squarespace. Vous choisissez probablement WordPress et recevez ensuite votre première clé API de Weglot. Traitez cette clé comme un mot de passe et ne révélez cette valeur à personne.

Copiez donc la clé API affichée dans votre presse-papiers et allez dans la zone d'administration de votre site WordPress. Cherchez le plugin WordPress "Weglot" et installez-le. Dans les paramètres du plugin, vous devez saisir la clé API précédemment enregistrée et vous pouvez maintenant commencer à traduire votre site web.

![Installer le plugin WordPress Weglot](install-weglot-in-wordpress.png)

Installer le plugin WordPress Weglot.

Sélectionnez la langue que vous utilisez actuellement sur votre site web et choisissez la langue que vous souhaitez ajouter maintenant par Weglot. 

### Votre site web est désormais disponible en plusieurs langues.

Ce qui suit relève presque de la magie. Dès à présent, les visiteurs de votre site web ont accès à toutes les pages en deux langues. En plus de la page web d'origine, il y a maintenant pour chaque nouvelle langue une nouvelle URL dans laquelle l'abréviation de la langue a été insérée.

> **https://seatable.com/blog/** - notre langue originale en allemand  
> **https://seatable.com/en/blog/** - site anglais traduit par Weglot  
> **https://seatable.com/fr/blog/** - site français traduit par Weglot

Chaque fois qu'une page est consultée par un utilisateur, Weglot vérifie si cette page a déjà été traduite ou si quelque chose a été modifié et effectue ensuite la traduction correspondante. Weglot combine différentes techniques de traduction, telles que [Google Translate](https://translate.google.com/) et [Deepl](https://www.deepl.com/translator), et génère à partir des différentes traductions une traduction qui, dans la plupart des cas, est tout à fait appropriée. Lorsqu'une page doit d'abord être traduite, il peut s'écouler un court instant avant que la page ne soit réellement chargée. Ce délai ne se produit toutefois que lors de la première visite. Chaque visiteur suivant voit la page s'afficher immédiatement.

En plus de la traduction automatique, Weglot affiche désormais sur toutes les pages un menu déroulant permettant de changer de langue. La plupart des utilisateurs n'en auront toutefois pas besoin, car Weglot essaie de diriger automatiquement l'utilisateur vers la bonne page en fonction de la langue du navigateur.

### Plus de 100 langues possibles pour vos affaires internationales

Weglot permet actuellement de traduire dans [plus de 100 langues différentes](https://www.weglot.com/documentation/available-languages). Vous n'en aurez probablement pas besoin d'autant, car il vaut la peine de se concentrer sur les langues les plus parlées dans le monde. Vous trouverez un bon aperçu dans la [liste des langues les plus parlées sur Wikipedia](https://de.wikipedia.org/wiki/Liste_der_meistgesprochenen_Sprachen).

Mais Weglot ne se contente pas de traduire votre site web, il veille également à ce que Google et les autres moteurs de recherche trouvent ces nouveaux contenus et à ce que l'ensemble du contenu soit correctement indexé. Pour ce faire, les _hreflang_\-Les moteurs de recherche trouvent ainsi facilement les textes correspondants.

### Correction manuelle ou traduction professionnelle pour votre WordPress multilingue parfait

Bien sûr, il peut arriver qu'une traduction ne soit pas tout à fait parfaite. Dans ce cas, Weglot permet de corriger facilement la traduction erronée via votre compte Weglot. Pour ce faire, il suffit de sélectionner la langue et l'URL correspondantes, puis d'afficher toutes les traductions dans un tableau de traduction.

![Weglot permet de corriger facilement toute traduction](weglot-uebersetzungstabelle.png)

Weglot permet de corriger facilement toute traduction.

Dès que vous adaptez une traduction, cette modification est immédiatement prise en compte sur votre site web et sera toujours présentée de la même manière à l'avenir.

Si l'on ne souhaite pas corriger soi-même les traductions, il est possible de faire appel à des traducteurs professionnels via Weglot. Ceux-ci sont payés au mot traduit, mais nous n'avons pas encore fait appel à eux pour SeaTable. 

Une autre fonction importante de Weglot est la possibilité de définir des termes qui ne doivent pas être traduits et d'exclure certains éléments de la traduction. SeaTable, par exemple, est un de ces mots que Weglot ne doit jamais traduire. De plus, nous avons défini que tous les éléments avec la classe HTML _dont-translate_ ne sont pas traduits. 

![Avec les classes css ou les ids, on peut demander à Weglot de ne pas traduire quelque chose.](weglot-uebersetzung-verhindern.png)

Avec les classes css ou les ids, on peut demander à Weglot de ne pas traduire quelque chose.

## Comment nous avons construit notre stratégie de référencement international sur seatable.io avec Weglot

Chez SeaTable, nous croyons fermement que seul le trafic organique fonctionne vraiment à long terme. Nous nous sommes donc fixé dès le départ l'objectif de créer un contenu riche et de qualité pour notre site web, qui serait ensuite proposé dans différentes langues. Weglot promettait justement de rendre cela possible. En même temps, il était important pour moi de pouvoir reproduire techniquement tout ce que j'avais en tête et que les coûts directs ainsi que les coûts indirects comme la maintenance soient bien proportionnés aux avantages réels.

Produire un bon contenu a moins posé problème. Mais nous n'avons pas de locuteur natif dans notre équipe pour chacune des langues que nous avons choisies. Nous avons donc décidé très tôt de ne contrôler et, le cas échéant, de ne corriger que la traduction anglaise de nos textes allemands. Tous les textes espagnols, français et russes ne sont pas modifiés. Cela comporte bien sûr le risque d'effrayer certains utilisateurs avec des traductions erronées, mais nous estimons que les traductions sont suffisamment bonnes et nous prenons ce risque calculé.

Grâce aux langues allemande, anglaise, française, espagnole et russe, nous couvrons une grande partie de la population mondiale. Un coup d'œil sur le monitoring de notre site web montre que 50 % du trafic de notre site web provient d'Allemagne, bien que nous n'ayons reçu jusqu'à présent des articles de presse et l'attention des médias que dans ce pays. Je dirais donc que nous devons environ 50 % du trafic actuel de notre site web à Weglot. 

![Plus de trafic grâce aux visiteurs internationaux](zugriffe-weltweit.png)

Plus de trafic grâce aux visiteurs internationaux grâce à Weglot

Par ailleurs, nous ne faisons aucun effort supplémentaire pour notre référencement international. Weglot veille à ce que les moteurs de recherche trouvent les contenus traduits et à ce que ceux-ci apparaissent dans les moteurs de recherche des pays concernés.

## Weglot par rapport à d'autres plug-ins de traduction comme WTFD, TranslatePress, Polylang, Loco Translate et ConveyThis

Avant d'opter pour Weglot avec SeaTable, nous avons également examiné d'autres plug-ins WordPress pour traduire le site web.  
Le plugin le plus connu pour un WordPress multilingue est, avec le paragraphe, le plugin [WPML](https://wpml.org/). Contrairement à Weglot, WPML ne se charge pas de la traduction automatique des contenus, mais offre _uniquement_ une plate-forme pour les propres traductions. Les autres plugins [TranslatePress](https://translatepress.com/?ref=174), [Polylang](https://polylang.pro/) et [Loco Translate](https://de.wordpress.org/plugins/loco-translate/) fonctionnent de la même manière. 

![WPML est de loin le plug-in de traduction le plus populaire pour WordPress.](weglot-bei-google-trends.png)

WPML est de loin le plug-in de traduction le plus populaire pour WordPress.

Il s'agit certainement de bons plug-ins, mais nous voulions absolument une traduction automatique du contenu de nos pages web afin de nous épargner cette tâche fastidieuse.  
Juste pour vous donner une idée : sur le site seatable.io, on trouve actuellement plus de [90 articles de blog]({{< relref "posts" >}}) et plus de 50 pages. En tout, le site compte près d'un million de mots. Il n'est certainement pas exagéré de considérer que la traduction d'une page ou d'un article dans quatre autres langues nécessite au moins une heure à chaque fois. Cela représenterait donc au moins 140 heures, soit près de 18 jours de travail. C'est le temps que Weglot nous a permis d'économiser complètement. 

### Il existe un autre plugin WordPress qui propose des traductions automatiques

Dans le cadre de notre évaluation de Weglot, nous sommes également tombés sur le plugin [ConveyThis](https://www.conveythis.com/). À première vue, ce plugin semble être une copie assez similaire et presque équivalente à Weglot sur le plan fonctionnel. Lors de nos tests, nous avons toutefois dû constater qu'il ne fallait en aucun cas toucher à ConveyThis. Les traductions sont loin d'être aussi bonnes et il manque une documentation et une assistance aussi bonnes que celles que l'on trouve chez Weglot. De notre point de vue, le plugin prétendument moins cher n'en vaut pas la peine, car les traductions sont de bien moins bonne qualité et qu'il faut soit améliorer davantage, soit que la qualité de son propre site web ne soit pas aussi élevée.

## Prix de Weglot

Vous devriez maintenant avoir compris l'importance de Weglot pour le succès de notre site web. Grâce à Weglot, nous pouvons créer un site web multilingue avec un minimum d'efforts et ainsi distribuer notre logiciel presque partout dans le monde. Cela justifie également le [prix de Weglot](https://www.weglot.com/pricing), qui est inhabituellement élevé pour un plug-in WordPress. Mais en même temps, je tiens à souligner que, de notre point de vue, Weglot vaut chaque euro. 

![Les prix du plugin WordPress Weglot](weglot-preise.png)

Les prix du plugin WordPress Weglot.

Actuellement, nous utilisons le _Advanced_\-L'abonnement à Weglot, qui permet de traduire jusqu'à 10 langues et 1 million de mots. Nous payons 1 990 euros pour cela, mais comme nous l'avons déjà mentionné, cela nous a permis d'économiser au moins 18 jours de travail sur les deux années. Le gain de temps est probablement encore beaucoup plus important. Les abonnements peuvent être mis à niveau à tout moment, même pendant la période de validité, et la valeur résiduelle de l'abonnement actuel est entièrement déduite du prix de l'abonnement supérieur. 

Nous allons bientôt passer au _plan étendu_ pour pouvoir faire traduire d'autres articles de blog et, à ce moment-là, nous allons probablement activer une autre langue sur seatable.io. Cette étape ne me prendra que deux clics de souris.

### L'outil Word-Count vous permet de déterminer vos propres besoins

Si vous n'êtes pas sûr de l'abonnement dont vous avez besoin, l'[outil Word-Count de Weglot](https://wordcount.weglot.com/) vous aidera. Grâce à lui, vous savez immédiatement de quel plan vous avez besoin et à quels coûts vous devez vous attendre chaque année. 

![l'outil de comptage de mots Weglot](weglot-word-counter.png)

Le compteur de mots Weglot vous donne une idée de l'abonnement dont vous avez besoin.

## Problèmes que nous avons dû surmonter avec Weglot

Un rapport d'expérience sur Weglot ne serait pas complet si l'on ne parlait pas des défis et des pièges que nous avons dû surmonter au cours de ces deux années. Cependant, nous avons tous pu résoudre les problèmes suivants grâce à une bonne documentation et à un excellent support. 

**1) Redirection automatique et cache**  
Weglot essaie de rediriger chaque visiteur vers la traduction qui lui convient en fonction de la langue de son navigateur. Malheureusement, ce mécanisme n'est pas compatible avec une mise en cache du site WordPress. Dès que l'on active la mise en cache, tous les utilisateurs sont redirigés vers la langue du premier visiteur. Nous avons donc désactivé la redirection automatique et écrit nous-mêmes un javascript.

**2) les liens spéciaux de notre thème ne sont pas pris en charge**

Sur SeaTable.io, nous utilisons le thème Enfold et, en plus des liens dans le corps du texte, nous utilisons également des boîtes de liens - par exemple sur notre site web. [Page d'aide]({{< relref "help" >}})où la boîte entière sert de lien. Malheureusement, cette boîte de lien n'est pas reconnue comme un lien par Weglot et les utilisateurs sont toujours redirigés vers la langue d'origine. Nous avons pu remédier à ce comportement en ajoutant une _Action in der functions.php beheben._

![Weglot a eu des problèmes avec les boîtes de lien](weglot-boxen-als-links.png)

Weglot avait des problèmes avec les boîtes de liens de notre rubrique d'aide.

**3) Optimisation SEO lorsque la langue d'origine n'est pas la langue de repli**

La langue originale de seatable.io est l'allemand et Weglot traduit les textes allemands dans toutes les autres langues. Néanmoins, comme l'anglais est la langue universelle, nous aimerions que Google la présente à chaque utilisateur à qui nous ne pouvons pas proposer une langue qui lui convienne. Nous avons également réussi à le faire avec quelques lignes de code dans la _functions.php_ atteindre.

**4) Les liens d'ancrage ne sont pas traduits**

Un autre problème survenait sur seatable.io lorsque l'on créait un lien vers les textes d'ancrage des titres. Malheureusement, un clic sur un tel lien renvoyait toujours le visiteur à la langue d'origine de Weglot, alors que ce n'était pas du tout ce qui était souhaité dans ce cas, car le texte d'ancrage était également traduit. Une fois que nous avons compris le mécanisme, nous avons pu ajouter des liens sans codage en ajoutant simplement _id-tags_ résoudre facilement le problème.

Si vous souhaitez en savoir plus sur ces problèmes, je vous conseille de consulter mon [article sur Medium](https://christophdb.medium.com/common-pitfalls-and-challenges-with-the-translation-plugin-weglot-on-the-way-to-more-traffic-and-1f51e8c607f4). J'y décris en détail nos adaptations et nos codages. 

## Les avantages du plug-in de traduction Weglot en résumé

J'avoue que je suis un grand fan de Weglot. Il y a des choses pour lesquelles il vaut la peine de payer si on est déchargé de beaucoup de travail. Weglot est définitivement un de ces cas. Nous générons de nouveaux contenus dans notre langue maternelle, l'allemand, et Weglot produit pour nous les autres traductions.  
Pour moi, les principaux arguments en faveur de l'utilisation de Weglot sont les suivants :

- Weglot conduit à plus de contenu, à des classements supplémentaires et meilleurs sur Google et, au final, à plus de trafic et à une plus grande portée.
- La facilité d'installation de Weglot est un argument en sa faveur. En moins d'une minute, on obtient un site web multilingue.
- Weglot promet la compatibilité avec pratiquement tous les thèmes WordPress et de nombreux plug-ins, y compris WooCommerce, Yoast et Elementor. De même, nous n'avons jamais eu de conflits avec les plugins ou notre thème.
- Weglot est optimisé pour le référencement multilingue. Il ajoute automatiquement des attributs de balise `hreflang`, crée des URL entièrement dédiées pour chaque langue et indexe vos pages traduites.
- La qualité de la traduction est vraiment bonne. Les retouches manuelles sont rarement nécessaires et elles peuvent alors être facilement effectuées via le site web de Weglot.
- Weglot dispose d'une équipe d'assistance dédiée de plus de dix personnes ayant une compétence technique marquée dans la traduction d'applications web.

## Ma conclusion après plus d'un an d'utilisation de Weglot

[Weglot](https://www.weglot.com/) ne promet pas seulement beaucoup, mais fournit aussi extrêmement bien. Weglot permet de transformer n'importe quel site WordPress en un site multilingue en un rien de temps. Même si nous avons rencontré quelques obstacles techniques, nous avons pu les surmonter et réaliser exactement ce que nous voulions.  
Le prix de Weglot semble à première vue élevé si on le compare à d'autres plug-ins WordPress populaires. En même temps, le prix de la traduction de son propre site web est plus que justifié. Je choisirais à nouveau Weglot à tout moment et j'espère que ce témoignage vous aura été utile. Si vous souhaitez en savoir plus sur nos adaptations individuelles, je vous recommande mon [article Medium](https://christophdb.medium.com/common-pitfalls-and-challenges-with-the-translation-plugin-weglot-on-the-way-to-more-traffic-and-1f51e8c607f4).
