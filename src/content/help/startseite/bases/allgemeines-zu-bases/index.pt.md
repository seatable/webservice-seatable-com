---
title: 'Informações gerais sobre as bases em SeaTable'
date: 2022-08-25
lastmod: '2023-05-03'
categories:
    - 'arbeiten-mit-bases'
author: 'cdb'
url: '/pt/ajuda/bases-funcionalidades-gestao-seatable'
aliases:
    - '/pt/ajuda/bases'
seo:
    title: 'Bases no SeaTable: recursos, gestão e compartilhamento'
    description: 'Informações sobre bases no SeaTable: administrar, compartilhar, exportar, excluir, restaurar e trabalhar produtivamente com seus dados.'
star: true
weight: 1
---

As bases são de importância central no SeaTable. Sempre que entra, analisa, edita ou partilha dados no SeaTable, está numa base.

À primeira vista, uma base é apenas um **recipiente** para uma ou mais **tabelas**. Nesta perspectiva, parece óbvio comparar uma base com uma pasta de trabalho em Excel. No entanto, esta comparação não faz justiça a uma base. As bases em SeaTable são muito superiores às pastas de trabalho, pois são conhecidas a partir de folhas de cálculo convencionais, porque oferecem:

- Funções das [bases de dados relacionais]({{< relref "posts/relationale-datenbank" >}}) e a [ligação de tabelas]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}})
- [Mais de 20 tipos de colunas]({{< relref "help/base-editor/spalten/uebersicht-alle-spaltentypen" >}}) cobrindo todos os formatos de dados comuns
- Várias [opções de partilha para]({{< relref "help/startseite/freigaben/base-und-ansichtsfreigaben-im-ueberblick" >}}) dados
- [Colaboração]({{< relref "help/erste-schritte/einfuehrung-funktionen/zusammenarbeit" >}}) em tempo real com outros utilizadores e transmissão em tempo real de todas as alterações
- Uma [função de comentário para]({{< relref "help/base-editor/zeilen/zeilen-kommentieren" >}}) cada registo numa linha
- [Versões]({{< relref "help/base-editor/historie-und-versionen/historie-und-logs" >}}) todas as mudanças
- Um [editor de formulários web]({{< relref "help/base-editor/webformulare/webformulare" >}}) integrado e [plugins]({{< relref "help/base-editor/ansichten" >}}) gráficos
- Opções de integração simples graças ao REST API

As bases são, portanto, muito mais do que "contentores de tabela" na Web. Estas vantagens são-lhe rapidamente reconhecidas e nunca mais vai querer passar sem elas!

## Proprietário de Bases

Cada Base tem um (e apenas um) **proprietário**. Contudo, a transferência de propriedade de uma Base de um utilizador para outro utilizador é possível.

O proprietário de uma base é ou um **utilizador** ou um **grupo**. Se um utilizador é o proprietário de uma base, então apenas este utilizador tem todo o poder de disposição. Se a base pertencer a um grupo, todos os administradores do grupo têm pleno acesso à mesma. Aqui pode saber mais sobre as [permissões dos membros individuais do grupo]({{< relref "help/startseite/gruppen/gruppenmitglieder-und-ihre-berechtigungen" >}}).

A transferência directa de propriedade de um utilizador para outro não é actualmente (a partir de 20.3.2023) possível. Contudo, é possível **mudar** a propriedade indirectamente exportando uma base e fazendo-a importar pelo novo proprietário. Mais informações sobre importação e exportação de bases podem ser encontradas no artigo [Importação e exportação de dados]({{< relref "help/startseite/import-von-daten/datenimport-und-export" >}}).

## Criação de bases

Cria **novas bases** através da página inicial. Está sempre na página inicial quando inicia sessão no SeaTable. Se estiver actualmente a trabalhar numa base, pode voltar à página inicial clicando no **ícone da base** {{< seatable-icon icon="dtable-icon-dtable-logo" >}} no canto superior esquerdo.

Na área **Minhas Bases** e em cada **grupo** em que é administrador, encontrará o botão **Adicionar uma Base ou Pasta**. Clique neste botão para criar uma nova base onde quiser.

Tem **três opções** ao criar uma nova base. Pode ler mais sobre isto nos respectivos artigos:

- [Criar uma base vazia]({{< relref "help/startseite/bases/eine-neue-base-erstellen" >}})
- [Importar base a partir de um ficheiro]({{< relref "help/startseite/import-von-daten/welche-import-formate-unterstuetzt-seatable" >}})
- [Criar base a partir de um modelo]({{< relref "help/startseite/bases/anlegen-einer-base-mithilfe-einer-vorlage" >}})

## Gestão de base

Gerem as bases através do **menu de contexto** na página inicial. Se mover o ponteiro do rato sobre uma das suas bases, aparece um **ícone de lápis** à direita do nome {{< seatable-icon icon="dtable-icon-rename" >}} e um **ícone de três pontos** {{< seatable-icon icon="dtable-icon-more-vertical" >}} para as opções avançadas. Irá precisar delas regularmente para gerir as suas bases.

Não é possível **gerir** bases que lhe tenham sido cedidas. Apenas duas opções estão disponíveis nas funções avançadas de tais bases: **Sair de bases partilhadas** e **Copiar**.

## Renomear bases

Pode subsequentemente **renomear** bases das quais é o proprietário ou administrador. Mova o ponteiro do rato para o nome da base a ser renomeada e depois clique no **ícone do lápis** {{< seatable-icon icon="dtable-icon-rename" >}}. Pode agora alterar o nome e guardá-lo, clicando na **tecla Enter**. Leia [aqui]({{< relref "help/startseite/bases/eine-neue-base-erstellen" >}}) o que deve ter em mente ao dar um nome a uma base.

## Mudar o ícone e a cor de uma base

Pode dar um novo visual às bases de que é proprietário ou administrador. Pode descobrir como fazer isto [aqui]({{< relref "help/startseite/bases/aussehen-einer-base-anpassen-icon-und-farbe" >}}). Para trazer uma lufada de ar fresco às suas bases, tem **mais de 10 cores** e **mais de 25 ícones** à sua disposição.

## Adicionar Descrição Base

Pode adicionar uma descrição às suas bases para dar a outros utilizadores "instruções de utilização" ou para registar informações adicionais sobre uma base. Pode aprender [aqui]({{< relref "help/base-editor/weitere-optionen/wie-man-einer-base-eine-beschreibung-hinzufuegt" >}}) como utilizar esta função.

## Bases de lançamento

Pode **partilhar** bases que possui ou administrar com outros **utilizadores e grupos**, dando-lhes acesso aos dados. A partilha é feita com diferentes permissões, para que tenha sempre controlo sobre as alterações nas suas bases.

Mais informações sobre esta importante e extremamente útil função podem ser encontradas no artigo [Base e ver os comunicados]({{< relref "help/startseite/freigaben/base-und-ansichtsfreigaben-im-ueberblick" >}}) num relance.

## Base de cópia

É possível **copiar** todas as bases às quais tem acesso. Dependendo da origem da base e do local para onde pretende copiar a base, o artigo Duplicar [uma]({{< relref "help/startseite/bases/eine-base-in-eine-gruppe-kopieren" >}}) ajudá-lo-ão.

## Mover bases para pastas ou adicionar aos favoritos

Se um grande número de bases tiver acumulado na sua página inicial, pode ser útil para a clareza [agrupar várias bases em pastas]({{< relref "help/startseite/bases/eine-base-zu-den-favoriten-hinzufuegen" >}}).

## Base de exportação

É possível exportar bases para backup de dados, para transferência para outro utilizador ou para transferência para outro servidor SeaTable. Basicamente, a exportação tem lugar num [ficheiro DTABLE]({{< relref "help/startseite/import-von-daten/dtable-dateiformat" >}}).

Para mais informações sobre bases de exportação, ver o artigo [Salvando uma Base como Ficheiro DTABLE]({{< relref "help/startseite/import-von-daten/datenimport-und-export" >}}).

## Eliminar e restaurar bases

Pode [apagar as]({{< relref "help/startseite/papierkorb/loeschen-einer-base" >}}) bases que possui ou administrar, se necessário, e [restaurá-las]({{< relref "help/startseite/papierkorb/eine-geloeschte-base-wiederherstellen" >}}) por até 30 dias. Siga as instruções contidas nos artigos ligados.

### Restaurar Base a partir de Snapshot

Pode visualizar e restaurar instantâneos das bases que possui ou administrar. Tudo o que precisa de saber sobre instantâneos no SeaTable pode ser encontrado nos seguintes artigos

- [Salvar a base actual como um instantâneo]({{< relref "help/base-editor/historie-und-versionen/speichern-der-aktuellen-base-als-snapshot" >}})
- [Restauração de um instantâneo]({{< relref "help/base-editor/historie-und-versionen/wiederherstellung-eines-snapshots" >}})

## Criar uma conta de e-mail numa base

Se quiser enviar e-mails a partir de uma Base, precisa de ligar a sua conta de e-mail à Base. Mostramos-lhe como fazer uso desta útil função no SeaTable no artigo [Criar uma conta de correio electrónico numa Base]({{< relref "help/base-editor/weitere-optionen/einrichtung-eines-e-mail-kontos-in-einer-base" >}}).
