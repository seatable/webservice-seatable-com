---
title: 'SeaTable 2.7: Formatação celular condicional, fixação flexível da coluna e valor prático da data por defeito - SeaTable'
description: 'Controle melhor sua planilha: destaque valores com regras, calcule rankings, congele várias colunas e defina datas padrão. Novidade: proteção por senha para bases, reforço em buscas, restauração de links, gerenciamento fácil de 2FA e recursos avançados de personalização na edição de dados.'
date: 2022-02-02
lastmod: '2022-02-03'
author: 'rdb'
url: '/pt/seatable-release-2-7'
color: '#c29eca'
categories:
    - 'product-features'
seo:
    title: 'SeaTable 2.7: Formatação condicional intuitiva'
    description: 'Formatação de células, congelamento de colunas, datas padrão e bases protegidas fortalecem o SeaTable na versão 2.7.'
---

Esta manhã, o [SeaTable Cloud](https://cloud.seatable.io) foi actualizado para a versão 2.7. Isto significa que todos os utilizadores do Cloud podem agora também desfrutar das novas funções e melhorias da nova versão, que já está disponível para download para auto-gerentes em Docker Hub por alguns dias. O editor de tabela beneficiou mais com a mudança de versão: a formatação de célula condicional, a nova operação de processamento de dados "Calcular classificação", a fixação de coluna alargada e a função de valor por defeito para colunas de data oferecem muitas novas funcionalidades. Fora do editor de mesa, as bases protegidas por palavra-passe são uma melhoria importante. Todas as mudanças podem ser encontradas - como sempre - no [SeaTable changelog]({{< relref "pages/changelog" >}}).

## Formatação condicional para colunas

Qualquer pessoa que trabalha regularmente com o [Excel]({{< relref "pages/landing-pages/alternatives/excel-alternative" >}}) conhece a função de formatação condicional. Com a versão 2.7, esta função está agora também disponível em SeaTable. Com formatação condicional, formata ou colora células em função do seu valor (ou da ausência desse valor) e pode assim realizar a estruturação e análise dos dados visuais.

Para todas as colunas, o SeaTable oferece uma formatação condicional baseada em regras. Uma regra é a descrição de um conteúdo hipotético de uma célula (por exemplo, valor > 50 ou data após 31.12.2021) e uma instrução de formatação. Se a regra for cumprida, a célula é formatada de acordo com a instrução. Regras escolhidas com inteligência podem, entre outras coisas, tornar aberrantes os valores estatísticos ou valores pouco usuais facilmente reconhecíveis. É claro que também pode definir várias regras por coluna para mapear requisitos exigentes.

![Formatação condicional de células com gradiente de cor e regras para valores numa coluna](Conditional_cell_formatting2.png)

Se uma coluna tiver valores de células numéricas, o SeaTable oferece formatação por valores para além da formatação baseada em regras. Esta formatação condicional colore as células com um gradiente de cor. Os valores grandes são coloridos com a extremidade superior do gradiente, os valores pequenos com a extremidade inferior. Isto torna a magnitude de um valor celular clara num relance.

## Sequência de valores

Se quiser não só mostrar a ordem de grandeza dos valores das células numa coluna, mas também precisar da classificação dos valores, então a nova operação de processamento de dados Calcular a classificação é exactamente o que precisa! Calcula a classificação e escreve o resultado numa coluna separada. O maior valor recebe a classificação 1. Se dois ou mais valores de células tiverem o mesmo valor, então todas as células recebem a mesma classificação e uma ou mais posições de classificação subsequentes são ignoradas. A operação funciona para colunas com conteúdos numéricos, mas também para os tipos de colunas data, duração e classificação.

## Fixação de colunas

Em tabelas com muitas colunas, há frequentemente o problema de as primeiras colunas desaparecerem do visor quando se desloca para a direita. Até agora, a primeira coluna podia ser fixada e assim exposta permanentemente mesmo em grandes mesas. Esta função mostra um lado mais flexível no novo lançamento: a partir da versão 2.7, podem ser fixadas colunas adicionais do lado esquerdo. Desta forma, mesmo quando navega em grandes mesas, sabe em que entrada se encontra.

![Vista de tabela com várias colunas fixas à esquerda e restantes colunas deslocáveis](Freeze-columns.png)

Para fixar várias colunas, basta usar o rato: mover o ponteiro do rato para a linha vertical que separa a numeração das linhas da primeira coluna. Agora arraste o rato para a direita para definir o número de colunas fixas. Se quiser remover a fixação da coluna, mover o ponteiro do rato para a moldura entre a última coluna fixa e a coluna seguinte e arrastar a linha toda para a esquerda.

## Valores por omissão para a coluna de datas

![Definições de coluna de data com seleção de data predefinida estática ou dinâmica](Default_value_date_column.png)

Repetidamente solicitado, agora cumprido: Após o texto, número e colunas de selecção única, SeaTable 2.7 também dá à coluna de datas uma função de valor padrão. Com ele adiciona-se automaticamente um valor de data estático ou dinâmico às novas entradas.

A data de lançamento do SeaTable 2.7, 2 de fevereiro de 2022, é um exemplo de um valor de data estático. Os valores de data dinâmicos estabelecem uma referência relativa e mudam ao longo do tempo. Para além da data atual ("Today"), x dias antes ou depois da data atual é também um valor de data dinâmico. Ambos podem agora ser mapeados na coluna de data com a função de valor standard. Em combinação com as funções de data da coluna de fórmulas, praticamente todos os valores de data podem ser gerados automaticamente para novas entradas, que por sua vez podem ser utilizadas para automatizações.

## Bases protegidas por palavra-passe

Para bases com dados confidenciais, muitos clientes querem uma protecção de acesso alargada. O SeaTable 2.7 oferece agora tal protecção com a protecção opcional por palavra-passe para bases. Só depois de introduzir a palavra-passe é que a base será acedida e os dados apresentados. A protecção por senha pode ser criada e removida pelos proprietários para as suas próprias bases e pelos administradores do grupo para as bases do grupo.

As bases protegidas por palavra-chave podem ser partilhadas com outros utilizadores. É claro que também devem introduzir a palavra-passe ao chamar a base. O mesmo se aplica quando se copia uma base protegida por palavra-passe. A protecção adicional de acesso não vem ao preço de uma flexibilidade reduzida.

## ... e muito mais

Como a maioria das novas versões, o Release 2.7 contém mais uma vez mais características que vale a pena mencionar do que as Notas de Lançamento podem digerir a um comprimento aceitável. Por conseguinte, aqui fica uma visão geral de outras inovações:

Ao ligar entradas, o assistente de ligação no SeaTable 2.7 oferece uma melhor função de pesquisa. Ao introduzir vários termos de pesquisa separados por espaços, o SeaTable faz pesquisas em todas as colunas da tabela ligada. Especificamente: Se procura uma determinada entrada numa determinada data, basta introduzir a data e, separados por espaços, outra propriedade da entrada que procura. O assistente então apenas exibe as entradas correspondentes e é poupado a muito trabalho de pesquisa manual. Até agora, o SeaTable procurava a entrada como um todo numa coluna.

Os formulários web podem agora ser embelezados com uma imagem de capa ou um esquema de cores. Juntamente com um logótipo inserido, podem ser construídas formas atractivas e individuais. (Esta função é reservada a subscritores empresariais).

Os administradores de equipa podem agora impor a autenticação de 2 factores para os membros da sua equipa e também desactivá-la individualmente. O administrador da equipa pode assim reagir individualmente a requisitos de segurança acrescidos e mais facilmente desarmar situações em que os utilizadores tenham perdido o seu segundo factor.

Até agora, as ligações das filas eliminadas e depois restauradas continuaram perdidas. Com a versão 2.7, são também criadas novamente ligações quando uma fila é restaurada.

A função de arquivo introduzida com a [versão 2.3]({{< relref "posts/seatable-releases/seatable-release-2-3" >}}) deu mais passos para uma utilização produtiva: as entradas podem agora ser eliminadas do arquivo e as entradas podem também ser editadas. (As ligações, contudo, ainda não podem ser criadas ou alteradas).
