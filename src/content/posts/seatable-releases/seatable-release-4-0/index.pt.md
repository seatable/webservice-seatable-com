---
title: 'SeaTable 4.0: novo tipo de coluna, gestão de ficheiros melhorada e progressos com o Universal App Builder - SeaTable'
description: 'Assinatura digital chega como novo campo; file manager reúne uploads/folders/edição/drag&drop; integração Seafile amplia limites; estatísticas moduladas e App Builder evoluído. Logo próprio, várias correções e atualização de preços para times prontos à transformação digital.'
date: 2023-06-27
lastmod: '2023-06-27'
author: 'kgr'
url: '/pt/seatable-release-4-0'
color: '#3aa3f4'
categories:
    - 'product-features'
seo:
    title: 'SeaTable 4.0: assinatura digital e arquivos'
    description: 'Gerencie arquivos, assine digitalmente, integre Seafile, obtenha novas estatísticas e recursos no App Builder. SeaTable 4.0 moderniza sua base!'
---

Enquanto o sol está a brilhar lá fora, os nossos programadores mantiveram a cabeça fria e concluíram a quarta grande versão do SeaTable. A versão 4.0 do SeaTable melhora as funções existentes, mas também sacia a sede de novas funcionalidades. Novidades na versão 4.0: um tipo de coluna para assinaturas digitais, um gestor de ficheiros integrado para facilitar a gestão de anexos e - para os nossos clientes Cloud Enterprise - uma função de logótipo personalizado como opção de marca.

O SeaTable 4.0 também optimiza a integração da sua aplicação irmã Seafile. A integração das bibliotecas Seafile no SeaTable Bases é agora não só mais fácil, mas também mais poderosa. O mesmo se aplica às funções estatísticas, que consolidámos no SeaTable 4.0. O Universal App Builder (Beta) faz grandes progressos e oferece excelentes possibilidades de preparação de dados para grupos de utilizadores individuais. Temos o prazer de apresentar estes destaques e muitas outras pequenas melhorias.

Esta manhã, actualizámos o SeaTable Cloud para a versão 4.0. Todos os auto-hosters podem fazer o mesmo: A imagem do SeaTable 4.0 está disponível para download no conhecido [repositórioDocker](https://hub.docker.com/r/seatable/seatable-enterprise) . Como sempre, pode encontrar a lista completa de alterações no [registo de alterações]({{< relref "pages/changelog" >}}).

## Novo tipo de coluna para assinaturas digitais

Nada é mais vinculativo do que uma assinatura - seja em contratos, em escrituras ou em cartas. No SeaTable é possível criar todos estes documentos. Então, o que poderia ser mais óbvio do que digitalizar assinaturas manuscritas com o SeaTable? A nova coluna de assinatura torna-o possível! Guarde a sua assinatura digital simplesmente assinando numa célula desta coluna de imagem especial com um gesto de varrimento utilizando o rato ou, em dispositivos com um ecrã tátil, com uma caneta ou um dedo.

![Adicionar uma assinatura numa coluna de assinatura](Add-a-signature-in-a-signature-column.gif)

Isto permite fluxos de trabalho para processos de empregados e clientes que anteriormente não podiam ser mapeados no SeaTable: Com um campo de assinatura inserido, é possível, por exemplo, ter pedidos de férias ou registos para seminários em [formulários Web]({{< relref "help/base-editor/webformulare" >}}) e [aplicações universais]({{< relref "help/app-builder/app-verwaltung/universelle-app" >}}) assinados pela pessoa que os preenche. Do mesmo modo, os clientes podem confirmar a um instalador que os serviços foram efectuados no local. Através do [plug-in de design de página]({{< relref "help/base-editor/plugins/anleitung-zum-seitendesign-plugin" >}}), as assinaturas podem ser facilmente inseridas em documentos, que podem depois ser enviados como anexos de correio eletrónico. A integração perfeita do novo tipo de coluna cria muitas oportunidades para tornar os processos mais vinculativos.

## Gestão avançada de ficheiros no Base

A gestão de ficheiros do SeaTable 4.0 revoluciona o trabalho com os ficheiros nas suas bases. Com o novo gestor de ficheiros, pode gerir fácil e comodamente os ficheiros diretamente nas suas bases e as novas pastas personalizadas oferecem-lhe ainda mais flexibilidade no armazenamento e na organização dos ficheiros. A anterior gestão de anexos, que só era acessível através das opções avançadas de uma base na página inicial, foi eliminada.

O gestor de ficheiros, que pode ser acedido através do ícone de três pontos no canto superior direito do Base e adicionado à barra de ferramentas, apresenta-se da forma mais familiar que se possa imaginar: Ficheiros e pastas à direita, navegação à esquerda - os utilizadores sentir-se-ão imediatamente em casa.

![Arrastar e largar ficheiros da gestão de ficheiros para uma coluna de ficheiros](dateien-aus-dem-dateimanagement-per-drag-and-drop-in-eine-dateispalte-ziehen.gif)

Os ficheiros existentes podem ser renomeados, copiados, movidos, descarregados e eliminados no gestor de ficheiros. Também é possível criar e editar novos documentos do Office diretamente através do editor integrado. Agora pode carregar facilmente ficheiros e pastas a partir do seu dispositivo ou adicioná-los ao gestor de ficheiros utilizando a função arrastar e largar. Os ficheiros também podem ser arrastados e largados do gestor de ficheiros para as células de colunas de tabelas correspondentes e, assim, atribuídos a registos de dados. Para proporcionar o máximo de espaço possível, o gestor de ficheiros pode ser redimensionado e fixado como uma barra lateral.

![Estrutura de pastas na gestão de ficheiros](Ordnerstruktur-im-Dateimanagement-2.png)

As pastas do sistema estão relacionadas com a estrutura do Base e contêm imagens, ficheiros e assinaturas das respectivas colunas, bem como os ficheiros de configuração de aplicações e formulários Web. Nas pastas personalizadas, pode armazenar e organizar ficheiros de forma independente em pastas individuais. Os ficheiros ficam então disponíveis em scripts Python e outras funções, como formulários Web ou o plug-in de design de páginas; no entanto, algumas destas integrações só serão concluídas em versões futuras.

## Integração facilitada do Seafile para grandes volumes de dados

Por falar em gestão de ficheiros: se guardar muitos ficheiros grandes (por exemplo, imagens e vídeos) nas suas bases, atingirá rapidamente o limite de 100 MB por base, a partir do qual deixará de poder [exportar]({{< relref "help/startseite/bases/speichern-einer-base-als-dtable-datei" >}}) as suas bases. Isto significa uma perda de flexibilidade. Outro limite que se torna relevante ao armazenar muitos ficheiros no SeaTable é o [limite de armazenamento]({{< relref "pages/prices" >}}) da subscrição. Para ambos os limites, o SeaTable 4.0 oferece uma solução de valor acrescentado com a nova opção de integração do Seafile, a aplicação irmã do SeaTable.

Enquanto solução empresarial de sincronização e partilha de ficheiros, [o Seafile](https://de.seafile.com/) está predestinado a gerir qualquer número de ficheiros de grandes dimensões. Além disso, graças aos seus clientes, oferece a melhor integração possível no ambiente de trabalho individual, incluindo suporte offline. A nova integração permite-lhe utilizar os ficheiros armazenados no Seafile diretamente no SeaTable. Combina os dois produtos numa solução a partir de uma única fonte e combina os pontos fortes do Seafile com os do SeaTable.

A integração do Seafile no SeaTable dificilmente poderia ser mais fácil: Gerar um token API para uma biblioteca Seafile através da interface web do Seafile, criar uma nova conta de terceiros no SeaTable e adicionar o token (ver figura). Após uma ligação bem sucedida, a biblioteca Seafile aparece na gestão de ficheiros.

![Integração facilitada do Seafile para grandes volumes de dados](verbesserte-integration-mit-seafile-release-notes.png)

Os servidores Seafile alojados e auto-hospedados podem ser ligados. [Por favor, contacte a nossa equipa de vendas]({{< relref "pages/contact" >}}) se pretender alojar um servidor Seafile. Para os clientes SeaTable Dedicated, oferecemos o co-hospedagem Seafile.

## O plug-in de estatísticas e o módulo de estatísticas fundem-se numa única ferramenta

O SeaTable oferece-lhe uma vasta gama de opções para a [análise de dados estatísticos]({{< relref "help/base-editor/statistiken" >}}) e a sua apresentação gráfica. Até agora, tinha à sua disposição um módulo de estatísticas com funções básicas e o plugin de estatísticas avançadas. No SeaTable 4.0, este último passa a ocupar o lugar do módulo básico, pelo que já não é necessário configurar um plug-in. Todo o poder estatístico do SeaTable está agora reunido numa ferramenta poderosa, à qual pode aceder com um clique através do botão "Estatísticas" no cabeçalho da Base.

![O plug-in de estatísticas e o módulo de estatísticas fundem-se numa única ferramenta](erweitertes-statistik-plugin-release-notes.gif)

Todos os gráficos e diagramas que já criou - quer no módulo Estatísticas, quer no plugin Estatísticas avançadas - serão obviamente mantidos e automaticamente transferidos para o novo painel de controlo.

## Progresso com o Universal App Builder

O [Universal App Builder]({{< relref "help/app-builder/app-verwaltung/universelle-app" >}}) (Beta) goza de grande popularidade, a nossa equipa de desenvolvimento está a trabalhar a todo o vapor nos retoques finais e os resultados são impressionantes! Todos os [tipos de página]({{< relref "help/app-builder/seitentypen-in-universellen-apps/ueberblick" >}}) têm agora um layout uniforme e oferecem a função de pesquisa de colunas nas definições de dados que já conhece das bases. Além disso, todos os tipos de página suportam agora o [filtro "ID real do utilizador com sessão iniciada"]({{< relref "help/base-editor/ansichten/was-ist-die-id-des-users-und-warum-kann-man-danach-filtern" >}}). Um dos focos do trabalho de desenvolvimento foi a página individual, cujo tratamento melhorámos significativamente. Também corrigimos erros nos diagramas. Os outros tipos de páginas não foram descurados. O suporte de colunas foi optimizado para as páginas de formulário Web, Kanban e Linha de tempo. Um destaque do Universal App Builder no SeaTable 4.0 é o novo tipo de página "Query", que integra a funcionalidade da [aplicação de consulta de dados]({{< relref "help/app-builder/app-verwaltung/datenabfrage-app" >}}) na Universal App.

![A aplicação universal](SeaTable_Universal-App.png)

Nas versões 4.1 e 4.2, serão acrescentadas outras funções que já estão estabelecidas nas bases. Estas incluem, por exemplo, a formatação condicional e a altura variável da linha. Nessa altura, a fase beta do Universal App Builder também terminará.

## E muito mais

As pequenas conquistas do SeaTable também tornam a vida mais agradável: as pastas na página inicial abrem agora numa janela separada, dando-lhe uma melhor visão geral das bases aí organizadas.

![Nova vista de pastas na página inicial](ordner-auf-der-startseite-release-notes.gif)

Bloquear uma linha - com uma regra de automatização ou manualmente através do menu de contexto da linha, o que já é possível para os utilizadores empresariais há algum tempo. Agora, a [coluna de botões]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}}) também tem "Bloquear linha" como uma nova ação. Utilize-a em combinação com as outras sete acções para concluir processos complexos com um simples clique do rato. Além disso, adicionámos valores de data dinâmicos à ação "Editar linha" e melhorámos a apresentação das opções de seleção.

Se clicar na célula de uma [coluna de ligação]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}), abre-se uma caixa de diálogo alargada do SeaTable 4.0: Pode ligar entradas existentes ou - o que é novo - adicionar uma linha. Isto permite-lhe criar uma nova linha na tabela ligada e uma entrada ligada na tabela aberta ao mesmo tempo, o que lhe poupa algum esforço: Anteriormente, tinha de mudar para a tabela ligada primeiro para adicionar uma nova linha, que podia depois ligar na outra tabela. Nas definições da coluna de ligação, pode também especificar que apenas podem ser criadas e ligadas novas entradas, seleccionando a opção para não mostrar o botão "Ligar entradas existentes".

Com uma subscrição Enterprise, pode utilizar o logótipo da sua própria empresa na página inicial em vez do logótipo SeaTable para ancorar o seu design empresarial. Se valoriza tanto a estética como o desempenho, vai adorar o seguinte: Simplificámos e acelerámos a criação de PDFs no [plug-in Design de páginas]({{< relref "help/base-editor/plugins/anleitung-zum-seitendesign-plugin" >}}), para que não tenha de perder tempo à espera.

## Novo limite

No registo da base, o SeaTable guarda as alterações que você e os membros da sua equipa fazem numa base. Até agora, era possível voltar ao passado e ver o histórico sem limite. Com o SeaTable 4.0, estamos a introduzir um limite de 1.000 entradas no registo da base. A documentação das alterações efectuadas ainda mais atrás no tempo será eliminada e, normalmente, já não é necessária. Pode encontrar informações adicionais sobre o histórico no SeaTable [aqui]({{< relref "help/base-editor/historie-und-versionen/historie-und-logs" >}}).

## Ajustamento de preços

Desde a versão 1.0, temos vindo a expandir a funcionalidade do SeaTable passo a passo. Fizemos também investimentos significativos em integrações mais simples e mais poderosas, melhorámos a documentação e aumentámos a segurança. Juntamente com a dinâmica de preços geralmente elevada, este facto exige um ajustamento dos nossos preços para as [licenças SeaTable Server]({{< relref "pages/product/seatable-server" >}}).

| Número de utilizadores | Preço até à data | Preço novo | Alterar   |
| ---------------------- | ---------------- | ---------- | --------- |
| 3                      | 0 €              | 0 €        | \--       |
| 10                     | 400 €            | 500 €      | \+ 25,0 % |
| 25                     | 1.500 €          | 1.250 €    | \- 16,7 % |
| 50                     | 3.500 €          | 4.500 €    | \+ 28,6 % |

Para os novos clientes, os novos preços das licenças aplicar-se-ão a partir de 1 de agosto de 2023. Os clientes actuais do SeaTable Server continuarão a receber extensões de licenças aos preços antigos até 31 de dezembro de 2023.

**O ajustamento de preços aplica-se explicitamente apenas aos auto-hosters. Os preços para o SeaTable Cloud não são alterados.**
