---
title: 'SeaTable 4.3: Novas ligações para formulários, automatizações e funcionalidades da aplicação'
description: 'Gere URLs sob medida, crie PDFs e notificações sem esforço, atribua colaboradores livremente, comente direto nas apps, use cartões e containers. E-mails ricos em texto, temas visuais flex, novas permissões, export fácil – cada recurso para acelerar projetos e integração de equipes.'
date: 2024-02-08
lastmod: '2024-02-16'
author: 'kgr'
url: '/pt/seatable-release-4-3'
color: '#fd5d04'
categories:
    - 'product-features'
seo:
    title: 'SeaTable 4.3: links, automação e apps avançadas'
    description: 'Links de formulário personalizados, PDFs automáticos, avisos em apps e upgrades universais: mais criatividade e praticidade no SeaTable 4.3.'
---

A época carnavalesca na Alemanha está a aproximar-se do seu auge - e os canhões de confettis também estão a rebentar no SeaTable! A versão 4.3 traz consigo algumas funções e melhorias há muito esperadas.

Aguarde um novo diálogo para criar **ligações de formulários**, no qual pode adaptar os URLs aos seus desejos pessoais. Utilize duas novas **automatizações** para criar documentos e enviar notificações aos utilizadores da aplicação. Ou experimente as novas funcionalidades da **aplicação universal**: Entre outras coisas, pode esperar comentários, dois elementos adicionais para a página individual e uma melhor personalização do esquema de cores.

Esta manhã, actualizámos o SeaTable Cloud para a versão 4.3. Todos os auto-hosters podem fazer o mesmo: A imagem do SeaTable 4.3 está disponível para download no conhecido [repositórioDocker](https://hub.docker.com/r/seatable/seatable-enterprise) . Como sempre, pode encontrar a lista completa de alterações no [registo de alterações]({{< relref "pages/changelog" >}}).

Também actualizámos os plugins para Webpack 5 e actualizámos a estrutura para React 17.0.2, o que garantirá maior segurança e estabilidade no futuro e permitirá funções adicionais.

## Novo diálogo e ligações definidas pelo utilizador para formulários Web

Para partilhar os seus [formulários Web]({{< relref "help/base-editor/webformulare" >}}) com outros utilizadores, existiam anteriormente duas caixas de diálogo diferentes: uma em que podia copiar uma **hiperligação gerada automaticamente** e outra em que podia ampliar esta hiperligação com [valores pré-preenchidos]({{< relref "help/base-editor/webformulare/formularfelder-per-url-vorbefuellen" >}}). Agora combinámos estas opções numa única caixa de diálogo para aumentar a facilidade de utilização.

Adicionámos também a nova opção de criar **URLs personalizados** para formulários Web. Pode depois editá-los, guardá-los como código QR, copiá-los ou apagá-los.

![Novo diálogo de ligação de formulários no SeaTable 4.3](Formularlink-Dialog.gif)

{{< warning headline="Nota" text="A parte definida pelo utilizador que é anexada à ligação deve ter **entre 5 e 30 caracteres** e só pode conter **letras**, **números** e **hífenes**. Além disso, cada URL deve ser único: Se um URL definido pelo utilizador já estiver a ser utilizado, aparece uma mensagem de erro." />}}

## Acções automatizadas: Guardar PDF e enviar notificação da aplicação

Atenção fãs da automatização! O SeaTable 4.3 adiciona duas novas opções às [acções automatizadas]({{< relref "help/base-editor/automationen/automations-aktionen" >}}):

1. Em primeiro lugar, tem a possibilidade de guardar periodicamente PDFs para entradas que preencham determinadas condições.
2. Em segundo lugar, agora é possível enviar notificações que determinados utilizadores de uma aplicação universal devem receber.

Anteriormente, só era possível [criar documentos PDF]({{< relref "help/base-editor/schaltflaechen/ein-pdf-dokument-per-schaltflaeche-in-einer-spalte-speichern" >}}) manualmente no SeaTable [através de um botão]({{< relref "help/base-editor/schaltflaechen/ein-pdf-dokument-per-schaltflaeche-in-einer-spalte-speichern" >}}). A nova opção para criar **automaticamente** documentos a partir de registos de dados específicos num determinado momento poupa-lhe cliques e torna os seus processos ainda mais fáceis.

É possível utilizar as **notificações da aplicação** para informar os utilizadores de uma aplicação sobre alterações a registos de dados relevantes, por exemplo. Esta ação pode ser accionada por todos os quatro [eventos de acionamento]({{< relref "help/base-editor/automationen/automations-trigger" >}}).

![Enviar notificação de aplicação](App-Benachrichtigung-senden.png)

Os utilizadores da respectiva aplicação podem aceder às suas notificações através do ícone de sino {{< seatable-icon icon="dtable-icon-notice" >}} junto ao seu avatar no canto superior direito.

## Coluna de colaboradores de várias equipas

Na [coluna de]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}}) colaboradores, anteriormente só era possível selecionar pessoas que já tinham acesso à respectiva base. A partir do SeaTable 4.3, é possível introduzir **todos os membros da sua equipa** nas colunas de colaboradores, mesmo que não tenham acesso a determinadas bases. Desta forma, é muito mais fácil atribuir registos de dados aos seus colaboradores, independentemente da sua autorização de acesso.

Esta funcionalidade é particularmente útil na aplicação Universal. Pode ativar a opção para que os membros da equipa sejam visíveis para todos os utilizadores na lista pendente nas [definições]({{< relref "help/app-builder/einstellungen/einstellungen-einer-universellen-app-aendern/" >}}) da aplicação Universal. Se não quiser que os utilizadores possam ver os registos de dados de outros, defina **filtros predefinidos**: Se uma página for filtrada pela coluna do empregado com a condição "inclui o utilizador atual", cada utilizador da aplicação universal só vê as entradas que lhe estão atribuídas na tabela.

![Coluna do empregado na aplicação universal](Mitarbeiter-Spalte-in-der-Universellen-App.gif)

## Mais melhorias na aplicação universal

Uma nova funcionalidade da aplicação Universal é a [função de comentários]({{< relref "help/base-editor/zeilen/zeilen-kommentieren" >}}), que já reconhece na mesma forma da aplicação Base. Registe os seus comentários ou informações adicionais sobre os registos de dados para outros utilizadores da aplicação e realize debates no local.

{{< warning headline="É bom saber" text="Os comentários na aplicação são completamente **independentes** dos comentários na base. Isto significa que cada comentário só é visível no local onde é publicado." />}}

Na [página individual]({{< relref "help/app-builder/seitentypen-in-universellen-apps/individuelle-seiten-in-universellen-apps" >}}), pode contar com dois novos elementos: o **contentor** e o **mapa**. O contentor fornece uma grelha com a qual pode organizar mais facilmente outros elementos (textos, imagens, estatísticas) e agrupá-los.

![Elemento de contentor na página personalizada no SeaTable 4.3](Container-element-on-custom-page.png)

O cartão, que combina uma imagem, um título e um texto num modelo de design, também garante uma apresentação de página bonita.

![Elemento de cartão na página personalizada no SeaTable 4.3](Card-element-on-custom-page.png)

Além disso, a **cor de fundo** das páginas individuais pode ser definida conforme desejado a partir do SeaTable 4.3 e a sobreposição indesejada de elementos foi corrigida. O design geral da aplicação universal é agora também apresentado numa cor uniforme em todas as páginas, que pode ser selecionada nas [definições globais]({{< relref "help/app-builder/einstellungen/einstellungen-einer-universellen-app-aendern/" >}}).

### Autorizações nas páginas do quadro

A herança de [autorizações de colunas]({{< relref "help/base-editor/spalten/spaltenberechtigungen-festlegen" >}}) a partir da base foi abolida com o SeaTable 4.3. Se pretender bloquear uma coluna na aplicação universal para edição, pode defini-la como **"só de leitura"** nas definições da [página da tabela]({{< relref "help/app-builder/seitentypen-in-universellen-apps/tabellenseiten-in-universellen-apps" >}}).

Todas as restrições para [acções de botão]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}}) também foram removidas. Cada utilizador da aplicação pode agora fazer alterações predefinidas aos registos de dados, mesmo que as colunas afectadas estejam bloqueadas e o utilizador não esteja autorizado a editar a página.

## Anúncio importante: Remoção da galeria e da aplicação de consulta de dados

Na versão 4.4, a [aplicação de galeria]({{< relref "help/app-builder/seitentypen-in-universellen-apps/galerieseiten-in-universellen-apps" >}}) e a [aplicação de consulta de dados]({{< relref "help/app-builder/app-verwaltung/datenabfrage-app" >}}) desaparecerão, uma vez que a sua funcionalidade pode agora ser totalmente mapeada com os **tipos de página** correspondentes na aplicação universal. O Universal App Builder será, portanto, a única opção para criar aplicações no SeaTable no futuro.

Se utilizar as duas aplicações que estão a expirar, recomendamos que reconstrua os seus casos de utilização com [páginas de galeria]({{< relref "help/app-builder/seitentypen-in-universellen-apps/galerieseiten-in-universellen-apps" >}}) e [páginas]({{< relref "help/app-builder/seitentypen-in-universellen-apps/abfrageseiten-in-universellen-apps" >}}) de consulta no App Builder antes da próxima versão. A propósito, agora é possível adicionar campos às páginas de consulta que permitem aos utilizadores pesquisar **colunas de ligação** para valores específicos.

{{< warning headline="Atenção, perigo de confusão!" >}}

Também conhece a [galeria]({{< relref "help/base-editor/ansichten/die-galerie-ansicht" >}}) e a [consulta SQL]({{< relref "help/base-editor/plugins/anleitung-zum-sql-abfrage-plugin" >}}) como **plugins** que pode adicionar às suas bases. Estes manter-se-ão, naturalmente, em vigor.

{{< /warning >}}

## E muito mais

Se [enviar mensagens de correio eletrónico através da automatização]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}}), anteriormente só podia introduzir a sua mensagem como **texto simples** no campo de texto. A partir do SeaTable 4.3, é possível compor as mensagens em **formato rich text ou HTML** utilizando botões, tal como no envio de mensagens de correio eletrónico. Para tal, basta ativar o cursor à direita, por cima do campo de texto.

![Rich text em mensagens de correio eletrónico automatizadas](Rich-text-in-automated-e-mail-messages.png)

Se gosta de utilizar **autorizações de coluna** para proteger os valores de alterações indesejadas, poderá defini-las de forma ainda mais precisa no futuro. Para além de _utilizadores específicos_, _administradores_ e _ninguém_, **determinados grupos** estão agora também disponíveis como opção.

No futuro, haverá uma opção para [exportar]({{< relref "help/startseite/bases/speichern-einer-base-als-dtable-datei" >}}) bases sem os anexos carregados no gestor de ficheiros se estes excederem o limite de exportação de 100 MB por base.

Em termos de API, o SeaTable 4.3 suporta pela primeira vez [consultas JOIN](https://developer.seatable.com/scripts/sql/reference/), com as quais é possível consultar os registos de dados de diferentes tabelas que partilham uma intersecção comum de atributos. Pode obter mais informações sobre este assunto no Manual do Programador.

## Instalação simplificada do SeaTable e componentes adicionais

Por fim, temos uma surpresa especial para os **clientes locais**: para coincidir com o lançamento da versão 4.3 do SeaTable Cloud, também revimos as **instruções de instalação** no nosso [manual de administração](https://admin.seatable.com).

O nosso principal objetivo é facilitar ainda mais a **instalação e as futuras actualizações do seu próprio servidor SeaTable**. Por exemplo, no futuro, o serviço será iniciado automaticamente quando iniciar o contentor associado e já não terá de iniciar manualmente as actualizações da base de dados. Estas são apenas algumas das muitas pequenas melhorias que irão facilitar a sua vida como administrador e que podem agora ser encontradas no manual de administração.

Também simplificamos a instalação de componentes adicionais, como o **pipeline Python** para executar código Python no SeaTable e a **plataforma de automatização n8n**. Cada uma destas extensões é fornecida por nós pronta a utilizar e pode ser instalada com apenas alguns comandos. Assim, pode tirar ainda mais partido do seu servidor.
