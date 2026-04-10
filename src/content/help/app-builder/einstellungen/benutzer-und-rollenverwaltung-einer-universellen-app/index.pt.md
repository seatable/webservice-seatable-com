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
    title: 'Gerenciando usuários e funções na aplicação'
    description: 'Saiba como adicionar usuários, atribuir papéis e criar links para convidar em aplicações do SeaTable. Guia detalhado para controle de acesso.'
---

Quer seja para adicionar **novos utilizadores**, atribuir **funções** ou criar **ligações de convite** - pode realizar várias actividades administrativas na administração de utilizadores e funções de uma aplicação. Pode aceder à administração de **utilizadores e funções** através do modo de edição da sua aplicação.

{{< warning  headline="Autorização necessária no grupo"  text="Para poder editar uma aplicação, tem de ser o **proprietário** ou **administrador do grupo** em que a **base** subjacente se encontra. **Os membros** simples **do grupo** só podem ver e utilizar as aplicações." />}}

## Administração de utilizadores e funções da aplicação

1. Abra uma **Base** à qual já tenha adicionado uma aplicação.
2. Clique em **Apps** no cabeçalho Base.

![Clique em Apps no cabeçalho Base](images/click-apps-in-the-base-header.jpg)

4. Passe o rato sobre a aplicação e clique no **ícone do lápis** {{< seatable-icon icon="dtable-icon-rename" >}}.

![Clique no ícone de edição](images/add-page-to-universal-app-1.png)

6. Abra a **administração de utilizadores e funções** no canto superior esquerdo da página.

![Ícone para gestão de utilizadores e funções](images/Symbol-fuer-Benutzer-und-Rollenverwaltung.png)

8. Efectuar as **definições** pretendidas.

## As definições em pormenor

### Utilizador

Na primeira secção, encontrará uma visão geral de todos os **utilizadores** que têm acesso à sua aplicação. Além disso, encontrará também a **função** e o **estado do** respectivo utilizador.

![Descrição geral do separador Utilizadores da Administração de utilizadores e funções de uma aplicação](images/user-and-role-management-overview-1.png)

Esta secção também lhe fornece várias opções para **gerir os utilizadores actuais da** sua aplicação.

Utilize a **função de pesquisa para** encontrar um utilizador específico. Esta função pode ser especialmente útil se tiver um grande número de utilizadores de aplicações.

![Função de pesquisa para utilizadores de aplicações](images/search-function-app-users.png)

Para adicionar um utilizador à aplicação, clique em **Importar utilizador**, procure o **utilizador** no campo de entrada e, em seguida, atribua uma função ao utilizador.

![Clique em Importar utilizador ](images/import-user-to-app.jpg)

![Importar um utilizador para a sua aplicação](images/import-users-to-app.png)

Clique em **Sincronizar utilizadores com a Base** para recolher automaticamente os **utilizadores da aplicação** numa tabela na sua Base.

![Clique em Sincronizar utilizador com a base](images/click-sync-users-to-base-1.jpg)  
![Tabela em que os utilizadores da aplicação são recolhidos automaticamente](images/table-with-app-users.png)

Se, no futuro, adicionar mais utilizadores desta forma, pode sempre clicar novamente em **Sincronizar utilizadores com a Base** para adicionar os **novos utilizadores** à tabela.

![Se, no futuro, adicionar mais utilizadores à sua aplicação, ...](images/if-you-add-more-users-to-your-app.png)

![... pode sempre clicar novamente em Sincronizar utilizadores com a Base para adicionar automaticamente os novos utilizadores à tabela.](images/added-imported-app-users-to-table.png)

Para **eliminar** um utilizador da aplicação, basta clicar no **símbolo X**, que se encontra à direita do estado do respectivo utilizador.

![Eliminar utilizador](images/delete-user.jpg)

Ao clicar nos **ícones de lápis** {{< seatable-icon icon="dtable-icon-rename" >}}, que encontrará para cada utilizador, pode editar a sua **função** e o seu **estado**.

{{< warning  headline="Nota importante"  text="Tenha em atenção que o **utilizador** que adicionou a aplicação à Base é automaticamente registado como **Administrador**. Tanto a função como o estado deste utilizador **não podem** ser editados e o utilizador não pode **ser** removido da aplicação." />}}

![Editar ícones para cada utilizador ](images/edit-icons-users.jpg)

Para a **função de um utilizador,** todas as funções estão disponíveis para selecção no menu pendente, que pode ser definido na secção seguinte da administração de utilizadores e funções.

![Seleccionar a função de um utilizador ](images/select-role-of-user.png)

O **estado de** um utilizador pode ser definido como **Activo** ou **Inactivo**. Enquanto os utilizadores **activos** têm acesso à aplicação e ao seu conteúdo, os utilizadores **inactivos** perdem esse acesso.

![Editar o estado de um utilizador da aplicação](images/edit-status-of-app-user.png)

Os utilizadores que não têm acesso à sua aplicação verão esta mensagem:

![Acesso negado à aplicação para utilizadores inactivos ](images/no-permission-for-inactive-users.png)

### Rolos

Nesta secção, pode definir qualquer número de **funções**, que pode atribuir aos vários utilizadores da aplicação na secção acima.

![Definição de diferentes funções para os utilizadores da aplicação ](images/define-roles-for-app-users.jpg)

Aqui, inicialmente, apenas define os **nomes das** funções. Pode definir quais as **permissões** que os utilizadores com as diferentes funções têm individualmente para cada página da aplicação.

[Saiba mais sobre as permissões de página aqui.]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}})

### Ligação do convite

Na terceira secção da administração de utilizadores e funções, é possível gerar uma **ligação de convite** individual para a aplicação.

Primeiro, defina a **função dos** utilizadores que acedem à aplicação utilizando a ligação de convite.

![Selecção da função que será atribuída ao utilizador que irá utilizar a aplicação através da ligação de convite.](images/select-role-for-invite-link.png)

Tem então a opção de definir uma **palavra-passe** que deve ser introduzida depois de abrir a ligação de convite para obter acesso à aplicação.

![Adicionar uma palavra-passe à ligação de convite](images/add-password-protection.png)

Opcionalmente, pode também adicionar um **tempo de expiração** automático **à** ligação de convite para indicar o período de validade da mesma.

![Adicionar tempo de expiração automático à ligação de convite ](images/add-auto-expiration.png)

Clique em **Gerar** para criar a ligação de convite. A ligação é então apresentada abaixo e tem a opção de a **copiar** ou **eliminar**.

![Ligação de convite gerada com opções disponíveis para copiar e eliminar a ligação de convite](images/copy-and-delete-link-universal-app.png)

Em alternativa, tem a opção de gerar um **código QR** para abrir e partilhar a aplicação.

![Apresentar o código QR para abrir e partilhar a aplicação](images/show-qr-code-universal-app.png)

Digitalize o **código QR** apresentado para abrir a sua aplicação ou partilhe-o com outros utilizadores para lhes dar **acesso à** sua aplicação.

![Código QR para abrir e partilhar a aplicação](images/qr-code-to-share-universal-app.png)
