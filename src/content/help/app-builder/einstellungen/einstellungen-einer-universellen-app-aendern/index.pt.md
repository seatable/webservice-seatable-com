---
title: 'Alterar as definições globais de uma aplicação'
date: 2023-05-03
lastmod: '2025-07-03'
categories:
    - 'universelle-apps'
author: 'kgr'
url: '/pt/ajuda/alterar-configuracoes-globais-app-universal'
aliases:
    - '/pt/ajuda/einstellungen-einer-universellen-app-aendern'
seo:
    title: 'Alterar configurações globais em uma aplicação'
    description: 'Veja como ajustar facilmente as configurações globais, URLs e permissões em uma aplicação no SeaTable.'
---

Numa **aplicação**, pode fazer várias **definições globais** que afectam a configuração e o aspeto de toda a aplicação com apenas alguns cliques.

## Alterar as definições de uma aplicação

1. Abra uma **base** na qual pretende editar uma aplicação existente.
2. Clique em **Apps** no cabeçalho Base.
![Clique em Apps no cabeçalho Base](images/click-apps-in-the-base-header.jpg)
3. Passe o rato sobre a aplicação e clique no **ícone do lápis** {{< seatable-icon icon="dtable-icon-rename" >}}.
![Editar aplicações](images/Apps-bearbeiten.png)
4. Clique no **símbolo da roda dentada** no canto superior esquerdo da página.
![Ícone de roda dentada para as definições da aplicação](images/Zahnrad-Symbol-fuer-App-Einstellungen.png)
5. Efectuar os ajustes desejados nas **definições** da aplicação.

{{< warning  headline="Autorização necessária no grupo"  text="Para poder editar uma aplicação, tem de ser o **proprietário** ou **administrador do grupo** em que a **base** subjacente se encontra. **Os membros** simples **do grupo** só podem ver e utilizar as aplicações." />}}

## Editar o nome da aplicação

Na primeira secção das definições da aplicação, pode personalizar o **nome da** aplicação e guardá-lo clicando em **Submeter**.

![Alterar o nome da aplicação](images/Change-app-name.png)

## URL definido pelo utilizador

Na segunda secção, pode personalizar parte do **URL** com o qual pode chamar e ligar à sua aplicação. Basta introduzir o URL pretendido no **campo de texto** e ter em atenção os **requisitos** abaixo indicados ao introduzi-lo. Em seguida, pode **guardar** e **copiar** o URL introduzido.

![Editar URL personalizado](images/Edit-custom-URL.png)

**Requisitos:** A parte do URL definida pelo utilizador deve ter entre 5 e 30 caracteres e só pode conter **letras (a-z), números (0-9) e hífenes**.

## Mostrar e ocultar a navegação

Na terceira secção, pode decidir se a **barra de navegação** deve ser mostrada ou ocultada por predefinição quando a aplicação é aberta. A barra de navegação é a área do lado esquerdo que todos os utilizadores utilizam para navegar para as [páginas e pastas]({{< relref "help/app-builder/einstellungen/seiten-und-ordner-in-einer-universellen-app-anlegen-und-verwalten" >}}) da aplicação.

![Ocultar a navegação da aplicação por predefinição](images/Hide-app-navigation-by-default.png)

Esta é apenas uma definição predefinida quando a aplicação é aberta pela primeira vez. Cada utilizador da aplicação pode mostrar e ocultar a barra de navegação conforme necessário, utilizando os **ícones** correspondentes ou **combinações de teclas**.

![Mostrar e ocultar a navegação](images/Hide-and-show-navigation.gif)

## Definições para colaboração

Na quarta secção, pode decidir se a sua **lista de empregados** deve ser visível para todos os utilizadores da aplicação. Pode então introduzir pessoas nas [colunas de empregados]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}}) ou adicioná-las aos [comentários]({{< relref "help/base-editor/zeilen/zeilen-kommentieren" >}}). Se quiser que os seus empregados permaneçam invisíveis para os outros, deve desativar esta função.

![Carregar lista de colaboradores em aplicações](images/Load-collaborator-list-in-apps.png)

Também pode definir se pretende carregar os **comentários a partir da base subjacente**. Por defeito, apenas os comentários escritos na aplicação são visíveis na aplicação. Se não quiser que os utilizadores da aplicação vejam os comentários da base, deve desativar esta função.

{{< warning type="warning" headline="Os comentários são possíveis nestes tipos de página" text="A função de comentário da aplicação pode atualmente ser encontrada em páginas de tabela, galeria, kanban, calendário e linha de tempo." />}}

## Gestão de grandes volumes de dados

Esta secção só é relevante se tiver ativado o [armazenamento de grandes volumes de dados]({{< relref "help/base-editor/big-data/aktivieren-des-big-data-backends-in-einer-base" >}}) na sua Base. As aplicações podem então aceder aos dados no armazenamento de grandes volumes de dados e guardar as entradas criadas através da aplicação diretamente aí. No entanto, por defeito, os novos registos são guardados na Base. Para definir o armazenamento de Big Data como o **local de armazenamento para novas entradas**, basta ativar o seletor. Como mostra a captura de ecrã, pode especificar para cada tabela se as novas linhas devem ser escritas na base (caixa vazia) ou no armazenamento de grandes volumes de dados (caixa assinalada).

![Gestão de grandes volumes de dados em aplicações](images/Big-data-management-in-apps.png)

## Acesso sem restrições

Na última secção, pode definir **o acesso aberto** para a sua aplicação. Pode permitir que **os utilizadores não registados** acedam publicamente àsua aplicação, para que qualquer pessoa que aceda à ligação possa ver (mas não alterar) os dados.

![Acesso aberto a uma aplicação](images/Open-access-to-an-app.png)

Pode também permitir o **Download de ficheiros e imagens**. No entanto, se não quiser que todos possam utilizar a sua aplicação sem restrições, também pode ativar a **Proteção por palavra-passe**. Ao aceder ao URL da aplicação, os utilizadores têm de introduzir a palavra-passe correta para poderem ver os dados.

No entanto, também pode ativar que **cada utilizador com sessão iniciada que utilize a sua aplicação seja automaticamente registado como um utilizador da aplicação**. Ao fazê-lo, determina que **função** é atribuída aos utilizadores durante o registo. Dependendo da sua [autorização]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}) nas páginas individuais, os utilizadores com esta função também podem adicionar, editar ou eliminar linhas.

## Editar definições de páginas individuais

As definições mencionadas até agora afectam **toda** uma aplicação. Se pretender alterar as definições de uma **página individual**, clique no **símbolo da roda dentada** {{< seatable-icon icon="dtable-icon-set-up" >}} da página correspondente na navegação.

![Abrir as definições da página](images/page-permissions-universal-app.png)
