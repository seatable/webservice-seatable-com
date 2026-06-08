---
title: 'Exemplo de fórmula: Procura de uma palavra num texto'
date: 2023-01-28
lastmod: '2023-09-19'
categories:
    - 'formeln'
author: 'nsc2'
url: '/pt/ajuda/exemplo-formula-buscar-palavra-texto'
aliases:
    - '/pt/ajuda/formelbeispiel-nach-einem-wort-in-einem-text-suchen'
seo:
    title: 'Exemplo de fórmula SeaTable: buscar palavra em texto e destacar resultados'
    description: 'Veja como procurar palavras em campos de texto em SeaTable com fórmulas e como sinalizar achados de forma automática na coluna de resultados.'
---

As fórmulas SeaTable oferecem-lhe diferentes formas de trabalhar com os dados das suas tabelas. Uma possibilidade é procurar **palavras num texto**. Ao introduzir uma fórmula correspondente, pode procurar automaticamente numa [coluna de texto]({{< relref "help/base-editor/spaltentypen/die-spalte-formatierter-text" >}}) por quaisquer palavras e obter uma sugestão - por exemplo, "palavra encontrada/não encontrada" - escrita como resultado numa coluna de fórmula da sua tabela.

## Procura de uma palavra num texto

No exemplo concreto, o objetivo é procurar uma **palavra** na coluna de texto **"Pedido"** utilizando uma fórmula.

![Tabela de exemplo de pesquisa de palavras num texto utilizando uma fórmula ](images/example-table-search-words-in-text.png)

Para o fazer, comece por adicionar uma **coluna de fórmula** à tabela, em cujo editor pode então inserir a **fórmula**.

![Introduzir a fórmula no campo de texto previsto para o efeito](images/input-formula-example-text.jpg)

Para procurar uma palavra numa coluna de texto, comece por adicionar um operador **Se** à fórmula, que se encontra no editor de fórmulas no separador **Funções lógicas**. Este operador examina se uma **condição** definida se aplica ou não e devolve um determinado **valor** consoante o resultado seja positivo ou negativo.

![Acrescentar a função "se" à fórmula.](images/add-if-to-formular.jpg)

Na etapa seguinte, alarga-se a fórmula com a função **procurar**, com a ajuda da qual a coluna de texto pode ser pesquisada por uma palavra específica. A função encontra-se no editor de fórmulas, nas **funções de texto**.

![Acrescentar a função de texto "encontrar" à fórmula](images/add-find-to-formula.jpg)

As duas funções são seguidas na fórmula pela **palavra específica** que se pretende procurar na coluna de texto. Escreva a palavra **entre aspas** na fórmula.

![Acrescentar a palavra que procura na coluna de texto](images/add-the-word-searching-for.jpg)

O próximo componente da fórmula é o **nome da coluna** que deve ser verificada quanto à presença da palavra pesquisada. É particularmente importante que o nome da coluna esteja **entre parênteses rect** os, caso contrário o SeaTable **não consegue** reconhecer o texto que deve ser verificado utilizando a fórmula.

{{< warning  headline="Dica"  text="Os **nomes das colunas** na tabela são apresentados à esquerda no **editor de fórmulas** e podem ser inseridos na fórmula com um **duplo clique**." />}}

![Acrescentar o nome da coluna a ser verificada para a presença da palavra procurada.](images/add-reference-column.jpg)

Hinter dem Spaltennamen fügen Sie die mathematische Gleichung “**1 > 0**” ein. Diese ist für die Formel von Bedeutung, da Sie angibt, dass ein spezifischer **Wert** zurückgegeben wird, sobald das gesuchte Wort **mindestens einmal** in der Text-Spalte gefunden wird. Achten Sie in der Formel darauf, die Klammer **nach** der ersten Zahl zu **schließen**. Die **Vergleichszeichen** ( > , < , = , etc.) finden Sie im Formeleditor unter **Operatoren**.

![Acrescentar a equação matemática para completar a condição](images/add-.jpg)

Finalmente, define os **valores** na coluna de fórmulas que lhe são devolvidos por **encontrar** ou **não** a palavra pesquisada no texto. O **primeiro** valor introduzido aparece sempre na coluna de fórmulas se a palavra procurada foi **encontrada** no texto, o segundo valor no caso oposto. Coloque sempre os valores **entre aspas** e separe-os com uma **vírgula**.

![Acrescentar os valores que serão devolvidos se a palavra procurada estiver presente ou ausente na coluna da fórmula.  ](images/add-values.jpg)

Antes de confirmar, é ainda importante notar que é necessário **fechar os parênteses** para que a fórmula seja aceite como válida.

![Terminar a fórmula com o fecho do suporte](images/finish-formula.jpg)

Depois de confirmar a fórmula introduzida, pode ver, a partir do valor na **coluna da fórmula**, se a palavra procurada foi encontrada na coluna do texto.

![O resultado da fórmula aparece automaticamente na coluna da fórmula após a confirmação da fórmula.](images/table-after-formular-search-word.png)
