---
title: "Les tarifs de SeaTable : Des tarifs transparents pour toutes les tailles d'équipe"
description: ''
date: '2025-03-30'
url: '/fr/prix'
aliases:
    - '/fr/preise/'
    - '/fr/prices/'
seo:
    title: 'Tarifs SeaTable : transparence & souplesse'
    description: 'Découvrez toutes les offres SeaTable, comparez les fonctionnalités et les tarifs adaptés à chaque équipe.'

sections:
    - name: hero-price
      weight: 1
      title: SeaTable Cloud. Sur mesure pour vous.
      subtitle: Notre offre
      text: Commencez gratuitement et obtenez plus de fonctionnalités et des limites supérieures à partir de 7€ par utilisateur/mois quand vous en avez besoin
      title2: SeaTable Server. Contrôle total pour votre organisation.
      subtitle2: Ce que vous obtenez
      text2: Installez SeaTable sur votre propre serveur et profitez d'une souveraineté totale sur vos données, d'une personnalisation individuelle et de toutes les fonctionnalités Enterprise.


    - name: 'price-1'
      weight: 2
      xshow: 'showCloud'

    - name: price-table
      weight: 3
      xshow: 'showCloud'
      classes:
        - curved
        - bg-gray-100
      title: Comparez tous les détails
      table:
        head: ['Gratuit', 'Plus', 'Entreprise', 'Dédié']
        rows:
          - type: section
            label: 'Prix (par utilisateur, hors TVA)'
          - key: 'Facturation annuelle'
            values: ['0€', '7€', '14€', '*']
          - key: 'Facturation mensuelle'
            values: ['0€', '9€', '18€', '*']
          - type: section
            label: 'Utilisation (total par équipe)'
          - key: 'Bases'
            values: ['∞', '∞', '∞', '∞']  
          - key: 'Tables'
            values: ['∞', '∞', '∞', '∞']
          - key: 'Lignes'
            values: ['10 000', '50 000', '∞', '∞']
          - key: 'Nombre maximum de lignes dans une base'
            values: ['10.000', '50.000', '100.000', '200.000']
          - key: 'Espace de stockage'
            values: ['2 Go', '50 Go', '100 Go', '∞']
          - key: 'Durée de rétention des snapshots'
            values: ['1 mois', '6 mois', '12 mois', '24 mois']
          - key: 'Exécutions JavaScript (par mois)'
            values: ['∞', '∞', '∞', '∞']
          - key: 'Exécutions Python (par mois)'
            values: ['100', '5 000', '∞', '∞']
          - key: 'Appels API (par mois et utilisateur)'
            values: ['3.000 (fixe)', '10.000', '50.000', '∞']
          - key: 'Taille maximale de l’équipe'
            values: ['25', '∞', '∞', '∞']
          - type: section
            label: 'Fonctionnalités'
          - key: '25 types de colonnes'
            values: ['+', '+', '+', '+']
          - key: 'Filtrage, regroupement et tri'
            values: ['+', '+', '+', '+']
          - key: 'Vues'
            values: ['+', '+', '+', '+']
          - key: 'Vues privées'
            values: ['-', '+', '+', '+']
          - key: 'Partage de vues'
            values: ['-', '+', '+', '+']
          - key: 'Formulaires web'
            values: ['+', '+', '+', '+']
          - key: 'Jeux de données partagés'
            values: ['+', '+', '+', '+']
          - key: 'Import / Export (CSV, XLSX et DTABLE)'
            values: ['+', '+', '+', '+']
          - key: 'Notifications'
            values: ['+', '+', '+', '+']
          - key: 'Plugins'
            values: ['+', '+', '+', '+']
          - key: 'Support JavaScript et Python'
            values: ['+', '+', '+', '+']
          - key: 'App Builder'
            values: ['+', '+', '+', '+']
          - key: 'Autorisations de partage individuelles (Base)'
            values: ['-', '+', '+', '+']
          - key: 'Autorisations de table, vue et colonne (Base)'
            values: ['-', '+', '+', '+']
          - key: 'Verrouillage des lignes'
            values: ['-', '+', '+', '+']
          - key: 'Autorisations de page (App)'
            values: ['-', '-', '+', '+']
          - key: 'Personnalisation du formulaire web (logo, image d’en-tête)'
            values: ['-', '-', '+', '+']
          - key: 'Automatisations (par mois et utilisateur)'
            values: ['100 (fixe)', '500', '5 000', '∞']
          - key: 'Crédits IA (par mois et utilisateur)'
            values: ['12,5 (fixe)', '50', '500', '∞']
          - key: 'Stockage Big Data'
            values: ['-', '-', '+', '+']
          - type: section
            label: 'Support'
          - key: 'Centre d’aide'
            values: ['+', '+', '+', '+']
          - key: 'Forum SeaTable'
            values: ['+', '+', '+', '+']
          - key: 'Support par e-mail'
            values: ['-', '-', '+', '+']
          - key: 'Services professionnels (payants)'
            values: ['-', '-', '+', '+']
          - type: section
            label: 'Admin & Sécurité'
          - key: 'Authentification à deux facteurs'
            values: ['+', '+', '+', '+']
          - key: 'Panneau d’administration Entreprise'
            values: ['-', '-', '-', '+']
          - key: 'Authentification via AD/LDAP, SAML ou OAuth'
            values: ['-', '-', '-', '+']
          - type: section
            label: 'Facturation'
          - key: 'Paiement par carte bancaire'
            values: ['+', '+', '+', '+']
          - key: 'Paiement par virement bancaire (min. 10 utilisateurs, paiement annuel)'
            values: ['-', '-', '+', '+']


    # details on-premise
    - name: 'content-9'
      weight: 3
      classes:
          - bg-gray-100
          - curved
      xshow: '!showCloud'
      title: Avantages de votre propre serveur
      subtitle: Raisons pour le on-premises
      items:
      - headline: Fonctionnalités Enterprise
        text: Avec votre propre serveur, il n’y a pas de versions différentes. Vous bénéficiez toujours de l’ensemble complet des fonctionnalités de SeaTable Enterprise.
        icon: robot
      - headline: Support Enterprise
        text: Le prix de la licence SeaTable Enterprise inclut toujours notre support Enterprise.
        icon: award
      - headline: Personnalisation
        text: Avec votre système SeaTable Enterprise, vous pouvez utiliser votre propre URL, des modèles personnalisés, des codes couleur individuels ainsi que des rôles et des autorisations.
        icon: paint-roller
      - headline: Protection maximale des données
        text: SeaTable est l’une des rares solutions cloud que vous pouvez également obtenir en version sur site.<br><br>Vous achetez une licence SeaTable Enterprise Server et pouvez installer et exploiter le logiciel serveur où vous le souhaitez.
        icon: file-shield
      - headline: Authentification
        text: SeaTable prend en charge toutes les méthodes d’authentification courantes telles que SAML, OAuth, Shibboleth, Active Directory et LDAP. Il permet l’authentification à deux facteurs et le Single Sign-On.
        icon: fingerprint
      - headline: Limites personnalisées
        text: Dans votre système, vous décidez des limites API à appliquer, ou même s’il doit y en avoir.
        icon: compass

    - name: 'customer-1'
      weight: 9
      title: 'Des entreprises et équipes de toutes tailles font confiance à SeaTable dans le monde entier'
      subtitle: 'Vous êtes en bonne compagnie'
      show_numbers: 'no'
      buttons: []

    - name: content-11
      weight: 10
      title: Remises pour les organisations à but non lucratif
      subtitle: Accessible à tous
      items:
          - text: Nous sommes heureux de soutenir les projets exceptionnels. Les organisations à but non lucratif et les établissements d'enseignement bénéficient d'une remise de 50%. Dans des cas exceptionnels, les associations locales peuvent obtenir jusqu'à 75% de réduction sur les abonnements SeaTable Plus et SeaTable Enterprise. Envoyez-nous [votre demande de remise via la gestion d'équipe]({{< relref "help/teamverwaltung/abonnement/rabatte" >}}).
      image: /images/image-341.png
      image_alt: 'Graphique SeaTable sur les remises pour organisations à but non lucratif, établissements d’enseignement et institutions publiques'

    - name: platform-selector
      weight: 18

    - name: faq
      weight: 19
      xshow: '!showCloud'
      title: Questions Fréquentes
      items:
          - q: Qu'est-ce qu'un utilisateur ?
            a: "Un utilisateur désigne un compte utilisateur (actif) sur une instance de SeaTable Server. Un compte utilisateur (actif) permet l'authentification et la connexion au système
            Un login, et donc un compte utilisateur, est nécessaire pour les actions suivantes :<br>
            – Création, édition et suppression de bases, d'applications et de formulaires web<br>
            – Saisie, édition et suppression de données dans les bases et les applications<br><br>
            Aucun login et donc aucun compte utilisateur n'est requis pour ces actions :<br>
            – Utilisation d'applications publiques<br>
            – Accès aux bases/vues via des liens externes<br>
            – Soumission de formulaires web publics"
          - q: Qu'est-ce qu'un utilisateur inactif ?
            a: Un utilisateur inactif désigne un compte d'utilisateur qui a été défini comme inactif et qui ne permet pas de se connecter au système. Les utilisateurs inactifs ne comptent pas pour la licence et celle-ci ne limite pas non plus le nombre d'utilisateurs inactifs. Le statut d'activité d'un utilisateur peut être modifié à tout moment par un administrateur système.
          - q: Quels modes de paiement puis-je utiliser ?
            a: Vous pouvez en principe payer par carte de crédit ainsi qu'avec Apple Pay et Google Pay. Vous pouvez également payer une licence pour 50 utilisateurs et plus par virement bancaire.
          - q: Puis-je acheter une licence pour SeaTable Server sans renouvellement automatique ?
            a: Si vous souhaitez acheter une licence SeaTable Server sans renouvellement automatique de la licence, veuillez acheter une licence avec renouvellement automatique et désactiver le renouvellement automatique dans le portail [de gestion des abonnements SeaTable Server](https://licenses.seatable.com/p/login/5kA4j61uU641eqY000) immédiatement après l'achat.
          - q: Comment puis-je annuler le renouvellement automatique de ma licence pour SeaTable Server ?
            a: Vous pouvez désactiver le renouvellement automatique à tout moment sur le portail [de gestion des abonnements SeaTable Server](https://licenses.seatable.com/p/login/5kA4j61uU641eqY000).
          - q: Comment puis-je adapter l'adresse de facturation ?
            a: Vous pouvez à tout moment modifier l'adresse de facturation dans le portail [de gestion des abonnements SeaTable Server](https://licenses.seatable.com/p/login/5kA4j61uU641eqY000).<br><br>Il n'est pas possible de modifier une facture ultérieurement.
          - q: Puis-je modifier la taille d'une licence SeaTable Server en cours ?
            a: Vous pouvez à tout moment augmenter la taille d'une licence SeaTable Server pour 50 utilisateurs ou plus. Veuillez contacter sales@seatable.com en indiquant la clé de licence et le nombre d'utilisateurs souhaités. Le prix de la licence pour les utilisateurs supplémentaires sera calculé au prorata du temps.<br><br>Vous ne pouvez pas augmenter la taille d'une licence SeaTable Server pour 10 et 25 utilisateurs pendant sa durée de validité. Si vous avez besoin de plus d'utilisateurs, vous devez acheter une nouvelle licence.<br><br>Il n'est pas possible de combiner plusieurs licences. Une instance de SeaTable Server ne peut être associée qu'à une seule licence.
          - q: Puis-je combiner plusieurs licences SeaTable Server ?
            a: Il n'est pas possible de combiner plusieurs licences SeaTable Server. Une seule licence est activée à la fois sur une instance de SeaTable Server.
          - q: Comment s'effectue le renouvellement automatique ?
            a: Environ 30 jours avant l'expiration de votre licence SeaTable Server, vous recevrez un e-mail vous informant du renouvellement à venir. L'e-mail expliquera quand le renouvellement aura lieu et quel mode de paiement sera utilisé. L'e-mail contient également un lien vers le portail [de gestion des abonnements SeaTable Server](https://licenses.seatable.com/p/login/5kA4j61uU641eqY000). Vous pouvez y modifier l'adresse de facturation et le mode de paiement. Une fois le renouvellement effectué, vous recevrez la facture et les documents de licence par e-mail. Pour activer la licence renouvelée, téléchargez le fichier de licence sur votre instance SeaTable Server.
          - q: Puis-je indiquer un numéro de commande ou un centre de coûts lors de l'achat d'une licence ?
            a: "Si vous avez besoin d'une référence sur la facture, veuillez contacter sales@seatable.com. Indiquez les informations suivantes dans votre demande : Nombre d'utilisateurs, adresse de facturation, numéro de TVA, adresse e-mail de contact et, le cas échéant, adresse e-mail de facturation. Vous recevrez ensuite une offre par e-mail. Veuillez nous communiquer la référence lors de la confirmation de l'offre. La référence sera ensuite mentionnée sur la facture."
          - q: Est-ce que je bénéficie d'une réduction en tant qu'organisme public ou organisation à but non lucratif ?
            a: Les institutions publiques et les organisations à but non lucratif bénéficient d'une réduction sur les licences SeaTable Server. Veuillez contacter [notre service des ventes]({{< relref "pages/contact" >}}).<br><br>En principe, aucune remise n'est accordée sur les licences SeaTable Server pour 10 et 25 utilisateurs.
          - q: Pour quelles périodes de licence puis-je acheter une licence pour SeaTable Server ?
            a: La durée minimale d'une licence logicielle pour SeaTable Server est d'un an. Vous pouvez également acheter des licences d'une durée de 2 et 3 ans. Vous économisez respectivement 5% et 10% sur les licences de 2 et 3 ans.<br><br>Les frais de licence sont en principe facturés et exigibles au début de la période de licence pour toute la durée de celle-ci.<br><br>Pour les licences de longue durée, veuillez contacter [notre service des ventes]({{< relref "pages/contact" >}}) et indiquer la durée souhaitée ainsi que le nombre d'utilisateurs. Vous recevrez ensuite une offre par e-mail.
          - q: Comment activer la licence du serveur SeaTable ?
            a: Vous devez être actif pour activer la licence ! Connectez-vous à votre instance de serveur SeaTable en tant qu'utilisateur avec des droits d'administrateur et accédez à l'administration du système. Pour ce faire, cliquez sur votre avatar dans le coin supérieur droit de la page d'accueil. Dans la zone d'information de l'administration système, vous pouvez télécharger le fichier de licence. La période de validité de la licence est alors immédiatement affichée dans la zone d'information.<br><br>Si l'interface web de votre instance de serveur SeaTable n'est plus accessible, vous devez alors sauvegarder le fichier de licence dans le système de fichiers de l'hôte. Pour plus d'informations, consultez le [manuel d'administration de SeaTable](https://admin.seatable.com).
          - q: Quels sont les droits que me confère la licence du logiciel SeaTable Server ?
            a: Une licence logicielle pour SeaTable est l'autorisation donnée au titulaire de la licence d'utiliser SeaTable Server. Les droits d'utilisation accordés par la licence et les autres droits sont décrits dans le [CLUF de SeaTable Server Enterprise Edition]({{< relref "pages/legal/eula" >}}).
          - q: Une licence est-elle transférable ?
            a: Le [CLUF de SeaTable Server Enterprise Edition]({{< relref "pages/legal/eula" >}}) exclut tout transfert des droits d'utilisation. Vous ne pouvez pas vendre ou céder une licence.
          - q: Puis-je acheter une licence SeaTable Server auprès d'un revendeur ?
            a: Vous ne pouvez acheter des licences SeaTable Server que directement auprès de SeaTable GmbH.
          - q: Quelle est la configuration minimale requise pour faire fonctionner le serveur SeaTable ?
            a: Consultez le [manuel d'administration de SeaTable](https://admin.seatable.com) pour toute question technique.

    - name: faq
      weight: 20
      xshow: 'showCloud'
      title: Questions Fréquentes
      items:
        - q: Puis-je utiliser SeaTable Cloud gratuitement ?
          a: "Avec notre abonnement Free, vous pouvez utiliser SeaTable Cloud en permanence avec jusqu'à 25 utilisateurs sans frais. L'inscription active automatiquement cet abonnement.<br><br>
Si les limites ou fonctionnalités de l'abonnement Free sont insuffisantes, vous pouvez à tout moment passer aux abonnements payants Plus ou Enterprise avec des limites étendues et des fonctionnalités supplémentaires."

        - q: Puis-je tester les fonctionnalités Enterprise ?
          a: Nous pouvons mettre à niveau temporairement votre abonnement Free ou Plus vers Enterprise sans frais. [Envoyez une demande via la gestion d'équipe](https://account.seatable.com/).

        - q: Qu'est-ce qu'une équipe et un utilisateur ?
          a: Dans SeaTable Cloud, vous travaillez en équipe. Chaque membre possède un compte utilisateur (une équipe peut ne compter qu'une personne).<br><br>Lors de l'inscription, une équipe est créée dont vous êtes l'administrateur. Vous pouvez ajouter des membres et désigner d'autres administrateurs.<br><br>Les utilisateurs sont identifiés par email et ne peuvent appartenir qu'à une seule équipe.

        - q: Puis-je modifier le nombre d'utilisateurs dans mon équipe ?
          a: "Vous pouvez ajuster le nombre d'utilisateurs à tout moment.<br><br>Pour les abonnements Free, Plus et Enterprise, utilisez la [gestion d'équipe](https://account.seatable.com/). Pour SeaTable Dedicated, contactez votre responsable.<br><br>La version Free est limitée à 25 utilisateurs. Les versions Plus, Enterprise et Dedicated n'ont pas de limite."

        - q: Puis-je combiner différents abonnements dans une même équipe ?
          a: "Il est impossible de combiner différents abonnements dans une même équipe.<br><br>Mais vous pouvez répartir les utilisateurs entre plusieurs équipes avec des abonnements différents."

        - q: Puis-je combiner différentes périodes de facturation ?
          a: "Le mélange de périodes de facturation est impossible. Toute l'équipe est facturée soit mensuellement soit annuellement.<br><br>Le paiement annuel offre environ 20% d'économie."

        - q: Comment résilier un abonnement Plus ou Enterprise ?
          a: "La résiliation s'effectue via la [gestion d'équipe](https://account.seatable.com/). Les fonctionnalités restent accessibles jusqu'à la fin de la période payée.<br><br>Après résiliation, l'abonnement repasse en version Free, ce qui peut limiter l'accès aux données."

        - q: "Que se passe-t-il quand j'atteins les limites de mon abonnement ?"
          a: "Nous vous en informerons. Vous conservez l'accès aux bases mais ne pourrez plus ajouter de lignes ou fichiers."

        - q: "Quels moyens de paiement sont acceptés ?"
          a: "Cartes bancaires, Apple Pay et Google Pay. Les clients Enterprise avec paiement annuel (10+ utilisateurs) peuvent payer par virement bancaire."

        - q: "Comment modifier l'adresse de facturation ?"
          a: "Modifiez l'adresse à tout moment via la [gestion d'équipe](https://account.seatable.com/).<br><br>Les factures déjà émises ne peuvent être modifiées."

        - q: "Qu'en est-il de la confidentialité et sécurité ?"
          a: "C'est notre priorité absolue. Vos données sont traitées exclusivement dans des centres de données allemands sous surveillance constante. Plus de détails dans [Confidentialité]({{< relref \"pages/legal/data-privacy\" >}}) et [Sécurité]({{< relref \"pages/legal/security\" >}})."

        - q: "Comment supprimer mon compte ?"
          a: "L'administrateur peut supprimer des utilisateurs ou des équipes via la [gestion](https://account.seatable.com). Le seul membre d'une équipe en est l'administrateur.<br><br>Nous regrettons votre départ. [Partagez-nous vos raisons]({{< relref \"pages/contact\" >}}).<br><br>Les [Conditions d'utilisation]({{< relref \"pages/legal/terms-of-service\" >}}) détaillent le traitement des données après suppression."

---
