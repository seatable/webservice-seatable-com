---
title: 'Envio de e-mails via automatização'
date: 2023-03-03
lastmod: '2023-03-03'
categories:
    - 'beispiel-automationen'
author: 'nsc2'
url: '/pt/ajuda/enviar-emails-automaticos-por-automacao'
aliases:
    - '/pt/ajuda/e-mail-versand-per-automation'
seo:
    title: 'Enviar e‑mails automáticos no SeaTable – guia prático'
    description: 'Saiba como automatizar o envio de e‑mails no SeaTable usando gatilhos, regras e contas de e‑mail externas via SMTP.'
---

Com a ajuda de automatizações, já não tem de enviar e-mails manualmente a utilizadores seleccionados, mas pode mandar enviá-los automaticamente. Basta definir uma automatização correspondente para qualquer visualização de tabela.

## Envio de e-mails por automatização

![Envio de e-mails por automatização](images/how-to-use-automations-for-locking-rows-3.png)

1. Clique em {{< seatable-icon icon="dtable-icon-rule" >}} no cabeçalho da Base e depois nas **Regras de Automatização**.
2. Clique em **Add Rule (Adicionar regra)**.
3. **Nomear a** automatização e definir a **tabela** e a **vista em** que deve funcionar.
4. Definir um **evento de disparo que desencadeia** a automatização.
5. Clique em **Adicionar acção** e seleccione **Enviar e-mail** como acção automatizada.
6. Confirmar com **Submeter**.

## Criar a automatização

Definir primeiro um **evento de disparo** para a automatização.

![Eventos de activação basicamente disponíveis para selecção](images/trigger-options-for-archivating-rows.png)

{{< warning  headline="Nota" >}}

A ação automática **Enviar e-mail** está disponível após todos os eventos de acionamento:

- As inscrições preenchem certas condições após a edição
- É acrescentada uma nova entrada
- Desencadeamento periódico
- Acionador periódico para as entradas que preenchem determinadas condições

{{< /warning >}}

Em seguida, seleccione **Enviar e-mail** como acção automatizada.

![Adicionar a acção automatizada](images/add-an-action.png) ![Adicionar a acção automatizada](images/example-send-email-action.png)

No passo seguinte, seleccione primeiro uma **conta de e-mail** a partir da qual pretende enviar os e-mails. Para poder utilizar a sua conta de e-mail para o envio, **tem** primeiro de a **adicionar** como prestador terceiro na sua base SeaTable. Pode encontrar instruções detalhadas para este passo [aqui]({{< relref "help/integrationen/integrationen-innerhalb-von-seatable/gmail-fuer-den-versand-von-e-mails-per-smtp-einrichten" >}}).

{{< warning  type="warning" headline="Nota importante"  text="Se **não** tiver adicionado uma conta de e-mail como prestador terceiro na sua base SeaTable, **não** lhe será apresentada qualquer conta. A adição de uma conta de e-mail constitui, assim, um **pré-requisito** importante para a automatização." />}}

![Selecção de uma conta de e-mail para o envio](images/select-email-account.png)

Depois de seleccionar a conta de e-mail, defina o **assunto**, o **destinatário** e o **conteúdo** do e-mail. Pode introduzir **vários endereços de e-mail** separados por vírgulas e em CC. Tem ainda a possibilidade de adicionar **anexos** a partir de uma [coluna de ficheiros]({{< relref "help/base-editor/spaltentypen/die-datei-spalte" >}}).

![Definição do e-mail a enviar através da automatização](images/define-email.png)

Por fim, confirme a automatização com um clique em **Submeter**.

![Confirmação da automatização](images/confirm-the-automation.jpg)

## Exemplo de aplicação

Um **caso de utilização** concreto para este tipo de automatização poderia surgir, por exemplo, se trabalhasse na comissão de trabalhadores de uma empresa. Pretende informar automaticamente o departamento de Recursos Humanos de que aprovou o despedimento de um colaborador.

Do seu lado, isto pode ser concretizado com uma tabela na qual são mantidos vários **dados** de todos os colaboradores da sua empresa. Neste contexto, poderia registar, entre outros, os **nomes** dos colaboradores, o **estado de emprego** e o estado dos seus **pagamentos salariais**.

![Tabela de exemplo do caso de utilização concreto](images/example-table-email-automation.png)

Com a ajuda de uma automatização, o SeaTable deve agora enviar automaticamente um **e-mail** ao departamento de Recursos Humanos assim que aprovar o despedimento de um colaborador na comissão de trabalhadores.

### Criar a automatização

Primeiro, atribua um **nome** à automatização e seleccione tanto a **tabela** (employee list) como a **vista** (employees ressort marketing) na qual a automatização deve actuar.

![Definições básicas da automatização](images/basic-settings-automation.png)

Como **evento desencadeador** da automatização, seleccione a opção **As entradas satisfazem determinadas condições após o processamento**. Para que os e-mails sejam enviados **apenas** em caso de despedimento de um colaborador, adicione como **condição de filtro** que a entrada na coluna **status of employment** tenha de ser alterada para **terminated**.

![Definição do evento desencadeador](images/condition-of-the-trigger-event.png)

Como **acção automatizada**, defina a acção **Enviar e-mail**.

![Adicionar a acção automatizada](images/example-send-email-action.png)

No passo seguinte, seleccione uma **conta de e-mail** a partir da qual pretende enviar os e-mails ao departamento de Recursos Humanos. Para poder utilizar a sua conta de e-mail para o envio, **tem** primeiro de a **adicionar** como prestador terceiro na sua base SeaTable. Pode encontrar instruções detalhadas para este passo [aqui]({{< relref "help/integrationen/integrationen-innerhalb-von-seatable/gmail-fuer-den-versand-von-e-mails-per-smtp-einrichten" >}}).

{{< warning  type="warning" headline="Nota importante"  text="Se **não** tiver adicionado uma conta de e-mail como prestador terceiro na sua base SeaTable, neste passo **não** lhe será apresentada qualquer conta. A adição de uma conta de e-mail constitui, assim, um **pré-requisito** importante para a automatização." />}}

![Selecção de uma conta de e-mail para o envio](images/select-email-account-1.png)

Após seleccionar a sua conta de e-mail, defina o **assunto**, o **destinatário** e o **conteúdo** dos e-mails. Pode introduzir **vários endereços de e-mail** separados por vírgulas e em CC. Por fim, tem ainda a possibilidade de adicionar **anexos** a partir de uma [coluna de ficheiros]({{< relref "help/base-editor/spaltentypen/die-datei-spalte" >}}).

{{< warning  headline="Dica"  text="Através de chavetas, pode citar **conteúdos de colunas de tabela** no corpo do e-mail. Utilize esta funcionalidade para inserir automaticamente os **nomes** dos colaboradores despedidos no texto." />}}

![Definição do e-mail para a automatização do caso de utilização](images/definition-email-example.png)

Quando tiver terminado o e-mail a enviar, confirme a automatização com **Submeter**.

### Testar a automatização

Se, em seguida, na tabela seleccionada, alterar o estado de emprego de um colaborador para **terminated**, o **e-mail** pré-definido será automaticamente enviado ao departamento de Recursos Humanos para o informar do despedimento.

![Uma vez alterado o estado de emprego de um colaborador para "terminated", o e-mail pré-definido é automaticamente enviado aos destinatários seleccionados ](images/test-automation-email.jpg)

### Outros exemplos interessantes de automatizações:

- [Bloquear linhas através de automatização]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-sperren" >}})
- [Ligação de entradas através de automatização]({{< relref "help/base-editor/automationen/beispiel-verlinken-von-eintraegen-per-automation" >}})
- [Adicionar linhas através de automatização]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-hinzufuegen" >}})
- [Adicionar entradas a outras tabelas através de automatização]({{< relref "help/base-editor/automationen/beispiel-eintraege-in-andere-tabellen-per-automation-hinzufuegen" >}})
- [Enviar notificações através de automatização]({{< relref "help/base-editor/automationen/benachrichtigungen-per-automation-versenden" >}})
