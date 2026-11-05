---
title: 'Webhook para várias alterações simultâneas'
date: 2024-02-13
lastmod: '2026-11-05'
categories:
    - 'webhooks'
author: 'cdb'
url: '/pt/ajuda/webhook-alteracoes-simultaneas'
aliases:
    - '/pt/ajuda/webhook-bei-mehreren-gleichzeitigen-aenderungen'
seo:
    title: 'Webhooks em alterações simultâneas no SeaTable'
    description: 'Veja como o SeaTable agrupa webhooks em alterações simultâneas, o que significa o parâmetro row_count e como consultar todas as linhas alteradas.'

---

O SeaTable normalmente envia um webhook para cada alteração numa linha. No entanto, se uma operação alterar várias linhas ao mesmo tempo, é gerado apenas um webhook com o parâmetro adicional _row\_count_. Isto também se aplica à API: uma chamada à API gera um webhook, independentemente de alterar uma ou várias linhas.

No editor Web, isto acontece, por exemplo, se copiar um valor para a área de transferência com {{< key "CTRL" >}}+{{< key "C" >}} e depois o colar em várias outras linhas com {{< key "CTRL" >}}+{{< key "V" >}}. Este processo gera apenas um webhook. O gráfico seguinte mostra o webhook correspondente.

![Várias alterações simultâneas através de webhook.](images/webhook_multiple_changes.jpg)

## O que o webhook contém

O parâmetro _row\_count_ indica o número de linhas afetadas. Os restantes dados, como _row\_id_, _row\_name_ e _row\_data_, referem-se apenas a uma linha, normalmente a primeira da operação. _op\_type_ também permanece no singular, ou seja, _insert\_row_, _modify\_row_ ou _delete\_row_.

Atualmente, não existe a opção de criar um webhook separado para cada linha. O webhook também não contém uma lista de todas as linhas afetadas.

## Consultar as linhas alteradas após um webhook

{{< warning headline="Os webhooks não se destinam à sincronização" text="Se pretender sincronizar dados com outro sistema, o webhook deve ser apenas o acionador da sincronização. Não contém todas as alterações e a sua entrega não é garantida." />}}

Após o webhook, consulte as linhas alteradas através da [interface SQL](https://developer.seatable.com/sql/select/):

```sql
SELECT * FROM Table1 WHERE _mtime >= '2026-11-05T18:30:00+01:00' ORDER BY _mtime, _id LIMIT 1000 OFFSET 0
```

Tenha em conta os seguintes pontos:

- **Comparar com `>=`:** A coluna _\_mtime_ tem normalmente uma precisão de apenas um segundo. Com `>`, perderia as alterações efetuadas no mesmo segundo da sua última sincronização. Como `>=` devolve novamente algumas linhas, o seu sistema tem de conseguir processar duplicados.
- **Indicar o fuso horário:** Uma hora sem fuso horário não é interpretada como UTC. Por isso, indique sempre o desvio, por exemplo, `+01:00`.
- **Obter os resultados por páginas:** Sem `LIMIT`, uma consulta SQL devolve no máximo 100 linhas, e o máximo por consulta é de 10.000 linhas. Aumente `OFFSET` até que uma consulta devolva menos linhas do que o `LIMIT` definido.
- **Linhas eliminadas e ligações:** As linhas eliminadas não aparecem nesta consulta, e adicionar uma ligação não altera _\_mtime_. Por isso, compare de vez em quando os ID das linhas e as colunas de ligação em ambos os sistemas.

## Sincronizar também regularmente

Os webhooks não garantem uma entrega completa: as entregas falhadas não são repetidas, um webhook pode ser [desativado após erros]({{< relref "help/integrationen/webhooks/deaktivierung-eines-webhooks-bei-fehlern" >}}) e, em casos isolados, pode nem sequer ser enviado. Por isso, execute também a sincronização segundo um calendário fixo e verifique regularmente se o webhook continua ativo.
