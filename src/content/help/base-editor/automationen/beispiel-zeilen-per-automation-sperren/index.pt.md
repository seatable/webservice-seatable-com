---
title: 'Bloquear linhas via automatização'
date: 2023-01-27
lastmod: '2023-03-31'
categories:
    - 'beispiel-automationen'
author: 'nsc2'
url: '/pt/ajuda/bloquear-linhas-automacao'
aliases:
    - '/pt/ajuda/zeilen-per-automation-sperren'
seo:
    title: 'Bloquear linhas no SeaTable automaticamente: tutorial'
    description: 'Saiba como bloquear linhas via automatização – defina acionadores e condições e restrinja facilmente a edição das tabelas para toda a equipa.'
---

Com a ajuda de automatizações, já não tem de bloquear manualmente as linhas nas suas tabelas, mas pode fazer com que o [bloqueio de linhas]({{< relref "help/base-editor/zeilen/sperren-einer-zeile" >}}) seja executado automaticamente. Isto é muito útil se quiser evitar sempre que uma linha continue a ser editada após um determinado momento (por exemplo, quando uma operação é concluída).

![Bloquear uma linha com uma automatização](images/lock-row-with-an-automation.png)

{{< warning  headline="Desbloqueio apenas possível manualmente"  text="As linhas bloqueadas com uma automatização **não** podem ser **desbloqueadas** da mesma forma. Isto só é possível manualmente e com os **direitos de administrador** necessários." />}}

## Criar a automatização

1. Nas opções da base, clique em {{< seatable-icon icon="dtable-icon-rule" >}} e depois em **Regras de automatização**.
2. Clique em **Adicionar regra**.
3. **Dê um nome** à automatização e defina a **tabela** e a **vista** em que deve ter efeito.
4. Defina um **evento de disparo** que desencadeie a automatização.
5. Clique em **Adicionar ação** e selecione **Bloquear registro** como ação automatizada.

![Seleção da ação automatizada: "Bloquear registro"](images/lock-record.png)

6. Confirme com **Submeter**.

{{< warning headline="Nota importante" >}}

A ação automatizada **Bloquear registro** só está disponível para os seguintes eventos de disparo:

- Quando uma linha é alterada
- Quando uma linha é adicionada
- Numa hora programada para entradas que preencham determinadas condições

{{< /warning >}}

## Exemplo de aplicação

Se, por exemplo, quiser **bloquear** cada linha de uma das suas tabelas em que uma determinada entrada atinja um **valor** específico, defina o evento **Quando uma linha é alterada** como acionador da automatização.

![Definição do evento de disparo de automatização](images/trigger-example-1.png)

Em seguida, defina o **valor** e a **coluna** em que este deve ser alcançado.

![Definição do evento de disparo de automatização](images/trigger-example-2.png)

Por fim, defina **Bloquear registro** como ação automatizada.

![Definição da ação automatizada](images/automated-action-example.png)

A partir deste momento, a automatização criada bloqueará **todas as linhas** em que as **entradas** mudem de tal forma que cumpram a regra da automatização.

![Ação automatizada definida: "Bloquear registro"](images/automated-action-example-2.png)

{{< warning  headline="Tenha em atenção"  text="Com uma automatização, só pode bloquear as linhas em que o acionador da automatização ocorreu. Uma regra de automatização de acordo com o padrão **Evento na linha X desencadeia o bloqueio da linha Y** não é possível." />}}

## Bloquear várias linhas ao mesmo tempo

As automatizações são extremamente úteis se quiser bloquear várias linhas ao mesmo tempo. Para o fazer, selecione o acionador **Numa hora programada para entradas que preencham determinadas condições** e defina as condições correspondentes. Em vez de definir a frequência e a hora de execução, clique em **Executar agora** na parte inferior para bloquear imediatamente todas as linhas desejadas.

Para mais informações sobre o bloqueio de linhas, consulte o artigo [Bloquear uma linha]({{< relref "help/base-editor/zeilen/sperren-einer-zeile" >}}).

### Mais artigos úteis na secção Automatizações:

- [Visão geral das automatizações]({{< relref "help/base-editor/automationen/uebersicht-ueber-automationen" >}})
- [Como funcionam as automatizações]({{< relref "help/base-editor/automationen/funktionsweise-von-automationen" >}})
- [Criar uma automatização]({{< relref "help/base-editor/automationen/anlegen-einer-automation" >}})
- [Gerir e agrupar automatizações]({{< relref "help/base-editor/automationen/automationen-verwalten-und-gruppieren" >}})
- [Pausar as automatizações]({{< relref "help/base-editor/automationen/automationen-stoppen" >}})
- [Eliminar automatizações]({{< relref "help/base-editor/automationen/automationen-loeschen" >}})
- [Mostrar o registo de execução de uma automatização]({{< relref "help/base-editor/automationen/ausfuehrungslog-einer-automation-anzeigen" >}})
- [Acionadores de automatização]({{< relref "help/base-editor/automationen/automations-trigger" >}})
- [Ações de automatização]({{< relref "help/base-editor/automationen/automations-aktionen" >}})
- [Ligação de entradas via automatização]({{< relref "help/base-editor/automationen/beispiel-verlinken-von-eintraegen-per-automation" >}})

### Outros exemplos interessantes de automatizações:

- [Ligação de entradas via automatização]({{< relref "help/base-editor/automationen/beispiel-verlinken-von-eintraegen-per-automation" >}})
- [Adicionar linhas via automatização]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-hinzufuegen" >}})
- [Adicionar entradas a outras tabelas via automatização]({{< relref "help/base-editor/automationen/beispiel-eintraege-in-andere-tabellen-per-automation-hinzufuegen" >}})
- [Enviar notificações via automatização]({{< relref "help/base-editor/automationen/benachrichtigungen-per-automation-versenden" >}})
- [Envio de e-mails via automatização]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}})
