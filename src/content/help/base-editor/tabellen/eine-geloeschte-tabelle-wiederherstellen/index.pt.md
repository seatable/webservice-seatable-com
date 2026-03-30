---
title: 'Restaurar uma tabela eliminada'
date: 2022-11-17
lastmod: '2023-01-12'
categories:
    - 'arbeiten-in-tabellen'
author: 'nsc2'
url: '/pt/ajuda/restaurar-tabela-excluida-seatable'
aliases:
    - '/pt/ajuda/eine-geloeschte-tabelle-wiederherstellen'
seo:
    title: 'Como restaurar uma tabela apagada no SeaTable'
    description: 'No SeaTable, recupere facilmente tabelas, colunas e linhas excluídas pelo recurso da lixeira. Erros são reversíveis rapidamente.'

---

No SeaTable, não tem de se preocupar em perder os seus dados. Mesmo tabelas eliminadas acidentalmente - e mesmo colunas e linhas individuais - podem ser facilmente restauradas posteriormente através do **caixote da reciclagem** nas **opções de base**.

## Restaurar uma tabela eliminada

![Restaurar tabelas](images/Wiederherstellung-von-Tabellen.png)

2. Clique em **Versões** no canto superior direito das opções da Base.
3. Abrir o **caixote do lixo da reciclagem**.
4. Verá agora todas as **tabelas**, **filas** e **colunas** que foram eliminadas dentro desta base no passado.
5. Seleccione a **tabela** desejada que deseja restaurar e clique em **Restaurar à** direita do tempo de eliminação.
6. A tabela seleccionada é então automaticamente adicionada de volta à sua **base**.

## Conteúdo da tabela que é restaurada

Quando se recupera uma tabela do caixote da reciclagem, esta é restaurada exactamente como estava quando foi apagada. Isto inclui os seguintes componentes:

- Dados da tabela
- [Vistas de tabela]({{< relref "help/base-editor/ansichten" >}})
- [Comentários]({{< relref "help/base-editor/zeilen/zeilen-kommentieren" >}})
- [Formulários Web]({{< relref "help/base-editor/webformulare" >}})
- Automatizações
- Representações e avaliações nos plug-ins do SeaTable

{{< warning headline="Os links para a tabela eliminada devem ser restaurados separadamente" text="Um dos pontos fortes do SeaTable é a sua capacidade de ligar as tabelas. Se se eliminar uma tabela, todas as colunas de ligação que tinham esta tabela eliminada como alvo desaparecem. Se agora restaurar a tabela original, as colunas de ligação não são automaticamente recriadas, mas estas também podem ser restauradas a partir do lixo. Assim, nenhuma informação é perdida." />}}

![Restaurando uma Coluna de Ligação Eliminada](images/restore-deleted-link-column.png)

## Artigos mais úteis em torno da recuperação de dados

SeaTable oferece várias opções para a restauração de conteúdos apagados. Não só os quadros apagados podem ser recuperados, mas também as suas últimas alterações, versões antigas ou bases inteiras. O [artigo de síntese sobre recuperação de dados no SeaTable]({{< relref "help/base-editor/historie-und-versionen/moeglichkeiten-der-datenwiederherstellung" >}}) irá certamente ajudá-lo.
