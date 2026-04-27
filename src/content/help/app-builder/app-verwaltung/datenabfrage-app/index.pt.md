---
title: 'Aplicação de consulta de dados'
date: 2023-05-02
lastmod: '2024-05-15'
categories:
    - 'apps'
author: 'nsc2'
url: '/pt/ajuda/aplicativo-consulta-dados'
aliases:
    - '/pt/ajuda/datenabfrage-app'
seo:
    title: 'Aplicativo de consulta de dados: pesquisa eficiente'
    description: 'Veja como usar o aplicativo de consulta de dados para pesquisar grandes conjuntos e compartilhar resultados com facilidade.'
---

Com a ajuda de uma **aplicação de consulta de dados**, pode permitir que outros utilizadores pesquisem os seus registos em **campos** específicos para **valores** específicos. Este **ecrã de pesquisa** é particularmente útil para grandes conjuntos de dados, como catálogos de produtos ou bibliotecas.

## Criar a aplicação Data Query

Para utilizar uma aplicação de recuperação de dados na sua base, deve primeiro **adicioná-la** à sua base.

![A aplicação Data Query](images/data-query-app-preview.png)

[Saiba como adicionar uma aplicação à sua base aqui.]({{< relref "help/app-builder/app-verwaltung/apps-zu-einer-base-hinzufuegen" >}})

## Editar definições de uma aplicação de recuperação de dados

Depois de ter criado com êxito a sua aplicação de consulta de dados, pode selecionar a **tabela** e as **colunas** que podem ser pesquisadas para determinados **valores** nas definições da aplicação. {{< seatable-icon icon="dtable-icon-rename" >}} Para o fazer, basta abrir a aplicação no [modo de edição]({{< relref "help/app-builder/app-verwaltung/apps-bearbeiten" >}}) utilizando o **ícone de lápis**.

Como a aplicação de consulta de dados se baseia no App Builder, as seguintes opções de definição são idênticas às **páginas de consulta na aplicação**:

![Definições de página da aplicação de consulta de dados](images/Seiteneinstellungen-der-Datenabfrage-App.png)

[Saiba mais sobre as opções de definição das páginas de consulta.]({{< relref "help/app-builder/seitentypen-in-universellen-apps/abfrageseiten-in-universellen-apps" >}})

## Editar o nome, a cor e o ícone de uma aplicação de consulta de dados

Pode **mudar o nome de** uma aplicação de recuperação de dados em qualquer altura. {{< seatable-icon icon="dtable-icon-rename" >}} Basta abrir a aplicação através do ícone do lápis no **modo de edição**. Se clicar no **ícone da roda dentada** no canto superior esquerdo, pode alterar o nome, a cor e o ícone da aplicação.

[Saiba mais sobre as definições globais da aplicação aqui.]({{< relref "help/app-builder/einstellungen/einstellungen-einer-universellen-app-aendern" >}})

## Partilhar uma aplicação de consulta de dados

Pode **partilhar** as suas aplicações de consulta de dados com outros utilizadores com apenas alguns cliques. Para tal, aceda à [administração de utilizadores e funções]({{< relref "help/app-builder/einstellungen/einstellungen-einer-universellen-app-aendern" >}}) da aplicação.

![Partilhar a aplicação de consulta de dados](images/Datenabfrage-App-teilen.png)

Ligação da aplicação gerada pelo SeaTable

![Ligação personalizada de uma aplicação de consulta de dados](images/Benutzerdefinierter-Link-einer-Datenabfrage-App.png)

Ligação personalizada à aplicação

{{< warning  headline="Acesso sem restrições"  text="Ambas as opções concedem **acesso aberto**. Isto significa que pode disponibilizar a hiperligação a qualquer número de pessoas (com ou sem uma conta SeaTable), que apenas têm de clicar na hiperligação para aceder à aplicação e obter dados." />}}

## Procurar um valor na aplicação Data Query

Depois de ter partilhado com êxito a sua aplicação de consulta de dados, os outros utilizadores podem começar a consultar e a aceder aos dados partilhados. Para procurar **valores** específicos nos seus registos, basta introduzi-los nos **campos de consulta** e clicar em **Consultar**.

![Valores encontrados de uma consulta na aplicação Data Query](images/found-results-data-query.png)

## Visualização dos registos de dados encontrados

Depois de os utilizadores terem clicado em **Query (Consultar** ), os registos de dados encontrados são imediatamente apresentados numa tabela. Os utilizadores da aplicação só podem ver os valores das colunas de um registo de dados que **não tenha** sido **ocultado**. Além disso, não podem eliminar quaisquer **filtros** que tenha **predefinido** para limitar o número de linhas pesquisáveis.

![Páginas de consulta em aplicações](images/Abfrageseiten-in-Universellen-Apps.png)

No entanto, os próprios utilizadores podem **ordenar** a lista de resultados consultados e **ajustar** a **altura da linha** para obter uma melhor visão geral.

## Copiar uma aplicação de recuperação de dados

Criou uma aplicação de consulta de dados que gostaria de utilizar de forma semelhante para outro grupo de utilizadores? Então, basta copiar a aplicação existente e adaptar a cópia como desejar. Pode descobrir como copiar uma aplicação [aqui]({{< relref "help/app-builder/app-verwaltung/apps-kopieren" >}}).

## Desative um aplicativo de consulta de dados

Se você criou um aplicativo de consulta de dados que gostaria de impedir temporariamente de ser usado, você pode desativá-lo com apenas alguns cliques para revogar o acesso de todos os grupos de usuários. Você pode descobrir como fazer isso [aqui]({{< relref "help/app-builder/app-verwaltung/apps-zeitweise-deaktivieren" >}}) .

## Eliminar uma aplicação de recuperação de dados

Você pode **excluir** um aplicativo de consulta de dados desnecessário a qualquer momento. Não se preocupe: excluir um aplicativo de consulta de dados **não excluirá nenhum dado da base** . [Saiba mais sobre como excluir aplicativos aqui.]({{< relref "help/app-builder/app-verwaltung/apps-loeschen" >}})
