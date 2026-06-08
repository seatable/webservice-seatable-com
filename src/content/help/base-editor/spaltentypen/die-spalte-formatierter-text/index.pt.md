---
title: 'As colunas Texto e Texto formatado'
date: 2023-02-21
lastmod: '2023-11-08'
categories:
    - 'text-und-zahlen'
author: 'nsc2'
url: '/pt/ajuda/texto-vs-texto-formatado-seatable'
aliases:
    - '/pt/ajuda/die-spalten-text-und-formatierter-text'
seo:
    title: 'Texto vs. texto formatado: tipos de coluna SeaTable'
    description: 'Campo texto para registros simples; texto formatado para descrições, listas e estrutura avançada – conheça os dois jeitos!'

---

SeaTable fornece dois tipos diferentes de colunas para a introdução de **cordas** e **textos** de qualquer tipo: **Texto** e **Texto formatado**. Mas qual é exactamente a diferença entre os dois tipos de coluna? E em que casos é que faz sentido utilizar a coluna de texto formatado?

## A coluna de texto

A coluna de texto é um dos **tipos de coluna** mais básicos no SeaTable e é também apresentada em primeiro lugar no menu de seleção do tipo de coluna.

![A coluna de texto regular](images/select-regular-text-column.png)

Além disso, SeaTable adiciona automaticamente uma **coluna de texto** como a primeira coluna a cada tabela criada recentemente.

![A coluna de texto "regular ](images/text-column-new.png)

A **primeira coluna de** uma tabela tem várias [características especiais]({{< relref "help/base-editor/spalten/die-besonderheiten-der-ersten-spalte" >}}), como se pode ler no artigo ligado.

### Usando a Coluna de Texto

A coluna de texto é particularmente adequada para recolher entradas curtas, tais como **termos**, **nomes**, **palavras** ou outras **cadeias de caracteres** que não tenham um valor numérico calculável, por exemplo, endereços e números de telefone.

![Exemplo de aplicação da coluna de texto regular](images/regular-text-example.png)

Ao utilizar a coluna, faz sentido manter as entradas **curtas**, uma vez que apenas um **número limitado de caracteres** pode ser exibido sem ter de aumentar a largura da coluna.

![As entradas que são demasiado longas não podem ser apresentadas na sua totalidade numa coluna de texto sem aumentar a largura da coluna.](images/use-short-entries.png)

{{< warning  headline="Nota importante"  text="Tenha em atenção que **não** estão disponíveis **opções de formatação** para as entradas na coluna de texto normal." />}}

Existem dois outros tipos de colunas baseadas em texto no SeaTable para casos de uso especial: a [coluna de correio electrónico]({{< relref "help/base-editor/spaltentypen/die-e-mail-spalte" >}}) e a [coluna URL]({{< relref "help/base-editor/spaltentypen/die-url-spalte" >}}).

### Definir valor por defeito

É possível definir um [valor]({{< relref "help/base-editor/spalten/standardwert-fuer-eine-spalte-festlegen" >}}) predefinido para cada coluna de texto. Este valor é automaticamente introduzido em cada nova linha da tabela.

Se especificar a referência **{creator.name}** ou **{creator.id}** como valor predefinido, o **nome** ou **ID do utilizador** que adicionou a linha é automaticamente introduzido.

![Referência ao nome do utilizador com um valor predefinido](images/Set-creator-name-as-default-value.png)

## A coluna Texto formatado

O tipo de coluna **Texto formatado** é um dos tipos de coluna mais específicos e é exibido em segundo lugar quando se selecciona o tipo de coluna.

![A coluna Texto formatado](images/formatted-text-column.png)

### Utilização da coluna Texto formatado

As colunas de texto formatadas são particularmente adequadas para manter **textos mais longos**, por exemplo, descrições de produtos, listas de verificação ou mensagens nos meios de comunicação social.

**Não** escreva as suas entradas directamente na célula, mas num **editor** que pode ser chamado com um clique, que oferece várias **opções de formatação**. Em contraste com a coluna de texto, também pode estruturar textos mais longos.

![Exemplo de aplicação de uma coluna de texto formatada](images/long-text-example.png)

Entre outras coisas, pode escolher um **formato de parágrafo**, definir a **fonte** para itálico ou negrito e inserir **links**, **citações**, **listas**, **tabelas** e **imagens**.

{{< warning  headline="Limite de caracteres"  text="Aplica-se um limite de 100.000 caracteres às células individuais do tipo Texto Formatado. Isto corresponde a aproximadamente 25 páginas A4 de texto. O limite de caracteres só deverá, portanto, ter um impacto no seu trabalho em casos excepcionais." />}}
