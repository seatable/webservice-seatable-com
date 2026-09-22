---
title: 'Configurar o GMX ou WEB.DE para enviar mensagens de correio eletrónico através de SMTP'
date: 2023-03-10
lastmod: '2025-02-14'
categories:
    - 'integrationen-innerhalb-von-seatable'
author: 'cdb'
url: '/pt/ajuda/configurar-gmx-ou-web-de-para-envio-smtp'
aliases:
    - '/pt/ajuda/gmx-oder-web-de-fuer-den-versand-von-e-mails-per-smtp-einrichten'
seo:
    title: 'Configurar GMX ou WEB.DE para envio SMTP no SeaTable'
    description: 'Aprenda a conectar contas GMX ou WEB.DE no SeaTable para envio de emails seguro via SMTP com guia passo a passo detalhado.'
---

Os serviços de correio eletrónico GMX e WEB.DE são muito populares nos países de língua alemã. Pode utilizar as contas GMX e WEB.DE para enviar mensagens de correio eletrónico a partir de um SeaTable Bases.

Este artigo explica como configurar uma conta de correio eletrónico **GMX** ou **WEB.DE** numa SeaTable Base e quais as medidas preparatórias necessárias.

{{< warning headline="Procedimento idêntico para GMX e WEB.DE" text="**GMX** e **WEB.DE** são ofertas do fornecedor de telecomunicações alemão 1&1. O procedimento para integrar uma conta de correio eletrónico num SeaTable Base é demonstrado neste artigo de ajuda utilizando o GMX como exemplo. Se pretender utilizar uma conta WEB.DE, siga as instruções da mesma forma. O passo preparatório deve ser efectuado nas definições da conta WEB.DE." />}}

**Neste vídeo tutorial, mostraremos como configurar sua conta de e-mail no SeaTable (com legendas em português).**

{{< youtube 5AcQzZiwCx0 >}}

## Permitir a recuperação de POP3/IMAP

Por defeito, as contas GMX e WEB.DE só podem ser utilizadas através dos webmailers ou das aplicações dos dois fornecedores. A recuperação e o envio de mensagens de correio eletrónico com um programa de terceiros, como o Outlook, o Thunderbird e o SeaTable, têm de ser explicitamente aprovados. Pode fazê-lo nas definições da sua conta.

1. Inicie sessão na sua **conta de correio eletrónico GMX**.
2. Chame as **definições** da sua conta.

![Definições dentro do GMX](images/gmx-free-email-smtp-versand-mit-seatable.jpg)

4. Clique em **Recuperação POP3/IMAP** nas definições de correio eletrónico.
5. Ativar **Permitir acesso POP3 e IMAP**.

![Permitir SMTP para GMX e WEB.De.](images/activate_smtp_for_gmx.png)

7. **Guarde** o seu troco.

Já fez todos os preparativos para poder utilizar esta conta de correio eletrónico no SeaTable para enviar mensagens de correio eletrónico.

## Criação da conta de correio eletrónico no SeaTable

Agora, adicione a sua conta de correio eletrónico como **fornecedor de terceiros** no seu SeaTable Base. Para tal, são necessários os seguintes passos:

![Integração de terceiros através das opções de base avançadas](images/Integration-von-Drittanbietern-ueber-die-erweiterten-Base-Optionen.png)

1. {{< seatable-icon icon="dtable-icon-more-level" >}}Abra as opções da base alargada clicando no **ícone de três pontos**.
2. Selecione a opção **Integração de fornecedores terceiros**.
3. Clique em **Adicionar conta de correio eletrónico**.

4. Introduza a seguinte informação:
    - **Nome da conta**: qualquer nome para a conta, por exemplo, "GMX
    - **Remetente**: O seu endereço GMX, por exemplo, "seatable@gmx.de
    - **Servidor SMTP**: 'mail.gmx.net'
    - **Porta SMTP**: '587'
    - **Nome de utilizador**: O seu endereço GMX, por exemplo, "seatable@gmx.de
    - **Palavra-passe**: a palavra-passe da sua conta GMX

Os campos anfitrião IMAP e porta IMAP podem permanecer vazios. Os dados do servidor SMTP para o WEB.DE podem ser encontrados na [secção de ajuda do WEB.DE.](https://hilfe.web.de/pop-imap/imap/imap-serverdaten.html)

Um exemplo de configuração para uma conta GMX é o seguinte:  
![Definições SMTP do GMX](images/smtp-settings-gmx.jpg)

## Envio de e-mails por automatização

Pode então utilizar a conta de e-mail criada na sua Base SeaTable para enviar e-mails através de automatização ou [botão]({{< relref "help/base-editor/schaltflaechen/eine-e-mail-per-schaltflaeche-verschicken" >}}).

Se quiser saber mais sobre esta automatização útil, leia o artigo [Envio por correio electrónico através de automatização]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}}).
