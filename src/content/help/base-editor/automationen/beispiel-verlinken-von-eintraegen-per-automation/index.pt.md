---
title: 'Ligação de entradas via automatização'
date: 2023-01-30
lastmod: '2023-04-06'
categories:
    - 'beispiel-automationen'
author: 'nsc2'
url: '/pt/ajuda/vincular-entradas-automacao'
aliases:
    - '/pt/ajuda/verlinken-von-eintraegen-per-automation'
seo:
    title: 'Vincular entradas no SeaTable por automação: tutorial'
    description: 'Vincule registros automaticamente no SeaTable: defina acionadores, escolha colunas e conecte dados entre tabelas sem esforço manual.'


---

Com a ajuda de automatizações, já não tem de ligar manualmente as entradas nas suas tabelas, mas pode ter estas etapas executadas automaticamente. Basta definir uma automatização correspondente para qualquer vista de tabela.

## Ligação de entradas via automatização

![Linhas de bloqueio e de arquivo com automatização](images/how-to-use-automations-for-locking-rows-3.png)

1. Clique em {{< seatable-icon icon="dtable-icon-rule" >}} no cabeçalho da Base e depois nas **Regras de Automatização**.
2. Clique em **Add Rule (Adicionar regra)**.
3. **Nomear a** automatização e definir a **tabela** e a **vista em** que deve funcionar.
4. Definir um **evento de disparo que desencadeia** a automatização.
5. Clique em **Adicionar acção** e seleccione **Adicionar ligações** como acção automatizada.
6. Confirmar com **Submeter**.

## Criar a automatização

Definir primeiro um **evento de disparo** para a automatização.

![Eventos de activação para o bloqueio e arquivamento de linhas](images/trigger-options-for-archivating-rows.png)

{{< warning  headline="Nota importante" >}}

A ação automática **Adicionar ligações** está disponível para si **exclusivamente** está disponível para os seguintes eventos de desencadeamento:

- "As entradas satisfazem determinadas condições após o processamento"
- "Foi adicionada uma nova entrada"
- "Acionador periódico"

{{< /warning >}}

Em seguida, seleccione **"Adicionar ligações"** como acção automatizada.

![Adicionar a acção automatizada](images/add-an-action.png) ![Adicionar a acção automatizada: "Adicionar ligações"](images/add-action-add-links.png)

Por fim, seleccione uma **coluna** que deve ser ligada à tabela seleccionada e defina uma **condição específica** que tem de ser cumprida para que a automatização seja executada.

![Definição da acção automatizada](images/automated-actions-add-links.png)

Por fim, confirme a automatização com um clique em **Submeter**.

![Confirmação da automatização](images/confirm-the-automation.jpg)

## Exemplo de aplicação

Um **caso de utilização** concreto para este tipo de automatização poderia surgir, por exemplo, se trabalhasse no departamento de contabilidade de uma empresa. Pretende manter tanto uma tabela com todos os pagamentos recebidos numa conta da empresa (**Payments**), como uma tabela com todas as facturas que devem ser pagas à empresa (**Invoices**).

Na tabela **Payments**, para além dos **números de transacção** dos pagamentos (P-0001, etc.), já regista os **montantes** dos diferentes pagamentos (coluna **"Value"**).

![Tabela de exemplo Payments](images/Table-Payments-1.png)

A sua tabela **Invoices**, por sua vez, contém os **números das facturas** (coluna **"Invoice-No"**) e os respectivos **montantes das facturas** (coluna **"Price Total"**).

![Tabela de exemplo "Invoices"](images/Table-Invoices.png)

Com a ajuda de uma **automatização**, pretende agora **ligar** as duas tabelas **Payments** e **Invoices**, para que possa atribuir automaticamente os **pagamentos** recebidos a uma **factura** com base nos seus números de factura.

### Preparação da automatização

Antes de poder criar a automatização, tem primeiro de adicionar duas colunas à tabela **Payments**. Na coluna **"Inv-No"** introduz manualmente os números das facturas que correspondem aos respectivos pagamentos — o que, mais tarde, irá **activar** a automatização. Na coluna **"Invoices"** serão adicionadas automaticamente as **entradas ligadas** da tabela **Invoices** depois de criada a automatização.

![Extensão manual da tabela "Payments" com duas colunas](images/Manuelle-Erweiterung-der-Tabelle-22Payments22.png)

Na tabela **Invoices** necessita igualmente de mais uma coluna (**"Collected Payments"**) na qual as entradas ligadas da tabela **Payments** serão adicionadas no decurso da automatização.

![](images/Hinzufuegen-der-Spalte-22Collected-PAyments22.png)

Em seguida, pode criar uma **automatização** para a tabela **Payments**.

### Criar a automatização

Primeiro, atribua um nome à automatização e seleccione a tabela **Payments** juntamente com a vista com o mesmo nome na qual a automatização deve actuar.

![Definição da automatização do caso de utilização](images/definition-of-the-automation-1.png)

Como **evento desencadeador** da automatização, seleccione a opção **"As entradas satisfazem determinadas condições após o processamento"**. Como condição de filtro, adicione que as duas colunas **"Inv-No"** e **"Value"** da tabela "Payments" **não estão vazias**. Esta condição faz sentido, pois a automatização deve ser desencadeada assim que existirem entradas nestas colunas.

![Definição do evento desencadeador do caso de utilização ](images/trigger-example-1-1.png) ![Definição do evento desencadeador do caso de utilização ](images/trigger-example-2-1.png)

Como **acção automatizada** da automatização, defina por fim a acção **"Adicionar uma coluna ligada à tabela"**.

![Adicionar a acção automatizada: "Adicionar ligações"](images/add-action-add-links.png)

A coluna **"Invoices"** é a coluna na qual as entradas ligadas serão adicionadas no decurso da automatização.

![Selecção da coluna na qual as entradas ligadas são adicionadas](images/automated-action-example-1.png)

No último passo da definição da automatização, deve definir uma outra **condição** que tem de ser cumprida para que uma entrada ligada seja adicionada à coluna. Neste exemplo, define-se que cada **entrada** adicionada na coluna **"Inv-No"** tem também de ser encontrada na coluna **"Invoice-No"** da tabela **Invoices**.

Concretamente, isto significa que cada **número de factura** que atribui manualmente a um pagamento na tabela **Payments** tem de existir já na tabela **Invoices** para que as respectivas **entradas** das duas tabelas possam ser **ligadas** entre si.

![Definição da condição final para activar a automatização](images/automated-action-example-2-1.png)

### Testar a automatização

Se, em seguida, introduzir na coluna **"Inv-No"** da tabela **Payments** um número de factura que já se encontra na tabela **Invoices**, a respectiva **entrada ligada** será automaticamente adicionada à tabela na coluna **"Invoices"**.

![Adicionar as entradas ligadas ao activar a automatização](images/Ausloesen-der-Automation-Beispiel-1-1-1.png)

{{< warning  type="warning" headline="Nota importante"  text="Se adicionar números de factura na coluna **\\"Inv-No\\"** que **ainda não** se encontram na tabela **Invoices**, a automatização **não** será activada e, por conseguinte, **nenhuma** entrada ligada será adicionada à coluna, uma vez que a entrada correspondente na tabela **Invoices** simplesmente ainda não existe." />}}

Com um clique na entrada ligada, abre-se uma janela na qual pode consultar o conteúdo da **entrada ligada** da tabela **Invoices**.

![Com um clique na entrada ligada, é possível consultar o conteúdo da coluna ligada na outra tabela.](images/Informationen-der-verlinkten-Spalte.png)

Além disso, ao activar a automatização são também adicionadas as **entradas ligadas** da tabela **Payments** à tabela **Invoices**. Na coluna **"Collected Payments"** é automaticamente atribuído a cada número de factura o **número de pagamento (P-000X)** correspondente. Graças à **automatização**, pode assim consultar, para cada factura, o **pagamento** correspondente e determinar rapidamente que facturas estão pagas e quais continuam em aberto.

![Adicionar as entradas ligadas ao activar a automatização](images/Ausloesen-der-Automation-Beispiel-2.png)

Também nesta tabela, com um clique na entrada ligada, pode abrir uma janela na qual pode consultar o conteúdo da **entrada ligada** da tabela **Payments**.

![Com um clique numa entrada ligada, é possível consultar o conteúdo da coluna ligada na outra tabela.](images/Informationen-der-verlinkten-Spalte-2.png)

### Outros artigos úteis na secção Automatizações:

- [Visão geral das automatizações]({{< relref "help/base-editor/automationen/uebersicht-ueber-automationen" >}})
- [Como funcionam as automatizações]({{< relref "help/base-editor/automationen/funktionsweise-von-automationen" >}})
- [Criar uma automatização]({{< relref "help/base-editor/automationen/anlegen-einer-automation" >}})
- [Gerir e agrupar automatizações]({{< relref "help/base-editor/automationen/automationen-verwalten-und-gruppieren" >}})
- [Parar automatizações]({{< relref "help/base-editor/automationen/automationen-stoppen" >}})
- [Eliminar automatizações]({{< relref "help/base-editor/automationen/automationen-loeschen" >}})
- [Mostrar o registo de execução de uma automatização]({{< relref "help/base-editor/automationen/ausfuehrungslog-einer-automation-anzeigen" >}})
- [Accionadores de automatização]({{< relref "help/base-editor/automationen/automations-trigger" >}})
- [Acções de automatização]({{< relref "help/base-editor/automationen/automations-aktionen" >}})
- [Bloquear linhas através de automatização]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-sperren" >}})

### Outros exemplos interessantes de automatizações:

- [Bloquear linhas através de automatização]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-sperren" >}})
- [Adicionar linhas através de automatização]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-hinzufuegen" >}})
- [Adicionar entradas a outras tabelas através de automatização]({{< relref "help/base-editor/automationen/beispiel-eintraege-in-andere-tabellen-per-automation-hinzufuegen" >}})
- [Enviar notificações através de automatização]({{< relref "help/base-editor/automationen/benachrichtigungen-per-automation-versenden" >}})
- [Enviar e-mails através de automatização]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}})
