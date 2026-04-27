---
title: 'A vista de galeria'
date: 2025-12-03
lastmod: '2025-12-03'
categories:
    - 'grundlagen-von-ansichten'
author: 'kgr'
url: '/pt/ajuda/vista-de-galeria'
aliases:
    - '/pt/ajuda/guia-plugin-galeria-seatable'
    - '/pt/ajuda/anleitung-zum-galerie-plugin'
    - '/pt/ajuda/adicionar-linha-plugin-galeria'
    - '/pt/ajuda/eine-neue-zeile-ueber-das-galerie-plugin-hinzufuegen'
seo:
    title: 'Vista de galeria: apresente imagens de forma clara no SeaTable'
    description: "Com a vista de galeria, pode obter uma visão geral de todos os registos de dados que contêm imagens"
weight: 12
---

A **vista de galeria** utiliza imagens de pré-visualização de uma [coluna de imagem]({{< relref "help/base-editor/spaltentypen/die-bild-spalte" >}}) para organizar os registos de dados claramente em mosaicos. Várias imagens são resumidas num **álbum**. Esta apresentação é adequada para uma variedade de casos de utilização, por exemplo [perfis de empregados]({{< relref "templates/human-resources/employee-directory" >}}), [bibliotecas de produtos]({{< relref "templates/product-design/product-library" >}}), [listas de inventário]({{< relref "templates/operations/inventory-list" >}}) ou [gestão de colecções]({{< relref "templates/operations/art-gallery-management" >}}).

![A vista da galeria](images/gallery-view.jpg)

## Como criar uma vista de galeria

1. Clique no **nome da vista atual**.
2. Clique em **Adicionar vista ou pasta** e selecione o **tipo de vista** pretendido.

![criar uma vista de galeria](images/create-gallery-view.jpg)

3. Atribua um **nome** à nova vista.
4. Active o cursor se a nova vista não deve ser visível para todos mas **privada**.
5. Confirme com **Submeter**.
6. Em seguida, especifique nas definições de que **coluna de imagens** devem vir as imagens. A nova vista é então gerada automaticamente.
7. No campo **Título**, introduza a coluna cujas entradas pretende utilizar como título do álbum.

![Criar uma vista de galeria](images/create-gallery-view.gif)

## Opções de visualização

Pode utilizar as seguintes opções numa vista de galeria:
- [Bloquear vista]({{< relref "help/base-editor/ansichten/ansicht-sperren" >}})
- [Filtrar]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}}) ou [ordenar]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}}) por qualquer valor
- [Partilhar a vista com outros]({{< relref "help/startseite/freigaben/freigabe-einer-ansicht-an-ein-teammitglied" >}})

## Mostrar e ocultar informações

Nas **Configurações da galeria**, às quais pode aceder através do **ícone da roda dentada** {{< seatable-icon icon="dtable-icon-set-up" >}}, pode apresentar mais ou menos informações, mostrando ou ocultando colunas. Active os **deslizadores** das respectivas colunas para apresentar mais informações dos registos de dados na galeria.

![Mostrar informações de outras colunas na galeria](images/other-fields-shown-in-gallery-view.jpg)

## Várias imagens num álbum

O **número de imagens** por álbum é apresentado na galeria com um **número cinzento**. Logicamente, o número só é apresentado se houver mais do que uma imagem num álbum.

![Número de imagens número cinzento](images/image-number.jpg)

Clique na imagem de pré-visualização para abrir o álbum em **modo de ecrã completo**, no qual pode ampliar e reduzir as imagens utilizando as **lentes de aumento** e alternar entre as imagens utilizando as **setas**.

![Modo de ecrã inteiro na vista da galeria](images/gallery-image-preview.gif)

## Adicionar um novo registo na vista de galeria

![Adicione um novo registo na vista da galeria](images/add-new-record-in-gallery-view.jpg)

Clique no **círculo roxo com o símbolo de mais** no canto inferior direito. Abrir-se-á uma nova janela. Crie um novo registo de dados nos **detalhes da linha** e introduza as informações e imagens pretendidas. As alterações são automaticamente guardadas quando fecha a janela.

## Editar registos de dados na vista de galeria

![Editar registos na vista de galeria](images/modify-records-in-gallery-view.jpg)

Clique no **título** de um álbum e abrir-se-á uma janela com os **detalhes da linha**. Faça os ajustes desejados no registo. As alterações são guardadas automaticamente quando fecha a janela.