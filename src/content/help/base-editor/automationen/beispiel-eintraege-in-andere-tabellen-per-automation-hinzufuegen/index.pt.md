---
title: 'Adicionar entradas a outras tabelas via automatização'
date: 2023-03-03
lastmod: '2023-04-12'
categories:
    - 'beispiel-automationen'
author: 'nsc2'
url: '/pt/ajuda/adicionar-entradas-tabelas-automacao-seatable'
aliases:
    - '/pt/ajuda/eintraege-in-andere-tabellen-per-automation-hinzufuegen'
seo:
    title: 'Adicione entradas automaticamente noutras tabelas no SeaTable'
    description: 'Crie entradas em várias tabelas do SeaTable com automação sempre que um gatilho for ativado, sem digitação manual.'
---

Com a ajuda de automatizações, já não tem de fazer entradas noutras tabelas manualmente, mas pode ter estas etapas executadas automaticamente. A grande vantagem disto é que o gatilho não tem de estar na mesma tabela que a acção desencadeada.

## Adicionar entradas a outras tabelas através de automatização

![Adicionar entradas a outras tabelas através de automatização](images/how-to-use-automations-for-locking-rows-3.png)

1. Clique em {{< seatable-icon icon="dtable-icon-rule" >}} no cabeçalho da Base e depois nas **Regras de Automatização**.
2. Clique em **Add Rule (Adicionar regra)**.
3. **Nomear a** automatização e definir a **tabela** e a **vista em** que deve ser desencadeada.
4. Definir um **evento de disparo que desencadeia** a automatização.
5. Clique em **Add Action** e seleccione **Add New Entry in Other Table** como a acção automatizada.
6. Definir a **tabela** na qual a entrada deve ser inserida e os **campos** pré-preenchidos.
7. Confirmar com **Submeter**.

## Criar a automatização

Definir um **evento de disparo** para a automatização depois de primeiro determinar em que **tabela** e **visualizar** a mesma irá ocorrer.

![Eventos de activação basicamente disponíveis para selecção](images/trigger-options-for-archivating-rows.png)

{{< warning  headline="Nota importante" >}}

A ação automática "Adicionar nova entrada noutra tabela" está disponível. **exclusivamente** está disponível para os seguintes eventos de desencadeamento:

- ["As entradas satisfazem determinadas condições após o processamento]({{< relref "help/base-editor/automationen/automations-trigger" >}}#automations-trigger_eintraege_erfuellen_nach_bearbeitung_bestimmte_bedingungen)"
- ["Foi adicionada uma nova entrada]({{< relref "help/base-editor/automationen/automations-trigger" >}}#automations-trigger_ein_neuer_eintrag_wird_hinzugefuegt)"

{{< /warning >}}

Em seguida, seleccione **Adicionar nova entrada noutra tabela** como acção automatizada.

![Adicionar a acção automatizada](images/add-an-action.png) ![Selecção da acção automatizada](images/add-action-example2.png)

No passo seguinte, seleccione a **tabela** na qual a entrada deve ser adicionada após o disparo do acionador.

![Selecção da tabela na qual a entrada será adicionada ao ser desencadeada a automatização](images/select-table.png)

Em seguida, clique em **Adicionar campo** para seleccionar as colunas para as quais pretende definir valores predefinidos na nova entrada.

![Clique em Adicionar campo](images/add-field.png)

Agora, no menu suspenso, seleccione uma **coluna** correspondente e defina o **valor** pré-preenchido no campo de entrada. Dependendo do [tipo de coluna]({{< relref "help/base-editor/spalten/uebersicht-alle-spaltentypen" >}}
) seleccionado, dispõe de diferentes **opções**.

![Definição da entrada e da coluna à qual esta deve ser adicionada](images/set-table-and-entry.png)

Por fim, confirme a automatização com um clique em **Submeter**.

![Confirmação da automatização](images/confirm-the-automation.jpg)

## Exemplo de aplicação

Um **caso de utilização** concreto para este tipo de automatização poderia surgir, por exemplo, se, enquanto responsável de uma empresa, for responsável pelos novos colaboradores que se juntam à sua equipa. No processo de integração, poderia estar definido que, no primeiro dia de trabalho, deve solicitar o **pagamento do salário** do colaborador e documentar a **entrega de uma viatura de serviço**.

Quando adiciona o novo colaborador à sua tabela, pretende informar automaticamente o departamento de Recursos Humanos de que entregou a viatura de serviço e de que pode preparar o processamento salarial do primeiro mês. Para isso, o SeaTable deve **adicionar uma nova entrada à tabela do departamento de Recursos Humanos**.

Do seu lado, isto pode ser concretizado com uma tabela na qual mantém vários dados dos colaboradores. Neste contexto, poderia registar, entre outros, o nome dos colaboradores ou dos novos colaboradores, o seu departamento e a sua data de entrada.

![Tabela de exemplo do caso de utilização](images/example-table.3.png)

Com a ajuda de uma automatização, sempre que adicionar um novo colaborador à tabela, deverá ser automaticamente adicionada uma nova entrada a outra tabela, utilizada pelo departamento de Recursos Humanos para gerir os pagamentos salariais e as viaturas de serviço.

### Criar a automatização

Primeiro, atribua um **nome** à automatização e seleccione tanto a **tabela** (employee lists) como a **vista** (new employees) nas quais a automatização deve ser desencadeada.

![Nomeação da automatização, selecção da tabela e da vista nas quais a automatização deve actuar](images/set-table-and-view-example-3.png)

Como **evento desencadeador** da automatização, seleccione a opção **As entradas satisfazem determinadas condições após o processamento**.

![Selecção do evento desencadeador](images/trigger-condition.png)

Para que **apenas** sejam adicionadas novas entradas à tabela do departamento de Recursos Humanos assim que tiver introduzido o **nome** de um novo colaborador **na sua tabela**, seleccione como **condição de filtro** que a coluna "employee" **não esteja vazia** após o processamento.

![Adicionar uma condição de filtro](images/set-condition-example-3.png)

Como **acção automatizada**, defina a acção **Adicionar nova entrada noutra tabela**.

![Selecção da acção automatizada](images/add-action-example2.png)

No passo seguinte, seleccione a tabela "Payments" como **tabela** à qual será adicionada uma entrada após o disparo da automatização.

![Selecção da tabela à qual a entrada é adicionada quando a automatização é desencadeada](images/select-table-example3.png)

Em seguida, defina os **valores** com os quais determinados campos devem ser pré-preenchidos. Para citar o nome de um novo colaborador na nova entrada da tabela do departamento de Recursos Humanos, escreva o **nome** da coluna da sua tabela na qual este se encontra, entre chavetas, no campo de texto: {employee}

![Definição das entradas a adicionar à tabela seleccionada](images/define-the-entrys-in-the-second-table.png)

### Testar a automatização

Se, após a confirmação da automatização, introduzir o nome de um novo colaborador na sua tabela, ...

![Adicionar um novo colaborador à sua tabela](images/example-after-trigger-3.1.png)

... as entradas definidas serão automaticamente adicionadas à tabela do departamento de Recursos Humanos.

![Tabela do departamento de Recursos Humanos após o disparo da automatização](images/example-after-trigger-3.2.png)

### Outros exemplos interessantes de automatizações:

- [Bloquear linhas através de automatização]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-sperren" >}})
- [Ligação de entradas através de automatização]({{< relref "help/base-editor/automationen/beispiel-verlinken-von-eintraegen-per-automation" >}})
- [Adicionar linhas através de automatização]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-hinzufuegen" >}})
- [Enviar notificações através de automatização]({{< relref "help/base-editor/automationen/benachrichtigungen-per-automation-versenden" >}})
- [Enviar e-mails através de automatização]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}})
