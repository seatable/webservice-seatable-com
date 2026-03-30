---
title: 'Visão geral das automatizações'
date: 2023-01-31
lastmod: '2025-11-05'
categories:
    - 'automationen'
author: 'kgr'
url: '/pt/ajuda/automatizacoes-visao-exemplos-seatable'
aliases:
    - '/pt/ajuda/uebersicht-ueber-automationen'
seo:
    title: 'Automatizações no SeaTable: visão geral e exemplos'
    description: 'Veja como agilizar tarefas com as automações SeaTable: acionadores, ações, registro de execuções e exemplos práticos de uso para melhorar o seu fluxo.'
star: true
weight: 1
---

{{< required-version "Empresa" >}}

As automatizações são uma característica útil do SeaTable que o ajuda a **automatizar os processos de trabalho**. Com a ajuda de automatizações, pode não só **poupar tempo**, mas também **minimizar** o número de **erros humanos** na manutenção dos seus dados, uma vez que as etapas do processo completadas automaticamente já não têm de ser executadas manualmente por um utilizador.

Consequentemente, as automatizações têm um efeito particularmente grande em **grandes conjuntos de dados** em que podem tratar um elevado número de processos de trabalho.

O artigo seguinte destina-se a dar-lhe uma visão geral do tema das automatizações no SeaTable e contém links para os vários artigos de ajuda em torno desta característica.

## O editor de automatização

Pode aceder ao editor de automatização de uma base através do ícone correspondente no cabeçalho da base.

![Acesso ao editor de automatização](images/access-automation-editor.jpg)

O editor de automatização estende-se por toda a largura da janela, permitindo assim uma disposição clara: A **lista de todas as regras de automatização existentes** encontra-se do lado esquerdo. Assim, pode alternar entre duas regras com apenas um clique. Também pode adicionar novas regras e gerir as existentes aqui.

![editor de automatização em ação](images/automation-editor-in-action.gif)

Na área central, pode ver a configuração da automatização atualmente selecionada. Esta é constituída por um **acionador** e uma ou mais **acções**. As definições do acionador ou das acções são apresentadas dinamicamente no lado direito - dependendo do elemento em que acabou de clicar.

Também pode recolher a lista de regras de automatização para criar mais espaço na área central. Outro fator de conveniência é a **altura variável do painel do editor**. Isto permite-lhe ver a vista, os nomes das colunas e os registos de dados enquanto trabalha num automatismo.

## Criar uma automatização

O primeiro passo para processos de trabalho automatizados é a criação de uma automatização. Para garantir que tudo corre de acordo com o planeado e que as regras de automatização criadas têm o efeito desejado, resumimos neste artigo as informações mais importantes para si.

Aprenda [aqui]({{< relref "help/base-editor/automationen/anlegen-einer-automation" >}}) como criar uma automatização.

## Gerir automatizações

Pode, evidentemente, gerir automatizações activas que já foram criadas. Neste artigo mostrar-lhe-emos quais as configurações que pode fazer ao automatizar os seus processos de trabalho.

Saiba mais sobre a gestão das automatizações [aqui]({{< relref "help/base-editor/automationen/automationen-verwalten-und-gruppieren" >}}).

## Funcionalidade das automatizações

Este artigo explica as bases de como funcionam as automatizações no SeaTable e é por isso adequado como uma **introdução ao tema das automatizações**.

Saiba mais sobre como as automatizações funcionam [aqui]({{< relref "help/base-editor/automationen/funktionsweise-von-automationen" >}}).

## Acionadores de automatização

Os desencadeadores de automatização são a primeira das duas componentes essenciais das automatizações. Os gatilhos, que pode definir individualmente para cada automatização, desencadeiam diferentes tipos de acções automatizadas.

Saiba mais sobre os acionadores de automação [aqui]({{< relref "help/base-editor/automationen/automations-trigger" >}}).

## Acções de automatização

As acções automatizadas representam a segunda das duas componentes essenciais das automatizações. As acções são desencadeadas pelos eventos de desencadeamento definidos. Dependendo do gatilho, a SeaTable pode realizar diferentes acções de automatização.

Saiba mais sobre acções de automatização [aqui]({{< relref "help/base-editor/automationen/automations-aktionen" >}}).

## Mostrar o registo de execução de uma automatização

Para verificar a execução das automatizações, tem a opção de exibir o registo de execução para cada regra de automatização. Neste registo, pode visualizar informações sobre cada execução de automatização.

Saiba mais sobre o registo de execução de uma automatização [aqui]({{< relref "help/base-editor/automationen/ausfuehrungslog-einer-automation-anzeigen" >}}).

## Parar as automatizações

As automatizações activas de que já não necessita durante um determinado período de tempo podem simplesmente ser pausadas e reactivadas conforme necessário.

Aprenda [aqui]({{< relref "help/base-editor/automationen/automationen-stoppen" >}}) como parar as automatizações.

## Eliminar automatizações

Também pode apagar as automatizações que já não são necessárias. É favor notar que não é possível restaurar as automatizações apagadas.

Saiba [aqui]({{< relref "help/base-editor/automationen/automationen-loeschen" >}}) como apagar as automatizações.

## Bloquear as filas com uma automatização

Com a ajuda das automatizações, já não tem de bloquear as filas nas suas tabelas manualmente, mas pode ter este bloqueio efectuado automaticamente. Isto é muito útil se quiser evitar sempre que uma fila seja editada mais depois de um certo tempo (por exemplo, quando um processo foi concluído).

Aprenda [aqui]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-sperren" >}}) como bloquear as filas com uma automatização.

## Acrescentar linhas via automatização

Com a ajuda de automatizações, já não tem de adicionar manualmente linhas com determinadas entradas às suas tabelas, mas pode ter estas etapas executadas automaticamente. Isto é particularmente vantajoso se quiser automatizar vários passos do processo nas suas tabelas.

Aprenda [aqui]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-hinzufuegen" >}}) como adicionar linhas através da automatização.

## Adicionar entradas a outras tabelas através de automatização

Com a ajuda de automatizações, já não tem de fazer entradas noutras tabelas manualmente, mas pode ter estas etapas executadas automaticamente. A grande vantagem disto é que o gatilho não tem de estar na mesma tabela que a acção que é desencadeada. Esta automatização é particularmente vantajosa se utilizar tabelas diferentes, cujo conteúdo esteja relacionado entre si.

Aprenda [aqui]({{< relref "help/base-editor/automationen/beispiel-eintraege-in-andere-tabellen-per-automation-hinzufuegen" >}}) como adicionar entradas a outras tabelas através da automatização.

## Envio de e-mails por automatização

Com a ajuda de automatizações, já não tem de enviar e-mails manualmente a utilizadores seleccionados, mas pode mandar enviá-los automaticamente. Isto é especialmente útil se, por exemplo, quiser informar imediatamente os utilizadores sobre alterações aos dados de certas tabelas.

Descubra [aqui]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}}) como pode enviar e-mails através de automatização.

## Ligação de entradas via automatização

Com a ajuda de automatizações, já não tem de ligar manualmente as entradas nas suas tabelas, mas pode ter estas etapas executadas automaticamente. Isto é útil se precisar de certos dados em várias tabelas.

Aprenda [aqui]({{< relref "help/base-editor/automationen/beispiel-verlinken-von-eintraegen-per-automation" >}}) como ligar as entradas via automatização.

## Porque não consigo encontrar as automatizações na minha base?

Não consegue encontrar a função de automatização nas suas bases? Pode ter algo a ver com a sua assinatura SeaTable.

Descubra [aqui]({{< relref "help/base-editor/automationen/warum-finde-ich-in-meiner-base-die-automationen-nicht" >}}) porque pode ser este o caso.
