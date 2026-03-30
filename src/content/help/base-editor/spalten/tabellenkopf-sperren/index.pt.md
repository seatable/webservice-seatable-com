---
title: 'Bloquear o cabeçalho da tabela'
date: 2023-03-03
lastmod: '2023-03-03'
categories:
    - 'arbeiten-mit-spalten'
author: 'nsc2'
url: '/pt/ajuda/travar-cabecalho-seatable'
aliases:
    - '/pt/ajuda/tabellenkopf-sperren'
seo:
    title: 'Trave o cabeçalho da tabela no SeaTable com facilidade'
    description: 'Evite alterações indesejadas nas colunas travando o cabeçalho da tabela e mantenha sua estrutura intacta no SeaTable.'
---

Se tiver a autorização necessária, pode **bloquear** o **cabeçalho da tabela em** cada tabela para impedir a adição, deslocação e edição de colunas na tabela. A grande vantagem é que pode bloquear **todas as colunas ao mesmo tempo** com um clique.

Isto pode ser útil, por exemplo, se trabalhar em conjunto com outros utilizadores numa tabela e não quiser que sejam feitas alterações à **estrutura da coluna**.

{{< warning  headline="Dica" >}}

Se quiser apenas bloquear **colunas individuais da** sua tabela para edição, pode fazê-lo através das [permissões das colunas]({{< relref "help/base-editor/spalten/spaltenberechtigungen-festlegen" >}}).

{{< /warning >}}

## Bloquear o cabeçalho da tabela

1. Abra a **tabela** em que pretende bloquear o cabeçalho da tabela.
2. Clicar no **cadeado preto aberto** no cabeçalho da tabela.

![Bloqueio do cabeçalho da tabela](images/lock-the-table-head.jpg)

4. Se o cadeado for então exibido a **vermelho**, o cabeçalho da tabela foi bloqueado com sucesso.

![Símbolo de bloqueio para cabeçalho de tabela bloqueado com sucesso](images/locked-table-head.jpg)

{{< warning  headline="Nota importante" >}}

Não confundir esta função com a função **Ícone de bloqueio nas opções de visualização**. Pode utilizá-lo para alterar as definições de um [Vista da tabela de bloqueio]({{< relref "help/base-editor/ansichten/ansicht-sperren" >}}).

{{< /warning >}}

![Ícone de bloqueio para bloquear as vistas nas opções de vista](images/Bildschirmfoto-2022-10-28-um-15.22.16.png)

## Efeitos do confinamento

Uma vez que o cabeçalho da tabela tenha sido bloqueado, já não é possível **adicionar colunas** à tabela correspondente até que o bloqueio seja novamente cancelado. O **\+-símbolo** para [adicionar uma coluna]({{< relref "help/base-editor/spalten/hinzufuegen-einer-spalte" >}}) é portanto **não** apresentado em tabelas com um cabeçalho de tabela bloqueado.

![Ícone em falta para adicionar colunas em tabelas com cabeçalho de tabela bloqueado](images/tables-with-locked-table-head.png)

Também já não é possível mover colunas, o que significa que a **estrutura da coluna** permanece sempre a mesma até o bloqueio terminar.

Além disso, depois de um cabeçalho de tabela ter sido bloqueado, já não é possível efetuar várias **configurações** nas colunas da tabela. Isso afeta as seguintes opções de coluna:

- Mudar o nome da coluna
- Adicionar descrição da coluna
- Personalizar o tipo de coluna
- Duplicar coluna
- Inserir esquerda (coluna)
- Inserir à direita (coluna)
- Eliminar coluna

As opções relevantes estão **acinzentadas** nas definições de coluna quando o cabeçalho da tabela está bloqueado.

![Definições de coluna que estão a cinzento e, por isso, não estão disponíveis quando o cabeçalho da tabela está bloqueado](images/ausgegraute-spalten-einstellungen.png)

No entanto, todas as outras **configurações de coluna** não são afectadas pelo bloqueio e ainda podem ser editadas mesmo que o cabeçalho da tabela esteja bloqueado. Estas incluem as seguintes opções:

- Definições de formato
- Editar autorizações de coluna
- Formatar células de coluna
- Ocultar
- Ordenar por ordem ascendente
- Ordenar por ordem decrescente

## Desbloquear

Para desbloquear um cabeçalho de tabela, basta clicar de novo no **trava (vermelho)** do cabeçalho da tabela.

![Desbloquear um cabeçalho de tabela](images/unlock-the-table-head.jpg)

Se o desbloqueio for bem sucedido, é novamente apresentado um **trinco preto e aberto**. Pode então adicionar colunas à tabela novamente e editar as colunas existentes.

Tenha em atenção que o cabeçalho bloqueado das tabelas que pertencem a um grupo só pode ser desbloqueado novamente pelos **proprietários** e **administradores** do grupo. Os membros simples do grupo **não** estão autorizados a desbloquear e verão a seguinte mensagem quando clicarem no símbolo de bloqueio:

![Nota para membros de grupos simples que não estão autorizados a desbloquear um cabeçalho de tabela](images/no-permission-to-unlock-head-of-a-table.png)
