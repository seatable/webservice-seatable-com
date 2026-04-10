---
title: 'A gestão de ficheiros de uma base'
date: 2023-06-27
lastmod: '2024-03-15'
categories:
    - 'dateien-und-bilder'
author: 'nsc2'
url: '/pt/ajuda/gerenciamento-arquivos-base-seatable'
aliases:
    - '/pt/ajuda/das-dateimanagement-einer-base'
seo:
    title: 'Gerenciamento de arquivos na base do SeaTable'
    description: 'Aprenda a organizar, gerenciar e editar arquivos e pastas com facilidade na sua base do SeaTable.'

---

**A gestão de ficheiros** revoluciona a forma como trata os ficheiros na sua Base. Pode carregar, renomear, copiar, mover, descarregar e apagar **ficheiros** diretamente na Base. Pode até criar **novos documentos** (por exemplo, ficheiros Excel, Word ou PowerPoint) e editá-los utilizando o editor integrado.

Neste artigo de síntese, encontrará todas as informações sobre a estrutura e as funções individuais do gestor de ficheiros.

## Visão geral da gestão de ficheiros

O gestor de ficheiros contém várias pastas, que por sua vez contêm vários ficheiros. Pode ser feita uma distinção básica entre **três tipos de pastas**:

- **As pastas próprias** são independentes da estrutura de uma base e podem ser criadas e organizadas livremente pelo utilizador.

![Pastas próprias criadas e organizadas livremente pelo utilizador na gestão de ficheiros ](images/costum-folders.png)

- **As pastas do sistema** são criadas automaticamente pelo SeaTable quando cria determinadas colunas, aplicações ou formulários Web. Estas pastas contêm [ficheiros]({{< relref "help/base-editor/webformulare/webformulare" >}}).

![Pastas do sistema criadas e organizadas pelo sistema SeaTable na gestão de ficheiros](images/system-folders.png)

- Uma **pasta Seafile** contém todos os ficheiros que carregou anteriormente para o armazenamento externo na nuvem com o mesmo nome. Pode descobrir [aqui]({{< relref "help/integrationen/integrationen-innerhalb-von-seatable/eine-seafile-bibliothek-an-seatable-anbinden" >}}) como funciona exatamente a integração das bibliotecas Seafile e quais as vantagens que traz.

![Pasta Seafile em Gestão de ficheiros](images/seafile-library.png)

O diagrama seguinte mostra uma visão geral da **estrutura** completa de **pastas do gestor de ficheiros**:

![Estrutura de pastas na gestão de ficheiros](images/Ordnerstruktur-im-Dateimanagement-2.png)

## Aceder ao gestor de ficheiros

1. Abra uma **base** na qual pretende gerir ficheiros.
2. Clique nos três pontos no cabeçalho da base para abrir as **opções avançadas da base**.
3. Ir para **Gestão de ficheiros**.

![Abrir a gestão de ficheiros através das opções de base avançadas](images/open-file-management.jpg)

5. Uma janela redimensionável com a **estrutura de pastas** abrir-se-á automaticamente - o gestor de ficheiros Base.

![Gestão de ficheiros abertos de uma base](images/opened-file-management.png)

Também pode **adicionar** o gestor de ficheiros **à barra de ferramentas** clicando no **ícone central** no canto superior direito da janela.

![Adicionando o Gerenciamento de Arquivos à Barra de Ferramentas no Cabeçalho Base](images/add-file-management-to-toolbar.png)

Isto significa que pode sempre aceder ao **gestor de ficheiros** com apenas um clique a partir da sua barra de ferramentas.

![Gestão de ficheiros adicionada à barra de ferramentas no cabeçalho de base](images/file-management-in-toolbar.jpg)

Se pretender **remover** o gestor de ficheiros da sua barra de ferramentas, basta clicar novamente no ícone na extremidade da janela.

## Ajustar o tamanho e a posição da janela do gestor de ficheiros

Tem a opção de ajustar o tamanho da janela do gestor de ficheiros para que possa manter um olho nas suas tabelas e dados enquanto gere os seus ficheiros e arrastar ficheiros do gestor de ficheiros diretamente para as colunas apropriadas das suas tabelas.

Para isso, basta abrir o gestor de ficheiros e mover o ponteiro do rato sobre as **duas linhas** na parte superior da janela até aparecer uma **seta dupla**. Em seguida, mantenha premido o botão do rato e arraste a janela para a posição pretendida e solte-a assim que a alcançar.

![Ajustar o tamanho da janela de gestão de ficheiros](images/edit-the-window-size-of-the-file-management.gif)

Para além de ajustar o tamanho da janela, também tem a opção de **fixar** o gestor de ficheiros **no lado direito da página**. Para o fazer, clique no **primeiro ícone a contar da esquerda**, no canto superior direito.

![Fixar o gestor de ficheiros na margem direita da página](images/pin-file-management-to-side.png)

O gestor de ficheiros aparece então numa janela no lado direito da página.

![Gestão de ficheiros fixada na margem direita da página ](images/pinned-file-management-to-side.png)

Pode fixar novamente o gestor de ficheiros na margem inferior da mesma forma.

## As várias funções de gestão de ficheiros em pormenor

Existem várias opções de gestão disponíveis na gestão de ficheiros.

### Criar um novo ficheiro no gestor de ficheiros

Pode criar e editar novos ficheiros diretamente no gestor de ficheiros com apenas alguns cliques. Para tal, clique primeiro em **Novo** e, em seguida, seleccione a opção **Novo ficheiro** ou os vários **tipos de ficheiros** disponíveis para seleção.

![Criar um novo ficheiro na Gestão de ficheiros](images/create-new-file-in-file-management.jpg)

O ficheiro recém-criado aparece então na sua **própria pasta** correspondente. Clique no nome do ficheiro para o abrir e editar no editor.

![Ficheiro recentemente criado na gestão de ficheiros ](images/new-created-file-in-file-management.png)

### Criar a sua própria pasta no gestor de ficheiros

Para além dos ficheiros, também pode criar as **suas próprias pastas** diretamente no gestor de ficheiros. Para o fazer, clique em **Novo** na área **As minhas pastas** e, em seguida, seleccione a opção **Nova pasta**.

![Criar uma nova pasta na Gestão de ficheiros](images/create-folder-in-file-management.png)

A pasta recém-criada é então adicionada à navegação na área **As minhas pastas**.

![Pasta recentemente criada na gestão de ficheiros](images/added-new-created-folder.png)

### Carregar ficheiros e pastas para o gestor de ficheiros

Também pode carregar ficheiros guardados no seu dispositivo para o gestor de ficheiros com apenas alguns cliques. Para tal, clique primeiro em **Carregar** e, em seguida, seleccione a opção **Carregar ficheiros**.

![Carregar ficheiros para o sistema de gestão de ficheiros](images/upload-files-in-the-file-management.jpg)

Os ficheiros carregados no gestor de ficheiros são sempre guardados nas **Minhas pastas**. Além disso, abre-se uma janela de carregamento, que mostra o progresso de grandes quantidades de dados e na qual pode cancelar ou repetir o carregamento, se necessário.

![Ficheiro carregado no sistema de gestão de ficheiros](images/uploaded-file-to-file-management.png)

Para além de carregar ficheiros, também tem a opção de carregar **pastas inteiras** com ficheiros para o gestor de ficheiros.

![Carregar pastas inteiras para a gestão de ficheiros](images/upload-folders-in-the-file-management.png)

As pastas carregadas são sempre adicionadas automaticamente a **As minhas past** as.

![Pasta recentemente carregada para a gestão de ficheiros](images/new-uploaded-folder.png)

{{< warning  headline="Dica"  text="Também pode **carregar** ficheiros e pastas **utilizando a função arrastar e largar**. Para tal, arraste os elementos da localização de armazenamento no seu dispositivo para uma pasta separada no gestor de ficheiros aberto." />}}

### Arrastar e largar ficheiros nas colunas de tabela adequadas

Outra função útil do gestor de ficheiros é a **movimentação** conveniente **de ficheiros**. Pode não só **arrastar e largar** ficheiros no gestor de ficheiros, mas também inseri-los a partir do gestor de ficheiros em colunas de ficheiros na tabela.

{{< warning  headline="Dica"  text="Em primeiro lugar, **reduza o tamanho da** janela de gestão de ficheiros ou fixe-a no lado direito da página para facilitar o arrastamento de ficheiros para as colunas da tabela." />}}

![Arraste e largue ficheiros da gestão de ficheiros para as colunas da tabela adequadas.](images/drag-files-via-drag-and-drop-from-file-management-to-columns.gif)

### Mudar o nome de um ficheiro ou pasta

{{< warning  headline="Nota importante"  text="Esta função **só** está disponível para ficheiros e pastas na área **As minhas pastas**. **Não é possível** mudar o nome de ficheiros nas pastas do sistema e nas bibliotecas Seafile ou nas próprias pastas." />}}

Pode **mudar o nome de** ficheiros e pastas na área **As minhas pastas** com apenas alguns cliques. Basta mover o rato sobre um ficheiro ou pasta, clicar nos **três pontos** que aparecem e selecionar **Mudar** o nome.

![Mudar o nome de uma pasta na Gestão de ficheiros](images/rename-a-folder.jpg)

![Mudar o nome de um ficheiro na Gestão de ficheiros](images/rename-a-file.jpg)

Em seguida, introduza o novo **nome do** ficheiro ou **da** pasta no **campo de texto** e confirme-o com a **tecla Enter**.

### Copiar um ficheiro para uma pasta

{{< warning  headline="Nota importante"  text="Esta função **só** está disponível para ficheiros na área **As minhas pastas**. **Não é possível** copiar ficheiros das pastas do sistema e das bibliotecas Seafile." />}}

Um ficheiro pode ser copiado para a sua própria pasta com apenas alguns cliques. O ficheiro copiado fica então disponível tanto na pasta de origem como na pasta de destino.

Basta passar o rato sobre um ficheiro, clicar nos **três pontos** que aparecem e selecionar **Copiar** para.

![Copiar um ficheiro para uma pasta](images/copy-file-to-folder.png)

Em seguida, seleccione a **pasta de destino** e confirme com **Enviar**.

![Selecionar a pasta de destino e confirmar o processo de cópia](images/copy-file-to-folder-2.jpg)

### Copiar a sua própria pasta para outra pasta

{{< warning  headline="Nota importante"  text="Esta função **só** está disponível para pastas na área **As minhas pastas**. As pastas do sistema e as bibliotecas Seafile **não podem** ser copiadas." />}}

Tal como acontece com a cópia de ficheiros, as pastas próprias também podem ser copiadas para outra pasta com apenas alguns cliques. A pasta copiada fica então disponível na localização original, bem como no destino.

Para tal, basta mover o rato sobre a sua própria pasta, clicar nos **três pontos** que aparecem e selecionar **Copiar para**.

![Copiar uma pasta para outra pasta](images/copy-folder-into-folder.png)

Em seguida, seleccione a **pasta de destino** e confirme com **Enviar**.

![Selecionar a pasta de destino e confirmar o processo de cópia](images/copy-folder-into-folder-2.jpg)

### Mover ficheiros para uma pasta

{{< warning  headline="Nota importante"  text="Esta função **só** está disponível para ficheiros na área **As minhas pastas**. **Não é possível** mover ficheiros nas pastas do sistema e nas bibliotecas Seafile." />}}

Um ficheiro pode ser movido para a sua própria pasta com apenas alguns cliques. O ficheiro movido deixa **de** estar disponível na pasta original e passa a estar disponível **apenas na pasta de destino**.

Para tal, basta passar o rato sobre um ficheiro, clicar nos **três pontos** que aparecem e selecionar **Mover vista**.

![Mover ficheiros para uma pasta](images/move-files-into-folder.png)

Em seguida, seleccione a **pasta de destino** e confirme com **Enviar**.

![Selecionar a pasta de destino e confirmar a operação](images/copy-file-to-folder-2.jpg)

### Mover uma pasta própria para outra pasta

{{< warning  headline="Nota importante"  text="Esta função **só** está disponível para pastas na área **As minhas pastas**. **Não é possível** mover as pastas do sistema e as bibliotecas Seafile." />}}

Da mesma forma que a deslocação de ficheiros, as pastas no gestor de ficheiros também podem ser deslocadas para outra pasta com apenas alguns cliques. A pasta movida deixa **de** estar disponível na sua localização original, mas **apenas na pasta de destino**.

Para tal, basta passar o rato sobre uma pasta, clicar nos **três pontos** e selecionar **Mover vista**.

![Mover uma pasta para outra pasta](images/move-folders-into-other-folder-1.png)

Em seguida, seleccione a **pasta de destino** e confirme com **Enviar**.

![Selecionar a pasta de destino e confirmar a operação](images/copy-folder-into-folder-2.jpg)

{{< warning  headline="Caminhos de destino inválidos"  text="As pastas próprias não podem ser movidas para **subpastas** das quais elas próprias são superordenadas. Se os caminhos de destino forem inválidos, aparece uma **mensagem de erro** correspondente." />}}

### Descarregar ficheiros

Pode **transferir** todos os ficheiros do gestor de ficheiros em qualquer altura com apenas alguns cliques. Utilize esta função para fazer cópias de segurança de ficheiros importantes no seu dispositivo.

Mova o rato sobre um ficheiro e clique no **símbolo de transferência** {{< seatable-icon icon="dtable-icon-download" >}}. O ficheiro selecionado será então automaticamente guardado no seu dispositivo.

![Descarregar ficheiros da gestão de ficheiros](images/download-files.jpg)

### Eliminar e restaurar ficheiros

Pode **eliminar** qualquer ficheiro do gestor de ficheiros com apenas alguns cliques. Para tal, basta passar o rato sobre um ficheiro e clicar no **ícone da reciclagem**.

![Eliminar um ficheiro da gestão de ficheiros](images/delete-files.jpg)

Em seguida, confirme o processo novamente com **Delete.**

![Confirmação do processo de eliminação](images/confirm-deletion.jpg)

Os ficheiros eliminados do gestor de ficheiros também desaparecem da sua Base (por exemplo, da assinatura, do ficheiro, das colunas de imagens, dos formulários Web ou das aplicações) e vão parar à **reciclagem**, onde permanecem durante 60 dias.

{{< warning  headline="Nota importante"  text="Tenha em atenção que os ficheiros na reciclagem são permanentemente removidos do sistema **após 60 dias**. Por conseguinte, certifique-se de que **apenas** os ficheiros que já não são necessários estão na reciclagem." />}}

Se pretender restaurar um ficheiro da reciclagem, por exemplo, porque foi apagado por engano, clique em **Restaurar**. O ficheiro será então encontrado na pasta onde se encontrava antes de ser apagado. Quando **esvazia** a reciclagem, todos os ficheiros e pastas eliminados são perdidos permanentemente.

![Esvaziar a lixeira ou restaurar arquivos da lixeira](images/Empty-and-restore-from-trash.png)

### Eliminar e restaurar a pasta

Pode eliminar as **suas próprias pastas** no gestor de ficheiros em qualquer altura com apenas alguns cliques. Para tal, passe o rato sobre qualquer pasta na barra de **navegação**, clique nos **três pontos** que aparecem e seleccione **Apagar**.

![Eliminar as próprias pastas](images/delete-costum-folders.png)

Confirmar a eliminação com **Delete**.

![Confirmar a eliminação](images/delete-costum-folders-2.jpg)

{{< warning  headline="Pasta do sistema"  text="**Não é possível** eliminar pastas de sistema superordenadas. Aqui só é possível remover **as subpastas** criadas pelo sistema." />}}

Em geral, também é possível eliminar **subpastas** de outra forma. Primeiro, clique na pasta em que se encontra a pasta a eliminar. Aparecerá uma visão geral de todas as pastas e ficheiros da pasta selecionada. Mova o rato sobre a pasta a eliminar e clique no **símbolo da reciclagem**.

![Eliminar pastas que já estão numa pasta](images/delete-folders-in-folders-way-2-2.jpg)

Confirmar a operação com **Apagar.**

![Confirmar a eliminação](images/delete-folders-in-folders-3.jpg)

As pastas que elimina do gestor de ficheiros vão para a **reciclagem**, onde permanecem durante 60 dias.

{{< warning  headline="Notas importantes"  text="Tenha em atenção que, ao eliminar pastas, **todos os ficheiros** nas respectivas pastas também são **eliminados**. O mesmo se aplica às subpastas de uma pasta eliminada. Por conseguinte, os ficheiros eliminados também desaparecem da sua base (por exemplo, da assinatura, do ficheiro, das colunas de imagens, dos formulários Web ou das aplicações). Certifique-se de que **só** elimina do gestor de ficheiros as pastas com ficheiros que já não são necessários. Após **60 dias** na reciclagem, tanto as pastas como os ficheiros são removidos permanentemente do sistema." />}}

Se pretender restaurar uma pasta da reciclagem, por exemplo, porque a apagou por engano, clique em **Restaurar**. A pasta aparece então no local onde estava antes de ser apagada. Quando **esvazia** a reciclagem, todos os ficheiros e pastas eliminados são perdidos permanentemente.

![Esvaziar a lixeira ou restaurar arquivos da lixeira](images/Empty-and-restore-from-trash.png)
