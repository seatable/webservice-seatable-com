---
title: 'Adicionar filas via automatização'
date: 2023-03-02
lastmod: '2023-03-31'
categories:
    - 'beispiel-automationen'
author: 'nsc2'
url: '/pt/ajuda/adicionar-linhas-automaticamente-seatable'
aliases:
    - '/pt/ajuda/zeilen-per-automation-hinzufuegen'
seo:
    title: 'Adicione linhas automaticamente no SeaTable'
    description: 'Crie novas linhas em tabelas SeaTable automaticamente por regras ou agenda – sem lançamentos manuais repetitivos.'
---

Com a ajuda de automatizações, já não tem de adicionar manualmente linhas com determinadas entradas às suas tabelas, mas pode ter estas etapas executadas automaticamente. Basta definir uma automatização correspondente para qualquer visualização de tabela.

## Como adicionar linhas com uma automatização

![Adicionar entradas via automatização](images/how-to-use-automations-for-locking-rows-3.png)

1. Clique em {{< seatable-icon icon="dtable-icon-rule" >}} no cabeçalho da Base e depois nas **Regras de Automatização**.
2. Clique em **Add Rule (Adicionar regra)**.
3. **Nomear a** automatização e definir a **tabela** e a **vista em** que deve funcionar.
4. Definir um **evento de disparo que desencadeia** a automatização.
5. Clique em **Add Action** e seleccione **Add Row** como a acção automatizada.
6. Confirmar com **Submeter**.

## Criar a automatização

Definir primeiro um **evento de disparo** para a automatização.

![Eventos de activação basicamente disponíveis para selecção](images/trigger-options-for-archivating-rows.png)

{{< warning  headline="Nota importante" >}}

A ação automática **Adicionar linha** está disponível para si **exclusivamente** disponíveis após os seguintes eventos de disparo:

- Foi adicionada uma nova entrada
- As entradas satisfazem determinadas condições após o processamento
- Acionador periódico

{{< /warning >}}

Em seguida, seleccione **Adicionar linha** como acção automatizada.

![Adicionar a acção automatizada](images/add-an-action.png) ![Selecção da acção automatizada](images/action-add-records.png)

No passo seguinte, defina as **entradas** que devem aparecer numa linha após o disparo da automatização. Com um clique em **Adicionar campo**, pode definir qualquer entrada.

![Clique em Adicionar campo para definir entradas](images/add-field.png)

Primeiro, seleccione a **coluna** na qual a entrada deve ser inserida.

![Selecção da coluna na qual a entrada é adicionada](images/select-column-to-add-record.jpg)

Em seguida, pode definir a **entrada**. Dependendo do [tipo de coluna]({{< relref "help/base-editor/spalten/uebersicht-alle-spaltentypen" >}}
) seleccionado, dispõe de diferentes **opções**.

![Defina a entrada que pretende adicionar à tabela](images/define-record-to-add.png)

Por fim, active a automatização com um clique em **Submeter**.

![Confirmação da automatização](images/confirm-the-automation.jpg)

## Exemplo de aplicação

Um **caso de utilização** concreto deste tipo de automatização poderia surgir, por exemplo, se registasse as suas reuniões semanais de equipa numa tabela. Pretende que, todas as semanas, antes do início da reunião, seja criada automaticamente uma linha com determinadas entradas, de modo a que apenas tenha de introduzir manualmente a informação restante.

Neste contexto, poderia predefinir, entre outros, a **data** da reunião, a **sala de reuniões** e os **temas** fixos.

![Tabela de exemplo para o caso de utilização concreto](images/example-table-case-record-to-table.png)

### Criar a automatização

Primeiro, atribua um **nome** à automatização e seleccione tanto a **tabela** (aqui: Team Meetings) como a **vista** (aqui: Weekly Team Meeting) na qual a automatização deve actuar.

![Nomeação da automatização, selecção da tabela e da vista nas quais a automatização deve actuar](images/basic-settings-automation-example.png)

Como **evento desencadeador** da automatização, seleccione a opção **Acionador periódico**.

![Selecção do evento desencadeador](images/select-trigger.png)

Em seguida, defina os intervalos em que a automatização deve ser executada. Para que a linha com as entradas correspondentes seja adicionada à tabela todas as semanas, seleccione **semanalmente**.

![Selecção dos intervalos em que a automatização deve ser executada](images/run-frequency.png)

Pode ainda seleccionar um **dia da semana** concreto e uma **hora** concreta em que a automatização será desencadeada. No nosso caso de utilização, faz sentido escolher como momento uma hora antes do início da reunião semanal de segunda-feira de manhã.

![Selecção do momento concreto de execução da automatização](images/set-weekday-and-hour.png)

Como **acção automatizada**, defina no passo seguinte a acção **Adicionar linha**.

![Selecção da acção automatizada](images/select-add-record-as-a-action.png)

Com um clique em **Adicionar campo**, pode definir quantas **entradas** desejar, que aparecerão automaticamente na linha.

![Clique em Adicionar campo para definir entradas](images/add-field.png)

Para que a linha registe automaticamente a respectiva data da reunião de equipa marcada para o mesmo dia, seleccione a **coluna de data** e o valor **O dia da execução**.

![Definição das entradas](images/definiton-of-the-records.png)

Com um clique em **Adicionar campo** pode definir quaisquer **entradas** adicionais que preencham a linha após o disparo da automatização. Basta seleccionar uma **coluna** correspondente da sua tabela a partir do menu suspenso e definir um valor no campo de entrada ao lado.

![Defina quantas entradas desejar ](images/other-records.jpg)

Se, por exemplo, a reunião de equipa decorrer habitualmente numa sala específica, pode definir essa sala como valor fixo. E se determinados temas (como novas contratações/saídas/aniversários) constarem da agenda de todas as reuniões de equipa, também pode fazer com que sejam sempre introduzidos na linha.

### Testar a automatização

Se a automatização funcionar como pretendido, o SeaTable adicionará automaticamente à sua tabela uma linha com as **entradas** previamente definidas após o disparo do acionador periódico (aqui: todas as segundas-feiras às 7 h). Isto poupa-lhe alguns toques no teclado e poderá, em seguida, introduzir manualmente os dados em falta.

![Tabela após o disparo da automatização definida ](images/table-after-automation-new-record-to-current-table.png)

{{< warning  type="warning" headline="Dica"  text="Para poupar efectivamente trabalho e **não** ter de efectuar alterações aos valores introduzidos automaticamente, é aconselhável definir **apenas** valores já fixos que **não** tenha de ajustar manualmente a posteriori. Os ajustes às entradas adicionadas automaticamente são possíveis a qualquer momento, mas limitam consideravelmente a utilidade da automatização." />}}

### Outros exemplos interessantes de automatizações:

- [Bloquear linhas através de automatização]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-sperren" >}})
- [Ligação de entradas através de automatização]({{< relref "help/base-editor/automationen/beispiel-verlinken-von-eintraegen-per-automation" >}})

- [Adicionar entradas a outras tabelas através de automatização]({{< relref "help/base-editor/automationen/beispiel-eintraege-in-andere-tabellen-per-automation-hinzufuegen" >}})
- [Enviar notificações através de automatização]({{< relref "help/base-editor/automationen/benachrichtigungen-per-automation-versenden" >}})
- [Enviar e-mails através de automatização]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}})
