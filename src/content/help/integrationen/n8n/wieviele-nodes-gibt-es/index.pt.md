---
title: 'As razões para dois Community Nodes: SeaTable e SeaTable-Admin'
date: '2025-10-03'
seo:
    title: 'Nós SeaTable no n8n: diferença entre o nó de utilizador e o nó de administrador'
    description: 'SeaTable no n8n: use o nó de utilizador para operações de dados com token API e o nó admin para tarefas de gestão com direitos de administrador.'
categories:
    - 'n8n-integration'
url: '/pt/ajuda/porque-existem-dois-community-nodes'
---

No n8n existem dois Community Nodes SeaTable distintos, cada um desenvolvido para diferentes áreas de utilização, permitindo-lhe conceber os seus workflows de forma precisa e segura.

## 1. Nó SeaTable – Interação com os seus dados

O nó SeaTable é o padrão comprovado quando se trata de trabalhar com os dados nas suas bases SeaTable. Quer pretenda adicionar novos registos, atualizar os existentes ou eliminar entradas, este nó torna-o possível.

Está disponível tanto na versão Core como na versão Community no n8n. Mais detalhes neste [artigo]({{< relref "help/integrationen/n8n/n8n-community-vs-core" >}}).

Para utilizá-lo, precisa apenas de um **token API SeaTable** que lhe dá acesso aos dados da sua base.

## 2. Nó SeaAdmin – Controlo administrativo

Se pretende realizar tarefas administrativas no SeaTable, o nó SeaAdmin é a escolha perfeita.

Com ele, pode comodamente:

- Visualizar todas as bases disponíveis ou consultar especificamente as bases de um determinado utilizador
- Verificar os registos do sistema
- Criar, eliminar contas de utilizador ou repor palavras-passe

Para estas funções, necessita de um **token de conta com direitos de administrador**.

## Porquê esta separação clara?

Ao dividir as funções em dois nós, cada função permanece exatamente onde pertence: as **operações de dados para utilizadores** e a **gestão e controlo para administradores**. Isto garante maior clareza, segurança e facilidade de utilização nos seus workflows n8n.

## Conclusão

- O **nó SeaTable** é a sua ferramenta para todas as operações de dados diárias com um token API.
- O **nó SeaAdmin** apoia-o nas tarefas administrativas com um token de conta de administrador.

Assim, oferece no n8n a solução ideal para ambos os papéis: eficiente, segura e claramente estruturada.
