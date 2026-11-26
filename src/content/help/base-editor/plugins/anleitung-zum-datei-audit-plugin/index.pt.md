---
title: 'Instruções para o plugin de auditoria de ficheiros'
date: 2026-11-26
lastmod: '2026-11-26'
categories:
    - 'plugins'
author: 'bha'
url: '/pt/ajuda/guia-plugin-auditoria-ficheiros'
aliases:
    - '/pt/ajuda/anleitung-zum-datei-audit-plugin'
seo:
    title: 'Guia do plugin de auditoria de ficheiros do SeaTable'
    description: 'O plugin de auditoria de ficheiros do SeaTable encontra os ficheiros que uma base já não usa, as referências a ficheiros em falta e o que ocupa o armazenamento.'
---

O **plugin de auditoria de ficheiros** analisa os **ficheiros armazenados na sua base**: tudo o que foi carregado para a base — em colunas de ficheiro, de imagem e de assinatura, em texto longo, em comentários, formulários e apps — e ainda os ficheiros das suas próprias pastas personalizadas do [gestor de ficheiros]({{< relref "help/base-editor/dateien/das-dateimanagement-einer-base" >}}). Compara o que está no armazenamento com aquilo que a sua base realmente referencia e indica a diferença nos dois sentidos: **ficheiros que já ninguém usa** e **referências a ficheiros que já não existem**. Mostra-lhe também onde está a ser gasto o espaço.

No SeaTable, o armazenamento vai enchendo sem que se dê por isso, porque remover um ficheiro de uma célula **não o elimina**: o ficheiro fica no gestor de ficheiros da base, para poder ser [restaurado]({{< relref "help/haeufig-gestellte-fragen/wissen-und-tipps/zugriff-auf-geloeschte-anhaenge" >}}). Com o tempo, uma base pode acabar por armazenar muito mais do que as suas linhas mostram.

O plugin não precisa de configuração: da primeira vez que o abre, a auditoria é executada automaticamente. Executar a auditoria não altera nada — os ficheiros só são eliminados e as referências só são removidas quando o pede, um elemento ou um grupo de cada vez.

{{< zoom image="images/file-audit-plugin.png" alt="O plugin de auditoria de ficheiros a mostrar o armazenamento de uma base por pasta e os seus ficheiros órfãos" >}}

Pode descobrir como ativar um plugin numa base [aqui]({{< relref "help/base-editor/plugins/aktivieren-eines-plugins-in-einer-base" >}}).

## Como funciona a auditoria {#how-the-audit-works}

Uma auditoria faz três coisas:

1. **Lista o armazenamento da base**: cada ficheiro, com a sua pasta e o seu tamanho.
2. Reúne todos os ficheiros que a base **referencia**, onde quer que sejam usados:
    - as **colunas de ficheiro e de imagem** de todas as tabelas, e as **assinaturas** das colunas de assinatura,
    - as imagens inseridas em células de **texto longo**,
    - as imagens da **descrição da base** e dos **comentários das linhas**,
    - as imagens dos **formulários web** da base e dos formulários das suas **apps**,
    - as **linhas arquivadas**, que são lidas como as outras.
3. Verifica as **outras bases a que tem acesso**, para encontrar nelas linhas que mostrem ficheiros armazenados nesta base (ver [Ficheiros partilhados entre bases](#files-shared-between-bases) mais abaixo).

Depois compara as listas e mostra o resultado. A auditoria é executada com **os seus próprios direitos** — não é preciso criar nenhum token — e o relatório é guardado com a base: quando volta a abrir o plugin, encontra o último resultado, com a respetiva data, em vez de uma nova execução. **Executar auditoria novamente** volta a iniciá-la, o que deve fazer depois de qualquer alteração.

{{< warning type="warning" headline="Os scripts não são auditados" text="Os **scripts** da base são armazenados como ficheiros à parte, mas o plugin não os vê de todo: tal como no gestor de ficheiros, não aparecem na árvore de ficheiros da base, o seu tamanho não é contabilizado e **o seu conteúdo não é lido** — um ficheiro usado por um script não é considerado uma referência. Os scripts fazem, no entanto, parte dos ficheiros da base: ao exportá-la, **só a opção *Include assets* os conserva**." />}}

## O que o plugin indica

### Resumo e armazenamento por pasta

O topo do relatório faz o balanço: o **total de arquivos no armazenamento**, quantos estão **referenciados na base**, quantos são **órfãos** e que parte do armazenamento representam, e depois o número de **referências ausentes** e de **URLs externas**.

**Armazenamento por pasta** mostra onde está a ser gasto o espaço. Clique numa pasta para ver o seu conteúdo em pormenor. As suas próprias pastas (**pastas personalizadas**) são apresentadas à parte das **pastas do sistema** que o SeaTable cria para as colunas de ficheiro e de imagem, as assinaturas, os formulários e as apps. Algumas pastas do sistema contêm ficheiros de que o SeaTable precisa para fazer funcionar a base e que, por natureza, nenhuma linha referencia — ficheiros de plugins, as páginas e definições de cada app, logótipos e imagens de fundo dos formulários, e modelos de design de páginas: estão assinaladas como **Pasta do sistema — NÃO EXCLUIR** e nunca são listadas como órfãs. Já os ficheiros que os utilizadores carregam através de uma app são auditados como qualquer outro carregamento.

### Ficheiros órfãos {#orphaned-assets}

Um **ficheiro órfão** é um ficheiro no armazenamento que já nenhuma linha referencia — normalmente um ficheiro removido de uma célula, ou um que ficou para trás depois de uma linha ter sido eliminada. A lista está agrupada por pasta: pode eliminar um único ficheiro, ou todos os ficheiros órfãos de uma pasta de uma só vez.

Se um dos locais listados [acima](#how-the-audit-works) **não tiver podido ser lido** durante uma execução — os comentários ou as linhas arquivadas, por exemplo — a secção indica-o e **a eliminação fica desativada** nessa execução: caso contrário, todos os ficheiros usados apenas nesse local seriam propostos para eliminação. Execute a auditoria novamente para tentar outra vez.

Antes de eliminar o que quer que seja, leia os avisos dessa secção e as [limitações](#limitations) mais abaixo: um órfão é um ficheiro *para o qual o plugin não encontrou nenhuma referência*, o que não é bem o mesmo que um ficheiro de que ninguém precisa.

{{< warning type="warning" headline="Os ficheiros eliminados vão para o lixo" text="Os ficheiros que o plugin elimina vão para o **lixo** do gestor de ficheiros, onde ficam durante **60 dias** e podem ser restaurados. Depois disso, ou quando o lixo é esvaziado, perdem-se definitivamente: os instantâneos não incluem ficheiros. Para guardar uma cópia de segurança completa, **exporte a base com a opção *Include assets*** antes de eliminar o que quer que seja." />}}

### Referências ausentes

Uma **referência ausente** é o contrário: uma linha cuja coluna de ficheiro ou de imagem aponta para um ficheiro que **já não existe** no armazenamento. A célula continua a mostrar uma entrada, mas não há nada por trás dela. Pode remover a referência obsoleta de uma linha, de todas as linhas de uma coluna, ou de todo o lado de uma só vez. O resto da célula não é alterado.

### URLs externas

As colunas de imagem também podem conter ligações para ficheiros **alojados fora do SeaTable**. O plugin lista-as, agrupadas por tabela e coluna. Não são verificadas durante a auditoria, o que a tornaria mais lenta: inicie a verificação com **Verificar URLs externos**. Cada ligação fica então como **OK**, **quebrada** ou **não verificável** — muitos sites não permitem que um navegador verifique os seus ficheiros a partir de outro site, por isso *não verificável* não significa que a ligação esteja quebrada. Pode depois remover as ligações quebradas.

### Ficheiros partilhados entre bases {#files-shared-between-bases}

As duas últimas secções tratam dos **ficheiros que passam de uma base para outra** — um caso fácil de passar despercebido, e a razão pela qual o plugin verifica as suas outras bases em cada auditoria.

Quando **copia uma célula ou uma linha** de uma base para outra, o SeaTable copia a referência ao ficheiro, **não o ficheiro em si**. O ficheiro continua armazenado na base de origem, e a outra base mostra-o a partir daí — mesmo que esteja noutro espaço de trabalho. Nada, em nenhuma das bases, indica que estão agora ligadas. **Importar uma tabela** de outra base funciona de outra forma: copia também os ficheiros, pelo que as duas bases ficam independentes a seguir. **Prefira este método** sempre que precisar dos ficheiros nas duas bases.

- **Arquivos usados por outras bases** lista os ficheiros armazenados *nesta* base que linhas de *outra* base mostram. Ficam fora da lista de órfãos, mesmo que já nada nesta base os referencie: eliminar um deles estragaria a outra base.
- **Referências a arquivos de outras bases** é o inverso: linhas *desta* base que mostram um ficheiro armazenado *noutra* base. Aqui não são nem órfãos nem referências ausentes, e o plugin não pode verificar se esses ficheiros ainda existem.

Um ficheiro mostrado desta forma mantém as **permissões da base que o armazena**. Quem não tem acesso a essa base vê uma **célula vazia** onde o utilizador vê o ficheiro — por isso a mesma linha pode ter um aspeto diferente para duas pessoas.

## Permissões e segurança

- Com acesso **só de leitura** à base, pode ler o relatório inteiro, mas os botões de eliminar e de remover não estão disponíveis.
- Num **grupo** que não administra, pode continuar a eliminar ficheiros, mas o plugin avisa-o de que podem ter sido carregados por outros membros e pede uma confirmação explícita.
- Antes de alterar uma linha pela primeira vez — ao remover uma referência ausente ou uma ligação quebrada — o plugin cria um **instantâneo** da base. Este permite recuperar o **conteúdo das células** que o plugin removeu: os nomes dos ficheiros e as ligações, não os próprios ficheiros. Eliminar ficheiros não altera nenhuma linha e não fica coberto: os instantâneos não incluem ficheiros (ver o aviso [acima](#orphaned-assets)).

## Limitações {#limitations}

{{< warning type="warning" headline="Só são verificadas as bases a que tem acesso" text="A procura de referências noutras bases abrange as bases que consegue ver: as dos seus espaços de trabalho e grupos, e as que foram partilhadas consigo. A base de um colega a que não tem acesso pode muito bem mostrar um ficheiro da sua, e o plugin não tem forma de o saber. **Um órfão no relatório nunca é, portanto, prova de que um ficheiro não é usado.** Essas bases nunca aparecem no relatório, uma vez que o plugin não sabe que existem. Só as bases que consegue ver mas que o plugin não conseguiu ler durante uma execução — depois de um erro, por exemplo — são indicadas no relatório, com o motivo." />}}

A auditoria tem mais alguns pontos cegos que convém conhecer antes de eliminar:

- **Só são lidos os locais listados [acima](#how-the-audit-works).** Um ficheiro referido de qualquer outra forma não é considerado uma referência e pode, por isso, ser listado como órfão — por exemplo, um ficheiro cujo endereço está guardado numa coluna de texto ou de URL, ou que é usado num script ou através de uma ferramenta externa (orquestrador, etc.).
- **As suas próprias pastas contam como as restantes.** Um ficheiro que carregou para uma pasta personalizada do gestor de ficheiros, para o guardar lá, é listado como órfão enquanto nenhuma linha o referenciar.
- **Os ficheiros das pastas personalizadas não são seguidos entre bases.** Uma linha refere-se a eles através de um identificador que não diz que base os armazena, por isso o plugin não consegue saber se outra base usa algum deles.
- **Uma base criada por importação ou cópia pode continuar a usar ficheiros da base original.** Quando importa uma base a partir de um ficheiro `.dtable` ou a copia, os seus ficheiros também são copiados, mas alguns locais mantêm as ligações à base original — consoante a forma como a base foi criada, as imagens da descrição da base, dos formulários web e dos formulários de apps, ou os ficheiros das linhas arquivadas. O plugin lista estas ligações em **Referências a arquivos de outras bases**, e as cópias que deixam sem uso nesta base aparecem como órfãs. As suas imagens são carregadas a partir da base original, e algumas podem não ser apresentadas a outras pessoas, mesmo que tenham acesso a essa base. Os comentários das linhas também não fazem parte de uma exportação nem de uma cópia, pelo que as imagens neles inseridas ficam igualmente órfãs na nova base.
- **O relatório descreve o momento em que foi executado.** Qualquer pessoa pode adicionar ou remover uma referência depois disso, nesta base ou noutra: execute a auditoria novamente antes de eliminar.
- Numa conta com muitas bases, verificá-las todas **demora algum tempo**.

## Outros artigos úteis

- [Todos os plugins num relance]({{< relref "help/base-editor/plugins/alle-plugins-in-der-uebersicht" >}})
- [A gestão de ficheiros de uma base]({{< relref "help/base-editor/dateien/das-dateimanagement-einer-base" >}})
- [Aceder a ficheiros e imagens eliminados]({{< relref "help/haeufig-gestellte-fragen/wissen-und-tipps/zugriff-auf-geloeschte-anhaenge" >}})
- [Como remover ficheiros permanentemente]({{< relref "help/base-editor/dateien/wie-man-dateien-dauerhaft-entfernt" >}})
- [Ativar um plugin numa base]({{< relref "help/base-editor/plugins/aktivieren-eines-plugins-in-einer-base" >}})
