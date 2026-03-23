---
title: 'Visão geral de todas as integrações em e com SeaTable'
date: 2023-03-22
lastmod: '2023-07-19'
categories:
    - 'skripte-api-integrationen'
author: 'cdb'
url: '/pt/ajuda/integracoes-seatable'
aliases:
    - '/pt/ajuda/integrationen-seatable'
seo:
    title: 'Integrações SeaTable: API, webhooks, automação e plugins'
    description: 'Conheça todas as integrações do SeaTable: API REST, webhooks, JS/Python, e-mail, Zapier, Make e plugins próprios para fluxos eficientes.'
---

As integrações alargam a forma como se pode trabalhar e interagir com o SeaTable. Por exemplo, as integrações permitem-lhe aceder aos seus dados dentro da SeaTable com outras ferramentas e soluções de software, ou pode conceber fluxos de trabalho que automatizam determinados passos. Alternativamente, pode desenvolver as suas próprias aplicações ou programas que utilizam SeaTable como backend.

Talvez já se tenha apercebido. Não existe "uma" integração SeaTable, mas dependendo da área de aplicação, estão disponíveis outras integrações. Este artigo dá-lhe uma visão geral das diferentes integrações e possibilidades.

## Visão geral das integrações disponíveis

A SeaTable oferece actualmente cinco opções de integração diferentes, que serão apresentadas em mais detalhe abaixo.

- Javascript e Python
- Integrações dentro da SeaTable
- SeaTable API
- Gancho Web
- Plataformas de automatização

## Roteiros em SeaTable

SeaTable permite-lhe executar scripts personalizados em JavaScript e Python numa base. Isto permite aos utilizadores que têm alguma experiência de programação automatizar etapas de trabalho ou tarefas recorrentes. Os scripts podem ser iniciados manualmente, usando um botão ou através de automatização.

## Integrações dentro da SeaTable

Numa base, a SeaTable oferece a possibilidade de activar **integrações de terceiros**. Actualmente, apenas a integração com uma conta de correio electrónico está disponível dentro desta integração. Esta integração de e-mail permite o envio de e-mails a partir do SeaTable utilizando automatismos ou botões. Outra opção é activar a sincronização de correio electrónico, o que torna todos os e-mails da conta de correio electrónico disponíveis no SeaTable.

## SeaTable API

O SeaTable API fornece uma interface universal através da qual se pode interagir com os dados dentro do SeaTable utilizando qualquer software ou linguagem de programação. Por exemplo, pode utilizar o SeaTable API para escrever automaticamente os dados capturados noutro software para o SeaTable. Ou se quiser construir uma interface personalizada para alguns dados SeaTable, pode usar a API para aceder directamente aos dados sem a interface web.

## Gancho Web

Os ganchos da Web são criados dentro da SeaTable para uma Base de cada vez. Uma vez criado um gancho web, o SeaTable envia uma mensagem para um URL à sua escolha sempre que é feita uma alteração nessa base. Neste URL, o software recebe os ganchos da Web e processa-os. Dependendo da alteração que foi feita na Base, pode realizar uma actividade de seguimento correspondente.

Um exemplo típico de um gancho da web seria o controlo do estado de pagamento de uma factura ou subscrição. Assim que se define uma factura para o estado _Pago_ em SeaTable, outro software deve realizar uma acção correspondente. Poderia facilmente implementá-la com um gancho para a Web. Cada alteração às facturas no SeaTable é enviada via webhook para o outro software e apenas reage à mensagem de estado que é relevante para si.

Os ganchos da Web são normalmente utilizados quando não se pretende consultar regularmente o estado de uma informação, mas quando se pretende ser informado proactivamente quando ocorrem alterações. Para consultas de estado regulares, a API da SeaTable é tipicamente a melhor escolha.

## Plataformas de automatização

Na vida quotidiana, as pessoas trabalham frequentemente não só com um software, mas com muitas soluções ao mesmo tempo. Os contactos comerciais são armazenados num CRM como o Hubspot ou Pipedrive, os compromissos e e-mails são armazenados no Google, as newsletters são enviadas com [Mailchimp](https://mailchimp.com/) ou Brevo(https://www.brevo.com/). Muitas vezes, deseja-se que um evento num software conduza a uma actividade noutro software. Assim, se enviar uma nova newsletter com Brevo, envia automaticamente um post no Facebook. Ou se alguém enviar um pedido de marcação no seu website, que os dados de contacto são automaticamente transferidos para o seu CRM.

É precisamente nestes casos que uma das muitas plataformas de automatização o pode ajudar. Estas ajudam-no a ligar duas ou mais soluções de software sem experiência de programação e a reagir a certos gatilhos com certas acções.

Actualmente, as seguintes plataformas de automação oferecem apoio ao SeaTable:

- [Zapier](https://zapier.com/apps/seatable/integrations)
- [Marca (anteriormente Integromat)](https://www.make.com/en/integrations/seatable)
- [n8n](https://n8n.io/integrations/seatable/)
- [Locoia](https://www.locoia.com/connector-integrations/)
- [Integrar de forma integrada](https://integrately.com/integrations/seatable)

## Desenvolvimento próprio

O SeaTable é do seu agrado, mas falta-lhe uma ou outra função? Pretende automatizar determinadas tarefas e pretende integrar o SeaTable em sistemas existentes? Com o SeaTable tem todas estas possibilidades! A capacidade de integrar e alargar faz parte do ADN do SeaTable.

Os plugins do SeaTable Market baseiam-se no Realtime SDK do SeaTable. Assim, pode desenvolver os seus próprios plugins com pouco esforço. [Pode encontrar todos os detalhes sobre o SeaTable SDK na documentação do programador](https://developer.seatable.com). Pode importar os seus próprios plugins através do Gestor de Plugins.

A integração do SeaTable com outros sistemas quase não tem limites graças ao poderoso REST API do SeaTable. Toda a informação sobre o SeaTable API pode ser encontrada na [documentação API do SeaTable](https://api.seatable.com).

Tanto para os plug-ins como para a integração, utiliza linguagens de programação bem conhecidas, como o JavaScript e o Python. Os seus programadores podem começar a trabalhar imediatamente.
