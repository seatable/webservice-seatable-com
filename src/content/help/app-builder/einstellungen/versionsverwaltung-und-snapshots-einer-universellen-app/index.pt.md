---
title: 'Gestão de versões e instantâneos de uma aplicação'
date: 2023-11-29
lastmod: '2024-02-16'
categories:
    - 'universelle-apps'
author: 'kgr'
url: '/pt/ajuda/controle-versoes-e-snapshots-app-universal'
aliases:
    - '/pt/ajuda/versionsverwaltung-und-snapshots-einer-universellen-app'
seo:
    title: 'Gestão de versões e snapshots de uma aplicação'
    description: 'Saiba como guardar, visualizar, restaurar e gerir versões de uma aplicação com snapshots para manter a segurança e a consistência.'
---

Pode utilizar **instantâneos** para guardar a versão atual de uma aplicação. Pode **criar**, **ver**, **restaurar** e **eliminar** instantâneos na gestão de versões do SeaTable App Builder. Também pode adicionar **notas** aos instantâneos individuais para registar informações sobre uma versão.

{{< warning  type="warning" headline="Permissão necessária no grupo"  text="Para poder utilizar instantâneos de aplicações, tem de ser **proprietário** ou **administrador do grupo** em que a **base** subjacente está localizada. Os simples **membros do grupo** não têm acesso à gestão de versões." />}}

## Quando é que os instantâneos de aplicações são úteis

Os instantâneos de aplicações são **registos momentâneos** do estado de uma aplicação e funcionam de forma semelhante aos [instantâneos de base]({{< relref "help/base-editor/historie-und-versionen/speichern-der-aktuellen-base-als-snapshot" >}}). Pode utilizar os instantâneos de aplicações para guardar a versão atual de uma aplicação como cópia de segurança, o que pode ser útil, por exemplo, se pretender efetuar alterações extensas e eventualmente restaurar um estado anterior.

{{< warning  type="warning" headline="Cuidado com a perda de dados"  text="Ao contrário dos instantâneos de base, os instantâneos de aplicações **não** guardam **registos**, mas apenas a **estrutura** e as **definições** da aplicação. Isto significa que, se alterar ou eliminar determinadas entradas na base subjacente através da aplicação, não as pode restaurar através dos instantâneos da aplicação." />}}

### O que um instantâneo de aplicação guarda

Um instantâneo de aplicação guarda os seguintes elementos e definições:

- [Definições]({{< relref "help/app-builder/einstellungen/einstellungen-einer-universellen-app-aendern" >}}) como o **nome**, o **ícone** e o **esquema de cores** da aplicação
- [Páginas e pastas]({{< relref "help/app-builder/einstellungen/seiten-und-ordner-in-einer-universellen-app-anlegen-und-verwalten" >}}) da aplicação
- Definições e [permissões]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}) das páginas individuais

### O que um instantâneo de aplicação não guarda

Um instantâneo de aplicação não guarda:

- o **URL personalizado** de uma aplicação
- os **dados** da base subjacente
- os **comentários** sobre registos individuais
- as [funções de utilizador e ligações de convite]({{< relref "help/app-builder/einstellungen/benutzer-und-rollenverwaltung-einer-universellen-app" >}}) da aplicação

## Criar um instantâneo da aplicação

1. Abra uma **aplicação** no [modo de edição]({{< relref "help/app-builder/app-verwaltung/apps-bearbeiten" >}}).
   ![SeaTable App Builder em modo de edição com lista de aplicações aberta](images/Apps-bearbeiten.png)
2. Clique em {{< seatable-icon icon="dtable-icon-history" >}} **Gestão de versões** no canto superior esquerdo da página.
   ![Gestão de versões de uma aplicação com lista de snapshots existentes](images/Version-management-in-Universal-App-Builder.png)
3. Abre-se uma janela. Crie aí um **novo instantâneo**.
4. Opcionalmente, pode adicionar uma **nota** ao instantâneo.
5. Confirme com **Submeter**.

![Criação de um novo snapshot da aplicação na gestão de versões com nota opcional](images/Version-management-in-Universal-Apps.gif)

{{< warning  headline="Numeração das versões"  text="Para cada instantâneo são registados a **hora de criação** exata e um **número de versão**. Não se surpreenda se os seus instantâneos não receberem números consecutivos (1, 2, 3 …). O SeaTable conta cada alteração que efetua numa aplicação como uma versão separada. Por isso, podem existir rapidamente dezenas de versões entre dois instantâneos." />}}

Assim que tiver criado um instantâneo, tem quatro operações à sua escolha:

- **Ver versão**
- **Restaurar versão**
- **Nota**
- **Eliminar versão**

## Ver um instantâneo da aplicação

Antes de restaurar um instantâneo e voltar precipitadamente a outra versão, deve primeiro dar uma vista de olhos a essa versão. Para o fazer, siga o mesmo procedimento descrito acima: clique nos **três pontos** na extremidade direita de um instantâneo e selecione a operação **Ver versão** no menu pendente.

![Pré-visualização de uma versão guardada da aplicação no SeaTable App Builder](images/Preview-version-of-app-snapshot.png)

## Restaurar um instantâneo da aplicação

Para restaurar um instantâneo da aplicação, clique nos **três pontos** e selecione a operação correspondente no menu pendente.

![Janela para restaurar um snapshot da aplicação como versão atual](images/Restore-version-of-app-snapshot.png)

{{< warning  type="warning" headline="Atenção"  text="O restauro de instantâneos no SeaTable App Builder funciona de forma diferente do que numa base, onde o instantâneo é restaurado numa nova base e a versão atual é mantida. **No SeaTable App Builder, pelo contrário, a versão atual é descartada quando restaura um instantâneo.**" />}}

Assim que restaurar um instantâneo, a aplicação é reposta no estado guardado dessa versão anterior. Todas as **alterações** que tenha efetuado desde então nas páginas, pastas e definições da aplicação **perdem-se**. Por isso, é aconselhável guardar também a versão atual num instantâneo antes de restaurar outro. Desta forma, pode alternar entre diferentes versões.

## Editar uma nota

Se pretender adicionar, alterar ou eliminar posteriormente a nota de uma versão, pode fazê-lo em qualquer altura. Abra o campo de texto correspondente clicando nos **três pontos** na extremidade direita de um instantâneo e selecionando **Nota** no menu pendente. Guarde as suas alterações com **Submeter**.

![Janela para editar ou adicionar uma nota a um snapshot da aplicação](images/Modify-notes-of-app-snapshot.png)

## Eliminar um instantâneo da aplicação

Pode eliminar em qualquer altura um instantâneo de que já não necessita. Clique nos **três pontos** na extremidade direita de um instantâneo e selecione a operação **Eliminar versão** no menu pendente.

![Janela de confirmação para eliminar permanentemente um snapshot da aplicação](images/Delete-version-of-app-snapshot.png)

{{< warning  type="warning" headline="Atenção"  text="A eliminação de um instantâneo de aplicação é definitiva. O estado guardado da versão anterior perde-se irrevogavelmente e não pode ser restaurado." />}}
