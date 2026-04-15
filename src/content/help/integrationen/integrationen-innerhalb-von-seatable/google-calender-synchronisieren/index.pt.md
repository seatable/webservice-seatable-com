---
title: 'Sincronizar os compromissos no SeaTable com um calendário do Google'
date: 2026-03-23
lastmod: '2026-03-23'
categories:
    - 'integrationen-innerhalb-von-seatable'
author: 'rdb'
url: '/pt/ajuda/sincronizar-compromissos-com-google-calendar'
seo:
    title: 'Sincronize os compromissos no SeaTable com um calendário do Google'
    description: 'Instruções passo a passo para sincronizar compromissos no SeaTable com um calendário do Google.'
---

Os compromissos num SeaTable Base podem ser automaticamente sincronizados com um ou mais **calendários do Google**. Isto significa que tem sempre os seus compromissos actuais disponíveis no seu calendário Google no seu PC e dispositivos móveis.

Antes de configurar a sincronização de compromissos, deve configurar a **conta Google** do calendário para o qual pretende transferir os compromissos no SeaTable. Isto é feito em dois passos: Primeiro, crie **credenciais de autenticação** na Consola Google Cloud. Em seguida, crie uma conta de terceiros no SeaTable com os dados de acesso e ligue-a ao Google. Isto é muito fácil com estas instruções passo a passo.

## Criação dos dados de acesso na Consola Google Cloud

Sendo uma plataforma para programadores, a Google Cloud Console parece inicialmente confusa para os utilizadores normais. Não deixe que isso o impressione. O seguinte guia passo a passo vai ajudá-lo a configurá-lo sem dores de cabeça.

1. Abra a [Consola Google Cloud](https://console.cloud.google.com/) e inicie sessão na sua **Conta Google** quando solicitado.
2. Clique em **Selecionar projeto** na parte superior, junto ao logótipo do Google Cloud, e crie um **Novo projeto**. Todas as definições explicadas abaixo são efectuadas neste projeto.
   ![seleção de projeto no Google Cloud](images/GoogleConsole_CreateNewProject_723.png)
3. Introduza um **Nome do projeto** (por exemplo, SeaTable Base XY) e selecione o **Local de armazenamento**. Se não existirem organizações definidas, selecione "No organization" (Sem organização). Confirme com **Criar**.
   ![criar novo projeto na Consola Google Cloud](images/GoogleConsole_NewProject_723.png)
4. Permita que o projeto criado utilize a API do Google Calendar. Para isso, clique com o rato no **campo de pesquisa** na parte superior da página, introduza **API do Google Calendar** e clique no resultado de pesquisa correspondente. Em seguida, active a API do Google Calendar.
   ![active a API do Google Calendar](images/GoogleConsole_EnableCalendarAPI_722.gif)
5. Clique no ícone do menu de hambúrguer no canto superior esquerdo para visualizar a navegação e, em seguida, selecione a opção **Todos os produtos** na secção "Soluções". Na página do produto, clique em **Google Auth Platform**.
   ![chame a Google Auth Platform](images/GoogleConsole_SwitchAuthPlatform_722.gif)
6. Efectue as configurações necessárias na Google Auth Platform, clicando em **Primeiros passos**: Introduza um **Nome da aplicação** e um **Endereço de correio eletrónico de apoio** (por exemplo, o seu endereço Gmail). Selecione **Externo** como grupo-alvo. Introduza um **Endereço de correio eletrónico de contacto** (por exemplo, o seu endereço Gmail). Aceite os **Termos de utilização** e finalize a configuração.
7. Clique em **Grupo alvo** na navegação lateral da Google Auth Platform. Adicione o seu endereço de e-mail do Google como **utilizador de teste**.
8. Clique em **Clients** na navegação lateral da Google Auth Platform e crie um cliente OAuth 2.0. Selecione a opção "Aplicação Web" como **Tipo de aplicação** para o cliente OAuth e introduza um **Nome** (por exemplo, SeaTable). Ignore "Fontes JavaScript autorizadas" e insira o seguinte URI como **URI de redireccionamento autorizado** antes de clicar em **Criar**:

    ```
    https://cloud.seatable.io/oauth/google-calendar/callback/
    ```

    Se estiver a utilizar o seu próprio sistema em vez do SeaTable Cloud, substitua cloud.seatable.io pelo nome do anfitrião da sua instância do SeaTable.

   ![Criar cliente OAuth](images/GoogleConsole_CreateClient_722.gif)

9. O cliente recém-criado é agora exibido na lista de clientes OAuth 2.0. As definições do cliente podem ser apresentadas clicando no seu nome. A **identificação do cliente** e a **chave do cliente** apresentadas são essenciais para a seguinte configuração no SeaTable.

{{< warning headline="Não entre em pânico" text="Se cometeu um erro durante a configuração e já não sabe onde está, clique no ícone do menu de hambúrguer no canto superior esquerdo. A partir daí, pode navegar de volta para a Plataforma de autenticação do Google através de **Acedido recentemente**." />}}

## Criar a conta Google no SeaTable

Agora precisa de adicionar a sua conta Google como uma **conta de terceiros no seu SeaTable Base**. Para tal, são necessários os seguintes passos:

1. Abra as opções avançadas da base clicando no ícone de **três pontos** {{< seatable-icon icon="dtable-icon-more-level" >}} no canto superior direito.
   ![abra o menu para integração de terceiros](images/third-party-integration.png)
2. Selecione a opção **Integração de terceiros**.
3. Clique em **Google Calendar** na navegação à esquerda e depois em **Adicionar conta Google Calendar** no canto superior direito.
   ![adicione uma conta do Google Calendar](images/add-google-calendar-account-in-seatable.png)
4. Introduza as seguintes informações:
    - **Nome da conta**: qualquer nome para a conta, por exemplo, Google
    - **ID do cliente**: a ID do cliente OAuth criado
    - **Chave do cliente**: a chave do cliente OAuth criado
5. Depois de ter clicado em **Submeter**, abre-se uma janela do browser. Clique em **Próximo** se for informado de que esta aplicação não foi verificada e permita o acesso à conta Google.
6. Pode encontrar a conta criada da mesma forma em **Contas do Google Calendar**.

## Transfira automaticamente os compromissos para o Calendário Google

Se tiver configurado a conta Google, pode transferir e atualizar automaticamente os compromissos do SeaTable para o seu Google Cloud Calendar. A configuração da transferência de dados do SeaTable para o Google Calendar é feita através de uma [ação]({{< relref "help/base-editor/automationen/automations-aktionen" >}}) numa regra de automatização.
