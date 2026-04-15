---
title: 'Acções de automatização'
date: 2023-01-27
lastmod: '2025-11-11'
categories:
    - 'automationen'
author: 'kgr'
url: '/pt/ajuda/acoes-automacao-seatable'
aliases:
    - '/pt/ajuda/automations-aktionen'
seo:
    title: 'Ações de automação no SeaTable: guia completo'
    description: 'Veja o que as automações SeaTable executam: e-mail, adicionar/bloquear linha, notificações, scripts Python, links e processamento de dados na Enterprise.'
weight: 6
---

As **acções automatizadas** representam uma das duas componentes essenciais das automatizações. As acções são desencadeadas por **eventos de desencadeamento** definidos. Dependendo do [accionador]({{< relref "help/base-editor/automationen/automations-trigger" >}}), SeaTable pode realizar diferentes acções de automatização. Este artigo fornece uma **visão geral** dos diferentes tipos de acções automatizadas.

## Acções de automatização disponíveis

A última versão do SeaTable oferece um total de 15 acções de automatização diferentes à sua escolha:

- Enviar notificação
- Enviar notificação de aplicação
- Enviar e-mail
- Adicionar registro
- Bloquear registro
- Modificar registro
- Adicionar ligações
- Adicionar uma nova entrada a outra tabela
- Executar o script Python
- Chamar a IA
- Gerir eventos no Google Calendar
- Executar processamento de dados
- Converter página em PDF
- Gerar PDF a partir do documento e enviar
- Arquivar

## Adicionar, duplicar, mover e eliminar acções de automatização

Para adicionar uma ação, clique no **botão grande com o símbolo de mais** e selecione a ação correspondente na lista pendente. Tenha em atenção que as acções disponíveis diferem consoante o acionador.

![Adicionar acções de automatização](images/automated-actions.jpg)

Se já tiver configurado acções mais complexas, como o envio de e-mails, o processamento de dados ou funções de IA, também as pode duplicar. Basta clicar nos **três pontos** e depois em **Duplicar**. Isto significa que só tem de fazer pequenos ajustes a estas acções e poupa-lhe muito tempo.

![duplicar acções de automatização](images/duplicate-automated-actions.jpg)

A ordem das acções pode ser facilmente alterada **arrastando e largando**. Mova o ponteiro do rato sobre uma caixa de ação, mantenha premido o botão esquerdo do rato na **área de arrastamento de seis pontos** e mova a ação para a posição pretendida. Isto permite-lhe personalizar de forma flexível a sequência de automatização.

![Mover acções de automatização](images/move-automated-actions.gif)

Naturalmente, também pode eliminar as acções que já não são necessárias. Para o fazer, clique nos **três pontos** e depois em **Eliminar**. Tenha em atenção que as acções automatizadas são removidas **imediata e permanentemente** e não podem ser restauradas.

![Eliminar acções automatizadas](images/delete-automated-actions.gif)

## Ação de automatização: Enviar notificação

Ao definir "Enviar notificação" como uma ação automática, pode definir uma notificação para um ou mais utilizadores. Os utilizadores selecionados receberão uma **notificação** sempre que o acionador correspondente for acionado. Esta ação de automatização está disponível **para todos os accionadores de automatização**.

Pode editar os **destinatários** e o **conteúdo** das notificações em qualquer altura nas **configurações** da ação. Para os destinatários, pode selecionar especificamente **utilizadores individuais** ou utilizadores numa coluna específica do tipo [Colaborador]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}}), [Criador]({{< relref "help/base-editor/spaltentypen/die-spalten-ersteller-und-erstelldatum" >}}) ou [Último modificador]({{< relref "help/base-editor/spaltentypen/die-spalten-letzter-bearbeiter-und-bearbeitungsdatum" >}}). Escreva a mensagem pretendida no campo de texto e utilize as referências de coluna entre chavetas para inserir valores específicos.

![Enviar notificação através de automatização](images/send-notification-action-settings.jpg)

Os utilizadores podem consultar as suas notificações através do {{< seatable-icon icon="dtable-icon-notice" >}} **ícone de campainha** junto ao seu avatar no canto superior direito.

![Notificação recebida](images/example-action-notification.png)

O artigo [Enviar notificações através de automatização]({{< relref "help/base-editor/automationen/benachrichtigungen-per-automation-versenden" >}}) analisa esta automatização utilizando um caso de utilização específico.

## Ação de automatização: Enviar notificação de aplicação

Ao definir "Enviar notificação de aplicação" como uma ação automatizada, pode definir uma notificação para um ou mais utilizadores de uma aplicação. Os utilizadores selecionados recebem uma **notificação** na aplicação sempre que o acionador correspondente é acionado. Esta ação de automatização está disponível **para todos os accionadores de automatização**.

Nas **Definições** da ação, pode definir para que **aplicação** e para que **receptores** as notificações devem ser enviadas. Para os destinatários, pode selecionar especificamente **utilizadores individuais da aplicação** ou notificar utilizadores numa coluna específica do tipo **Colaborador, Criador ou Último modificador**. Introduza o **conteúdo** pretendido da notificação no campo de texto. Utilize referências de coluna entre chavetas para inserir valores específicos.

![envie a notificação da aplicação através da automatização](images/send-app-notification-action-settings.jpg)

Os utilizadores da respectiva aplicação podem consultar as suas notificações através do {{< seatable-icon icon="dtable-icon-notice" >}} **ícone de campainha** junto ao seu avatar no canto superior direito.

![verifique as notificações na aplicação](images/check-app-notifications.jpg)

## Ação de automatização: Enviar e-mail

Ao definir "Enviar e-mail" como uma ação automatizada, pode enviar e-mails predefinidos a um ou mais utilizadores. SeaTable envia um **e-mail** a cada utilizador selecionado assim que o acionador correspondente é acionado. Esta ação de automatização está disponível **para todos os accionadores de automatização**.

Pode editar a **conta de e-mail**, o **assunto**, o **destinatário**, a **mensagem** e os **anexos** do e-mail em qualquer altura nas **configurações** da ação. Utilize referências de coluna entre chavetas para inserir determinados valores em campos de texto.

![definição da ação de automatização: Enviar e-mail](images/send-email-action-settings.jpg)

O artigo [Enviar e-mails através da automatização]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}}) analisa esta automatização utilizando um caso de utilização específico.

## Ação de automatização: Adicionar registro

Se definir "Adicionar registro" como uma ação automatizada, é adicionada uma **nova linha** à tabela sempre que o acionador correspondente é acionado. Pode definir antecipadamente os valores exactos para cada coluna individualmente.

![Ação automática: Adicionar registro](images/add-record-action-settings.jpg)

A ação de automatização "Adicionar registro" está atualmente disponível para os seguintes **accionadores de automatização**:
- Quando uma linha é alterada
- Quando uma linha é adicionada
- Numa hora programada

O artigo [Adicionar registros através da automatização]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-hinzufuegen" >}}) analisa esta automatização utilizando um caso de utilização específico.

## Ação de automatização: Bloquear registro

Se definir "Bloquear registro" como uma ação automatizada, a **linha** que desencadeou a automatização é bloqueada para edição. Não pode fazer quaisquer outras definições para esta ação – deve configurar as condições para o bloqueio da linha no **Acionador**. Tenha em atenção que já não pode **desbloquear** linhas bloqueadas sem direitos de administrador.

![definição da ação de automatização: Bloquear uma entrada na tabela](images/lock-record-action.jpg)

![bloqueio de uma entrada numa tabela acionada por uma automatização](images/example-locked-records.jpg)

A ação de automatização "Bloquear registro" está atualmente disponível para os seguintes **accionadores de automatização**:
- Quando uma linha é alterada
- Quando uma linha é adicionada
- Numa hora programada para entradas que preencham determinadas condições

O artigo [Bloquear linhas utilizando a automatização]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-sperren" >}}) analisa esta automatização utilizando um caso de utilização específico.

## Ação de automatização: Modificar registro

Se selecionar "Modificar registro" como uma ação automatizada, as **linhas** na tabela são ajustadas de acordo com as **configurações** previamente definidas depois de o acionador ser acionado. Pode definir um valor para cada coluna que as linhas adoptam automaticamente após a alteração.

![Ação automática: Modificar registro](images/modify-record-action-settings.jpg)

A ação de automatização "Modificar registro" está atualmente disponível para os seguintes **accionadores de automatização**:
- Quando uma linha é alterada
- Quando uma linha é adicionada
- Numa hora programada para entradas que preencham determinadas condições

## Ação de automatização: Adicionar ligações

Se selecionar "Adicionar ligações" como uma ação automática, é criada uma [ligação a outras entradas]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}}) na coluna correspondente quando o acionador é acionado. Nas **definições** da ação, pode especificar exatamente em que condições o link é adicionado à tabela.

![Ação de automatização: Adicionar ligações](images/add-links-action-settings.jpg)

A ação de automatização "Adicionar ligações" está atualmente disponível para os seguintes **accionadores de automatização**:
- Quando uma linha é alterada
- Quando uma linha é adicionada
- Numa hora programada

O artigo [Ligar entradas através da automatização]({{< relref "help/base-editor/automationen/beispiel-verlinken-von-eintraegen-per-automation" >}}) analisa esta automatização utilizando um caso de utilização específico.

## Ação de automatização: Adicionar nova entrada a outra tabela

Se selecionar "Adicionar nova entrada a outra tabela" como uma ação automatizada, é criada uma **linha noutra tabela** quando o acionador é acionado. Nas **definições** da ação, pode definir valores individuais para cada coluna que são atribuídos às linhas na tabela selecionada como parte da automatização. Também pode selecionar colunas do mesmo tipo na tabela de origem para copiar entradas de linha para a outra tabela.

![ação de automatização: Adicionar uma linha noutra tabela](images/add-record-to-other-table-action-settings.jpg)

A ação de automatização "Adicionar nova entrada noutra tabela" está atualmente disponível para os seguintes **accionadores de automatização**:
- Quando uma linha é alterada
- Quando uma linha é adicionada

O artigo [Adicionar entradas a outras tabelas através da automatização]({{< relref "help/base-editor/automationen/beispiel-eintraege-in-andere-tabellen-per-automation-hinzufuegen" >}}) analisa esta automatização utilizando um caso de utilização específico.

## Ação de automatização: Executar script Python

Se selecionar a execução de um script Python como uma ação automatizada, o acionador põe em movimento um **Script Python** previamente definido. Pode criar ou editar o script a qualquer momento no [editor de scripts]({{< relref "help/skripte/allgemein/anlegen-und-loeschen-eines-skriptes" >}}) e depois seleccioná-lo nas **definições** da ação.

![Ação de automatização: Executar script Python](images/run-python-script-action-settings.jpg)

A ação de automatização "Executar script Python" está atualmente disponível para os seguintes **accionadores de automatização**:
- Quando uma linha é alterada
- Quando uma linha é adicionada
- Numa hora programada

## Ação de automatização: Chamar a IA

Se selecionar a execução de uma função de IA como uma ação automatizada, o acionador chama um **modelo de IA** que executa uma ação predefinida na tabela. Pode configurar a ação exacta a ser executada nas **definições**. Dependendo do tipo de função de IA, podem ser necessárias **colunas de entrada**, **colunas de saída** e um **prompt**.

![definição de uma ação de automatização: Executar IA](images/run-ai-action-settings.jpg)

Pode fazer com que as seguintes **funções de IA** sejam executadas com um automatismo:

- **Resumir**: Resume o texto de uma ou mais colunas. Pode controlar a extensão, o tom, o formato e o idioma do resumo, personalizando o aviso.
- **Classificar**: Classifica os registos de uma ou mais colunas. Pode personalizar as categorias e regras utilizando o prompt. O resultado termina numa [coluna de seleção única]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}}) ou [coluna de seleção múltipla]({{< relref "help/base-editor/spaltentypen/die-mehrfachauswahl-spalte" >}}).
- **OCR**: Extrai texto de uma [coluna de imagem]({{< relref "help/base-editor/spaltentypen/die-bild-spalte" >}}). O conteúdo reconhecido é escrito na coluna de resultado do tipo [Texto ou Texto formatado]({{< relref "help/base-editor/spaltentypen/die-spalten-text-und-formatierter-text" >}}).
- **Extrair**: Extrai informações específicas de uma coluna do tipo texto ou número, de acordo com os seus requisitos. A informação extraída é escrita nas colunas de resultados.
- **Personalizar**: Gera conteúdo com base no seu pedido. Utilize {nome da coluna} entre chavetas para inserir o valor da coluna de uma linha.

![acções que podem ser executadas utilizando um modelo de IA](images/run-ai-functions.jpg)

A ação de automatização "Chamar IA" está atualmente disponível para os seguintes **accionadores de automatização**:
- Quando uma linha é alterada
- Quando uma linha é adicionada
- Numa hora programada

## Ação de automatização: Gerir eventos no Google Calendar

Se selecionar "Gerir eventos no Google Calendar" como uma ação automatizada, um compromisso do SeaTable é criado ou atualizado num calendário do Google quando o acionador é acionado. Existem alguns requisitos que devem ser cumpridos para que esta ação funcione sem problemas:
- Primeiro, tem de [sincronizar a sua conta do Google Calendar com SeaTable]({{< relref "help/integrationen/integrationen-innerhalb-von-seatable/google-calender-synchronisieren" >}}).
- Devem existir duas [colunas de data]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}) numa tabela, que definem o **início** e o **fim** das datas.
- Também precisa de uma [coluna de texto]({{< relref "help/base-editor/spaltentypen/die-spalten-text-und-formatierter-text" >}}) na qual o Google pode escrever o **identificador do evento** para que os compromissos possam ser sincronizados.

![requisitos para gerir eventos no Calendário Google](images/manage-events-in-google-calendar-part-1.png)

Também pode efetuar outras definições. Adicione um **título**, uma **descrição**, uma **localização** e **participantes** ao evento. Para o fazer, escreva os detalhes nos **campos de texto** ou trabalhe com **referências de coluna entre parênteses rectos** para inserir valores específicos da tabela. Ao ativar os **controladores**, pode decidir se pretende enviar notificações, se se trata de uma videoconferência e se os convidados podem editar o compromisso, ver a lista de convidados e convidar outros convidados.

![mais definições para eventos no Google Calendar](images/manage-events-in-google-calendar-part-2.png)

A ação de automatização "Gerir eventos no Google Calendar" está atualmente disponível para os seguintes **accionadores de automatização**:
- Quando uma linha é alterada
- Quando uma linha é adicionada

## Ação de automatização: Executar processamento de dados

Se selecionar a execução de processamento de dados como uma ação automatizada, o acionador inicia uma [operação de processamento de dados]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitungsoperationen-in-seatable" >}}) predefinida na tabela. Pode configurar a ação exacta a ser executada nas **definições**. Dependendo do tipo de operação, podem ser necessárias **certas colunas de entrada e saída**.

![definição de uma ação de automatização: Executar operação de processamento de dados](images/run-data-processing-action-settings.jpg)

Pode fazer com que as seguintes **operações de processamento de dados** sejam executadas com um automatismo:

- [Calcular delta]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-veraenderungen-berechnen" >}})
- [Calcular a porcentagem]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-prozentualen-anteil-berechnen" >}})
- [Calcular a classificação]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-rangliste-berechnen" >}})
- [Extraia o nome de usuário]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-benutzernamen-uebertragen" >}})
- [Comparar e copiar]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-vergleichen-und-kopieren" >}})

![Operações de processamento de dados que podem ser executadas utilizando a automatização](images/run-data-processing-available-operations.jpg)

A ação de automatização "Executar operação de processamento de dados" está atualmente disponível para o seguinte **acionador de automatização**:
- Numa hora programada

## Ação de automatização: Converter página em PDF

Se selecionar "Converter página em PDF" como uma ação automatizada, o SeaTable irá **criar um documento PDF a partir do conjunto de dados** quando o acionador for acionado e guardá-lo numa [coluna de ficheiro]({{< relref "help/base-editor/spaltentypen/die-datei-spalte" >}}). Para o fazer, selecione um **template** que tenha criado previamente no [plugin de design de página]({{< relref "help/base-editor/plugins/anleitung-zum-seitendesign-plugin" >}}). Também pode definir o **nome do ficheiro** nas definições da ação.

![Criar PDF através da automatização](images/convert-page-to-pdf-action-settings.jpg)

A ação de automatização "Converter página em PDF" está atualmente disponível com o seguinte **acionador de automatização**:
- Numa hora programada para entradas que satisfaçam determinadas condições

## Ação de automatização: Gerar PDF a partir do documento e enviar

Se selecionar "Gerar PDF a partir do documento e enviar" como uma ação automatizada, SeaTable irá **criar um documento PDF** quando o acionador for acionado e guardá-lo na [gestão de ficheiros]({{< relref "help/base-editor/dateien/das-dateimanagement-einer-base" >}}). O SeaTable também pode enviá-lo diretamente por correio eletrónico.

Nas **definições** da ação, selecione um **template** que tenha criado anteriormente no **Plugin de conceção de relatórios** e atribua um **nome de ficheiro**. Em seguida, active o cursor para selecionar uma **pasta própria** na qual gostaria de guardar o ficheiro. Se apenas pretender gerar o documento, pode terminar a configuração neste ponto.

![criar e enviar PDF a partir de um design de relatório utilizando a automatização](images/generate-pdf-from-document-action-settings.jpg)

Se pretender enviar o documento gerado, active o seletor "Enviar para e-mail". Pode editar a **conta de correio eletrónico**, o **destinatário**, o **assunto** e a **mensagem** do correio eletrónico em qualquer altura nas **configurações** da ação.

![criar e enviar PDF a partir de um desenho de relatório utilizando a automatização](images/generate-pdf-from-document-and-send-action-settings.jpg)

A ação de automatização "Gerar PDF a partir do documento e enviar" está atualmente disponível com o seguinte **acionador de automatização**:
- Numa hora programada

## Ação de automatização: Arquivar

Pode utilizar a ação de arquivamento para [mover automaticamente as linhas para a memória de big data]({{< relref "help/base-editor/big-data/zeilen-ins-big-data-backend-verschieben" >}}). A função de big data deve, naturalmente, ser activada na respectiva base. Uma vez que já definiu a **vista** e quaisquer condições de filtragem para as linhas a arquivar nas definições do acionador, não pode efetuar quaisquer definições para a própria ação.

![Arquivar linhas através da automatização](images/automated-action-archive.png)

A ação de automatização "Arquivar" está atualmente disponível para os seguintes **accionadores de automatização**:
- Numa hora programada
- Numa hora programada para entradas que preencham determinadas condições