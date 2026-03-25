---
title: 'SeaTable 3.0: Validação de dados, editores web de escritório e novo backend de armazenamento - SeaTable'
description: 'Defina padrões e garanta qualidade nas colunas de texto; edite Word, Excel e PowerPoint direto no navegador. Novo backend reduz uso de disco e acelera backups. Sincronização entre bases e menús mais claros para times de qualquer porte. Tudo para facilitar colaboração e controle de dados.'
date: 2022-06-21
lastmod: '2022-06-27'
author: 'rdb'
url: '/pt/seatable-release-3-0'
color: '#cfe107'
categories:
    - 'product-features'
seo:
    title: 'SeaTable 3.0: Validação & Office online fácil'
    description: 'Valide dados, edite documentos Office online e melhore o gerenciamento do time com novidades e armazenamento otimizado.'
---

A SeaTable 3.0 está aqui! O terceiro grande lançamento do SeaTable oferece edição online de documentos do Office, validação automática de dados, mais funções para conjuntos de dados partilhados e uma nova componente de servidor para um armazenamento mais eficiente de bases. Como sempre, o [changelog]({{< relref "pages/changelog" >}}) fornece informações sobre as muitas outras melhorias detalhadas e correcções de bugs na nova versão. As novas funções estão disponíveis imediatamente para os [utilizadores do SeaTable Cloud](https://cloud.seatable.io/). A imagem para SeaTable 3.0 foi disponibilizada hoje à noite em [Docker](https://hub.docker.com/r/seatable/seatable-enterprise/tags) Hub.  
Para além das melhorias funcionais na aplicação SeaTable, existe outra nova funcionalidade para os utilizadores do SeaTable Cloud: uma nova gestão de equipas com funções alargadas e design melhorado torna a gestão de equipas pequenas e especialmente maiores muito mais fácil. Pode saber mais sobre a nova gestão de equipas no artigo [A nova gestão de equipas]({{< relref "help/teamverwaltung/abonnement/die-funktionen-der-teamverwaltung-in-der-uebersicht" >}}).

## Validação automática de dados

Cordas de qualquer tipo e comprimento podem ser introduzidas em colunas de texto e oferecem assim uma grande flexibilidade. As colunas de selecção simples e múltiplas são ideais para estruturar dados devido aos seus valores pré-definidos. A nova função de validação de dados permite combinar as vantagens das colunas de texto com as das colunas de selecção.

Se a validação dos dados for activada, o SeaTable verifica se o valor introduzido na célula corresponde ao formato alvo definido. Se a entrada não corresponder ao formato alvo, a célula é destacada a vermelho. Em formulários web, uma entrada não conforme resultará numa mensagem de erro e o formulário não pode ser submetido.

![Validação de dados em SeaTable 3.0](FormatCheck.png)

O formato de destino é definido sob a forma de uma [expressão regular] (https://de.wikipedia.org/wiki/Regul%C3%A4rer_Ausdruck). Por exemplo, uma expressão regular para uma sequência de números com exatamente 5 dígitos é \[0-9\]{5}. Há dois argumentos a favor das expressões regulares: são um método amplamente utilizado e oferecem a máxima flexibilidade. O tipo de caracteres permitidos, o comprimento e também a sintaxe da entrada podem ser definidos com precisão através de expressões regulares.

A validação de dados está disponível em colunas de texto na versão 3.0. Se um formato alvo for adicionado posteriormente, todas as entradas existentes são também verificadas e os valores não conformes são marcados como tal. Portanto, nada impede a activação posterior da validação de dados nas colunas existentes.

## Edição online de documentos do Office

A SeaTable torna a colaboração de equipa interactiva. Uma base é partilhada com apenas alguns cliques e as entradas numa base partilhada são imediatamente exibidas a outros utilizadores. Os ficheiros de escritório numa base de SeaTable são diferentes. Para editar um documento Word, folha de cálculo Excel ou apresentação PowerPoint, este deve primeiro ser descarregado. A edição tem então lugar offline. Os outros utilizadores só têm acesso à versão alterada do documento após o carregamento manual. Isto foi um espinho no nosso lado.

SeaTable 3.0 estende a colaboração em tempo real conhecida do editor de tabelas aos documentos do Office. Os documentos podem ser editados directamente no browser e com várias pessoas ao mesmo tempo. As alterações dos co-autores são exibidas em tempo real, para que se saiba exactamente quem está a trabalhar no documento e onde. O carregamento manual também já não é necessário. Quando o último utilizador deixa o documento, o estado actual do documento é automaticamente transferido de volta para o SeaTable e armazenado na coluna do ficheiro como uma nova versão do documento.

Editar um documento Office a partir do SeaTable não poderia ser mais fácil: Um clique no ficheiro Word, Excel ou PowerPoint abre o documento num editor num novo separador. Os utilizadores que estão actualmente a editar o documento são exibidos no canto superior direito. As alterações feitas por estes utilizadores são efectuadas directamente no documento exposto e são indicadas por uma bandeira. A poupança tem lugar automaticamente.

Os editores utilizados para edição online são da [ONLYOFFICE](https://onlyoffice.com). Os editores do servidor de documentos ONLYOFFICE caracterizam-se por uma interface de utilizador moderna e por uma muito boa compatibilidade com os formatos de ficheiros Microsoft. Além disso, o servidor de documentos, tal como o SeaTable, pode ser auto-hospedado.

A edição online está disponível em todas as subscrições SeaTable Cloud, incluindo a subscrição gratuita. Para o funcionamento no local da SeaTable, o servidor de documentos ONLYOFFICE deve ser instalado e configurado. As instruções de configuração podem ser encontradas no [SeaTable Admin Manual](https://admin.seatable.com/).

## Melhoria da sincronização das bases

A função Registos Partilhados permite sincronizar os dados de uma Base com uma ou mais Bases. São particularmente úteis se pretender disponibilizar os dados a outros utilizadores para processamento e enriquecimento posterior, mas não pode dar a esses utilizadores direitos de acesso à lista que gere ("lista principal"). A versão 3.0 inclui várias melhorias para simplificar a criação, a sincronização e a duplicação de registos partilhados.

![Os conjuntos de dados comuns existentes são apresentados na caixa de diálogo "Novo conjunto de dados comum".](ExistingCDS.png)

A partir do SeaTable 3.0, os conjuntos de dados comuns já criados são apresentados na caixa de diálogo "Novo conjunto de dados comum". Isto evita a criação múltipla de conjuntos de dados comuns.

Na nova versão, as colunas criadas pela importação de um registo comum são marcadas com um ícone de sincronização. Isto facilita a distinção das colunas que serão sobregravadas com o conjunto de dados comum durante uma re-síntese de todas as outras colunas. A marcação visual reduz o risco de perda não intencional de dados.

![Colunas importadas de CDS marcadas com ícone de sincronização](ColumnIconsCDS.png)

Ao duplicar uma tabela com um conjunto de dados comuns importados, apenas os dados eram duplicados até agora. A ligação ao conjunto de dados comum não foi dada na tabela duplicada, de modo que não foi possível uma sincronização renovada. A função de duplicação foi agora alargada para que se possa transferir a ligação ao conjunto de dados comum para a nova tabela a ser criada ou descartá-la através de um interruptor.

## Maior eficiência de armazenamento

O novo componente SeaTable Server dtable-storage-server reduzirá significativamente os requisitos de memória para o armazenamento de bases, instantâneos e backups de filas arquivadas. A componente de servidor marítimo, que era anteriormente responsável por isto, continuará a desempenhar um papel importante mas reduzido

Tecnicamente, o dtable-storage-server é uma camada de abstracção simples para diferentes backends de armazenamento. Como anteriormente, o armazenamento local e o armazenamento de objectos S3 são suportados. SeaTable oferece assim opções atractivas de armazenamento para sistemas pequenos e simples, bem como para configurações altamente escaláveis.

Com os servidores SeaTable recentemente instalados, as bases são automaticamente armazenadas no servidor dtable-storage-server. Apenas o armazenamento de imagens e ficheiros continua a ser feito pelo servidor marítimo. A situação é diferente para os sistemas existentes. Ao actualizar um SeaTable Server 2.x, o dtable-storage-server não é automaticamente instalado e configurado. Isto tem de ser feito manualmente; o procedimento é descrito no [manual SeaTable](https://admin.seatable.com/upgrade/extra-upgrade-notice/#30). Recomenda-se uma migração das bases existentes para o dtable-storage-server. Para um pequeno número de bases, a exportação para um ficheiro DTABLE e a reimportação para uma nova base é o procedimento mais simples. Com um maior número de bases, este processo também pode ser automatizado através do API. No entanto, a migração não é necessária. O SeaTable 3.0 pode continuar a carregar bases a partir do SeaServer.

## Outras melhorias

Além disso, existem inúmeras outras melhorias, as três mais importantes das quais apresentamos aqui muito brevemente.

A estrutura do menu no cabeçalho da Base foi expandida e revista. A mudança mais óbvia é o avatar, que é agora exibido no canto superior direito, análogo à página inicial. Para dar lugar ao avatar, o botão de três pontos foi movido para baixo de uma linha. O menu por detrás deste botão foi revisto. De acordo com a sua importância, as regras de notificação e automatização, por exemplo, foram retiradas deste menu. Têm agora o seu próprio ícone no canto superior direito.

Os [ficheiros DTABLE]({{< relref "help/startseite/import-von-daten/dtable-dateiformat" >}}), ficheiros de exportação de bases, contêm agora também regras de automatização. O mesmo se aplica à cópia de uma base para outro grupo. Isto poupa retrabalho manual desnecessário ao transferir bases entre grupos e servidores SeaTable.

A coluna de título pode agora ser seleccionada no plugin Kanban. O valor das colunas de título está no topo da carta Kanban, independentemente da sequência das colunas na tabela.
