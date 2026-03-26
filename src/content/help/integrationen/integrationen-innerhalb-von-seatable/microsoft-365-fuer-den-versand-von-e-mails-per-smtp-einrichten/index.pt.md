---
title: 'Configurar o Microsoft 365 para enviar emails via SMTP'
date: 2023-04-28
lastmod: '2025-03-07'
categories:
    - 'integrationen-innerhalb-von-seatable'
author: 'nsc2'
url: '/pt/ajuda/microsoft-365-smtp-envio-email'
aliases:
    - '/pt/ajuda/microsoft-365-fuer-den-versand-von-e-mails-per-smtp-einrichten'
seo:
    title: 'Microsoft 365 com SeaTable: Configure envio de e-mails via SMTP seguro'
    description: 'Veja como integrar Microsoft 365 ao SeaTable para enviar e-mails via SMTP com OAuth2, incluindo cadastro da app, autenticação e configurações detalhadas.'
---

**O Microsoft 365**, o popular serviço online para as aplicações Office da Microsoft, pode ser utilizado para **enviar mensagens de correio eletrónico a partir do SeaTable**. A autenticação no seu Microsoft 365 deve ser efectuada utilizando a autenticação moderna da Microsoft. (A autenticação através do nome de utilizador e da palavra-passe do utilizador não é possível com o Microsoft 365).

{{< warning headline="Contas do Outlook" text="Estas instruções explicam o procedimento utilizando uma conta Microsoft 365. No entanto, o procedimento também se aplica a contas de correio eletrónico gratuitas do Outlook." />}}

## Preparação no Entra Admin Centre

Para poder utilizar a sua conta Microsoft 365 no SeaTable para enviar e-mails, deve primeiro criar e configurar uma aplicação no Entra Admin Centre da Microsoft.

1. Inicie sessão no [Microsoft Entra Admin Centre](https://entra.microsoft.com/). O utilizador necessita de direitos de administrador para a conta que será utilizada para o envio.
2. Clique em **Registos de aplicações** na barra de navegação da página.
3. Crie um novo login clicando em **\+ Novo registo**. Introduza um nome (por exemplo, 'SeaTable') e selecione **Qualquer Inquilino do Entra ID + contas Microsoft pessoais** como tipo de conta. Registe o seguinte URI de redirecionamento para uma aplicação do tipo **Web**.

    ```
    https://cloud.seatable.io/oauth/third-party-email-accounts/callback/
    ```

    Se não estiver a utilizar o SeaTable Cloud, substitua cloud.seatable.io pelo nome do anfitrião da sua instância do SeaTable. Conclua a criação do registo da aplicação clicando em **Registar**.

4. Tome nota do **ID da aplicação (cliente)** na página de resumo da aplicação atualmente registada. Isto é necessário para configurar a conta de correio eletrónico no SeaTable.
5. Para gerar a chave de cliente, aceda a **Certificados e segredos** no menu de navegação da aplicação. Clique em **Novo segredo de cliente**. Introduza uma descrição e uma data de validade para a chave.

    ![Criar um segredo de cliente para uma aplicação registada no Microsoft Entra](images/Creating_Client_Secret_Microsoft_Entra.gif)

6. Copia o valor da chave criada para a área de transferência.

Já fez todos os preparativos para poder utilizar a sua conta Microsoft 365 como uma conta de correio electrónico no SeaTable.

## Criação da conta de email no SeaTable

Agora é necessário adicionar a sua conta Microsoft 365 ao SeaTable Base. Para o fazer, são necessários os seguintes passos:

1. Abra as opções da base alargada clicando no **ícone de três pontos** {{< seatable-icon icon="dtable-icon-more-level" >}} no canto superior direito.
2. Seleccionar a opção **Integração de Terceiros**.
   ![Integração de terceiros através das opções de base avançadas](images/Integration-von-Drittanbietern-ueber-die-erweiterten-Base-Optionen.png)
3. Clique em **Adicionar conta de correio eletrónico**.
4. Selecione **Microsoft (Microsoft 365 and Outlook)** como o fornecedor de serviços.
5. Introduza as seguintes informações e, em seguida, clique no botão **Enviar** no canto superior direito:
    - **Nome da conta**: Uma breve descrição da conta (por exemplo, "Microsoft 365")
    - **ID da aplicação (cliente)**: o ID da aplicação (cliente) da aplicação criada
    - **Chave de cliente**: a chave de cliente secreta da aplicação criada
6. Conceda as permissões solicitadas clicando em **Aceitar**.
   ![O screencast aceita as permissões solicitadas](images/Accept-Permissions-Requested-Microsoft.gif)

## Enviar e-mails através de automação ou botão

Pode então utilizar a conta de correio electrónico criada no seu SeaTable Base para enviar mensagens de correio electrónico através de [automação]({{< relref "help/base-editor/schaltflaechen/eine-e-mail-per-schaltflaeche-verschicken" >}}) ou botão.

Se quiser saber mais sobre esta funcionalidade útil, leia o artigo [Configurar uma conta de correio electrónico numa Base]({{< relref "help/base-editor/weitere-optionen/einrichtung-eines-e-mail-kontos-in-einer-base" >}}).
