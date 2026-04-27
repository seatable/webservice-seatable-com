---
title: 'Les raisons de deux Community Nodes : SeaTable et SeaTable-Admin'
date: '2025-10-03'
seo:
    title: 'Nœuds SeaTable dans n8n : différence entre le nœud utilisateur et le nœud administrateur'
    description: 'SeaTable dans n8n : utilisez le nœud utilisateur pour les opérations de données avec un token API et le nœud admin pour les tâches de gestion avec des droits admin.'
categories:
    - 'n8n-integration'
url: '/fr/aide/pourquoi-deux-community-nodes'
---

Dans n8n, il existe deux Community Nodes SeaTable distincts, chacun développé pour différents domaines d'utilisation, vous permettant de concevoir vos workflows de manière précise et sécurisée.

## 1. Nœud SeaTable – Interaction avec vos données

Le nœud SeaTable est le standard éprouvé lorsqu'il s'agit de travailler avec les données de vos bases SeaTable. Que vous souhaitiez ajouter de nouveaux enregistrements, mettre à jour les existants ou supprimer des entrées, ce nœud le rend possible.

Il est disponible en version Core et en version Community dans n8n. Plus de détails dans [cet article]({{< relref "help/integrationen/n8n/n8n-community-vs-core" >}}).

Pour l'utiliser, vous avez simplement besoin d'un **token API SeaTable** qui vous donne accès aux données de votre base.

## 2. Nœud SeaAdmin – Contrôle administratif

Si vous souhaitez effectuer des tâches administratives dans SeaTable, le nœud SeaAdmin est le choix parfait.

Avec lui, vous pouvez facilement :

- Consulter toutes les bases disponibles ou spécifiquement les bases d'un utilisateur donné
- Vérifier les journaux système
- Créer, supprimer des comptes utilisateurs ou réinitialiser des mots de passe

Pour ces fonctions, vous aurez besoin d'un **token de compte avec des droits d'administrateur**.

## Pourquoi cette séparation claire ?

En répartissant les fonctions dans deux nœuds, chaque fonction reste exactement là où elle doit être : les **opérations de données pour les utilisateurs** et la **gestion et le contrôle pour les administrateurs**. Cela garantit plus de clarté, de sécurité et une manipulation plus facile dans vos workflows n8n.

## Conclusion

- Le **nœud SeaTable** est votre outil pour toutes les opérations de données quotidiennes avec un token API.
- Le **nœud SeaAdmin** vous accompagne dans les tâches administratives avec un token de compte administrateur.

Ainsi, vous offrez dans n8n la solution optimale pour les deux rôles : efficace, sécurisée et clairement structurée.
