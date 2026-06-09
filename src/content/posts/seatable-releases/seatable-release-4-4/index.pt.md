---
title: 'SeaTable 4.4: Aplicação universal, importação de Excel e conjuntos de dados comuns'
description: 'Botões nas páginas de consulta, autopreenchimento de colunas, arraste no calendário, campos de colaborador em formulários, dashboards aprimorados, títulos ocultáveis. Apps Galeria/Consulta fundidas na Universal, importação mais rápida e confiável, datasets sincronizáveis, padrão em todo processo.	/pt/seatable-release-4-4'
date: 2024-05-15
lastmod: '2024-05-15'
author: 'kgr'
url: '/pt/seatable-release-4-4'
color: '#96b228'
categories:
    - 'product-features'
seo:
    title: 'SeaTable 4.4: app universal, Excel, datasets'
    description: 'App Universal lança botões, calendários mais flexíveis, importação Excel potente, datasets otimizados e default global.'
---

No SeaTable 4.4, continuamos a desenvolver o Universal App Builder com entusiasmo. Muitas funções novas permitem aplicações Web ainda mais poderosas e práticas. Também aperfeiçoámos a função de importação e os conjuntos de dados partilhados. Os valores práticos por defeito aplicam-se agora universalmente.

Esta manhã, actualizámos o SeaTable Cloud para a versão 4.4. Todos os auto-hosters podem fazer o mesmo: A imagem do SeaTable 4.4 está disponível para download no conhecido [repositórioDocker](https://hub.docker.com/r/seatable/seatable-enterprise) . Como sempre, pode encontrar a lista completa de alterações no [registo de alterações]({{< relref "pages/changelog" >}}).

## App Builder mais flexível e mais potente

No SeaTable 4.4, voltámos a introduzir muitas melhorias e correcções de erros na [aplicação universal]({{< relref "help/app-builder/app-verwaltung/universelle-app" >}}), que beneficiarão quase todos os [tipos de páginas]({{< relref "help/app-builder/seitentypen-in-universellen-apps/ueberblick" >}}). O fim da fase beta está agora ao alcance.

### Botões nas páginas de consulta

[As páginas de consulta]({{< relref "help/app-builder/seitentypen-in-universellen-apps/abfrageseiten-in-universellen-apps" >}}) suportam agora a execução de acções de botão: Após uma consulta de dados bem sucedida, é possível premir [botões]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}}) na lista de resultados apresentada para executar acções. Esta é uma nova funcionalidade especial, uma vez que anteriormente não era possível interagir com as linhas consultadas em qualquer parte do SeaTable.

![Botões de execução nas páginas de consulta](Schaltflaechen-auf-Abfrageseiten-ausfuehren.gif)

Um exemplo de aplicação é um quadro de empregos interno: a página de consulta permite-lhe procurar rapidamente posições relevantes. Se for encontrada uma posição interessante, basta clicar no botão nos resultados da pesquisa para se candidatar diretamente à posição.

### Arrastar e largar no calendário

Até agora, não era possível alterar os compromissos na [página do calendário]({{< relref "help/app-builder/seitentypen-in-universellen-apps/kalenderseiten-in-universellen-apps" >}}). O SeaTable 4.4 dá-lhe mais flexibilidade nesta área. Agora pode mover convenientemente os seus compromissos no calendário utilizando a função arrastar e largar. Também pode editar os valores nas [colunas de datas]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}) correspondentes através dos detalhes da linha, desde que tenha a [autorização]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}) necessária.

### Tratamento simplificado dos dados na página da tabela

Tal como no Base, pode agora [selecionar todas as entradas de uma coluna]({{< relref "help/base-editor/tabellen/hinzufuegen-von-daten-per-copy-and-paste" >}}) nas [páginas de tabelas]({{< relref "help/app-builder/seitentypen-in-universellen-apps/tabellenseiten-in-universellen-apps" >}}) das suas aplicações com apenas um clique no cabeçalho da coluna. A prática [pega de preenchimento]({{< relref "help/base-editor/zeilen/duplizieren-einer-zeile" >}}) também é agora possível: arraste o pequeno quadrado no canto inferior direito de uma célula para baixo para transferir o valor para todas as linhas abaixo.

![Marcar entradas de coluna](Spalteneintraege-markieren-und-Fuellgriff-in-App.gif)

### Coluna do empregado disponível nas páginas do formulário

Se utilizar uma [coluna de empregado]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}}) na sua tabela, esta **não** está disponível em [formulários Web]({{< relref "help/base-editor/webformulare" >}}). No entanto, a partir do SeaTable 4.4, pode adicionar colunas de colaboradores a [páginas de formulários]({{< relref "help/app-builder/seitentypen-in-universellen-apps/formularseiten-in-universellen-apps" >}}) na aplicação universal. Por exemplo, os membros da sua equipa podem selecionar-se a si próprios para um pedido de férias e já não têm de introduzir os seus nomes manualmente. Primeiro, é necessário ativar a opção para apresentar a lista de colaboradores nas [definições da aplicação]({{< relref "help/app-builder/einstellungen/einstellungen-einer-universellen-app-aendern/" >}}).

### Mais opções de personalização para páginas individuais

Na versão 4.4, é possível ocultar a **barra de título** na [página individual]({{< relref "help/app-builder/seitentypen-in-universellen-apps/individuelle-seiten-in-universellen-apps" >}}). Isto permite-lhe criar páginas de destino visualmente apelativas. Para os elementos de imagem e mapa, os menus pendentes permitem-lhe **ligar** rapidamente a outras páginas da aplicação. Para as **estatísticas**, adicionámos mais tipos de gráficos e opções de configuração adicionais que tornam a criação de painéis de controlo ainda mais conveniente. Para apresentar claramente as muitas opções de estilo, dividimos o estilo do gráfico e o estilo geral em dois separadores diferentes.

## Galeria e aplicações de consulta de dados

Tal como anunciado nas últimas notas de versão, removemos o **Gallery App Builder** no SeaTable 4.4. Se pretender criar uma nova aplicação com uma [galeria]({{< relref "help/app-builder/seitentypen-in-universellen-apps/galerieseiten-in-universellen-apps" >}}), o Universal App Builder oferece-lhe uma alternativa mais funcional.

{{< warning headline="É bom saber" text="**As aplicações de galeria existentes continuarão a funcionar**. No entanto, recomendamos a mudança das aplicações de galeria existentes para aplicações universais, de modo a beneficiar de novos desenvolvimentos e melhorias." />}}

![Criar diálogo de aplicações](Create-app-dialog-.png)

Também houve algumas alterações na [aplicação de consulta de dados]({{< relref "help/app-builder/app-verwaltung/datenabfrage-app" >}}). O antigo App Builder para consultas de dados foi removido e substituído por um novo baseado no Universal App Builder. Isto significa que ainda é possível criar aplicações públicas para consultar as suas bases, mas a interface é agora semelhante à do Universal App Builder. O mesmo se aplica às aplicações de consulta existentes e às aplicações de galeria: não tem de fazer nada e pode continuar a utilizá-las.

{{< warning headline="Ganho de eficiência" text="As alterações descritas permitem-nos concentrarmo-nos no desenvolvimento do Universal App Builder e, assim, atingir uma maior velocidade de desenvolvimento para as próximas funcionalidades." />}}

## Experiência de utilizador mais agradável ao importar o Excel

O SeaTable 4.4 torna [a importação de tabelas Excel]({{< relref "help/startseite/import-von-daten/import-von-excel-dateien-in-seatable" >}}) mais rápida, mais flexível e mais estável: Tabelas com muitos milhares de linhas são agora disponibilizadas no SeaTable em apenas alguns momentos. Na janela de pré-visualização significativamente ampliada, pode agora selecionar quais as tabelas de um livro de trabalho - todas ou apenas as individuais - que pretende importar do ficheiro XLSX. Enquanto no passado os caracteres especiais nos nomes das colunas e outros casos especiais levavam a resultados indesejáveis, agora são tidos em conta de forma fiável. As mensagens de erro melhoradas fornecem indicações claras de conflitos, especialmente ao [importar para o armazenamento de Big Data]({{< relref "help/base-editor/big-data/eine-excel-tabelle-ins-big-data-backend-importieren" >}}).

![Importação do Excel](Excel-Import.png)

{{< warning headline="Uma pequena amostra" text="Com o SeaTable 5.0, estamos a tornar a importação ainda mais flexível! As colunas individuais de uma tabela podem ser seleccionadas e excluídas da importação." />}}

## Mais funções para registos de dados partilhados

[Os conjuntos de dados partilhados]({{< relref "help/startseite/gemeinsame-datensaetze/funktionsweise-von-gemeinsamen-datensaetzen" >}}) são muito úteis se o utilizador e os membros da sua equipa necessitarem de determinadas tabelas (por exemplo, uma lista de empregados) em diferentes [grupos]({{< relref "help/startseite/gruppen/einfuehrung-in-die-arbeit-mit-gruppen" >}}) das suas bases. O SeaTable 4.4 acrescenta três novas funções às já existentes:

1. Se tiver um [Base de cópia]({{< relref "help/startseite/bases/eine-base-in-eine-gruppe-kopieren" >}})Se copiar uma base para um grupo no qual estão incluídos registos de dados partilhados, o utilizador pode decidir se pretende manter a ligação a esses registos de dados. O grupo para o qual se copia a base deve, obviamente, ter acesso aos registos de dados partilhados.

    ![Manter a ligação ao conjunto de dados comum ao copiar uma base](Retain-link-to-common-dataset-when-copying-a-base.gif)

2. Após o [Restaurar bases a partir de instantâneos]({{< relref "help/base-editor/historie-und-versionen/wiederherstellung-eines-snapshots" >}}) ou o [Criar uma base a partir de um modelo]({{< relref "help/startseite/bases/anlegen-einer-base-mithilfe-einer-vorlage" >}}) é possível ligar tabelas existentes a um registo de dados partilhados e, assim, permitir a sincronização com os dados aí existentes. Anteriormente, os registos de dados partilhados não podiam ser reimportados, mas apenas integrados em novas tabelas.

    ![Reimportar conjunto de dados comum](Reimport-common-dataset.gif)

3. O criador de um registo de dados partilhados pode agora selecionar o [Sincronização]({{< relref "help/startseite/gemeinsame-datensaetze/synchronisation-eines-gemeinsamen-datensatzes" >}}) de todas as tabelas dependentes com o conjunto de dados e, assim, garantir que os outros utilizadores utilizam o estado atual dos dados nas suas bases. No passado, era necessário confiar nos utilizadores que configuravam a sincronização automática ou que a desencadeavam manualmente.

    ![Forçar a sincronização de um conjunto de dados comum](Force-sync-of-common-dataset.png)

## Os valores por defeito aplicam-se em todo o lado

Com a versão 4.4, o SeaTable generaliza a utilização dos [valores por defeito]({{< relref "help/base-editor/spalten/standardwert-fuer-eine-spalte-festlegen" >}}). Quando cria uma nova linha, seja na tabela de uma base ou aplicação, através de uma [coluna de ligação]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}), [formulário Web]({{< relref "help/base-editor/webformulare" >}}), [botão]({{< relref "help/base-editor/schaltflaechen/zeilen-per-schaltflaeche-in-eine-andere-tabelle-kopieren" >}}) ou [automatização]({{< relref "help/base-editor/automationen/automations-aktionen" >}}), os valores por defeito são aplicados em todo o lado quando a linha é criada. Anteriormente, os valores por defeito só eram aplicados quando uma nova linha era criada manualmente numa tabela.

Como o âmbito dos valores por defeito aumentou consideravelmente, criámos também um item de menu proeminente nas opções de coluna, que pode utilizar para definir convenientemente os valores por defeito.

![O valor por defeito aplica-se a todas as novas linhas](Standardwert-greift-ueberall-bei-neuen-Zeilen.gif)

{{< warning headline="Nota" text="Se for definido um valor predefinido na tabela e no formulário Web, o valor do formulário aplica-se a todas as linhas criadas através do formulário." />}}

A propósito: pode até ativar os valores predefinidos com o parâmetro correspondente ao criar novas linhas através da API.

## E muito mais

Já conhece o **editor de texto formatado** de vários locais no SeaTable, por exemplo, da [descrição de base]({{< relref "help/base-editor/weitere-optionen/wie-man-einer-base-eine-beschreibung-hinzufuegt" >}}), do [tipo de coluna para textos longos]({{< relref "help/base-editor/spaltentypen/die-spalte-formatierter-text" >}}) ou [mensagens de correio eletrónico]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}}). Com o SeaTable 4.4, melhorámos a facilidade de utilização e corrigimos alguns erros. Aqui estão apenas dois: Anteriormente, as quebras de linha múltiplas eram removidas ao fechar o editor e o texto existente era substituído ao escrever na célula. No novo editor, as quebras de linha múltiplas são mantidas e podem ser utilizadas para estruturar o texto de forma mais clara. Também eliminámos o risco de eliminações não intencionais: Ao digitar, o novo texto é colocado à frente do texto existente.

Na nova versão, também melhorámos o **centro de notificações** {{< seatable-icon icon="dtable-icon-notice" >}} na página inicial. Agora, pode ver todas as [notificações]({{< relref "help/startseite/benachrichtigungen/sinn-und-zweck-von-benachrichtigungen-in-seatable" >}}) no sistema num único local, localizar a origem da notificação e ir para a página relevante com um clique.

Por último, mas não menos importante, optimizámos o diálogo para **redefinir a palavra-passe do SeaTable**. Para o efeito, uniformizámos o design e acrescentámos mais funções. Se [alterar]({{< relref "help/startseite/persoenliche-einstellungen/eigenes-passwort-aendern" >}}) a [palavra-passe]({{< relref "help/startseite/persoenliche-einstellungen/eigenes-passwort-aendern" >}}) nas suas definições pessoais, pode agora visualizá-la em texto simples, clicando no símbolo do olho. Também lhe é mostrada automaticamente a força da sua nova palavra-passe.
