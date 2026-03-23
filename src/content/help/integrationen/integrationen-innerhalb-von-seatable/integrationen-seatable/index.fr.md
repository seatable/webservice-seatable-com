---
title: 'Aperçu de toutes les intégrations dans et avec SeaTable'
date: 2023-03-22
lastmod: '2023-07-19'
categories:
    - 'skripte-api-integrationen'
author: 'cdb'
url: '/fr/aide/integrations-seatable'
aliases:
    - '/fr/aide/integrationen-seatable'
seo:
    title: 'Intégrations SeaTable : API, webhooks, automatisations et extensions'
    description: 'Découvrez toutes les intégrations SeaTable : API REST, webhooks, JS/Python, e-mail, Zapier, Make et plugins pour des workflows efficaces.'
---

Les intégrations étendent la manière dont vous pouvez travailler et interagir avec SeaTable. Les intégrations vous permettent par exemple d'accéder à vos données dans SeaTable avec d'autres outils et solutions logicielles, ou de concevoir des processus de travail qui automatisent certaines étapes. Vous pouvez également développer vos propres applications ou programmes qui utilisent SeaTable comme backend.

Vous l'avez peut-être déjà remarqué. Il n'existe pas "une" intégration SeaTable, mais d'autres intégrations sont possibles en fonction du domaine d'application. Cet article a pour but de vous donner un aperçu des différentes intégrations et possibilités.

## Aperçu des intégrations disponibles

Actuellement, SeaTable propose cinq possibilités d'intégration différentes, qui seront présentées plus en détail par la suite.

- Javascript et Python
- Intégrations au sein de SeaTable
- API SeaTable
- Webhooks
- Plateformes d'automatisation

## Scripts dans SeaTable

SeaTable permet d'exécuter des scripts JavaScript et Python personnalisés dans une base. Les utilisateurs disposant d'une certaine expérience de la programmation peuvent ainsi automatiser des étapes de travail ou des tâches répétitives. Les scripts peuvent être lancés manuellement, à l'aide d'un bouton ou par une automatisation.

## Intégrations au sein de SeaTable

Dans une base, SeaTable offre la possibilité d'activer une **intégration tierce**. Actuellement, seule l'intégration avec un compte e-mail est disponible dans le cadre de cette intégration. Cette intégration d'e-mails permet d'envoyer des e-mails à partir de SeaTable à l'aide d'automatismes ou de boutons. Une autre possibilité est d'activer la synchronisation des e-mails, ce qui permet de disposer de tous les e-mails du compte de messagerie dans SeaTable.

## API SeaTable

L'API SeaTable est une interface universelle qui vous permet d'interagir avec les données de SeaTable à l'aide de n'importe quel logiciel ou langage de programmation. Par exemple, l'API SeaTable permet d'écrire automatiquement dans SeaTable des données saisies dans un autre logiciel. Ou si vous souhaitez créer une interface personnalisée pour certaines données SeaTable, vous pouvez utiliser l'API pour accéder directement aux données sans passer par l'interface web.

## Webhooks

Les webhooks sont configurés dans SeaTable pour une base à la fois. Une fois qu'un webhook est configuré, chaque fois qu'un changement est effectué dans cette base, SeaTable envoie un message à une URL que vous avez choisie. À cette URL, un logiciel reçoit les webhooks et les traite. En fonction de la modification apportée à la base, vous pouvez exécuter une activité de suivi correspondante.

Un exemple typique de webhook serait le suivi du statut de paiement d'une facture ou d'un abonnement. Dès que vous attribuez le statut _Payé_ à une facture dans SeaTable, un autre logiciel doit effectuer une action correspondante. Vous pourriez réaliser cela très facilement avec un webhook. Chaque modification apportée aux factures dans SeaTable est envoyée par webhook à l'autre logiciel, qui ne réagit qu'au message de statut qui vous concerne.

Les webhooks sont typiquement utilisés lorsque vous ne souhaitez pas consulter régulièrement le statut d'une information, mais que vous souhaitez être informé de manière proactive en cas de modification. L'API SeaTable est typiquement adaptée à la consultation régulière de l'état.

## Plateformes d'automatisation

Dans la vie de tous les jours, on ne travaille souvent pas avec un seul logiciel, mais avec plusieurs solutions à la fois. Les contacts professionnels sont enregistrés dans un CRM comme Hubspot ou Pipedrive, les rendez-vous et les e-mails sont sur Google, les newsletters sont envoyées avec [Mailchimp](https://mailchimp.com/) ou Brevo(https://www.brevo.com/). Souvent, on souhaite qu'un événement dans un logiciel entraîne une activité dans un autre logiciel. Ainsi, lorsque vous envoyez une nouvelle newsletter avec Brevo, vous publiez automatiquement un message sur Facebook. Ou si quelqu'un envoie une demande de rendez-vous sur votre site web, que les données de contact soient automatiquement transférées dans votre CRM.

C'est précisément dans ces cas-là qu'une des nombreuses plateformes d'automatisation peut vous aider. Celles-ci vous aident, sans expérience de la programmation, à relier entre elles deux ou plusieurs solutions logicielles et à réagir à certains déclencheurs par certaines actions.

Actuellement, les plateformes d'automatisation suivantes proposent un support pour SeaTable :

- [Zapier](https://zapier.com/apps/seatable/integrations)
- [Make (formerly Integromat)](https://www.make.com/en/integrations/seatable)
- [n8n](https://n8n.io/integrations/seatable/)
- [Locoia](https://www.locoia.com/connector-integrations/)
- [Intégralement](https://integrately.com/integrations/seatable)

## Développement interne

Vous avez apprécié SeaTable, mais il vous manque l'une ou l'autre fonction ? Vous souhaitez automatiser certaines tâches et vous voulez intégrer SeaTable dans des systèmes existants ? Avec SeaTable, vous avez toutes ces possibilités ! La capacité d'intégration et l'extensibilité font partie de l'ADN de SeaTable.

Les plugins de SeaTable Market sont basés sur le Realtime SDK de SeaTable. Celui-ci vous permet de développer vos propres plug-ins avec un minimum d'efforts. Vous trouverez tous les détails sur le SDK de SeaTable dans la [documentation destinée aux développeurs](https://developer.seatable.com). L'importation de vos propres plugins se fait via le Plugin Manager.

L'intégration de SeaTable dans d'autres systèmes est pratiquement illimitée grâce à la puissante API REST de SeaTable. Pour plus d'informations sur l'API SeaTable, consultez la [documentation de l'API SeaTable](https://api.seatable.com).

Tant pour les plug-ins que pour l'intégration, vous utilisez des langages de programmation connus comme JavaScript et Python. Vos développeurs peuvent se lancer immédiatement.
