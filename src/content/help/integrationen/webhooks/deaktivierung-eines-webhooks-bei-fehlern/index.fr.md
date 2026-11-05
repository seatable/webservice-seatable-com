---
title: "Désactiver un webhook en cas d'erreur"
date: 2023-02-28
lastmod: '2026-11-05'
categories:
    - 'webhooks'
author: 'cdb'
url: '/fr/aide/desactivation-webhooks-erreurs'
aliases:
    - '/fr/aide/deaktivierung-eines-webhooks-bei-fehlern'
seo:
    title: 'Désactivation des webhooks sur erreurs dans SeaTable'
    description: 'Guide SeaTable : découvrez comment les webhooks sont désactivés après plusieurs erreurs HTTP et comment les réactiver facilement.'

---

Si un webhook est configuré pour une Base SeaTable, SeaTable envoie une _requête POST_ à l'URL cible à chaque modification. Normalement, le système récepteur renvoie un message d'état sous la forme d'un [code d'état à trois chiffres](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes), que SeaTable traite ensuite et désactive le webhook si nécessaire.

## Les codes d'état HTTP les plus courants

Il existe toute une série de codes de statut, mais il suffit de connaître les réactions les plus fréquentes :

- **200** - Successful
- **400** - Requête incorrecte
- **403** - Forbidden
- **500 - 511** - Erreurs de serveur

Le code d'état de loin le plus important est 200. Il indique que la demande a été reçue et traitée avec succès. SeaTable considère tous les codes d'état de 200 à 299 comme un succès.

## SeaTable désactive les webhooks en cas d'erreur

Lorsque SeaTable envoie un webhook, il attend un retour sous la forme d'un code d'état HTTP. En cas d'erreur, le webhook passe à l'état _invalide_ et son exécution est interrompue. Le moment où cela se produit dépend du type d'erreur :

| Erreur                         | Exemples                                                                                   | Désactivation                        |
| ------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------ |
| **Réponse erronée ou absente** | Code d'état en dehors de la plage 200 à 299, pas de réponse sous 30 secondes               | après cinq erreurs consécutives      |
| **Livraison impossible**       | Nom impossible à résoudre, connexion refusée, erreur de certificat, URL cible non publique | immédiatement dès la première erreur |

Les redirections ne sont pas suivies : un code d'état comme 301 ou 302 compte comme une erreur. Une livraison réussie remet le compteur d'erreurs à zéro.

![Hoc Web non valide](images/invalid-webhook.png)

{{< warning headline="Uniquement des URL cibles publiques depuis la version 7.0.10" text="Depuis la version 7.0.10 de SeaTable, l'URL cible doit pointer vers une adresse publique. Les webhooks vers des adresses internes ne sont pas livrés et sont immédiatement désactivés." />}}

## Les livraisons échouées ne sont pas renouvelées

SeaTable ne renvoie pas un webhook si la livraison échoue. Les modifications effectuées pendant qu'un webhook est désactivé ne sont pas non plus livrées ultérieurement. Si votre système a besoin de données complètes, vous devriez donc [synchroniser les données régulièrement]({{< relref "help/integrationen/webhooks/webhook-bei-mehreren-gleichzeitigen-aenderungen" >}}).

## Réactiver un webhook inactif

Un webhook non valide peut être réactivé à tout moment. Passez à l'édition du webhook non valide en cliquant sur {{< seatable-icon icon="dtable-icon-rename" color="grey" >}} et enregistrez à nouveau le webhook sans effectuer de modification. Le webhook est alors immédiatement réactivé.

Pour éviter une nouvelle désactivation, le système récepteur doit traiter les webhooks de manière fiable et renvoyer le code d'état 200 dans un délai de 30 secondes.
