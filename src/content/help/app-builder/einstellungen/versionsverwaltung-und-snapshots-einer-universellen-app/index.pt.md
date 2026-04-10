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
    title: 'Controle de versões e snapshots de uma aplicação'
    description: 'Saiba como salvar, visualizar, restaurar e gerenciar versões de uma aplicação com snapshots para manter segurança e consistência.'
---

Pode utilizar **instantâneos** para guardar a versão atual de uma aplicação. Pode **criar**, **ver**, **restaurar** e **eliminar** instantâneos na gestão de versões do App Builder. Também pode fazer **anotações** nos instantâneos individuais para registar informações sobre uma versão.

{{< warning  headline="Autorização necessária no grupo"  text="Para poder utilizar instantâneos de aplicações, tem de ser o **proprietário** ou **administrador do grupo** em que a **base** subjacente está localizada. **Os membros** simples do **grupo** não têm acesso ao gerenciamento de versões." />}}

## Quando é que os instantâneos de aplicações são úteis

Os instantâneos de aplicações são **instantâneos** do estado de uma aplicação e funcionam de forma semelhante aos [instantâneos de base]({{< relref "help/base-editor/historie-und-versionen/speichern-der-aktuellen-base-als-snapshot" >}}). Pode utilizar os instantâneos da aplicação para guardar a versão atual de uma aplicação como uma cópia de segurança, o que pode ser útil, por exemplo, se pretender efetuar alterações extensas e possivelmente restaurar um estado anterior.

{{< warning  headline="Cuidado com a perda de dados"  text="Ao contrário dos instantâneos de base, os instantâneos de aplicação **não** guardam **registos de dados**, mas apenas a **estrutura** e **as definições** da aplicação. Isto significa que se alterar ou eliminar determinadas entradas na base subjacente através da aplicação, não as pode restaurar através dos instantâneos da aplicação." />}}

### O que um instantâneo de aplicação poupa

Um instantâneo de aplicação guarda os seguintes elementos e definições:

- [Definições]({{< relref "help/app-builder/einstellungen/einstellungen-einer-universellen-app-aendern" >}}) como o **nome**, o **ícone** e o **esquema de cores** da aplicação
- [Páginas e pastas]({{< relref "help/app-builder/einstellungen/seiten-und-ordner-in-einer-universellen-app-anlegen-und-verwalten" >}}) da aplicação
- Definições e [autorizações]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}) para as páginas individuais

### O que um instantâneo de aplicação não guarda

Um instantâneo de aplicação não é guardado:

- o **URL definido pelo utilizador** de uma aplicação
- os **dados** da base subjacente
- as **observações** sobre registos de dados individuais
- as [funções do utilizador e as ligações de convite]({{< relref "help/app-builder/einstellungen/benutzer-und-rollenverwaltung-einer-universellen-app" >}}) da aplicação

## Criar instantâneo da aplicação

1. Abra uma **aplicação** no [modo de edição]({{< relref "help/app-builder/app-verwaltung/apps-bearbeiten" >}}).

![App Builder em modo de edição com lista de aplicações aberta](images/Apps-bearbeiten.png)

3. Clique em {{< seatable-icon icon="dtable-icon-history" >}} **Gestão de versões** no canto superior esquerdo da página.

![Gestão de versões de uma aplicação com lista de snapshots existentes](images/Version-management-in-Universal-App-Builder.png)

5. Abre-se uma janela. Crie aí um **novo instantâneo**.
6. Opcionalmente, pode adicionar uma **nota** ao instantâneo.
7. Confirmar com **Submeter**.

![Criação de um novo snapshot da aplicação na gestão de versões com nota opcional](images/Version-management-in-Universal-Apps.gif)

{{< warning  headline="Numeração das versões"  text="A **hora** exacta **da criação** e um **número de versão** são registados para cada instantâneo. Não se surpreenda se os seus instantâneos não receberem números consecutivos (1, 2, 3 ...). O SeaTable conta cada alteração efectuada numa aplicação como uma versão separada. Isto significa que podem existir rapidamente dezenas de versões entre dois instantâneos." />}}

Assim que tiver criado um instantâneo, tem quatro operações à sua escolha:

- **Ver versão**
- **Restaurar versão**
- **Nota**
- **Eliminar versão**

## Ver instantâneo da aplicação

Antes de restaurar um instantâneo e voltar apressadamente para outra versão, deve primeiro dar uma vista de olhos a esta versão. Para o fazer, siga o mesmo procedimento acima descrito: Clique nos **três pontos** na extremidade direita de um instantâneo e seleccione a operação **Ver versão** no menu pendente.

![Pré-visualização de uma versão guardada da aplicação no App Builder](images/Preview-version-of-app-snapshot.png)

## Restaurar o instantâneo da aplicação

Para restaurar um instantâneo de aplicação, clique nos **três pontos** e seleccione a operação correspondente no menu pendente.

![Janela para restaurar um snapshot da aplicação como versão atual](images/Restore-version-of-app-snapshot.png)

{{< warning  headline="Atenção"  text="O restauro de instantâneos no App Builder funciona de forma diferente do que na Base, onde o instantâneo é restaurado numa nova Base e a versão atual é mantida. **No App Builder, no entanto, a versão atual é eliminada quando restaura um instantâneo.**" />}}

Assim que restaurar uma imagem instantânea, a aplicação é reposta no estado da memória desta versão anterior. Quaisquer **alterações** que tenha efectuado a páginas, pastas e definições na aplicação desde então serão **perdidas**. Por isso, é aconselhável guardar também a versão atual num instantâneo antes de restaurar um instantâneo. Isto permite-lhe saltar para trás e para a frente entre diferentes versões.

## Editar nota

Se pretender adicionar, alterar ou eliminar a nota de uma versão numa data posterior, pode fazê-lo em qualquer altura. Abra o campo de texto correspondente clicando nos **três pontos** na extremidade direita de um instantâneo e seleccionando **Nota** no menu pendente. Guarde as suas alterações clicando em **Submeter**.

![Janela para editar ou adicionar uma nota a um snapshot da aplicação](images/Modify-notes-of-app-snapshot.png)

## Eliminar o instantâneo da aplicação

Pode eliminar um instantâneo de que já não necessita em qualquer altura. Clique nos **três pontos** na extremidade direita de um instantâneo e seleccione a operação **Eliminar versão** no menu pendente.

![Janela de confirmação para eliminar permanentemente um snapshot da aplicação](images/Delete-version-of-app-snapshot.png)

{{< warning  headline="Atenção"  text="A eliminação de um instantâneo de aplicação é definitiva. O estado da memória da versão anterior perde-se irrevogavelmente e não pode ser restaurado." />}}
