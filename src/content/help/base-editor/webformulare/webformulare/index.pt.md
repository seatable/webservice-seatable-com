---
title: 'Formulários Web'
date: 2022-08-25
lastmod: '2026-11-26'
categories:
    - 'webformulare'
author: 'cdb'
url: '/pt/ajuda/formularios-web-seatable'
aliases:
    - '/pt/ajuda/webformulare'
seo:
    title: 'Formulários Web SeaTable: criação, personalização e compartilhamento'
    description: 'Formulários web no SeaTable: crie, configure e teste formulários para coletar dados facilmente de usuários internos e externos.'
weight: 1
star: true
---

Os **formulários web** são o instrumento de eleição para permitir que membros da equipa e terceiros externos introduzam novos registos nas suas tabelas. Os utilizadores acedem a um formulário através de um **link**, pelo que **não é necessário partilhar** a tabela. Por isso, os formulários web são particularmente adequados para a recolha de dados por um grande número de **pessoas dentro e fora da sua equipa**.

Familiarize-se com a funcionalidade de formulários do SeaTable para recolher dados comodamente através de formulários web!

## Funcionamento dos formulários web

O formulário web clássico é ideal para **inquéritos online**, **pedidos** e a recolha estruturada de novos dados. As colunas da tabela são integradas através de **campos do formulário** e os utilizadores são guiados pelo processo de preenchimento. Para o acesso, crie um link através do qual os utilizadores podem preencher o formulário web **sem conta de utilizador do SeaTable**. Um formulário web preenchido corresponde a **um novo registo** ou a uma linha adicionada na tabela correspondente.

Os formulários web referem-se sempre a uma **tabela** da base aberta. Por conseguinte, tem de selecionar primeiro a tabela relevante antes de criar um formulário. Pode criar e guardar **qualquer número** de formulários web em cada base.

## Criar um formulário

Abra a gestão de formulários através do botão {{< seatable-icon icon="dtable-icon-form" >}} **Formulários** no canto superior direito do cabeçalho da base. Se ainda não tiverem sido criados formulários na base, a gestão de formulários aparece como uma lista vazia. Caso contrário, os formulários existentes são apresentados na janela aberta.

![Criar um formulário clássico](images/create-a-web-form.gif)

Para criar um [novo formulário web]({{< relref "help/base-editor/webformulare/anlegen-eines-webformulars" >}}), clique em **Criar formulário web** na parte inferior da gestão de formulários e selecione em seguida **Formulário clássico**.

Introduza agora o **nome** do novo formulário web que também deve ser apresentado na gestão de formulários. Utilize um nome conciso para manter a visão geral quando tiver muitos formulários. Naturalmente, pode alterar o nome mais tarde.

Ao clicar no **ícone do lápis** {{< seatable-icon icon="dtable-icon-rename" >}}, abre-se o **editor de formulários web** com a sua vista dividida em duas partes: à esquerda, o formulário web é apresentado em modo de rascunho; à direita encontram-se as **definições**.

Existem numerosas [opções de configuração]({{< relref "help/base-editor/webformulare/konfigurationsmoeglichkeiten-eines-webformulars" >}}) para adaptar rápida e facilmente um formulário web aos seus desejos e ideias.

Nas **definições do formulário web**, à direita, pode tomar as seguintes decisões:

- A que **tabela** está ligado o formulário?
- Que **elementos estáticos** e **campos de tabela** pretende incluir no formulário?
- Pretende criar um **formulário com várias páginas** através de quebras de página?
- Deve ser enviada (para si) uma **notificação** quando o formulário for submetido?
- Quem pode **aceder** ao formulário?
- Todos os campos devem ser **obrigatórios**?
- Deve ser apresentada uma **barra de progresso** às pessoas que preenchem formulários com várias páginas?
- Deve ser apresentada a indicação "Powered by"?
- Que **mensagem** é apresentada ao participante após a submissão do formulário?
- Pretende **redirecionar** o participante para **um website** após a submissão do formulário?
- O formulário tem um **prazo de submissão**?
- O formulário tem um **limite de submissões**?

Os campos disponíveis no formulário dependem das **colunas** da tabela selecionada. Se adicionar ou eliminar colunas na tabela, os campos disponíveis nas definições ajustam-se automaticamente. Os **nomes** e a **ordem** dos campos de tabela são retirados diretamente da tabela subjacente.

![Adicionar e configurar campos num formulário web](images/Add-fields-to-a-web-form.gif)

**Arraste e largue** os campos da tabela para o seu rascunho ou clique no **símbolo de mais** à direita do nome da coluna. Pode alterar a ordem dos campos no formulário web como desejar, clicando no **símbolo de seis pontos** {{< seatable-icon icon="dtable-icon-drag" >}} no canto direito de um campo e arrastando e largando o campo na posição desejada.

{{< warning  type="warning" headline="Tipos de colunas não selecionáveis"  text="As colunas do tipo Colaborador, Fórmula, Fórmula para ligações, Criador, Data de criação, Último modificador, Última modificação, Número automático e Botão não podem ser incluídas num formulário web." />}}

No rascunho, pode clicar em cada campo para aceder às **definições do campo**. Para cada campo, pode especificar se ...

- deve ser apresentado no formulário um **nome de campo** diferente do nome da coluna,
- um campo recebe um **texto de ajuda** complementar como indicação de preenchimento,
- um campo é um **campo obrigatório**,
- um campo deve conter um **valor predefinido**,
- a apresentação do campo depende de uma **condição**.

{{< warning  headline="Campos de seleção"  text="Para campos de seleção única e múltipla, também pode especificar se os valores são apresentados como uma **lista** ou como um menu **pendente**." />}}

Para verificar o aspeto do formulário para o destinatário, clique no botão **Página do formulário web**, no canto superior direito. O formulário abre-se então num novo separador, tal como outro utilizador o veria.

## Partilhar o formulário

Para tornar o formulário acessível a outras pessoas, precisa de um **link**. Pode obter o link do formulário no editor de formulários web através do botão {{< seatable-icon icon="dtable-icon-share" >}} **Partilhar**. Pode utilizar o **link gerado automaticamente** ou criar os **seus próprios links** e complementá-los com [valores pré-preenchidos]({{< relref "help/base-editor/webformulare/formularfelder-per-url-vorbefuellen" >}}).

![Novo diálogo de link de formulários no SeaTable 4.3](images/Formularlink-Dialog.gif)

{{< warning  headline="Links próprios"  text="A parte personalizada que é anexada ao link deve ter **entre 5 e 30 caracteres** e só pode conter **letras**, **números** e **hífenes**. Além disso, cada URL deve ser único: se um URL personalizado já estiver a ser utilizado, aparece uma mensagem de erro." />}}

Antes de enviar o link do formulário ou de o tornar acessível ao público, deve testar exaustivamente o formulário.

## Testar o formulário

Testes exaustivos evitam a frustração por parte dos destinatários. Os problemas podem ser causados por ambiguidades ou conflitos no formulário. No pior dos casos, um formulário não pode ser submetido porque um campo obrigatório não pode ser preenchido (por exemplo, se não tiverem sido definidos valores para uma seleção única).

Abra o formulário web para o testar. A partir do editor de formulários web, isto é feito através do botão **Página do formulário web**. A partir da vista da tabela, abra primeiro a gestão de formulários e depois clique no nome do formulário web. Em ambos os casos, o formulário web abre-se num novo separador do navegador.

![Testar um formulário web](images/Test-a-web-form.gif)

Os valores introduzidos no formulário são guardados na tabela ligada. Não se esqueça de apagar os dados de teste da tabela antes da recolha de dados propriamente dita.

## Editar o formulário

Pode editar formulários web em qualquer altura, utilizando o editor de formulários web. Para voltar ao editor, abra a gestão de formulários, passe o ponteiro do rato sobre o nome do formulário e depois clique no **ícone do lápis** {{< seatable-icon icon="dtable-icon-rename" >}} à direita do nome.

## Copiar o formulário

Se já criou um formulário que pretende apenas alterar ligeiramente para outro caso de utilização, pode copiar o formulário. Para isso, passe o ponteiro do rato sobre o nome do formulário e clique no **ícone de cópia** {{< seatable-icon icon="dtable-icon-copy" >}} à direita do nome.

## Eliminar o formulário

Pode eliminar formulários web em qualquer altura através da gestão de formulários. Passe o ponteiro do rato sobre o nome do formulário e depois clique no **ícone do caixote do lixo** {{< seatable-icon icon="dtable-icon-delete" >}} à direita do nome.

![Opções da gestão de formulários](images/form-management-options.png)
