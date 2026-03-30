---
title: 'Como funcionam os Conjuntos de Dados Partilhados'
date: 2022-12-15
lastmod: '2024-06-12'
categories:
    - 'gemeinsame-datensaetze'
author: 'nsc2'
url: '/pt/ajuda/funcionamento-dados-compartilhados-seatable'
aliases:
    - '/pt/ajuda/funktionsweise-von-gemeinsamen-datensaetzen'
seo:
    title: 'Funcionamento dos conjuntos de dados compartilhados SeaTable'
    description: 'Compartilhe, sincronize e utilize dados em vários times. Entenda as vantagens e modos de operação dos conjuntos de dados compartilhados.'
star: true
weight: 1
---

Os conjuntos de dados partilhados permitem partilhar uma visão de tabela pré-definida com outros grupos e utilizadores para que possam aceder a dados específicos numa variedade de contextos e departamentos. Os conjuntos de dados partilhados são uma característica poderosa e extremamente útil no SeaTable, uma vez que podem facilitar o fluxo de trabalho na sua equipa.

## Vantagens de um conjunto de dados comum

Em comparação com uma partilha de [vistas]({{< relref "help/startseite/freigaben/freigabe-einer-ansicht-an-ein-teammitglied" >}}), um conjunto de dados partilhados oferece outras possibilidades, que são ilustradas pelo exemplo seguinte:

- Uma lista de pessoal que seja relevante para vários grupos de utilizadores (por exemplo, RH, contabilidade e comunicação interna) pode ser disponibilizada aos membros da sua equipa através de conjuntos de dados partilhados como **modelo para novas tabelas**.
- Depois dos membros da sua equipa terem importado o conjunto de dados comuns para uma base, podem adicionar colunas à tabela como desejarem e adaptá-la aos seus casos específicos de utilização (por exemplo, planeamento de férias, folha de pagamentos, lista de distribuição para boletins informativos internos).
- As tabelas de acesso a um conjunto de dados comum podem ser **sincronizadas** em qualquer altura, ou seja, comparadas com a última versão do conjunto de dados (por exemplo, quando novos empregados entram ou saem).
- Existe uma relação de cima para baixo: as alterações ao conjunto de dados comuns são transferidas para as tabelas dependentes durante a sincronização. No entanto, as alterações nestas tabelas **não** têm **qualquer** efeito sobre o conjunto de dados subjacentes.

{{< warning headline="Registros Compartilhados e Big Data Backend" text="No momento, não é possível usar registros compartilhados em uma visualização Big Data." />}}

Na síntese seguinte encontrará também os links para os vários artigos de ajuda na secção de Conjuntos de Dados Comuns.

## Criação de um conjunto de dados comum

Publicar primeiro qualquer vista de tabela juntamente com o seu filtro específico e condições de classificação como um conjunto de dados comum.

[Saiba mais sobre a criação de um registo partilhado.]({{< relref "help/startseite/gemeinsame-datensaetze/anlegen-eines-gemeinsamen-datensatzes" >}})

## Gestão de um conjunto de dados partilhados

Deseja alterar o nome de um registo de dados partilhado ou saber que bases estão ligadas a esse registo de dados?

[Saiba mais sobre a gestão de um conjunto de dados partilhados.]({{< relref "help/startseite/gemeinsame-datensaetze/verwaltung-eines-gemeinsamen-datensatzes" >}})

## Partilhar um registo comum com outro grupo

Para poder utilizar um registo partilhado em outros grupos, pode partilhá-lo com qualquer grupo.

[Saiba mais sobre a partilha de um registo comum.]({{< relref "help/startseite/gemeinsame-datensaetze/freigabe-eines-gemeinsamen-datensatzes-an-eine-andere-gruppe" >}})

## Sincronização de um conjunto de dados comum

Pode sincronizar cada tabela que tenha criado com um conjunto de dados comum. SeaTable compara os dados da tabela com os dados do conjunto de dados partilhados. Estes são sobrescritos se você ou os membros do seu grupo tiverem feito alterações ao conjunto de dados partilhados desde a última sincronização.

[Saiba mais sobre a sincronização de um conjunto de dados partilhados.]({{< relref "help/startseite/gemeinsame-datensaetze/synchronisation-eines-gemeinsamen-datensatzes" >}})

## Criar uma nova tabela com um registo comum

Se você ou os membros da sua equipa quiserem utilizar um conjunto de dados comum, podem importá-lo para uma base. Para o fazer, criar uma nova tabela com o conjunto de dados partilhados.

[Saiba mais sobre a criação de uma nova tabela com um registo comum.]({{< relref "help/startseite/gemeinsame-datensaetze/mit-einem-gemeinsamen-datensatz-eine-neue-tabelle-anlegen" >}})

## Adicionar colunas a uma tabela criada com um registo comum

Depois de ter importado um conjunto de dados comum como uma nova tabela para uma base desejada, pode alargar a tabela com as suas próprias colunas como desejar.

[Aprenda a adicionar colunas a uma tabela criada com um conjunto de dados comum.]({{< relref "help/startseite/gemeinsame-datensaetze/eine-mit-einem-gemeinsamen-datensatz-erstellte-tabelle-um-spalten-erweitern" >}})

## Reimportação de registos de dados partilhados

Se copiar bases nas quais estão integrados registos de dados partilhados ou se as restaurar a partir de instantâneos, a ligação aos registos de dados partilhados perde-se. Embora os dados estejam então disponíveis numa tabela normal, já não podem ser sincronizados.

[Aqui pode descobrir como reimportar registos de dados partilhados para tabelas existentes.]({{< relref "help/startseite/gemeinsame-datensaetze/reimport-von-gemeinsamen-datensaetzen" >}})

## Eliminação de um registo comum

Os conjuntos de dados partilhados também podem, evidentemente, ser apagados. No entanto, é favor notar os efeitos que uma eliminação tem tanto sobre os dados do conjunto de dados partilhados como sobre as tabelas que você e os membros do seu grupo criaram com o conjunto de dados partilhados.

[Saiba mais sobre como apagar um registo partilhado.]({{< relref "help/startseite/gemeinsame-datensaetze/loeschen-eines-gemeinsamen-datensatzes" >}})

### Artigos mais úteis na secção de Conjuntos de Dados Comuns

- [Porque é que os registos partilhados só funcionam em grupos?]({{< relref "help/startseite/gemeinsame-datensaetze/warum-funktionieren-gemeinsame-datensaetze-nur-in-gruppen" >}})
