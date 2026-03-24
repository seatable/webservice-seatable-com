---
title: 'Changelog'
seo:
    title: 'Changelog SeaTable : Mises à jour & évolutions'
    description: 'Consultez toutes les évolutions du serveur SeaTable : nouveautés, corrections et notes de version détaillées.'
url: '/fr/changelog'

sections:
    - name: 'hero-2'
      weight: 1
      title: Journal des modifications de SeaTable Server
      subtitle: Quoi de neuf
      text: "Tous les changements, mises à jour et améliorations se trouvent dans ce journal des modifications. Plus d'informations sur les changements majeurs sont fournies dans les notes de version."

    - name: 'content-27'
      weight: 2
      title: 'Aller directement à la dernière version :'
      subtitle: 'Versions disponibles'
      text: "Nous vous recommandons de vous abonner à notre newsletter pour toujours recevoir des informations sur la dernière version la plus récente et la plus sécurisée de SeaTable Server"
      items:
          - icon: fingerprint
            headline: 'SeaTable 6'
            link: '#release-6'
          - icon: bullseye
            headline: 'SeaTable 5'
            link: '#release-5'
          - icon: code
            headline: 'Versions antérieures'
            link: '#release-4'

    - name: 'content-11'
      weight: 3
      title: Choisissez le cloud européen ou gérez votre propre serveur
      subtitle: La confidentialité nécessite la sécurité
      description: "La confidentialité et la sécurité sont indissociables — une véritable confidentialité ne peut exister sans des mesures de sécurité robustes. Protéger vos données contre les accès non autorisés, les   violations et les abus est essentiel pour maintenir la confidentialité et la confiance. Rester à jour avec les dernières normes de sécurité et les meilleures pratiques est crucial pour garantir que vos informations personnelles et professionnelles restent privées et protégées.<br><br>
      Avec SeaTable, vous avez la flexibilité de choisir la solution qui correspond le mieux à vos besoins en matière de confidentialité et de conformité. Vous pouvez opter pour notre offre SaaS hébergée en Europe, qui est entièrement conforme au RGPD et bénéficie de lois européennes strictes sur la protection des données et de centres de données sécurisés. Alternativement, vous pouvez exécuter votre propre serveur SeaTable, ce qui vous donne un contrôle total sur vos données et votre infrastructure de sécurité. Les deux options sont conçues pour vous offrir transparence, conformité et tranquillité d’esprit."
      image: ''

    - name: "content-26"
      weight: 10
      title: SeaTable Release 6
      subtitle: Détails de la version
      anchor: release-6
      items:
        - text: 'Version **6.0.10** le 4 novembre 2025 : [Notes de version 6.0]({{< relref "posts/seatable-releases/seatable-release-6-0" >}})'
        - text: 'Version **6.1.8** le 20 mars 2026 : [Notes de version 6.1]({{< relref "posts/seatable-releases/seatable-release-6-1" >}})'
      template: "c9124bcd934b47bc8f30"

    - name: "content-26"
      weight: 11
      title: SeaTable Release 5
      subtitle: Détails de la version
      anchor: release-5
      items:
        - text: 'Version **5.3.10** le 16 juin 2025 : [Notes de version 5.3]({{< relref "posts/seatable-releases/seatable-release-5-3" >}})'
        - text: 'Version **5.2.7** le 25 février 2025 : [Notes de version 5.2]({{< relref "posts/seatable-releases/seatable-release-5-2" >}})'
        - text: 'Version **5.1.9** le 8 novembre 2024 : [Notes de version 5.1]({{< relref "posts/seatable-releases/seatable-release-5-1" >}})'
        - text: 'Version **5.0.7** le 15 juillet 2024 : [Notes de version 5.0]({{< relref "posts/seatable-releases/seatable-release-5-0" >}})'
      template: "5964c9e4b6534372b1d8"

    - name: "content-26"
      weight: 12
      title: SeaTable Release 4
      subtitle: Détails de la version
      anchor: release-4
      items:
        - text: 'Version **4.4.9** le 15 mai 2024 : [Notes de version 4.4]({{< relref "posts/seatable-releases/seatable-release-4-4" >}})'
        - text: 'Version **4.3.8** le 8 février 2024 : [Notes de version 4.3]({{< relref "posts/seatable-releases/seatable-release-4-3" >}})'
        - text: 'Version **4.2.11** le 22 novembre 2023 : [Notes de version 4.2]({{< relref "posts/seatable-releases/seatable-release-4-2" >}})'
        - text: 'Version **4.1.9** le 23 août 2023 : [Notes de version 4.1]({{< relref "posts/seatable-releases/seatable-release-4-1" >}})'
        - text: 'Version **4.0.7** le 27 juin 2023 : [Notes de version 4.0]({{< relref "posts/seatable-releases/seatable-release-4-0" >}})'
      template: "d2ccee45fb3b4301836a"

    - name: "content-26"
      weight: 13
      title: SeaTable Release 3
      subtitle: Détails de la version
      anchor: release-3
      items:
        - text: 'Version **3.5.10** le 12 avril 2023 : [Notes de version 3.5]({{< relref "posts/seatable-releases/seatable-release-3-5" >}})'
      template: "3d65a8f8c8ad4482abea"

    - name: "faq"
      weight: 14
      title: Questions fréquemment posées sur le journal des modifications
      subtitle: Tout ce que vous devez savoir
      items:
        - q: Quel est le cycle de publication de SeaTable ?
          a: SeaTable Server est mis à jour régulièrement. Nous publions une nouvelle version majeure (X.0) chaque été et une nouvelle version mineure (5.X) tous les deux à trois mois.
        - q: Comment rester informé des nouvelles versions ou des changements ?
          a: Nous vous recommandons de vous abonner à notre newsletter pour toujours recevoir des informations sur la version la plus récente et la plus sécurisée de SeaTable Server adaptée à vos besoins.
        - q: Existe-t-il différentes versions pour SeaTable Cloud ou SeaTable Server ?
          a: Non, il n'y a qu'une seule version de SeaTable. Nous utilisons la même image Docker pour SeaTable Cloud, que vous pouvez télécharger pour exécuter votre propre serveur.
        - q: Où puis-je télécharger SeaTable ?
          a: 'SeaTable est publié sous forme de conteneur Docker. Vous pouvez obtenir la dernière image sur [Docker Hub](https://hub.docker.com/r/seatable/seatable-enterprise)'
        - q: 'Je souhaite exécuter mon propre serveur SeaTable. Où puis-je obtenir plus d’informations ?'
          a: 'Veuillez consulter le [Manuel d’administration SeaTable](https://admin.seatable.com) pour des instructions sur l’installation de votre propre serveur. Vous pouvez acheter un fichier de licence directement sur notre [page des tarifs]({{< relref "pages/prices" >}}).'
---
