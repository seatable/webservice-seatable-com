---
title: 'Gestão de utilizadores e funções de uma aplicação'
date: 2023-05-02
lastmod: '2024-12-13'
categories:
    - 'universelle-apps'
author: 'nsc2'
url: '/pt/ajuda/gerenciamento-usuarios-e-funcoes-app-universal'
aliases:
    - '/pt/ajuda/benutzer-und-rollenverwaltung-einer-universellen-app'
seo:
    title: 'Gestão de utilizadores e funções na aplicação'
    description: 'Saiba como adicionar utilizadores, atribuir funções e criar ligações de convite nas aplicações do SeaTable. Guia detalhado para o controlo de acessos.'
---

Quer se trate de adicionar **novos utilizadores**, atribuir **funções** ou criar **ligações de convite** – na gestão de utilizadores e funções de uma aplicação, pode realizar diversas tarefas administrativas. Pode aceder à **gestão de utilizadores e funções** através do modo de edição da sua aplicação.

{{< warning  headline="Autorização necessária no grupo"  text="Para poder editar uma aplicação, tem de ser **proprietário** ou **administrador do grupo** em que se encontra a **base** subjacente. Os simples **membros do grupo** só podem ver e utilizar as aplicações." />}}

## Gestão de utilizadores e funções da aplicação

1. Abra uma **base** à qual já tenha adicionado uma aplicação.
2. Clique em **Apps** no cabeçalho da base.
   ![Clique em Apps no cabeçalho da base](images/click-apps-in-the-base-header.jpg)
3. Passe o rato sobre a aplicação e clique no **ícone do lápis** {{< seatable-icon icon="dtable-icon-rename" >}}.
   ![Clique no ícone do lápis](images/add-page-to-universal-app-1.png)
4. Abra a **gestão de utilizadores e funções** no canto superior esquerdo da página.
   ![Ícone da gestão de utilizadores e funções](images/Symbol-fuer-Benutzer-und-Rollenverwaltung.png) 
5. Efetue as **definições** pretendidas.

## As definições em pormenor

### Utilizadores

Na primeira secção, encontrará uma visão geral de todos os **utilizadores** que têm acesso à sua aplicação. Além disso, encontrará aqui também a **função** e o **estado** de cada utilizador.

![Visão geral do separador Utilizadores da gestão de utilizadores e funções de uma aplicação](images/user-and-role-management-overview-1.png)

Nesta secção, dispõe ainda de várias opções para **gerir os utilizadores atuais** da sua aplicação.

Utilize a **função de pesquisa** para encontrar um utilizador específico. Esta função pode ser especialmente útil se a sua aplicação tiver um grande número de utilizadores.

![Função de pesquisa para utilizadores da aplicação](images/search-function-app-users.png)

Para adicionar um utilizador à aplicação, clique em **Importar utilizadores**, procure-o no campo de entrada e, em seguida, atribua-lhe uma função.

![Clique em Importar utilizadores](images/import-user-to-app.jpg)

![Importar um utilizador para a sua aplicação](images/import-users-to-app.png)

Clique em **Sincronizar utilizadores com a base** para recolher automaticamente os **utilizadores da aplicação** numa tabela da sua base.

![Clique em Sincronizar utilizadores com a base](images/click-sync-users-to-base-1.jpg) ![Tabela em que os utilizadores da aplicação são recolhidos automaticamente](images/table-with-app-users.png)

Se, no futuro, adicionar mais utilizadores desta forma, pode sempre clicar novamente em **Sincronizar utilizadores com a base** para adicionar os **novos utilizadores** à tabela.

![Se, no futuro, adicionar mais utilizadores à sua aplicação, ...](images/if-you-add-more-users-to-your-app.png)

![... pode sempre clicar novamente em Sincronizar utilizadores com a base para adicionar automaticamente os novos utilizadores à tabela.](images/added-imported-app-users-to-table.png)

Para **eliminar** um utilizador da aplicação, basta clicar no **ícone X**, que se encontra à direita do estado do respetivo utilizador.

![Eliminar utilizador](images/delete-user.jpg)

Ao clicar nos **ícones de lápis** {{< seatable-icon icon="dtable-icon-rename" >}} que encontra para cada utilizador, pode editar a respetiva **função** e o respetivo **estado**.

{{< warning  headline="Nota importante"  text="Tenha em atenção que o **utilizador** que adicionou a aplicação à base é automaticamente registado como **Admin**. **Não** é possível editar nem a função nem o estado deste utilizador, e este também **não** pode ser removido da aplicação." />}}

![Ícones de edição para cada utilizador](images/edit-icons-users.jpg)

Para a **função de um utilizador**, o menu pendente disponibiliza todas as funções que pode definir na secção seguinte da gestão de utilizadores e funções.

![Seleção da função de um utilizador](images/select-role-of-user.png)

O **estado** de um utilizador pode ser definido como **Ativo** ou **Inativo**. Enquanto os utilizadores **ativos** têm acesso à aplicação e ao seu conteúdo, os utilizadores **inativos** perdem esse acesso.

![Edição do estado de um utilizador da aplicação](images/edit-status-of-app-user.png)

Os utilizadores que não têm acesso à sua aplicação veem esta mensagem:

![Acesso negado à aplicação para utilizadores inativos](images/no-permission-for-inactive-users.png)

### Funções

Nesta secção, pode definir qualquer número de **funções**, que pode atribuir aos vários utilizadores da aplicação na secção acima.

![Definição de diferentes funções para os utilizadores da aplicação](images/define-roles-for-app-users.jpg)

Aqui, define inicialmente apenas os **nomes** das funções. Quais as **permissões** que os utilizadores com as diferentes funções têm, pode definir individualmente para cada página da aplicação.

[Saiba mais sobre as permissões de página aqui.]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}})

### Ligação de convite

Na terceira secção da gestão de utilizadores e funções, pode gerar uma **ligação de convite** individual para a aplicação.

Primeiro, defina a **função** dos utilizadores que irão aceder à aplicação através da ligação de convite.

![Seleção da função que os utilizadores que acedem à aplicação através da ligação de convite irão receber](images/select-role-for-invite-link.png)

Em seguida, tem a opção de definir uma **palavra-passe** que deve ser introduzida depois de abrir a ligação de convite para obter acesso à aplicação.

![Adicionar uma palavra-passe à ligação de convite](images/add-password-protection.png)

Opcionalmente, pode também adicionar à ligação de convite um **prazo de expiração** automático que determina durante quanto tempo esta é válida.

![Adicionar um prazo de expiração automático à ligação de convite](images/add-auto-expiration.png)

Clique em **Gerar** para criar a ligação de convite. A ligação é então apresentada abaixo e tem a opção de a **copiar** ou **eliminar**.

![Ligação de convite gerada com as opções disponíveis para a copiar e eliminar](images/copy-and-delete-link-universal-app.png)

Em alternativa, tem a opção de gerar um **código QR** para abrir e partilhar a aplicação.

![Apresentar o código QR para abrir e partilhar a aplicação](images/show-qr-code-universal-app.png)

Digitalize o **código QR** apresentado para abrir a sua aplicação, ou partilhe-o com outros utilizadores para lhes dar **acesso** à sua aplicação.

![Código QR para abrir e partilhar a aplicação](images/qr-code-to-share-universal-app.png)
