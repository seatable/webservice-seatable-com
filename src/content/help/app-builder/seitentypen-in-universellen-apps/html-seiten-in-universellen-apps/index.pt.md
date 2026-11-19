---
title: 'Páginas HTML em aplicações de SeaTable'
date: 2026-08-11
lastmod: '2026-08-11'
categories:
    - 'seitentypen-in-universellen-apps'
author: 'kgr'
url: '/pt/ajuda/paginas-html-apps-seatable'
seo:
    title: 'Adicionar páginas HTML em SeaTable Apps: guia'
    description: 'Adicione à sua aplicação páginas totalmente personalizadas baseadas em HTML, JavaScript e CSS para conceber a interface a seu gosto.'
weight: 12
---

Os outros [tipos de página de uma aplicação]({{< relref "help/app-builder/seitentypen-in-universellen-apps/ueberblick" >}}) oferecem, é certo, inúmeras possibilidades de configuração, mas determinam a estrutura e o comportamento de uma página. Com as **páginas HTML**, pode adicionar à sua aplicação páginas totalmente personalizadas baseadas em HTML, JavaScript e CSS. Deste modo, pode conceber aplicações exatamente de acordo com as suas ideias e implementar sem problemas até interações complexas. Os **casos de utilização típicos** são:
- Formulários, listas e páginas informativas com um design individual
- Tipos de gráficos ou diagramas próprios com elementos clicáveis
- Vistas combinadas, p. ex. uma tabela e um registo individual numa só página

![Exemplo de uma página HTML](images/html-page.png)

As páginas HTML podem apresentar **conteúdos estáticos**, mas revelam o seu verdadeiro potencial em combinação com os **dados de uma base**. Tal como os outros tipos de página do App Builder, podem obter dados de uma base e alterar registos numa base. Na **conceção da interface do utilizador** praticamente não existem limitações. Tudo o que pode ser implementado com HTML, CSS e JavaScript também pode ser integrado na sua aplicação como página HTML.

{{< warning headline="Ainda não é uma abordagem no-code" >}}

Atualmente, este tipo de página destina-se a **utilizadores com experiência de programação**. Todo o código da página tem de ser criado fora do SeaTable e, em seguida, carregado na aplicação como um pacote. No entanto, já está em desenvolvimento uma funcionalidade de IA que lhe permitirá, no futuro, criar páginas HTML em linguagem natural e sem conhecimentos de programação.

{{< /warning >}}

**Veja o nosso vídeo explicativo com legendas em português.**
{{< youtube pPdRwUx_Io8 >}}

## Como criar uma página HTML

1. Abra uma aplicação no **modo de edição**. Para tal, coloque o cursor do rato sobre a aplicação e clique no **ícone de lápis** {{< seatable-icon icon="dtable-icon-rename" >}}.
   ![Editar aplicações](images/edit-apps.png)
2. Clique em cima à esquerda no **círculo cor de laranja com o ícone de mais** e selecione em seguida **Adicionar página HTML**.
   ![Adicionar página HTML](images/add-html-page.png)
3. Dê um **nome** à página e defina opcionalmente um **ícone** para a página.
   ![Criar página HTML](images/create-html-page.png)
4. Confirme com **Enviar**.
5. Crie no seu dispositivo um **ficheiro zip** que contenha os ficheiros HTML, JavaScript e CSS.
6. **Carregue o ficheiro**, clicando na área prevista para o efeito ou arrastando o ficheiro para lá.
   ![Carregar ficheiro zip](images/upload-zip-file.png)
7. Em seguida, SeaTable apresenta o ficheiro como **página na aplicação**.

{{< warning headline="Atenção" >}}

O ficheiro zip pode ter no **máximo 10 MB** e tem de conter um ficheiro HTML com o nome **index.html**.

{{< /warning >}}

## Como criar os ficheiros necessários

Existem **duas formas** de construir uma página HTML e de a disponibilizar como ficheiro zip:
- A **abordagem low-code**: Conceba a página num **editor HTML visual**, ligue-a à sua base com a ajuda de **excertos de código** predefinidos, adicione opcionalmente **imagens e gráficos** e junte tudo num **ficheiro zip**. Este procedimento é ideal para formulários, painéis e páginas com design individual e com operações simples de leitura e escrita.
- A **abordagem de programador**: Assim que pretender criar páginas HTML maiores com uma lógica mais complexa, p. ex. quando os elementos da página devem interagir entre si, necessita da **cadeia de ferramentas JavaScript completa**. Para o desenvolvimento são necessários **Node.js** e **npm**, um **servidor de desenvolvimento** com recarregamento em direto, bem como um **token de API** gerado na base.

Encontra mais informações, exemplos e modelos no nosso [manual do programador](https://developer.seatable.com/html-pages/).
