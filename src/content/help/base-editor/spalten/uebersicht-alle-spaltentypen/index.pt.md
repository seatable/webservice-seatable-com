---
title: 'Visão geral de todos os tipos de colunas'
date: 2022-08-25
lastmod: '2024-03-18'
categories:
    - 'arbeiten-mit-spalten'
author: 'cdb'
url: '/pt/ajuda/overview-tipos-coluna'
aliases:
    - '/pt/ajuda/uebersicht-alle-spaltentypen'
seo:
    title: 'Todos os tipos de coluna no SeaTable – funcionalidades'
    description: 'Veja todos os 26 tipos de coluna disponíveis no SeaTable: texto, número, arquivos, seleções, fórmulas e relações entre tabelas, dicas de uso.'
star: true
weight: 1
---

No SeaTable, pode guardar informações e dados numa grande variedade de formatos.

- Para além de informações simples baseadas em texto (por exemplo, palavras, números, quantias de dinheiro), o SeaTable também suporta o armazenamento de informações complexas (por exemplo, ficheiros, imagens, texto longo, incluindo elementos inseridos).
- Com os campos de selecção, pode dividir os seus dados em categorias definidas e as funções de validação integradas (por exemplo, URL, dados de posição) asseguram que as suas entradas estão num formato uniforme e directamente avaliável.
- Com as fórmulas pode efectuar operações aritméticas e com as ligações cria relações entre entradas de diferentes tabelas que permitem operações poderosas na base de dados.

Conheça aqui os 26 tipos de colunas diferentes do SeaTables!

## Colunas com introdução manual de dados

A cada coluna da tabela é atribuído um tipo. O tipo de coluna determina os dados que podem ser introduzidos nas células da coluna. Por exemplo, não é possível inserir ficheiros num campo de texto. A coluna de data, por outro lado, obriga-o a introduzir uma data no formato seleccionado.

### Texto

Símbolo: {{< seatable-icon icon="dtable-icon-single-line-text" >}} **Texto**

Este tipo de coluna armazena **texto** sem formatação e é um dos tipos de coluna mais básicos do SeaTable. O conteúdo do texto é constituído por **letras**, **números** e **caracteres especiais**, bem como **espaços**. Por isso, as colunas de texto são frequentemente utilizadas para nomes e descrições (curtas).

[Mais informações sobre a coluna de texto]({{< relref "help/base-editor/spaltentypen/die-spalten-text-und-formatierter-text" >}})

### Texto longo

Símbolo: {{< seatable-icon icon="dtable-icon-long-text" >}} **Texto longo**

Neste tipo de coluna, pode guardar **textos mais longos** com elementos inseridos, como **imagens** e **tabelas**. Estão também disponíveis várias opções de formatação e estruturação para os seus textos utilizando a linguagem de marcação Markdown. Por conseguinte, a coluna _Texto longo_ é frequentemente utilizada para descrições e documentação. Se for útil para a recolha de informações que os textos contenham elementos estruturantes e/ou que o texto e as imagens estejam próximos uns dos outros, então este tipo de coluna é ideal.

[Mais informações sobre a coluna Texto longo]({{< relref "help/base-editor/spaltentypen/die-spalten-text-und-formatierter-text" >}})

### Número

Símbolo: {{< seatable-icon icon="dtable-icon-number" >}} **Número**

As colunas de números armazenam **informações numéricas** e podem ser utilizadas de várias formas para trabalhar com números de todos os tipos. A informação numérica pode ser um **número**, uma **percentagem** ou um **montante monetário**. Além disso, as colunas de números permitem **calcular valores** que podem ser visualizados com fórmulas e [estatísticas]({{< relref "help/base-editor/statistiken" >}}). No entanto, as colunas de números não são adequadas para armazenar cadeias de caracteres de qualquer comprimento e a introdução de letras é recusada pelo SeaTable neste tipo de coluna.

[Mais sobre a coluna dos números]({{< relref "help/base-editor/spaltentypen/die-zahlen-spalte" >}})

### Data

Símbolo: {{< seatable-icon icon="dtable-icon-calendar-alt-solid" >}} **Data**

Com a ajuda da coluna de datas, pode introduzir **horas** e **datas** nas suas tabelas até ao minuto. Note que as colunas de datas interpretam sempre as informações introduzidas como uma data, de modo que as entradas que não podem ser interpretadas como datas são sempre descartadas como inválidas.

[Mais informações sobre a coluna de data]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}})

### Duração

Símbolo: {{< seatable-icon icon="dtable-icon-duration" >}} **Duração**

A coluna de duração é um tipo de coluna numérica especializada para armazenar **medições de tempo, períodos e intervalos,** podendo assim registar um período de tempo ao minuto ou mesmo ao segundo. Por esta razão, a coluna é particularmente adequada, entre outras coisas, para registar a duração de vários eventos. No entanto, ao utilizar a coluna, deve ter-se em atenção que as entradas não numéricas são sempre rejeitadas como inválidas.

[Mais informações sobre a coluna permanente]({{< relref "help/base-editor/spaltentypen/die-dauer-spalte" >}})

### Seleção única

Símbolo: {{< seatable-icon icon="dtable-icon-single-election" >}} **Seleção única**

Numa célula de uma coluna de seleção individual, é possível seleccionar um **valor** a partir de uma lista de opções definidas. A lista de opções definidas por coluna de seleção única é criada pelo próprio usuário e pode ser adaptada a circunstâncias variáveis a qualquer momento. A seleção única é, portanto, particularmente adequada para categorizar e agrupar os dados.

[Mais informações sobre a coluna de seleção única]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}})

### Seleção múltipla

Símbolo: {{< seatable-icon icon="dtable-icon-multiple-selection" >}} **Seleção múltipla**

Com uma seleção múltipla, é possível seleccionar **qualquer número de valores** de uma lista de opções definidas. Tal como na seleção única, o próprio utilizador cria a lista de valores possíveis e adapta-a às suas necessidades individuais. A seleção múltipla é, portanto, ideal para o registo de palavras-chave - também designado por etiquetagem.

[Mais informações sobre a coluna de seleção múltipla]({{< relref "help/base-editor/spaltentypen/die-mehrfachauswahl-spalte" >}})

### Imagem

Símbolo: {{< seatable-icon icon="dtable-icon-picture" >}} **Imagem**

O tipo de coluna Imagem armazena qualquer número de **ficheiros de imagem** nos formatos de ficheiro **BMP**, **GIF**, **ICO**, **JPG**, **PNG**, **SVG** e **TIF**. A coluna de imagem é assim uma coluna de ficheiro restrita aos formatos de ficheiro de imagem.

[Mais informações sobre a coluna de imagens]({{< relref "help/base-editor/spaltentypen/die-bild-spalte" >}})

### Arquivo

Símbolo: {{< seatable-icon icon="dtable-icon-file" >}} **Arquivo**

O tipo de coluna Arquivo armazena qualquer número de arquivos de **qualquer tipo de arquivo**. O SeaTable oferece uma função de pré-visualização para numerosos formatos de ficheiros de imagem.

[Mais informações sobre a coluna do Arquivo]({{< relref "help/base-editor/spaltentypen/die-datei-spalte" >}})

### E-mail

Símbolo: {{< seatable-icon icon="dtable-icon-email" >}} **E-mail**

As colunas de e-mail são colunas de texto especializadas para capturar e armazenar **endereços de e-mail** e permitem a utilização directa com um clique do rato. A coluna de correio electrónico é particularmente útil para formulários Web. A utilização de um campo de correio electrónico em vez de uma coluna de texto garante que a entrada tem a sintaxe de um endereço de correio electrónico válido. Além disso, as colunas de correio electrónico podem ser utilizadas para enviar mensagens de correio electrónico através de [botões]({{< relref "help/base-editor/schaltflaechen/eine-e-mail-per-schaltflaeche-verschicken" >}}) e [automatizações]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}}).

Se precisar de informações mais detalhadas sobre a coluna de correio electrónico, dê uma vista de olhos neste [artigo]({{< relref "help/base-editor/spaltentypen/die-e-mail-spalte" >}}).

### URL

Símbolo: {{< seatable-icon icon="dtable-icon-url" >}} **URL**

As colunas URL interpretam as informações introduzidas como um **recurso** na rede local ou na Internet e permitem o acesso directo através de um clique. Uma vez que as entradas neste tipo de coluna não são validadas, pode ser armazenado numa célula um endereço Internet (por exemplo, https://seatable.com) ou um endereço IP (por exemplo, 192.168.178.1).

[Mais informações sobre a coluna URL]({{< relref "help/base-editor/spaltentypen/die-url-spalte" >}})

### Caixa de seleção

Símbolo: {{< seatable-icon icon="dtable-icon-check-square-solid" >}} **Caixa de seleção**

As caixas de seleção permitem a recolha de **informações binárias**: Sim ou Não ou marca de verificação _definida_ vs. _marca de verificação não definida_. Não são possíveis outras entradas. Por conseguinte, são adequadas para marcar tarefas como concluídas, por exemplo, ou seja, para registar se as linhas cumprem uma determinada condição de sim/não. Por este motivo, as colunas de caixas de seleção também podem ser utilizadas de forma excelente para [filtrar]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}}), [ordenar]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}}) ou [agrupar]({{< relref "help/base-editor/ansichten/gruppieren-von-eintraegen-in-einer-ansicht" >}}).

[Mais informações sobre a coluna da caixa de seleção]({{< relref "help/base-editor/spaltentypen/die-checkbox-spalte" >}})

### Avaliação

Símbolo: {{< seatable-icon icon="dtable-icon-rate" >}} **Avaliação**

Uma coluna de avaliação permite-lhe **classificar** os seus registos para lhes atribuir uma **avaliação** ou **pontuação de qualidade**. Pode seleccionar uma escala de classificação de 1 a 10 e escolher entre diferentes cores e formas. Isto permite que os dados sejam avaliados e classificados de forma rápida e fácil para que todos compreendam.

[Mais informações sobre a coluna de avaliação]({{< relref "help/base-editor/spaltentypen/die-rating-spalte" >}})

### Número de telefone

Símbolo: {{< seatable-icon icon="dtable-icon-telephone" >}} **Número de telefone**

SeaTable tem o seu próprio tipo de coluna para números de telefone. Em comparação com uma coluna de texto normal, a coluna de número de telefone oferece a vantagem de poder **ligar para um número de telefone** com um clique do rato.

[Mais informações sobre a coluna de número de telefone]({{< relref "help/base-editor/spaltentypen/die-telefonnummer-spalte" >}})

### Fórmula

Símbolo: {{< seatable-icon icon="dtable-icon-formula" >}} **Fórmula**

Com a ajuda de fórmulas, é possível **ligar** diferentes valores de colunas de uma linha e criar diferentes **funções** com base no conteúdo dessas colunas. Entre outras coisas, pode calcular com valores nas suas tabelas, alterar valores ou relacionar valores da mesma linha.

Precisa de mais informações sobre a coluna de fórmulas? Então, consulte este [artigo]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}}). Como as fórmulas são uma característica muito complexa, encontrará muitos outros artigos de ajuda no nosso manual. Clique [aqui]({{< relref "help/base-editor/formeln" >}}) e será redireccionado para a página de resumo.

### Ligação a outras entradas

Símbolo: {{< seatable-icon icon="dtable-icon-link-other-record" >}} **Ligação a outras entradas**

Nas células deste tipo de coluna pode ser introduzido qualquer número de **referências a entradas noutras tabelas** da base. A coluna de ligação destina-se a mapear relações entre entradas em diferentes tabelas. A coluna de ligação pode ser utilizada para representar relações 1:n e n:1, bem como relações n:m.

Para mais informações sobre o tipo de coluna Ligação a outras entradas, [clique aqui]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}})

### Fórmula para ligações

Símbolo: {{< seatable-icon icon="dtable-icon-link-formulas" >}} **Fórmula para ligações**

Com a fórmula para ligações, é possível **exibir** dados de **tabelas ligadas** na tabela atual e **relacioná-los** entre si. Um total de cinco fórmulas diferentes estão disponíveis para o tipo de coluna, com as quais também é possível executar cálculos estatísticos. O pré-requisito para a utilização da coluna é a existência de pelo menos uma coluna do tipo **Ligação a outras entradas** na tabela.

[Mais sobre a coluna Fórmula para ligações]({{< relref "help/base-editor/spaltentypen/die-spalte-formel-fuer-verknuepfungen" >}})

### Colaborador

Símbolo: {{< seatable-icon icon="dtable-icon-collaborator" >}} **Colaborador**

Numa coluna de colaboradores, é possível introduzir qualquer número de **utilizadores** que tenham, pelo menos, acesso de leitura à base. Os utilizadores do SeaTable sem acesso não podem ser introduzidos na coluna como colaboradores. Também não são permitidas outras entradas. A coluna de colaboradores é particularmente útil para a gestão de projectos. Por exemplo, se introduzir tarefas a serem concluídas numa tabela, pode registar as pessoas que executam as tarefas e a pessoa responsável em colunas do tipo Colaborador.

[Mais informações sobre a coluna do Colaborador]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}})

### Botão

Símbolo: {{< seatable-icon icon="dtable-icon-button" >}} **Botão**

Com os botões, é possível **automatizar** o processamento de dados ou a execução de determinadas acções. No entanto, é importante ter em atenção que os botões têm sempre de ser accionados **manualmente**. Com a ajuda do botão que pode ser adicionado às linhas desta coluna, o usuário aciona determinadas ações definidas antecipadamente. Por esse motivo, esse tipo de coluna é particularmente adequado para automatizar etapas de processo.

Para mais informações sobre o botão e as acções que podem ser desencadeadas em colunas deste tipo, consulte este [artigo]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}}).

### Geolocation

Símbolo: {{< seatable-icon icon="dtable-icon-location" >}} **Geolocation**

Nesta coluna, pode registar **localizações** e visualizá-las mais tarde com o [plug-in do mapa]({{< relref "help/base-editor/plugins/anleitung-zum-karten-plugin" >}}). Para tal, pode seleccionar a entrada com país e região ou com latitude e longitude. Além disso, tem a opção de encontrar um país ou região utilizando a função de pesquisa e adicioná-lo como entrada.

[Mais informações sobre a coluna de geolocalização]({{< relref "help/base-editor/spaltentypen/die-geopositions-spalte" >}})

### Assinatura digital

Símbolo: {{< seatable-icon icon="dtable-icon-rename" >}} **Assinatura digital**

Pode armazenar **assinaturas digitais** numa coluna de assinaturas, que são automaticamente guardadas na gestão de ficheiros da sua Base. As assinaturas digitais são muito adequadas para a captura de dados através de **formulários Web**, por exemplo, para que as aplicações sejam convenientemente assinadas em linha.

[Mais informações sobre a coluna de assinaturas]({{< relref "help/base-editor/spaltentypen/die-signatur-spalte" >}})

## Tipos de colunas com recolha automática de dados

Para além dos tipos de colunas em que o utilizador como utilizador introduz dados, existem outros cinco tipos de colunas no SeaTable cujo conteúdo o SeaTable gera automaticamente. Estas colunas não podem ser editadas manualmente pelo utilizador. São utilizadas principalmente para fins de documentação.

### Criador

Símbolo: {{< seatable-icon icon="dtable-icon-creator" >}} **Criador**

SeaTable documenta automaticamente o **nome do utilizador** que criou a linha na coluna do criador.

[Mais informações sobre a coluna do criador]({{< relref "help/base-editor/spaltentypen/die-spalten-ersteller-und-erstelldatum" >}})

### Tempo criado

Símbolo: {{< seatable-icon icon="dtable-icon-creation-time" >}} **Tempo criado**

SeaTable documenta automaticamente **a data e a hora em que a linha foi criada** na coluna Tempo criado. A data e a hora são exibidas no formato AAAA-MM-DD HH:MM.

[Mais informações sobre a coluna Tempo criado]({{< relref "help/base-editor/spaltentypen/die-spalten-ersteller-und-erstelldatum" >}})

### Último modificador

Símbolo: {{< seatable-icon icon="dtable-icon-creator" >}} **Último modificador**

SeaTable documenta automaticamente o **nome do utilizador** que fez a **última alteração** a uma entrada na coluna do Último modificador. Uma vez que a coluna regista automaticamente as alterações às entradas, é bem adequada, por exemplo, como gatilho para automatismos, bem como para filtros e ordenação.

[Mais informações sobre a coluna Último modificador]({{< relref "help/base-editor/spaltentypen/die-spalten-letzter-bearbeiter-und-bearbeitungsdatum" >}})

### Último tempo modificado

Símbolo: {{< seatable-icon icon="dtable-icon-creation-time" >}} **Último tempo modificado**

SeaTable documenta **a data e a hora da última alteração de uma entrada** na coluna Último tempo modificado. A data e a hora são apresentadas no formato AAAA-MM-DD HH:MM. Uma vez que a coluna regista automaticamente as alterações às entradas, é adequada como acionador de automatismos, bem como para filtros e ordenação.

[Mais informações sobre a coluna Último tempo modificado]({{< relref "help/base-editor/spaltentypen/die-spalten-letzter-bearbeiter-und-bearbeitungsdatum" >}})

### Número automático

Símbolo: {{< seatable-icon icon="dtable-icon-autonumber" >}} **Número automático**

O tipo de coluna Número automático cria um **número automaticamente crescente** para cada nova linha. Este tipo de coluna é utilizado sempre que é necessário um identificador único para cada registo.

[Mais informações sobre a coluna Número automático]({{< relref "help/base-editor/spaltentypen/der-spaltentyp-automatische-nummer" >}}).
