---
title: 'Ações de automatização'
date: 2023-01-27
lastmod: '2026-11-25'
categories:
    - 'automationen'
author: 'kgr'
url: '/pt/ajuda/acoes-automacao-seatable'
aliases:
    - '/pt/ajuda/automations-aktionen'
seo:
    title: 'Ações de automação no SeaTable: guia completo'
    description: 'Visão geral: estas são as ações que pode executar com as automatizações do SeaTable – enviar e-mails, adicionar ligações, executar scripts, processamento de dados ou IA e muito mais.'
weight: 6
---

As **ações automatizadas** representam um dos dois componentes essenciais das automatizações. As ações são desencadeadas por **eventos de acionamento** definidos. Dependendo do [acionador]({{< relref "help/base-editor/automationen/automations-trigger" >}}), o SeaTable pode realizar diferentes ações de automatização. Este artigo fornece uma **visão geral** dos diferentes tipos de ações automatizadas.

## Ações de automatização disponíveis

A última versão do SeaTable oferece um total de 17 ações de automatização diferentes à sua escolha:

- Enviar notificação
- Enviar notificação de aplicação
- Enviar e-mail
- Adicionar registro
- Bloquear registro
- Modificar registro
- Adicionar ligações
- Adicionar uma nova entrada a outra tabela
- Adicionar entrada a uma tabela ligada
- Modificar entrada ligada noutra tabela
- Executar script Python
- Chamar a IA
- Gerir eventos no Google Calendar
- Executar processamento de dados
- Converter página em PDF
- Gerar PDF a partir do documento e enviar
- Arquivar

## Adicionar, duplicar, mover e eliminar ações de automatização

Para adicionar uma ação, clique no **botão grande com o símbolo de mais** e selecione a ação correspondente na lista pendente. Tenha em atenção que as ações disponíveis diferem consoante o acionador.

![Adicionar ações de automatização](images/automated-actions.jpg)

Se já tiver configurado ações mais complexas, como o envio de e-mails, o processamento de dados ou funções de IA, também as pode duplicar. Basta clicar nos **três pontos** e depois em **Duplicar**. Isto significa que só tem de fazer pequenos ajustes a estas ações e poupa muito tempo.

![Duplicar ações de automatização](images/duplicate-automated-actions.jpg)

A ordem das ações pode ser facilmente alterada **arrastando e largando**. Mova o ponteiro do rato sobre uma caixa de ação, mantenha premido o botão esquerdo do rato na **área de arrastamento de seis pontos** e mova a ação para a posição pretendida. Isto permite-lhe personalizar de forma flexível a sequência de automatização.

![Mover ações de automatização](images/move-automated-actions.gif)

Naturalmente, também pode eliminar as ações que já não são necessárias. Para o fazer, clique nos **três pontos** e depois em **Eliminar**. Tenha em atenção que as ações automatizadas são removidas **imediata e permanentemente** e não podem ser restauradas.

![Eliminar ações automatizadas](images/delete-automated-actions.gif)

## Ação de automatização: Enviar notificação

Ao definir "Enviar notificação" como uma ação automatizada, pode configurar uma notificação para um ou mais utilizadores. Os utilizadores selecionados receberão uma **notificação** sempre que o acionador correspondente for acionado. Esta ação de automatização está disponível **para todos os acionadores de automatização**.

Pode editar os **destinatários** e o **conteúdo** das notificações em qualquer altura nas **definições** da ação. Para os destinatários, pode selecionar especificamente **utilizadores individuais** ou notificar utilizadores numa coluna específica do tipo [Colaborador]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}}), [Criador]({{< relref "help/base-editor/spaltentypen/die-spalten-ersteller-und-erstelldatum" >}}) ou [Último modificador]({{< relref "help/base-editor/spaltentypen/die-spalten-letzter-bearbeiter-und-bearbeitungsdatum" >}}). Escreva a mensagem pretendida no campo de texto e utilize as referências de coluna entre chavetas para inserir valores específicos.

![Enviar notificação através de automatização](images/send-notification-action-settings.jpg)

Os utilizadores podem consultar as suas notificações através do {{< seatable-icon icon="dtable-icon-notice" >}} **ícone de campainha** junto ao seu avatar no canto superior direito.

![Notificação recebida](images/example-action-notification.png)

O artigo [Enviar notificações através de automatização]({{< relref "help/base-editor/automationen/benachrichtigungen-per-automation-versenden" >}}) analisa esta automatização utilizando um caso de utilização específico.

## Ação de automatização: Enviar notificação de aplicação

Ao definir "Enviar notificação de aplicação" como uma ação automatizada, pode configurar uma notificação para um ou mais utilizadores de uma aplicação. Os utilizadores selecionados recebem uma **notificação** na aplicação sempre que o acionador correspondente é acionado. Esta ação de automatização está disponível **para todos os acionadores de automatização**.

Nas **definições** da ação, pode definir para que **aplicação** e para que **destinatários** as notificações devem ser enviadas. Para os destinatários, pode selecionar especificamente **utilizadores individuais da aplicação** ou notificar utilizadores numa coluna específica do tipo **Colaborador, Criador ou Último modificador**. Introduza o **conteúdo** pretendido da notificação no campo de texto. Utilize referências de coluna entre chavetas para inserir valores específicos.

![Enviar notificação da aplicação através da automatização](images/send-app-notification-action-settings.jpg)

Os utilizadores da respetiva aplicação podem consultar as suas notificações através do {{< seatable-icon icon="dtable-icon-notice" >}} **ícone de campainha** junto ao seu avatar no canto superior direito.

![Verificar as notificações na aplicação](images/check-app-notifications.jpg)

## Ação de automatização: Enviar e-mail

Ao definir "Enviar e-mail" como uma ação automatizada, pode enviar e-mails predefinidos a um ou mais utilizadores. O SeaTable envia um **e-mail** a cada utilizador selecionado assim que o acionador correspondente é acionado. Esta ação de automatização está disponível **para todos os acionadores de automatização**.

Pode editar a **conta de e-mail**, o **assunto**, os **destinatários**, a **mensagem** e os **anexos** do e-mail em qualquer altura nas **definições** da ação. Utilize referências de coluna entre chavetas para inserir determinados valores em campos de texto.

![Definição da ação de automatização: Enviar e-mail](images/send-email-action-settings.jpg)

O artigo [Enviar e-mails através da automatização]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}}) analisa esta automatização utilizando um caso de utilização específico.

## Ação de automatização: Adicionar registro

Se definir "Adicionar registro" como uma ação automatizada, é adicionada uma **nova linha** à tabela sempre que o acionador correspondente é acionado. Pode definir antecipadamente os valores exatos para cada coluna individualmente.

![Ação de automatização: Adicionar registro](images/add-record-action-settings.jpg)

A ação de automatização "Adicionar registro" está atualmente disponível para os seguintes **acionadores de automatização**:
- Quando uma linha é alterada
- Quando uma linha é adicionada
- Numa hora programada

O artigo [Adicionar linhas através da automatização]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-hinzufuegen" >}}) analisa esta automatização utilizando um caso de utilização específico.

## Ação de automatização: Bloquear registro

Se definir "Bloquear registro" como uma ação automatizada, a **linha** que desencadeou a automatização é bloqueada para edição. Não pode efetuar quaisquer outras definições para esta ação – deve configurar as condições para o bloqueio da linha no **acionador**. Tenha em atenção que já não pode **desbloquear** linhas bloqueadas sem direitos de administrador.

![Definição da ação de automatização: Bloquear uma entrada na tabela](images/lock-record-action.jpg)

![Bloqueio de uma entrada numa tabela acionado por uma automatização](images/example-locked-records.jpg)

A ação de automatização "Bloquear registro" está atualmente disponível para os seguintes **acionadores de automatização**:
- Quando uma linha é alterada
- Quando uma linha é adicionada
- Numa hora programada para entradas que preencham determinadas condições

O artigo [Bloquear linhas utilizando a automatização]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-sperren" >}}) analisa esta automatização utilizando um caso de utilização específico.

## Ação de automatização: Modificar registro

Se selecionar "Modificar registro" como uma ação automatizada, as **linhas** na tabela são ajustadas de acordo com as **definições** previamente definidas depois de o acionador ser acionado. Pode definir um valor para cada coluna que as linhas adotam automaticamente após a alteração.

![Ação de automatização: Modificar registro](images/modify-record-action-settings.jpg)

A ação de automatização "Modificar registro" está atualmente disponível para os seguintes **acionadores de automatização**:
- Quando uma linha é alterada
- Quando uma linha é adicionada
- Numa hora programada para entradas que preencham determinadas condições

## Ação de automatização: Adicionar ligações

Se selecionar "Adicionar ligações" como uma ação automatizada, é criada uma [ligação a outras entradas]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}) na coluna correspondente quando o acionador é acionado. Nas **definições** da ação, pode especificar exatamente em que condições cada ligação é adicionada à tabela.

![Ação de automatização: Adicionar ligações](images/add-links-action-settings.jpg)

A ação de automatização "Adicionar ligações" está atualmente disponível para os seguintes **acionadores de automatização**:
- Quando uma linha é alterada
- Quando uma linha é adicionada
- Numa hora programada

O artigo [Ligar entradas através da automatização]({{< relref "help/base-editor/automationen/beispiel-verlinken-von-eintraegen-per-automation" >}}) analisa esta automatização utilizando um caso de utilização específico.

## Ação de automatização: Adicionar uma nova entrada a outra tabela

Se selecionar "Adicionar uma nova entrada a outra tabela" como uma ação automatizada, é criada uma **linha noutra tabela** quando o acionador é acionado. Nas **definições** da ação, pode definir valores individuais para cada coluna que são atribuídos às linhas na tabela selecionada como parte da automatização. Também pode selecionar colunas do mesmo tipo na tabela de origem para copiar entradas de linha para a outra tabela.

![Ação de automatização: Adicionar uma linha noutra tabela](images/add-record-to-other-table-action-settings.jpg)

A ação de automatização "Adicionar uma nova entrada a outra tabela" está atualmente disponível para os seguintes **acionadores de automatização**:
- Quando uma linha é alterada
- Quando uma linha é adicionada

O artigo [Adicionar entradas a outras tabelas através da automatização]({{< relref "help/base-editor/automationen/beispiel-eintraege-in-andere-tabellen-per-automation-hinzufuegen" >}}) analisa esta automatização utilizando um caso de utilização específico.

## Ação de automatização: Adicionar entrada a uma tabela ligada

Se selecionar "Adicionar entrada a uma tabela ligada" como uma ação automatizada, é criada uma **nova linha noutra tabela** quando o acionador é acionado. Além disso, o SeaTable **liga** a nova linha ao registro que acionou a automatização. Para isso, é necessária uma [coluna de ligação]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}) selecionável.

![Ação de automatização: Adicionar entrada a uma tabela ligada](images/add-record-to-linked-table-action-settings.png)

Nas **definições** da ação, pode definir valores individuais para cada coluna que são atribuídos à nova linha na tabela selecionada como parte da automatização. Também pode selecionar colunas do mesmo tipo na tabela de origem para copiar entradas de linha para a outra tabela.

A ação de automatização "Adicionar entrada a uma tabela ligada" está atualmente disponível para o seguinte **acionador de automatização**:
- Quando uma linha é alterada

## Ação de automatização: Modificar entrada ligada noutra tabela

Se selecionar "Modificar entrada ligada noutra tabela" como uma ação automatizada, os **registros ligados existentes noutra tabela** são modificados quando o acionador é acionado. Se, por exemplo, o estado de uma linha mudar, todos os registros ligados podem ser atualizados imediatamente. Nas **definições** da ação, tem de selecionar uma [coluna de ligação]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}) e pode depois definir valores individuais para cada coluna que são atribuídos às linhas na tabela selecionada como parte da automatização.

![Ação de automatização: Modificar entrada ligada noutra tabela](images/modify-linked-record-in-other-table-action-settings.png)

A ação de automatização "Modificar entrada ligada noutra tabela" está atualmente disponível para o seguinte **acionador de automatização**:
- Quando uma linha é alterada

## Ação de automatização: Executar script Python

Se selecionar a execução de um script Python como uma ação automatizada, o acionador põe em movimento um **script Python** previamente definido. Pode criar ou editar o script a qualquer momento no [editor de scripts]({{< relref "help/skripte/allgemein/anlegen-und-loeschen-eines-skriptes" >}}) e depois selecioná-lo nas **definições** da ação.

![Ação de automatização: Executar script Python](images/run-python-script-action-settings.jpg)

A ação de automatização "Executar script Python" está atualmente disponível para os seguintes **acionadores de automatização**:
- Quando uma linha é alterada
- Quando uma linha é adicionada
- Numa hora programada

## Ação de automatização: Chamar a IA

Se selecionar a execução de uma função de IA como uma ação automatizada, o acionador chama um **modelo de IA** que executa uma ação predefinida na tabela. Pode configurar a ação exata a ser executada nas **definições**. Dependendo do tipo de função de IA, podem ser necessárias **colunas de entrada**, **colunas de saída** e um **prompt**.

![Definição de uma ação de automatização: Executar IA](images/run-ai-action-settings.jpg)

Pode fazer com que as seguintes **funções de IA** sejam executadas com uma automatização:

- **Resumir**: Resume o texto de uma ou mais colunas. Pode controlar a extensão, o tom, o formato e o idioma do resumo, personalizando o prompt.
- **Classificar**: Classifica os registos de uma ou mais colunas. Pode personalizar as categorias e regras através do prompt. O resultado é guardado numa [coluna de seleção única]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}}) ou [coluna de seleção múltipla]({{< relref "help/base-editor/spaltentypen/die-mehrfachauswahl-spalte" >}}).
- **OCR**: Extrai texto de uma [coluna de imagem]({{< relref "help/base-editor/spaltentypen/die-bild-spalte" >}}). O conteúdo reconhecido é escrito na coluna de resultados do tipo [Texto ou Texto longo]({{< relref "help/base-editor/spaltentypen/die-spalte-formatierter-text" >}}).
- **Extrair**: Extrai informações específicas de uma coluna do tipo texto ou número, de acordo com os seus requisitos. A informação extraída é escrita nas colunas de resultados.
- **Personalizado**: Gera conteúdo com base no seu prompt. Utilize {nome da coluna} entre chavetas para inserir o valor da coluna de uma linha.

![Ações que podem ser executadas utilizando um modelo de IA](images/run-ai-functions.jpg)

A ação de automatização "Chamar a IA" está atualmente disponível para os seguintes **acionadores de automatização**:
- Quando uma linha é alterada
- Quando uma linha é adicionada

Encontra instruções detalhadas sobre cada função de IA, com exemplos passo a passo, na secção [Automatizações IA]({{< relref "help/ai/ai-automations/setup-ai-automation" >}}).

## Ação de automatização: Gerir eventos no Google Calendar

Se selecionar "Gerir eventos no Google Calendar" como uma ação automatizada, um compromisso do SeaTable é criado ou atualizado num calendário do Google quando o acionador é acionado. Existem alguns requisitos que devem ser cumpridos para que esta ação funcione sem problemas:
- Primeiro, tem de [sincronizar a sua conta do Google Calendar com o SeaTable]({{< relref "help/integrationen/integrationen-innerhalb-von-seatable/google-calender-synchronisieren" >}}).
- Devem existir duas [colunas de data]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}) numa tabela, que definam o **início** e o **fim** dos compromissos.
- Também precisa de uma [coluna de texto]({{< relref "help/base-editor/spaltentypen/die-text-spalte" >}}) na qual o Google possa escrever o **identificador do evento** para que os compromissos possam ser sincronizados.

![Requisitos para gerir eventos no Google Calendar](images/manage-events-in-google-calendar-part-1.png)

Também pode efetuar outras definições. Adicione um **título**, uma **descrição**, um **local** e **participantes** ao evento. Para o fazer, escreva os detalhes nos **campos de texto** ou trabalhe com **referências de coluna entre chavetas** para inserir valores específicos da tabela. Ao ativar os **controlos deslizantes**, pode decidir se pretende enviar notificações, se se trata de uma videoconferência e se os convidados podem editar o compromisso, ver a lista de convidados e convidar outros convidados.

![Mais definições para eventos no Google Calendar](images/manage-events-in-google-calendar-part-2.png)

A ação de automatização "Gerir eventos no Google Calendar" está atualmente disponível para os seguintes **acionadores de automatização**:
- Quando uma linha é alterada
- Quando uma linha é adicionada

## Ação de automatização: Executar processamento de dados

Se selecionar a execução de uma operação de processamento de dados como uma ação automatizada, o acionador inicia uma [operação de processamento de dados]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitungsoperationen-in-seatable" >}}) predefinida na tabela. Pode configurar a ação exata a ser executada nas **definições**. Dependendo do tipo de operação, podem ser necessárias **certas colunas de entrada e saída**.

![Definição de uma ação de automatização: Executar operação de processamento de dados](images/run-data-processing-action-settings.jpg)

Pode fazer com que as seguintes **operações de processamento de dados** sejam executadas com uma automatização:

- [Calcular delta]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-veraenderungen-berechnen" >}})
- [Calcular a porcentagem]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-prozentualen-anteil-berechnen" >}})
- [Calcular a classificação]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-rangliste-berechnen" >}})
- [Extrair o nome de usuário]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-benutzernamen-uebertragen" >}})
- [Comparar e copiar]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-vergleichen-und-kopieren" >}})

![Operações de processamento de dados que podem ser executadas utilizando a automatização](images/run-data-processing-available-operations.jpg)

A ação de automatização "Executar processamento de dados" está atualmente disponível para o seguinte **acionador de automatização**:
- Numa hora programada

## Ação de automatização: Converter página em PDF

Se selecionar "Converter página em PDF" como uma ação automatizada, o SeaTable irá **criar um documento PDF a partir do registo** quando o acionador for acionado e guardá-lo-á numa [coluna de ficheiro]({{< relref "help/base-editor/spaltentypen/die-datei-spalte" >}}). Para o fazer, selecione um **modelo** que tenha criado previamente no [plugin de design de página]({{< relref "help/base-editor/plugins/anleitung-zum-seitendesign-plugin" >}}). Também pode definir o **nome do ficheiro** nas definições da ação.

![Criar PDF através da automatização](images/convert-page-to-pdf-action-settings.jpg)

A ação de automatização "Converter página em PDF" está atualmente disponível para os seguintes **acionadores de automatização**:
- Quando uma linha é alterada
- Quando uma linha é adicionada
- Numa hora programada para entradas que preencham determinadas condições

## Ação de automatização: Gerar PDF a partir do documento e enviar

Se selecionar "Gerar PDF a partir do documento e enviar" como uma ação automatizada, o SeaTable irá **criar um documento PDF** quando o acionador for acionado e guardá-lo-á na [gestão de ficheiros]({{< relref "help/base-editor/dateien/das-dateimanagement-einer-base" >}}). O SeaTable também pode enviá-lo diretamente por e-mail.

Nas **definições** da ação, selecione um **modelo** que tenha criado anteriormente no **plugin de design de relatórios** e atribua um **nome de ficheiro**. Em seguida, ative o controlo deslizante para selecionar uma **pasta própria** na qual gostaria de guardar o ficheiro. Se apenas pretender gerar o documento, pode terminar a configuração neste ponto.

![Criar e enviar PDF a partir de um design de relatório utilizando a automatização](images/generate-pdf-from-document-action-settings.jpg)

Se, em seguida, pretender enviar o documento gerado, ative o controlo deslizante "Enviar para e-mail". Pode editar a **conta de e-mail**, o **destinatário**, o **assunto** e a **mensagem** do e-mail em qualquer altura nas **definições** da ação.

![Criar e enviar PDF a partir de um design de relatório utilizando a automatização](images/generate-pdf-from-document-and-send-action-settings.jpg)

A ação de automatização "Gerar PDF a partir do documento e enviar" está atualmente disponível para o seguinte **acionador de automatização**:
- Numa hora programada

## Ação de automatização: Arquivar

Pode utilizar a ação de arquivamento para [mover automaticamente as linhas para o armazenamento de big data]({{< relref "help/base-editor/big-data/zeilen-ins-big-data-backend-verschieben" >}}). A função de big data deve, naturalmente, ser ativada na respetiva base. Uma vez que já definiu a **vista** e quaisquer condições de filtragem para as linhas a arquivar nas definições do acionador, não pode efetuar quaisquer definições para a própria ação.

![Arquivar linhas através da automatização](images/automated-action-archive.png)

A ação de automatização "Arquivar" está atualmente disponível para os seguintes **acionadores de automatização**:
- Numa hora programada
- Numa hora programada para entradas que preencham determinadas condições