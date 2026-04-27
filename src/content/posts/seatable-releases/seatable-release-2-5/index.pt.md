---
title: 'SeaTable 2.5: Arquivo optimizado, processamento de dados e automatizações - SeaTable'
description: 'Arquivo suporta fórmulas e links; processamento de dados mais robusto; Python ativado via automation, rating com ícones/sumário automático, importação/exportação Excel melhorada, galeria adaptável, countitems e integração com 4 ferramentas de automação tornam seu workflow muito mais eficaz.'
date: 2021-11-16
lastmod: '2023-07-11'
author: 'rdb'
url: '/pt/seatable-release-2-5'
color: '#e7cae0'
categories:
    - 'product-features'
seo:
    title: 'SeaTable 2.5: arquivo, automação, colunas flex'
    description: 'Arquivo com fórmulas/vínculos, flujos de dados mais versáteis, automações fortalecidas, rating flexível: SeaTable 2.5 é completo!'
---

A SeaTable 2.5 está aqui! A nova imagem Docker foi disponibilizada em Docker Hub no final da semana passada e esta manhã o SeaTable Cloud foi actualizado para a versão mais recente. O novo lançamento torna muitas das características do SeaTable ainda melhores! A função de arquivo com a sua gama crescente de funções é recomendada para um número crescente de casos de utilização, as funções de processamento de dados disponíveis tornam-se mais flexíveis e as automatizações integradas, bem como a coluna de classificação oferecem novas opções. Também vale a pena mencionar: colunas do tipo link e fórmula para links são agora totalmente suportados em vistas externas. Continue a ler para saber mais sobre estas novas características. A lista completa de alterações pode ser encontrada - como sempre - no [SeaTable Changelog]({{< relref "pages/changelog" >}}).

## Função de arquivo revista

Desde a introdução do arquivo como função beta na [versão 2.3,]({{< relref "posts/seatable-releases/seatable-release-2-3" >}}) os nossos criadores têm trabalhado sem parar para que a função de arquivo fique pronta para uma utilização produtiva. Com a versão 2.5, ainda não atingimos este objectivo, mas a nova versão representa um enorme passo nessa direcção.

A função de arquivo suporta agora todas as 24 colunas, incluindo os três tipos de coluna fórmula, link e fórmula para link. A falta de acesso por escrito aos dados do arquivo continua a ser uma limitação no SeaTable 2.5, mas estas três colunas são casos especiais: Os valores nas duas colunas de fórmula são calculados dinamicamente, dependendo da especificação da fórmula. Se uma fórmula for alterada, então os valores nas filas arquivadas são recalculados. Se o utilizador alterar a coluna de consulta numa fórmula para ligações, os dados arquivados reflectem esta alteração. O mesmo se aplica à coluna de ligação. Uma alteração na coluna de visualização ocorre igualmente em todo o conjunto de dados, incluindo o arquivo. Desta forma, os dados arquivados permanecem comparáveis com os dados não arquivados.

![A visão revista do arquivo do SeaTable](archive-view.jpg)

SeaTable 2.5 também acrescenta uma função de impressão para vistas de arquivo e agora também permite a ocultação de colunas individuais em tal vista. Uma função de pesquisa e uma função de exportação Excel já foram implementadas no [SeaTable 2.4]({{< relref "posts/seatable-releases/seatable-release-2-4" >}}).

## Operações optimizadas de processamento de dados

As operações de processamento de dados da SeaTable são frequentemente necessárias para a migração de aplicações Excel para a SeaTable. No SeaTable 2.5, duas operações foram melhoradas.

A operação Comparar e Ligar cria automaticamente ligações entre filas semelhantes em duas tabelas. Com ele, a conversão das tabelas Excel numa base de dados relacional é feita em pouco tempo. Novo no SeaTable 2.5 é o suporte de todos os tipos de colunas importantes (incl. colunas de selecção únicas) para a definição da regra de comparação. Além disso, a operação oferece agora também mais flexibilidade no caso de as tabelas já estarem ligadas duas vezes. Neste caso, o utilizador é solicitado a seleccionar as colunas nas quais as ligações devem ser adicionadas através de um menu drop-down.

A operação Calcular Valores Acumulados calcula totais entre linhas para colunas de dados numéricos - uma função padrão em Excel. A operação tem estado disponível desde a introdução da função de processamento de dados no [SeaTable 2.1,]({{< relref "posts/seatable-releases/seatable-release-2-1" >}}) mas foi agora adaptada com base no feedback do utilizador. Especificamente, o tratamento da primeira coluna foi criticado. Agora, após a revisão, a operação soma exclusivamente através da coluna de origem e escreve os resultados na coluna de resultados.

## Novas automatizações e gatilhos

> **O SeaTable suporta agora quatro plataformas de automatização de processos:**  
> A automatização tem sido um ponto fulcral nas últimas semanas e meses. Temos orgulho em anunciar que o SeaTable está agora disponível em quatro plataformas de integração: Além de [Zapier](https://zapier.com/apps/seatable/integrations), sobre o qual o SeaTable já está presente desde o início de 2021, podem agora ser construídos fluxos de trabalho sofisticados com [Integromat](https://www.make.com/en/integrations/seatable), [n8n](https://n8n.io/integrations/seatable/) e [Locoia](https://www.locoia.com/connector-integrations/).

Com toda a atenção dada às [integrações]({{< relref "pages/integrations" >}}) externas, não perdemos de vista as próprias automatizações do SeaTable. A inovação central é a ação " Run Python Script". Pode ser accionada pelos accionadores "Nova linha", "As entradas cumprem uma determinada condição após a alteração" e "Executar periodicamente". A execução automática de scripts Python para uma única linha ou para todo um conjunto de dados, utilizando um conjunto claro de regras, é quase uma superpotência!

![Os guiões Python podem agora ser iniciados através da automatização.](python-script-durch-automation-511x448.jpg)

A ação existente "Bloquear linha" recebe o novo evento de disparo "Executar periodicamente para linhas que satisfazem uma determinada condição". Em combinação com os outros dois accionadores "Nova linha" e "As entradas cumprem determinadas condições após a alteração", o utilizador tem agora um controlo ótimo sobre o bloqueio automático de linhas.

Por fim, os dois eventos agendados "Executar periodicamente" e "Executar periodicamente para linhas que satisfazem uma determinada condição" receberam uma opção de execução manual. Isto facilita o teste de automatizações com estes accionadores.

## Mais opções para a coluna de classificação

Todos nós gostamos de uma escolha alargada! A nova coluna de classificação satisfaz exatamente este desejo de "mais". No SeaTable, a coluna de classificação oferece agora quatro estilos. Para além da estrela como ícone padrão, agora também pode escolher o coração, o polegar para cima ou a bandeira como ícone. Além disso, o ícone já não tem de ser cor de laranja.

![A nova coluna de classificação no SeaTable 2.5](Bewertungsspalte.jpg)

A coluna de Classificação revista não se refere apenas à estética, mas também à conveniência. Tal como com outras colunas numéricas, o SeaTable calcula agora valores agregados para colunas de classificação no fundo da tabela - mínimo, máximo, médio e total. Em vistas agrupadas, SeaTable também calcula valores agregados para os grupos individuais.

Finalmente, a coluna de classificação foi optimizada para utilização em dispositivos móveis. Pode criá-los facilmente num telemóvel com a versão mais recente. No passado, o SeaTable recusou-se a fazer isto. Além disso, os ícones da coluna de classificação foram ligeiramente aumentados, tornando-os mais confortáveis de utilizar em pequenos ecrãs.

Outro desenvolvimento para a coluna de classificação não chegou, infelizmente, à versão 2.5. Por conseguinte, aqui está o anúncio: A partir do SeaTable 2.6, as colunas de classificação também poderão ter um valor por defeito.

## Outras melhorias

A nova função countitems conta os elementos nos tipos de coluna que podem conter valores múltiplos. Estes incluem os tipos de coluna ficheiro, imagem, pauta e seleção múltipla. É a contrapartida da função "countlinks" para elementos não ligados.

A função de exportação e importação do Excel foi revista em vários locais. Exportar colunas de fórmula agora funciona sem problemas com SeaTable 2.5, mesmo que as colunas utilizadas na fórmula estejam ocultas. Outra nova característica é que novos dados podem ser importados tanto de ficheiros CSV como XLSX e que novas tabelas podem ser criadas a partir de ficheiros XLSX. Os utilizadores que transferem dados do SeaTable para o Excel ficarão satisfeitos por saber que a rotina de exportação trata agora correctamente de múltiplos campos de selecção.

As definições do plugin da galeria foram alargadas com uma opção de definição. O botão "Mostrar nomes das colunas" pode ser utilizado para mostrar ou ocultar os títulos por cima dos valores das colunas. Mesmo que isto não seja necessário em muitos casos, evita a confusão nos casos em que as colunas do mesmo tipo estão diretamente por baixo umas das outras.
