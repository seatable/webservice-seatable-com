---
title: 'Visualização condicional de campos de formulário individuais'
date: 2023-01-08
lastmod: '2024-02-14'
categories:
    - 'webformulare'
author: 'vge'
url: '/pt/ajuda/exibicao-condicional-campos-formulario'
aliases:
    - '/pt/ajuda/bedingte-anzeige-von-einzelnen-formularfeldern'
seo:
    title: 'Exibição condicional de campos de formulário SeaTable: passo a passo prático'
    description: 'Saiba como exibir campos em formulários web do SeaTable apenas quando uma condição é atendida – para pesquisas dinâmicas e dados mais qualificados.'
weight: 4
---

Ao criar **formulários web**, pode definir que certos **campos** só se tornem visíveis quando uma **condição** num campo anterior tiver sido cumprida. Isto permite-lhe melhorar a **orientação do utilizador** ao preencher o formulário.

## Definir uma condição para um campo de formulário

1. Abra um **formulário web** existente.
2. Clique num campo para abrir as **definições do campo**.
3. Aceda a **Mostrar campo apenas quando as condições forem cumpridas** e clique no botão com o símbolo de mais, através do qual pode **adicionar uma condição**.
4. Selecione o **campo anterior** ao qual a condição se deve referir.
5. Em seguida, defina a **condição**. Dependendo do tipo de coluna subjacente, tem diferentes opções à sua escolha.

{{< warning  headline="Nota"  text="Só tem a opção de uma exibição condicional se houver pelo menos um campo anterior." />}}

## Exemplo de aplicação

![Exibição condicional de campos em formulários web](images/Bedingte-Anzeige-von-Feldern-in-Webformularen.gif)

Digamos que pretende realizar um inquérito de satisfação dos trabalhadores na sua empresa. Por exemplo, quer fazer a pergunta "Qual é o seu grau de satisfação com o nosso leasing de viaturas da empresa?", mas sabe que só os trabalhadores em cargos de chefia têm direito a uma viatura da empresa. Por conseguinte, só quer fazer esta pergunta às suas chefias.

Em primeiro lugar, deve criar uma [coluna de avaliação]({{< relref "help/base-editor/spaltentypen/die-rating-spalte" >}}) na sua tabela e adicioná-la como **campo** ao seu formulário web. Em seguida, adicione a **condição** de que o campo de avaliação só é apresentado se a opção "Head of" ou "Team lead" tiver sido selecionada no **campo de seleção "Cargo"** anterior. O campo de seleção deve ser de **preenchimento obrigatório**, pois, caso contrário, as chefias que deixarem este campo em branco também não verão a pergunta sobre o leasing de viaturas da empresa.

Para que os participantes não consigam ver os campos ocultos simplesmente experimentando as condições, pode inserir **quebras de página**. Assim, depois de preencherem o campo obrigatório, os participantes têm primeiro de clicar em **Página seguinte** e os campos condicionais são-lhes ou não apresentados nessa página.
