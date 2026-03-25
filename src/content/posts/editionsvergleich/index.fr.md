---
title: 'Comparaison entre les éditions Developer et Enterprise de SeaTable'
description: "SeaTable est disponible en deux éditions différentes. L'édition Entreprise offre toutes les fonctionnalités et est donc utilisée pour les systèmes SeaTable en nuage et dédiés, tandis que l'édition Développeur est gratuite et constitue une base de données flexible pour les développeurs."
color: '#069214'
categories:
    - 'product-features'
lastmod: '2025-07-22'
url: '/fr/comparatif-editions'
aliases:
    - /fr/editionsvergleich
seo:
    title: 'SeaTable : Developer et Enterprise Edition comparées'
    description: "SeaTable propose deux éditions No-Code auto-hébergées : Enterprise et Developer. Découvrez fonctionnalités et cas d'usage."
---

SeaTable Server est SeaTable pour votre propre serveur. En installant SeaTable sur votre propre infrastructure, vous avez un contrôle total sur l'emplacement de vos données et sur les personnes qui y ont accès. SeaTable est donc également recommandé pour les cas d'application dans lesquels vous ne souhaitez pas confier vos données à l'extérieur. Vous pouvez également utiliser SeaTable Server uniquement sur votre réseau local, sans possibilité d'accès via Internet.

## SeaTable Server est disponible en deux éditions différentes

### SeaTable Server Enterprise Edition

SeaTable Server Enterprise Edition est la solution [sans code]({{< relref "posts/20250307-low-code" >}}) idéale pour les équipes et les organisations de toutes tailles qui souhaitent bénéficier de toutes les fonctionnalités et d'un contrôle total des données. Seule l'édition Enterprise offre la possibilité d'utiliser une authentification externe via LDAP ou SAML. De même, vous ne trouverez les autorisations de partage et les automatisations avancées que dans cette édition.  
Vous pouvez obtenir à tout moment une licence SeaTable Enterprise pour un maximum de trois utilisateurs. Vous trouverez le formulaire d'enregistrement correspondant [sous ce lien]({{< relref "pages/product/seatable-server" >}}). L'installation s'effectue conformément au [manuel d'administration](https://admin.seatable.com) à l'aide de Docker.

### SeaTable Server Developer Edition

SeaTable Server Developer Edition s'adresse en premier lieu aux développeurs qui souhaitent utiliser SeaTable comme base de données flexible et qui n'auront peut-être pas recours à l'application frontale. L'édition pour développeurs se distingue par la puissance de l'[API SeaTable](https://api.seatable.com/), les applications pour les différentes plateformes d'automatisation et la prise en charge complète de tous les types de colonnes. L'édition pour développeurs peut être utilisée gratuitement. Vous trouverez [ici](https://admin.seatable.com) les instructions d'installation.

## Différences dans la comparaison

|                                        | Édition pour développeurs                                                                          | Édition Entreprise                                                                             |
| -------------------------------------- | -------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| Plate-forme et environnement           |                                                                                                    |                                                                                                |
| Système d'exploitation serveur         | Linux                                                                                              | Linux                                                                                          |
| Méthode d'installation                 | Docker                                                                                             | Docker                                                                                         |
| Docker Images                          | [Docker Hub](https://hub.docker.com/r/seatable/seatable-developer)                                 | [Docker Hub](https://hub.docker.com/r/seatable/seatable-enterprise)                             |
| Licence                                |                                                                                                    |                                                                                                |
| Type de licence                        | [hybride (open source et propriétaire)](https://admin.seatable.com/introduction/requirements/#license)                  | [propriétaire]({{< relref "pages/legal/terms-of-service" >}})                                  |
| Modèle de prix de licence              | Gratuit                                                                                            | Basé sur l'utilisateur                                                                         |
| Limites                                |                                                                                                    |                                                                                                |
| Bases illimitées                       | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                  |
| Tables illimitées                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                  |
| Lignes illimitées                      | {{< icon icon="circle-check" class="text-seatable-orange" >}} **(mais pas de backend d'archives)** | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                  |
| Mémoire illimitée                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                  |
| Utilisateurs illimités                 | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}} **(licence requise)**            |
| Versionnement (snapshots)              | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                  |
| Saisie et traitement des données       |                                                                                                    |                                                                                                |
| 24 types de colonnes                   | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                  |
| Vues                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                  |
| Vues privées                           |                                                                                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                  |
| Filtre                                 | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                  |
| Regroupement                           | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                  |
| Triage                                 | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                  |
| Formatage conditionnel                 | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                  |
| Formulaires web                        | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                  |
| Ensembles de données partagés          | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                  |
| Traitements de données                 | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                  |
| Statistiques                           | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                  |
| Importation à partir de CSV et XLSX    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                  |
| Exportation en CSV et XLSX             | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                  |
| Notifications                          | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                  |
| Automatismes                           | {{< icon "circle-xmark" >}}                                                                        | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                  |
| Fonction d'archivage                   | {{< icon "circle-xmark" >}}                                                                        | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                  |
| Support JavaScript                     | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                  |
| Support de Python                      | {{< icon icon="circle-check" class="text-seatable-orange" >}} _(installation séparée requise)_     | {{< icon icon="circle-check" class="text-seatable-orange" >}} _(installation séparée requise)_ |
| Collaboration                          |                                                                                                    |                                                                                                |
| Collaboration en temps réel            | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                  |
| Liens externes                         | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                  |
| Liens d'invitation                     | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                  |
| Partage des bases                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                  |
| Afficher le communiqué                 | {{< icon "circle-xmark" >}}                                                                        | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                  |
| Autorisations de partage individuelles | {{< icon "circle-xmark" >}}                                                                        | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                  |
| Autorisations de table                 | {{< icon "circle-xmark" >}}                                                                        | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                  |
| Autorisations des colonnes             | {{< icon "circle-xmark" >}}                                                                        | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                  |
| Verrouillage de la ligne               | {{< icon "circle-xmark" >}}                                                                        | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                  |
| Plugins et extensions                  |                                                                                                    |                                                                                                |
| Calendrier                             | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                  |
| Ligne du temps                         | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                  |
| Galerie                                | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                  |
| Kanban                                 | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                  |
| Cartes                                 | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                  |
| Conception des pages                   | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                  |
| Statistiques avancées                  | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                  |
| Requête SQL                            | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                  |
| Intégration ONLYOFFICE                 | {{< icon "circle-xmark" >}}                                                                        | {{< icon icon="circle-check" class="text-seatable-orange" >}} _(installation séparée requise)_ |

---

|                                               | Édition pour développeurs                                     | Édition Entreprise                                            |
| --------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| API et options d'intégration                  |                                                               |                                                               |
| API REST                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Zapier                                        | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Integromat                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| n8n                                           | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Locoia                                        | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Marquage et personnalisation                  |                                                               |                                                               |
| Modèles propres                               | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Propre URL                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Propre logo                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Logo dans le formulaire web                   | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Image de couverture dans le formulaire web    | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| "Masquer "Powered by                          | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Gestion des utilisateurs et des autorisations |                                                               |                                                               |
| Base de données utilisateur locale            | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Authentification à 2 facteurs                 | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Authentification via AD/LDAP                  | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Authentification unique via SAML              | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Rôles des utilisateurs                        | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Backend et évolutivité                        |                                                               |                                                               |
| Support S3                                    | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Assistance aux clusters                       | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |

## Différences entre les versions

Les éditions **SeaTable Enterprise** et **Developer** peuvent être téléchargées facilement depuis Docker Hub :

- https://hub.docker.com/r/seatable/seatable-enterprise
- https://hub.docker.com/r/seatable/seatable-developer

**La principale différence entre les éditions réside dans leur gestion des versions :**

L'édition Developer fournit uniquement une version de base, par exemple **5.3.0**, basée sur la première version de l'édition Enterprise correspondante. En revanche, l'édition Enterprise est continuellement développée et maintenue. Vous y trouverez donc toujours la dernière version disponible, par exemple **5.3.12**.

Les problèmes détectés dans l'édition Developer ne sont corrigés qu'avec la prochaine version majeure (par ex. de 5.3.x à 5.4.0).

## Différences en matière de tests et de support

L'**édition SeaTable Enterprise** est rigoureusement testée afin de garantir une utilisation aussi stable et fiable que possible. En revanche, **aucun test systématique** n'est effectué pour l'**édition Developer**.

Le **support payant** est exclusivement disponible pour l'édition Enterprise ; **aucun support officiel** n’est proposé pour l'édition Developer.

Si vous avez des questions concernant l'édition Developer, nous vous recommandons d'utiliser le [forum communautaire SeaTable](https://forum.seatable.com). Notez cependant que la majorité des discussions portent sur l'édition Enterprise, car elle est plus largement utilisée et officiellement prise en charge.
