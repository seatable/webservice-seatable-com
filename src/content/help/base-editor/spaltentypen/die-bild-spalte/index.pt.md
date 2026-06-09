---
title: 'A coluna de imagem'
date: 2023-06-29
lastmod: '2024-08-02'
categories:
    - 'dateien-und-bilder'
author: 'nsc2'
url: '/pt/ajuda/coluna-imagens'
aliases:
    - '/pt/ajuda/die-bild-spalte'
seo:
    title: 'Coluna de imagens: fotos em tabelas SeaTable'
    description: 'Coluna de imagens SeaTable: carregue, gerencie e visualize imagens. Adicione por upload, URL, arrastar e soltar e gestão de arquivos.'
weight: 9
---

Com a ajuda de uma **coluna de imagens**, pode carregar, guardar e gerir novas imagens nas suas tabelas com apenas alguns cliques.

## Como criar uma coluna de imagens

![Criar uma coluna de imagens](images/create-image-column.gif)

1. Clique no **símbolo \[+\]** à direita da última coluna da sua tabela.
2. Dê um **nome** à coluna no campo superior.
3. Seleccione o tipo de coluna **Imagem** no menu pendente.
4. Confirmar com **Submeter**.

## Adicionar imagens

Numa coluna de imagens, tem várias opções para **adicionar** imagens. É assim que funciona:

![Primeiro, faça duplo clique em qualquer linha de uma coluna de imagem ou clique na seta azul](images/open-image-column.png)

1. Clique na **célula de** uma coluna de imagem.
2. Clique no **símbolo de mais** que aparece.
3. Abre-se uma nova janela. Aqui pode carregar **imagens do seu dispositivo**, incorporá-las através de **URL** ou adicioná-las a partir do [gestor de ficheiros]({{< relref "help/base-editor/dateien/das-dateimanagement-einer-base" >}}).

### Imagens locais

Na secção **Imagens locais**, pode clicar na caixa com o ícone de adicionar documentos, selecionar um ou mais **ficheiros de imagem no seu dispositivo** e carregá-los para a coluna de imagens.

![A área "Imagens locais" de uma coluna de imagens](images/image-column-local-images.png)

{{< warning  headline="Dica"  text="Além disso, pode selecionar todas as imagens que quiser no seu dispositivo e **arrastá-las** e largá-las no campo." />}}

### Ligação de imagem

Na área **Ligação de imagem**, pode adicionar imagens à coluna de imagem introduzindo o **URL** da imagem. Para o fazer, insira o URL no campo livre e clique no **símbolo de ligação** {{< seatable-icon icon="dtable-icon-url" >}}.

![Adicionar imagens a uma coluna de imagens utilizando o endereço de imagem ](images/image-link-image-column.png)

{{< warning  headline="URL da imagem"  text="Pode obter um URL de imagem, por exemplo, carregando as suas imagens para um serviço de carregamento de imagens como o Postimage ou incorporando-as no seu sítio Web através de um sistema de gestão de conteúdos como o WordPress." />}}

### Último carregamento

Na secção **Recentemente carregados**, tem acesso à [gestão de ficheiros]({{< relref "help/base-editor/dateien/das-dateimanagement-einer-base" >}}) da base. As imagens que já carregou nas **colunas de** **imagens** ou **ficheiros** ou nas **suas próprias pastas** são aí guardadas. Seleccione uma imagem e insira-a na coluna de imagens clicando em **Submeter**.

![A área "Último carregamento" de uma coluna de imagem](images/recently-uploaded-images-image-column.png)

### Por arrastar e largar

Também pode **inserir** imagens **diretamente numa tabela**. Para tal, seleccione qualquer número de **imagens no seu dispositivo** e arraste-as para a **célula de** uma coluna de imagens, mantendo premido o botão do rato.

![Arrastar e largar várias imagens de um dispositivo para uma coluna de imagens](images/drag-and-drop-files-into-file-column.gif)

## Pré-visualizar ficheiros de imagem

Assim que se insere um ficheiro de imagem na **coluna de imagem**, a imagem carregada é exibida como uma **miniatura reduzida**. Pode **ampliar** esta **miniatura** **fazendo duplo clique sobre** a imagem apresentada.

![Pré-visualizar ficheiros de imagem](images/Vorschau-von-Bilddateien.gif)

No **modo de ecrã inteiro**, pode utilizar as **lupas** para ampliar e reduzir as imagens e as **setas** para alternar entre várias imagens numa linha ou coluna. Também pode **apagar** ou **transferir** o ficheiro de imagem apresentado utilizando os ícones {{< seatable-icon icon="dtable-icon-delete" >}} e {{< seatable-icon icon="dtable-icon-download" >}}.

## Gestão de imagens

Para além de carregar imagens, também tem várias opções para gerir as suas imagens numa coluna de imagens.

### Descarregar imagens

Pode **descarregar** imagens armazenadas numa coluna de imagens com apenas alguns cliques. Para tal, comece por fazer **duplo clique** numa célula que já contenha imagens _ou_ no **símbolo de seta dupla azul**.

Em seguida, seleccione a **imagem** pretendida e clique no **ícone de transferência** {{< seatable-icon icon="dtable-icon-download" >}} na imagem.

![Descarregar imagens de uma coluna de imagens](images/Dana-White.jpg)

Se pretender transferir **todas as imagens de uma coluna**, abra o menu pendente acima do cabeçalho da coluna e seleccione **Transferir tudo**.

![Descarregar todas as imagens numa coluna](images/Download-all-images.png)

Pode então especificar **o seu próprio nome de ficheiro** e será apresentado o **número de ficheiros** contidos na exportação.

![Janela de diálogo para descarregar todos os ficheiros](images/Download-all-files-dialog.png)

Se clicar nos **três pontos**, tem duas opções para guardar o ficheiro: Ao **descarregar**, é guardado um ficheiro zip no seu dispositivo, do qual pode extrair todas as imagens. Também pode **guardar** as imagens **no Seafile**. Para o fazer, tem de [ligar primeiro uma biblioteca Seafile à sua Base]({{< relref "help/integrationen/integrationen-innerhalb-von-seatable/eine-seafile-bibliothek-an-seatable-anbinden" >}}).

### Eliminar imagens

Também é possível **eliminar** todas as imagens armazenadas numa coluna de imagens. Para o fazer, primeiro **faça duplo clique** numa célula que já contenha imagens _ou_ no **símbolo de seta dupla azul**.

Em seguida, seleccione a **imagem** pretendida e clique no **símbolo** {{< seatable-icon icon="dtable-icon-x" color="grey" >}}. Confirme o processo clicando em **Apagar**.

![Confirmação da supressão](images/confirm-delete.jpg)

{{< warning  headline="Atenção" >}}

As imagens excluídas de uma coluna de imagens ainda fazem parte do Base e, portanto, **não são** excluídas permanentemente. Leia os artigos [Aceder a ficheiros e imagens eliminados]({{< relref "help/haeufig-gestellte-fragen/wissen-und-tipps/zugriff-auf-geloeschte-anhaenge" >}}) e [Como remover ficheiros permanentemente]({{< relref "help/base-editor/dateien/wie-man-dateien-dauerhaft-entfernt" >}}).

{{< /warning >}}
