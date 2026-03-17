---
title: 'Exemples et conseils'
description: "Exemples pratiques et conseils pour une utilisation efficace du plugin de chat IA dans SeaTable."
weight: 4
url: '/fr/aide/plugin-chat-ia-exemples-et-conseils'
seo:
    title: 'Plugin de chat IA : exemples et conseils pour de bonnes questions'
    description: "Apprenez à tirer le meilleur parti du plugin de chat IA dans SeaTable avec des exemples concrets : interroger, analyser et modifier vos données."
---

Le plugin de chat IA comprend le langage naturel et travaille directement avec les données de votre base. Dans cet article, vous trouverez des exemples concrets pour des cas d'utilisation courants ainsi que des conseils pour obtenir de meilleurs résultats. Des recommandations générales sur la formulation de bonnes questions sont également disponibles dans l'article [Comment poser de bonnes questions]({{< relref "help/ai/ai-agents/good-questions" >}}).

## Interroger des données

Le cas d'utilisation le plus courant : vous posez une question et le chat vous renvoie les entrées correspondantes de votre base.

> *« Montre-moi toutes les tâches ouvertes dont l'échéance est cette semaine. »*

> *« Combien de clients avons-nous en France ? »*

> *« Quelles factures ne sont pas encore réglées ? »*

> *« Y a-t-il des projets sans responsable attribué ? »*

Plus vous nommez précisément les tableaux et les colonnes, plus la réponse sera précise. Si vous n'êtes pas sûr des colonnes existantes, demandez simplement :

> *« Décris la structure de ma base. »*

## Analyser des données

Le chat peut non seulement afficher vos données, mais aussi les évaluer, les regrouper et les résumer.

> *« Quel a été le chiffre d'affaires total du dernier trimestre, ventilé par commercial ? »*

> *« Résume les demandes d'assistance de la semaine dernière. »*

> *« Quels produits ont été les plus commandés ? »*

> *« Comment se répartissent les tickets ouverts par priorité ? »*

Ce type d'analyses fonctionne particulièrement bien lorsque votre base contient des données bien entretenues. En cas de valeurs manquantes ou incohérentes, le chat le signale généralement.

## Créer et modifier des données

Le plugin de chat IA peut également créer, modifier, lier et supprimer des entrées. Formulez de manière aussi claire que possible quel tableau, quelles colonnes et quelles valeurs sont concernés.

### Créer de nouvelles entrées

> *« Crée un nouveau contact : Nom "Müller GmbH", Ville "Hambourg", Statut "Prospect". »*

> *« Crée une entrée de suivi dans le tableau Activités pour chaque affaire ouverte. »*

### Modifier des entrées existantes

> *« Passe le statut de toutes les tâches en retard à "Escaladé". »*

> *« Change la priorité du ticket #412 à "Haute". »*

### Lier et supprimer des entrées

> *« Lie toutes les factures au client correspondant dans le tableau Contacts. »*

> *« Supprime toutes les entrées de test du tableau Brouillons. »*

Lors de la suppression, le chat demande une confirmation avant l'exécution par mesure de sécurité. Vérifiez tout de même au préalable avec une question de lecture si les bonnes entrées sont concernées.

## Conseils pour de meilleurs résultats

**Commencez par des questions de lecture.** Avant de faire modifier des données, vérifiez d'abord que le chat trouve les bonnes entrées. Demandez donc d'abord *« Quelles tâches sont en retard ? »* avant de dire *« Passe le statut à Escaladé. »*

**Décomposez les tâches complexes.** Pour les demandes en plusieurs étapes, vous obtiendrez plus rapidement des résultats en procédant étape par étape. Le chat conserve le contexte de la conversation et vous pouvez vous appuyer sur les réponses précédentes.

**Utilisez les noms de tableaux et de colonnes.** L'orthographe exacte n'est pas nécessaire, mais les bons termes aident le chat à interpréter correctement votre question.

**Exploitez le contexte.** Après une requête, vous pouvez faire référence aux résultats précédents avec « ceux-ci », « parmi eux » ou « les mêmes », sans tout répéter.

## Ce qui ne fonctionne pas

Le plugin de chat IA travaille exclusivement avec les données de votre base SeaTable. Les éléments suivants ne sont pas possibles :

- **Interroger des données inexistantes.** Si une colonne ou un tableau n'existe pas, le chat ne peut pas fournir de réponse. Il n'invente pas de données.
- **Actions en dehors de SeaTable.** Le chat ne peut pas envoyer d'e-mails, interroger des systèmes externes ni ouvrir des fichiers.
- **Opérations de masse très importantes.** Les requêtes individuelles visant à créer ou modifier simultanément des centaines d'entrées peuvent atteindre leurs limites. Décomposez ces tâches en étapes plus petites.
