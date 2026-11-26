---
title: 'Preencher previamente os campos do formulário'
date: 2023-01-08
lastmod: '2024-03-18'
categories:
    - 'webformulare'
author: 'vge'
url: '/pt/ajuda/preencher-campos-formulario-url'
aliases:
    - '/pt/ajuda/formularfelder-per-url-vorbefuellen'
seo:
    title: 'Formulários SeaTable: preencha campos por link ou URL personalizada'
    description: 'Formulários web do SeaTable: pré-preencher campos via link com valores padrão. Guia sobre tipos de coluna e modos de leitura.'
weight: 5
---

Para **pré-preencher formulários web**, tem a opção de definir valores predefinidos nos campos do formulário. Pode fazê-lo diretamente no URL ou através de uma função de fácil utilização no SeaTable.

## Gerar um link de formulário com valores predefinidos no SeaTable

O SeaTable oferece uma função com a qual pode gerar comodamente **links de formulário** em que os valores predefinidos já estão definidos previamente.

1. Crie um [formulário web]({{< relref "help/base-editor/webformulare/webformulare" >}}).
2. No editor de formulários web, clique no botão {{< seatable-icon icon="dtable-icon-share" >}} **Partilhar** no canto superior direito.
3. Agora clique no botão **Adicionar link de formulário** e aparecerá a seguinte máscara de introdução:
   ![Valores pré-preenchidos em links de formulário personalizados](images/Vorbefuellte-Werte-in-benutzerdefinierten-Formularlinks.png)
4. Dê um **nome** ao novo link. Em **URL personalizado**, pode definir pessoalmente uma parte do URL.
5. Para pré-preencher um campo do formulário com um valor predefinido, clique em **Adicionar campo**. Selecione o **campo do formulário** no menu pendente e introduza o **valor predefinido** pretendido.
6. Por último, pode decidir se o valor predefinido pode ser alterado ao preencher o formulário. Para isso, selecione **Leitura e escrita**. Se selecionar **Apenas leitura**, o valor não pode ser alterado no formulário.
7. Clique em **Criar** para gerar o link.

![Link de formulário personalizado com valor pré-preenchido](images/Benutzerdefinierter-Formularlink-mit-vorausgefuelltem-Wert.png)

O resultado, ou seja, o URL alargado, é o mesmo que o do procedimento manual descrito abaixo.

## Pré-preencher um formulário web diretamente através do URL

![Pré-preencher formulário web](images/prefill.png)

1. Crie um [formulário web]({{< relref "help/base-editor/webformulare/webformulare" >}}).
2. No editor de formulários web, clique no botão {{< seatable-icon icon="dtable-icon-share" >}} **Partilhar** para obter o link para o formulário web.
3. **Copie** o link e cole-o num novo separador na **barra de endereço do navegador**, onde o pode editar e testar.
4. Para pré-preencher um campo do formulário com um valor predefinido, acrescente a cadeia de caracteres **/?prefill_COLUMNNAME=PREFILLVALUE** ao link do formulário.

Em vez de **COLUMNNAME**, introduza o nome do campo que pretende preencher; em vez de **PREFILLVALUE**, introduza o valor predefinido pretendido. Os espaços devem ser escritos como **%20**. Tenha atenção às maiúsculas e minúsculas.

**Exemplo**: se quiser enviar a Joe Smith um formulário web personalizado no qual o nome dele já esteja preenchido, acrescente a cadeia de caracteres **/?prefill_Name=Joe%20Smith** ao link do formulário.

Para utilizar **vários valores predefinidos**, encadeie as entradas de pré-preenchimento com o carácter **&**: /?prefill_COLUMNNAME=PREFILLVALUE**&**prefill_COLUMNNAME=PREFILLVALUE

Depois de terminar, pode testar o link premindo a **tecla Enter** e abrindo o formulário web. Se tudo tiver funcionado, poderá ver os valores predefinidos pré-preenchidos nesta **pré-visualização**.

## Campos de formulário pré-preenchíveis

Dependendo do tipo de coluna em que um campo de formulário se baseia, nem sempre é possível o pré-preenchimento. Na seguinte síntese, pode ver quais os tipos de coluna que permitem o pré-preenchimento via URL e quais não permitem.

| Tipo de coluna       | Suporta pré-preenchimento                                     |
| -------------------- | ------------------------------------------------------------- |
| Número automático    | {{< icon "circle-xmark" >}}                                   |
| Imagem               | {{< icon "circle-xmark" >}}                                   |
| Caixa de seleção     | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Ficheiro             | {{< icon "circle-xmark" >}}                                   |
| Data                 | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Duração              | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Seleção única        | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| E-mail               | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Criador              | {{< icon "circle-xmark" >}}                                   |
| Criado em            | {{< icon "circle-xmark" >}}                                   |
| Texto formatado      | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Fórmula              | {{< icon "circle-xmark" >}}                                   |
| Fórmula de ligação   | {{< icon "circle-xmark" >}}                                   |
| Geoposição           | {{< icon "circle-xmark" >}}                                   |
| Último editor        | {{< icon "circle-xmark" >}}                                   |
| Seleção múltipla     | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Colaborador          | {{< icon "circle-xmark" >}}                                   |
| Classificação        | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Botão                | {{< icon "circle-xmark" >}}                                   |
| Assinatura           | {{< icon "circle-xmark" >}}                                   |
| Número de telefone   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Texto                | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| URL                  | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Número               | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Última edição        | {{< icon "circle-xmark" >}}                                   |
