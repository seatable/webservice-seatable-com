---
title: 'A vista de árvore'
date: 2026-04-01
lastmod: '2026-04-01'
categories:
    - 'grundlagen-von-ansichten'
author: 'kgr'
url: '/pt/ajuda/vista-de-arvore'
seo:
    title: 'Vista de árvore: Mostrar hierarquia de registos de dados ligados'
    description: 'Utilize a vista de árvore no SeaTable para visualizar a hierarquia dos registos de dados ligados e apresentar dados complexos de uma forma estruturada.'
weight: 16
---

A **vista de árvore** permite a **visualização hierárquica** compacta de registos de dados ligados. Isto significa que pode visualizar dados que estão localizados em diferentes **tabelas ligadas** em diferentes níveis num diagrama de árvore. A vista fornece uma síntese estruturada, especialmente para grandes quantidades de dados, tais como dados financeiros ou de projectos.

![a vista de árvore](images/tree-view.png)

{{< warning type="warning" headline="Requisitos" >}}

Para usar a vista em árvore de forma sensata, precisa de uma base com **pelo menos duas tabelas** que estejam ligadas entre si através de uma [coluna de ligação]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}}).

{{< /warning >}}

## Como funciona a vista de árvore

Antes de criar uma vista de árvore, deve considerar qual a **estrutura de árvore** (ou seja, a hierarquia de registos de dados ligados na sua base) que faz sentido: Num [portfólio de projectos]({{< relref "templates/projects/project-portfolio" >}}), por exemplo, podem ser os departamentos no primeiro nível, os projectos no segundo nível e as tarefas no terceiro nível. Por conseguinte, os departamentos, os projectos e as tarefas devem ser registados em três tabelas diferentes, ligadas entre si. Cada tarefa é atribuída a um projeto, que, por sua vez, está subordinado a um departamento.

![Exemplo de uma estrutura em árvore](images/example-for-tree-view.png)

Defina como os registos de dados dependem uns dos outros e que tabelas estão em que nível, utilizando os **Níveis**. Atualmente, pode exibir até três níveis, ou seja, dados de três tabelas, na vista em árvore.

## Como criar uma vista de árvore

1. Clique no **nome da vista atual**.
2. Clique em **Adicionar vista ou pasta** e selecione o **tipo de vista** pretendido.

![Crie uma vista de árvore](images/create-tree-view.png)

3. Atribua um **nome** à nova vista.
4. Active o cursor se a nova vista não deve ser visível para todos mas **privada**.
5. Confirme com **Submeter**.

![Vista de árvore de nomes](images/name-tree-view.png)

6. Clique no ícone da **roda dentada** {{< seatable-icon icon="dtable-icon-set-up" >}} no canto superior direito e ajuste as **configurações**.
7. Especifique qual a **tabela** que deve ser apresentada no respetivo nível. Para o fazer, clique no campo para **Nível 2** e **Nível 3** para selecionar a tabela pretendida na lista pendente. **Nível 1** é sempre ocupado pela tabela em que a vista está localizada.

![Definir hierarquia na vista de árvore](images/tree-view-settings.jpg)

Os registos de dados ligados no segundo e terceiro níveis do diagrama em árvore são então agrupados sob os respectivos registos de dados de nível superior.

## Mostre e oculte informação

Através das **Definições**, a que pode aceder clicando no ícone da **roda dentada** {{< seatable-icon icon="dtable-icon-set-up" >}}, pode definir as colunas visíveis para cada nível do diagrama em árvore. Para tal, selecione primeiro o **nível** no qual pretende mostrar ou ocultar colunas. Se depois desativar o **deslizador** correspondente no lado direito, as colunas não são visíveis no diagrama em árvore.

![Ocultar ou mover colunas na vista de árvore](images/hide-and-move-columns-in-tree-view.png)

### Mover colunas

Também tem a opção de organizar as colunas de forma diferente da vista de tabela em cada nível. Para o fazer, mantenha premido o botão esquerdo do rato na **área de agarrar com seis pontos** à frente do nome da coluna e mova a coluna **arrastando e largando** para a posição desejada.

## Opções de vista

Pode utilizar as seguintes opções numa vista de árvore:
- [Bloquear vista]({{< relref "help/base-editor/ansichten/ansicht-sperren" >}})
- [Filtrar]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}}) ou [ordenar]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}}) por qualquer valor
- **Colapsar tudo** ou **Expandir tudo**

## Recolher e expandir registos de dados ligados

Para recolher todos os registos de dados ligados sob uma entrada, clique na **seta pendente** à esquerda da linha. Para voltar a expandir os registos de dados, proceda da mesma forma.

![Recolher registos na vista de árvore](images/collapse-records-in-tree-view.gif)

## Ajuste a largura da coluna

Para evitar entradas truncadas ou grandes espaços entre os valores, pode **ajustar a largura da coluna** conforme necessário. Para o fazer, mantenha premido o botão esquerdo do rato na linha de limite entre duas colunas e arraste o cursor para a esquerda ou para a direita.

![Ajustar a largura da coluna na vista de árvore](images/adjust-column-width-in-tree-view.gif)

## Adicione e edite registos de dados na vista de árvore

Para adicionar um novo registo de dados no primeiro nível da vista em árvore, clique no **círculo laranja com o símbolo de mais** no canto inferior direito. Abrir-se-á então a janela **Detalhes da linha**. Preencha estes dados conforme necessário e feche a janela para guardar o registo de dados.

Para adicionar um novo registo de dados no segundo ou terceiro nível da vista em árvore, clique em **\+ Adicionar linha**. A linha criada é automaticamente ligada ao registo de dados principal e agrupada em conformidade. Pode preencher os restantes campos diretamente na linha.

![Adicionar e editar registos de dados na vista de árvore](images/add-record-in-tree-view.png)

As entradas existentes também podem ser editadas diretamente na vista de árvore. Também pode clicar em **Expandir** para abrir os detalhes da linha e efetuar alterações.

![Adicionar e editar registos de dados na vista de árvore](images/expand-record-in-tree-view.png)

Naturalmente, os dados também são guardados nas tabelas subjacentes.