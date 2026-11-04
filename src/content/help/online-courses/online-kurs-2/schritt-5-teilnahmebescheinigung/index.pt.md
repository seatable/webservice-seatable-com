---
title: 'Etapa 5: Certificado de participação'
date: 2024-09-19
lastmod: '2024-09-24'
categories:
    - 'online-kurs-2'
author: 'cdb'
url: '/pt/ajuda/etapa-5-certificado-de-participacao'
aliases:
    - '/pt/ajuda/schritt-5-teilnahmebescheinigung'
seo:
    title: 'Etapa 5: Certificado de participação PDF por email'
    description: 'Saiba como gerar e enviar automaticamente certificados PDF de participação aos inscritos do curso usando SeaTable.'
---

Depois de concluir o seu serviço, pretende concluir o processo enviando uma mensagem de correio eletrónico final aos participantes. Este correio eletrónico pode ter vários conteúdos, tais como

- Uma confirmação de participação
- Obrigado pela vossa participação
- Um pedido de feedback
- Um código de voucher para o próximo curso
- ...

## Criar e enviar a confirmação de participação

Nesta secção, utilizaremos o SeaTable para gerar uma confirmação de participação em PDF e enviá-la aos participantes por correio eletrónico.

### Fusão de correio com o plugin de conceção de páginas

O SeaTable oferece vários plug-ins que lhe permitem acrescentar visualizações e funções adicionais aos seus dados. O plugin de design de página permite-lhe criar documentos PDF - semelhante a uma fusão de correio no Microsoft Word.

Com este plugin, pode criar modelos que contêm conteúdo estático (como texto ou logótipos) e dados dinâmicos da sua base. Cada linha da tabela pode gerar um documento individual.

{{< warning  headline="Possibilidades de aplicação versáteis"  text="O plugin de conceção de páginas oferece muitas possibilidades: Para além dos certificados de participação, também pode criar facturas, certificados, circulares e muito mais." />}}

Já preparámos um modelo simples para este curso, para criar uma confirmação de participação. O nome, o curso e a data do curso são inseridos automaticamente, enquanto o resto do texto permanece inalterado.

Dedique alguns minutos a explorar as possibilidades do plug-in. Por exemplo, experimente adicionar um logótipo ou um gráfico à sua assinatura.

![](images/lvl2-page-design.png)

Se clicar em `{{< seatable-icon icon="dtable-icon-download" >}} PDF` o PDF gerado será guardado no seu PC.

{{< warning  headline="Os modelos referem-se sempre a uma tabela"  text="Ao criar um novo modelo, os dados só podem ser utilizados a partir de uma tabela. Se necessitar de dados de uma coluna ligada, deve incluí-los através de colunas de pesquisa. Esta é a razão pela qual a tabela Registrations existem três colunas de pesquisa ocultas. Estas colunas só são necessárias para o plugin de design da página e podem, por isso, permanecer ocultas." />}}

### Envio por correio eletrónico

É claro que não quer descarregar o PDF manualmente e carregá-lo novamente para o enviar por correio eletrónico. Em vez disso, pode clicar num botão no menu `Registrations` que executa duas acções em sucessão:

- `{{< seatable-icon icon="dtable-icon-pdf" >}} Crie PDF e salve na coluna`
- `{{< seatable-icon icon="dtable-icon-email" >}} Enviar email`

A configuração destas acções já deve ser familiar. Ao criar o PDF, selecione o modelo pretendido e a coluna na qual o documento deve ser guardado. Ao enviar o e-mail, especifique a coluna a partir da qual o anexo deve ser enviado.

{{< warning  headline="As acções são executadas uma após a outra"  text="Não é um problema que o botão crie primeiro o ficheiro PDF e depois o envie. O SeaTable aguarda até que o PDF tenha sido criado antes de enviar a mensagem de correio eletrónico." />}}

### Algumas palavras sobre a gestão de ficheiros

No SeaTable, os ficheiros e as imagens não são armazenados diretamente nas células, mas no armazenamento central de dados da base. As células contêm apenas ligações para os respectivos ficheiros. Esta gestão centralizada tem várias vantagens:

- Os ficheiros podem ser utilizados várias vezes sem ter de os carregar novamente.
- Mesmo que se elimine um ficheiro de uma célula, este continua disponível na administração central até ser eliminado definitivamente.

Dedique alguns minutos para se familiarizar com a gestão de ficheiros do SeaTable. Para mais informações, consulte os artigos de ajuda no final desta secção.

## Artigo de ajuda com mais informações

- [Guia de Plugin de Desenho de Páginas]({{< relref "help/base-editor/plugins/anleitung-zum-seitendesign-plugin" >}})
- [Guardar um documento PDF por botão numa coluna]({{< relref "help/base-editor/schaltflaechen/ein-pdf-dokument-per-schaltflaeche-in-einer-spalte-speichern" >}})
- [A Coluna Arquivo]({{< relref "help/base-editor/spaltentypen/die-datei-spalte" >}})
- [A gestão de ficheiros de uma base]({{< relref "help/base-editor/dateien/das-dateimanagement-einer-base" >}})
