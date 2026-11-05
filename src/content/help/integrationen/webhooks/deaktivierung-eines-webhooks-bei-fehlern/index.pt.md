---
title: 'Desactivação de um gancho em caso de erros'
date: 2023-02-28
lastmod: '2026-11-05'
categories:
    - 'webhooks'
author: 'cdb'
url: '/pt/ajuda/desativar-webhooks-erros'
aliases:
    - '/pt/ajuda/deaktivierung-eines-webhooks-bei-fehlern'
seo:
    title: 'Desativar webhooks em SeaTable após erros: instruções'
    description: 'Veja como o SeaTable desativa webhooks após erros HTTP e saiba como reativar ganchos inválidos para automação confiável.'

---

Se for criado um gancho para uma base SeaTable, SeaTable envia um _pedido POST_ para o URL alvo sempre que é feita uma alteração. Normalmente, o sistema receptor devolve uma mensagem de estado sob a forma de um [código de estado de três dígitos](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes), que o SeaTable então processa e desactiva o gancho da web, se necessário.

## Os códigos de status HTTP mais comuns

Existe toda uma gama de códigos de status, mas basta conhecer os feedbacks mais comuns:

- **200** - Bem sucedido
- **400** - Pedido incorreto
- **403** - Proibido
- **500 - 511** - Erros do servidor

O código de estatuto mais importante é de longe 200, o que indica que o pedido foi recebido e processado com sucesso. O SeaTable considera bem-sucedidos todos os códigos de estado de 200 a 299.

## SeaTable desactiva os ganchos da Web em caso de erros

Quando o SeaTable envia um webhook, espera uma resposta sob a forma de um código de estado HTTP. Em caso de erro, o webhook é definido como _inválido_ e a execução é interrompida. O momento em que isto acontece depende do tipo de erro:

| Erro                               | Exemplos                                                                        | Desativação                    |
| ---------------------------------- | ------------------------------------------------------------------------------- | ------------------------------ |
| **Resposta incorreta ou em falta** | Código de estado fora do intervalo 200 a 299, sem resposta em 30 segundos       | após cinco erros seguidos      |
| **Entrega impossível**             | Nome não resolúvel, ligação recusada, erro de certificado, URL alvo não público | imediatamente no primeiro erro |

Os redirecionamentos não são seguidos: um código de estado como 301 ou 302 conta como erro. Uma entrega bem-sucedida repõe o contador de erros.

![Gancho da rede inválido](images/invalid-webhook.png)

{{< warning headline="Apenas URL alvo públicos desde a versão 7.0.10" text="Desde a versão 7.0.10 do SeaTable, o URL alvo tem de apontar para um endereço público. Os webhooks para endereços internos não são entregues e são desativados imediatamente." />}}

## As entregas falhadas não são repetidas

O SeaTable não volta a enviar um webhook se a entrega falhar. As alterações efetuadas enquanto um webhook está desativado também não são entregues mais tarde. Se o seu sistema precisar de dados completos, deve por isso [sincronizar os dados regularmente]({{< relref "help/integrationen/webhooks/webhook-bei-mehreren-gleichzeitigen-aenderungen" >}}).

## Reativar um gancho inactivo na Internet

Um gancho inválido pode ser reactivado em qualquer altura. Mudar para a edição do gancho inválido clicando em {{< seatable-icon icon="dtable-icon-rename" color="grey" >}} e guardar o gancho novamente sem fazer quaisquer alterações. O gancho da rede ficará então imediatamente activo de novo.

Para evitar uma nova desativação, o sistema receptor deve processar os webhooks de forma fiável e devolver o código de estado 200 no prazo de 30 segundos.
