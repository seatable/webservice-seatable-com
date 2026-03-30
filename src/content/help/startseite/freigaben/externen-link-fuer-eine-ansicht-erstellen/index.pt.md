---
title: 'Criar uma ligação externa para uma vista'
date: 2022-10-26
lastmod: '2023-01-17'
categories:
    - 'freigaben'
author: 'nsc2'
url: '/pt/ajuda/criar-link-externo-visualizacao'
aliases:
    - '/pt/ajuda/externen-link-fuer-eine-ansicht-erstellen'
seo:
    title: 'Criar e compartilhar link externo para visualização SeaTable'
    description: 'Descubra como compartilhar uma visualização SeaTable com usuários externos usando link de só leitura, senha e data limite. Passo a passo completo.'
---

{{< required-version "Mais" "Empresa" >}}

Para partilhar vistas de tabela com utilizadores que **não estão registados no SeaTable**, é possível criar uma ligação externa para uma vista.

Em princípio, as ligações externas são **públicas** e, portanto, acessíveis sem necessidade de iniciar sessão. Fornecem **acesso apenas para leitura aos** dados na visão partilhada.

Além disso, estão disponíveis várias opções com as quais se pode assegurar uma ligação externa:

- Tem a opção de definir uma **data de expiração automática para** uma ligação externa. Após o número de dias seleccionado, a ligação externa perde a sua validade.
- Além disso, também pode definir qualquer **palavra-passe** para uma ligação externa. Isto deve ser introduzido correctamente por outro utilizador para ter acesso à vista.

Tudo o resto que deve saber sobre links externos pode ser encontrado no artigo [Creating an External Link for a Base]({{< relref "help/startseite/freigaben/externer-link-erklaert" >}}).

## Criar uma ligação externa para uma vista

![Criar uma ligação externa para uma vista em SeaTable](images/create-an-external-link-for-a-view-2.gif)

1. Abra a **vista** de uma tabela que deseja partilhar.
2. Clique em **Share View** e depois em **External Link**.
3. Se necessário, defina a sua própria **palavra-passe** ou uma **palavra-passe** gerada aleatoriamente e/ou uma **data de validade para** a ligação.
4. Seleccione se pretende gerar um **URL aleatório** para a ligação ou defina você mesmo um **URL desejado**.
5. Confirmar com **Create**.
6. A ligação criada é então exibida abaixo e pode simplesmente ser **copiada**.

## Embutir num sítio web

Também pode utilizar ligações externas para incorporar **vistas** numa página web. Para o fazer, basta inserir o **link** no editor do seu sistema de gestão de conteúdos.

Por exemplo, é este o aspecto da integração de uma tabela com comunicados de imprensa na nossa página de imprensa:

![Incorporação de vistas externas num website.](images/image-1666823263581.png)
