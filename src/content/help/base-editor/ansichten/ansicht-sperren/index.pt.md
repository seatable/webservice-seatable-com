---
title: 'Bloquear vistas'
date: 2022-10-26
lastmod: '2025-12-05'
categories:
    - 'ansichtsoptionen'
author: 'kgr'
url: '/pt/ajuda/bloquear-visualizacao-seatable'
aliases:
    - '/pt/ajuda/ansicht-sperren'
seo:
    title: 'Bloquear vistas no SeaTable: restrinja edições e preserve configurações'
    description: 'Veja como bloquear uma vista no SeaTable para evitar alterações por outros membros da equipe, proteger filtros, grupos e ordenações da planilha.'
weight: 9
---

Pode **bloquear vistas** de uma tabela em SeaTable. Esta característica é particularmente útil quando se trabalha em grupo. Aqui, **os utilizadores com direitos de proprietário ou administrador** têm a opção de bloquear uma vista para todos os outros membros do grupo que não possuam um destes dois níveis de permissão. Isto significa que estes membros já não podem fazer alterações às opções de visualização.

Entre outras coisas, os **filtros, classificação e agrupamento** de uma vista são afectados pela fechadura. A configuração seleccionada permanece em vigor até a fechadura ser removida por um utilizador com direitos de proprietário ou administrador.

Note-se, no entanto, que o bloqueio de uma vista **não** tem geralmente qualquer influência no **processamento de dados**. Os dados numa vista bloqueada ainda podem ser **editados** por todos os membros do grupo.

## Bloqueie uma vista

1. Abra a **vista** que pretende bloquear.
2. Clique no **ícone de bloqueio** nas opções de visualização acima da tabela.
3. O **bloqueio** da vista correspondente está agora **ativo** e pode ser cancelado clicando novamente no **símbolo de bloqueio**.

![Bloquear vista](images/lock-view.png)

## Impacto

Quando um utilizador com direitos de proprietário ou administrador bloqueia uma vista, congela a configuração actual da vista e impede a **definição de alterações** pelos membros do grupo sem esses direitos.

![opções de visualização bloqueadas](images/locked-view.png)

Na vista bloqueada, as seguintes configurações já **não** podem ser alteradas:

- Filtros
- Classificações
- Agrupamentos
- Ocultar colunas
- Realce das cores
- Ajustar a altura da fila

{{< warning type="warning" headline="Nota importante" >}} 
Note que o bloqueio de uma vista só se aplica à configuração da vista – vistas bloqueadas **não** impedem outros membros do grupo de ver e editar o conteúdo da vista. Se outros membros do grupo podem ou não editar uma opinião depende do seu estatuto de autorização dentro do grupo. Para mais informações, ver o artigo de síntese [Membros do grupo e respectivas permissões]({{< relref "help/startseite/gruppen/gruppenmitglieder-und-ihre-berechtigungen" >}}).

{{< /warning >}}

## Exemplos de aplicação

Em princípio, faz sentido recorrer ao bloqueio de uma vista se alterações de curto prazo e imprevistas na configuração de uma vista puderem afectar o fluxo de trabalho da sua equipa.

### Exemplos concretos onde o bloqueio de uma vista pode ser útil:

- Criou uma visão filtrada que necessita para uma apresentação a um dos seus clientes, e alterar as condições do filtro a curto prazo revelaria dados sensíveis.
- Criou uma vista para a nova campanha de recrutamento da sua empresa que pode ser acedida por vários potenciais candidatos. Se o aspeto da vista mudar agora, pode dar origem a mal-entendidos.
- Criou cuidadosamente uma nova vista de calendário. Se alterar a configuração desta vista, poderá transferir dados não desejados para o calendário.
