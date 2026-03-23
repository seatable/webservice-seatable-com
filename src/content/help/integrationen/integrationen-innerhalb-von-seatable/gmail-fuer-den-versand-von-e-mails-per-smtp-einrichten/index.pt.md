---
title: 'Configurar o Gmail para enviar e-mails via SMTP'
date: 2023-01-10
lastmod: '2025-03-07'
categories:
    - 'integrationen-innerhalb-von-seatable'
author: 'cdb'
url: '/pt/ajuda/configurar-gmail-para-smtp-seatable'
aliases:
    - '/pt/ajuda/gmail-fuer-den-versand-von-e-mails-per-smtp-einrichten'
seo:
    title: 'Como configurar Gmail para SMTP no SeaTable'
    description: 'Aprenda passo a passo a integrar Gmail ao SeaTable por SMTP, usando app password ou OAuth2. Resultados seguros e integração confiável.'
---

O **Gmail**, o popular serviço de correio eletrónico da Google, pode ser utilizado para **enviar mensagens de correio eletrónico a partir do SeaTable**. A autenticação da conta Google pode ser feita através de uma palavra-passe da aplicação ou através de OAuth. O OAuth é o método preferido pela Google, mas também é muito mais difícil de configurar. (A autenticação através do nome de utilizador e da palavra-passe do utilizador não é possível com o Gmail).

{{< warning headline="Atenção às contas do espaço de trabalho" text="Estas instruções explicam o procedimento utilizando uma conta simples do Gmail. No entanto, o procedimento aqui descrito também se aplica às contas do Google Workspace. Se tiver uma conta do Workspace, só tem de se certificar de que a verificação em duas etapas está activada." />}}

## Autenticação através da palavra-passe da aplicação

Uma [palavra-passe de aplicação](https://support.google.com/accounts/answer/185833?hl=de) é um código de segurança de 16 dígitos que as aplicações ou dispositivos podem utilizar para se autenticarem junto da Google e, assim, obterem acesso à sua conta Gmail. Pode criar palavras-passe de aplicações na sua [conta Google](https://myaccount.google.com/). As palavras-passe de aplicações só podem ser utilizadas em contas que tenham a autenticação de dois factores activada.

### Criação de uma palavra-passe de aplicação

1. Abra a [gestão de palavras-passe da aplicação](https://myaccount.google.com/apppasswords) do Google - inicie sessão na sua **conta Google** quando lhe for pedido.
2. Introduza um **nome**, por exemplo, "SeaTable", e clique em **Criar**.

![Gerar uma palavra-passe da aplicação Google](images/Google_App_Password.gif)

3. Copie a palavra-passe da aplicação gerada para a área de transferência.

{{< warning headline="As palavras-passe das aplicações destinam-se a uma utilização única" text="A palavra-passe da aplicação só é apresentada depois de ter sido criada. Não pode ser recuperada ou alterada posteriormente. Se pretender utilizar a sua conta Gmail em várias bases para enviar e-mails, recomendamos que crie várias palavras-passe de aplicações e que atribua a cada uma um nome descritivo." />}}

### Criação da conta de correio eletrónico no SeaTable

Agora precisa de adicionar a sua conta Gmail como terceiro na sua base SeaTable. Para tal, são necessários os seguintes passos:

1. Abra as opções da base alargada clicando no **ícone de três pontos** {{< seatable-icon icon="dtable-icon-more-level" >}} no canto superior direito.
2. Selecione a opção **Integração de fornecedores terceiros**.

![Integração de terceiros através das opções de base avançadas](images/Integration-von-Drittanbietern-ueber-die-erweiterten-Base-Optionen.png)

3. Clique em **Adicionar conta de correio eletrónico**.
4. Selecione Fornecedor de **correio eletrónico genérico** como fornecedor de serviços.
5. Introduza a seguinte informação:
    - **Nome da conta**: qualquer nome para a conta, por exemplo, 'Gmail'
    - **Servidor SMTP**: 'smtp.gmail.com'
    - **Porta SMTP**: '587'
    - **Nome de utilizador**: O seu endereço Gmail, por exemplo, 'seatable@gmail.com'
    - **Palavra-passe**: a palavra-passe da aplicação gerada a partir da cache

![Configurar o Gmail com a palavra-passe da aplicação para enviar mensagens de correio eletrónico a partir de uma base SeaTable](images/ThirdPartyIntegration_Gmail.png)

## Autenticação via OAuth 2.0

O OAuth 2.0, abreviatura de Open Authorisation 2.0, é um protocolo aberto que permite que as aplicações (Web) acedam de forma segura às contas de utilizador de outras aplicações. Isto significa que um utilizador pode utilizar recursos ou serviços de outra aplicação a partir de uma aplicação, por exemplo, enviar mensagens de correio eletrónico do SeaTable através do Gmail.

Para que o SeaTable aceda a uma conta Gmail através do OAuth 2.0, é necessário criar um ID de cliente e uma chave de cliente na Consola de Nuvem do Google e guardá-los no SeaTable.

### Criação de dados de acesso na Consola Google Cloud

Sendo uma plataforma para programadores, a Consola Cloud parece confusa para os utilizadores normais. Não se deixe impressionar por isso. Com o seguinte guia passo-a-passo, qualquer pessoa pode configurá-la.

1. Abra a [Consola do Google Cloud](https://console.developers.google.com/) e inicie sessão na sua **conta Google** quando lhe for solicitado.
2. Primeiro, crie um novo projeto. Todas as definições descritas abaixo são efectuadas neste projeto. Introduza um nome de projeto (por exemplo, "SeaTable") e selecione o local de armazenamento. (Se não estiverem definidas organizações, selecione "Nenhuma organização").
3. Permitir que o projeto criado utilize a API do Gmail. Para tal, clique com o rato no campo de pesquisa na parte superior do ecrã, introduza "Gmail API" e clique no resultado de pesquisa correspondente. Ativar a API do Google.
4. Todos os passos seguintes são efectuados na **plataforma Google Auth**. Clique no ícone de sanduíche no canto superior esquerdo e, em seguida, selecione "Todos os produtos" na secção "Soluções". Na página do produto, clique em "Google Auth Platform".

![Navegando para a Plataforma de autenticação do Google no Console do Google Cloud](images/GoogleAuthPlatform.png)

5. Efectue as **configurações necessárias** na plataforma Google Auth: Introduza um nome de aplicação, um endereço de correio eletrónico de apoio e um endereço de correio eletrónico de contacto (por exemplo, o seu endereço Gmail). Selecione "Externo" como grupo-alvo. Aceite os termos de utilização e finalize a configuração.
6. Clique em **Público-alvo** na página de navegação da Google Auth Platform. Adicione o seu endereço de e-mail do Google como um utilizador de teste.
7. Na página de navegação da Google Auth Platform, clique em **Clientes** e crie um cliente OAuth 2.0. Selecione "Aplicação Web" como o tipo de aplicação para o cliente OAuth e introduza um nome (por exemplo, "SeaTable"). Ignore as "Fontes JavaScript autorizadas" e adicione o seguinte URI como "URI de reencaminhamento autorizado":

    ```
    https://cloud.seatable.io/oauth/third-party-email-accounts/callback/
    ```

    Se não estiver a utilizar o SeaTable Cloud, substitua cloud.seatable.io pelo nome de anfitrião da sua instância do SeaTable. Role até a parte inferior da página e confirme a criação do cliente OAuth.

![Um cliente OAuth 2.0 configurado no Google Cloud Console](images/Configured_OAuth_Client_GoogleCloudConsole.png)

8. O cliente recém-criado é agora apresentado na lista de clientes OAuth 2.0. As definições do cliente podem ser apresentadas clicando no seu nome. O ID do cliente apresentado e a chave secreta do cliente são essenciais para a configuração subsequente no SeaTable.

Se cometeu um erro durante a configuração e já não sabe onde está, clique no ícone da sanduíche no canto superior direito. A partir daí, pode navegar de volta para a Plataforma de autenticação do Google.

### Criação da conta de correio eletrónico no SeaTable

Agora precisa de adicionar a sua conta Gmail como terceiro na sua base SeaTable. Para tal, são necessários os seguintes passos:

1. Abra as opções da base alargada clicando no **ícone de três pontos** {{< seatable-icon icon="dtable-icon-more-level" >}} no canto superior direito.
2. Selecione a opção **Integração de fornecedores terceiros**.
3. Clique em **Adicionar conta de correio eletrónico**.
4. Selecione **Gmail** como fornecedor de serviços.
5. Introduza a seguinte informação:

    - **Nome da conta**: qualquer nome para a conta, por exemplo, 'Gmail'
    - **ID do cliente**: o ID do cliente do cliente OAuth criado
    - **Chave secreta de cliente**: a chave de cliente do cliente OAuth criado

6. Clique em **Seguinte** quando for notificado de que esta aplicação não foi verificada e permita o acesso à conta Google.

## Envio de e-mails por automatização

Pode então utilizar a conta de e-mail criada na sua Base SeaTable para enviar e-mails através de automatização ou [botão]({{< relref "help/base-editor/schaltflaechen/eine-e-mail-per-schaltflaeche-verschicken" >}}).

Se quiser saber mais sobre esta automatização útil, leia o artigo [Envio por correio electrónico através de automatização]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}}).
