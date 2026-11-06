---
title: 'SeaTable 7.0: geração de páginas com IA, chat de IA pronto para produção e automatizações mais inteligentes'
description: 'O SeaTable 7.0 gira em torno da IA. Descreva uma página em linguagem natural e o App Builder gera-a como página HTML. O plugin de Chat IA sai da fase beta e passa a utilizar por predefinição um modelo alojado na Exoscale. Um SDK melhorado para páginas HTML, ações de automatização novas e melhoradas, numerosas melhorias de segurança e a retirada do construtor de aplicações de consulta de dados completam esta versão.'
date: 2026-11-06
author: 'rdb'
url: '/pt/seatable-release-7-0'
color: '#dc6165'
categories:
    - 'product-features'
seo:
    title: 'SeaTable 7.0: o no-code dá um salto em frente com a IA'
    description: 'O SeaTable 7.0 coloca a IA em primeiro plano: analise as suas bases com IA e crie páginas HTML para as suas aplicações com IA e o novo SDK para HTML.'
register:
    show: true
---

Com a versão 7.0, o SeaTable dá um grande passo em frente na inteligência artificial. Duas novidades destacam-se: no App Builder, pode agora gerar páginas HTML com IA, bastando descrever o que a página deve fazer e qual o seu aspeto. E o plugin de Chat IA, apresentado como beta no SeaTable 6.1, está agora pronto para utilização em produção. Ambas as funções assentam num modelo de IA mais potente que, no SeaTable Cloud, é executado na infraestrutura do nosso parceiro Exoscale.

Mas o SeaTable 7.0 oferece muito mais do que IA. O SDK para páginas HTML, que também é utilizado pelas páginas geradas com IA, recebe quatro melhorias pedidas pelos nossos utilizadores. As automatizações ganham duas novas ações para registos ligados, e duas ações existentes tornam-se mais versáteis. Nos bastidores, esta versão inclui numerosas correções de erros e melhorias de segurança que respondem ao risco imediato representado pelos bots com IA e pelos exploits gerados automaticamente. Pequenas melhorias nos formulários, nas estatísticas e na autenticação de dois fatores completam a versão. E há uma função que se retira: já não é possível criar novas aplicações de consulta de dados, mas as existentes continuam a funcionar.

Esta manhã atualizámos o SeaTable Cloud para a versão 7.0. Recomendamos a todos os administradores de sistemas auto-alojados que façam o mesmo, sobretudo devido às melhorias de segurança. A imagem Docker do SeaTable 7.0 está disponível para transferência no [Docker Hub](https://hub.docker.com/r/seatable/seatable-enterprise/). Como sempre, encontrará a lista completa de alterações no [registo de alterações]({{< relref "pages/changelog" >}}#release-7).

## Gerar páginas HTML com IA

O SeaTable 7.0 permite-lhe criar páginas HTML diretamente no App Builder através de um chat de IA. Descreva em linguagem natural o que a página deve fazer e qual o seu aspeto, e a IA cria-a por si. Para gerar a página, a IA utiliza o SDK do SeaTable para páginas HTML (encontrará mais informações sobre o SDK na secção seguinte). Por isso, uma página gerada com IA pode ser tão capaz como uma escrita à mão.

Começar é muito simples: clique no ícone “AI” na barra esquerda. Um assistente orienta-o na configuração: atribua um nome ao projeto, escolha um estilo de interface, defina as fontes de dados e as permissões da página e descreva a página pretendida. Em seguida, a IA gera uma primeira versão e apresenta-a numa pré-visualização. A partir daí, pode aperfeiçoar a página em conversa com a IA até que faça exatamente o que precisa. Com um clique em “Publicar”, a página é adicionada à sua aplicação SeaTable.

![Gerar uma página HTML com IA no SeaTable 7.0](AI-generated_HTML_page.png)

O chat guarda toda a conversa, juntamente com cada versão da página. Assim, pode retomar o trabalho onde o deixou a qualquer momento ou voltar a uma versão anterior se uma alteração não tiver resultado. As conversas e as páginas não publicadas são conservadas durante 365 dias. E se preferir afinar uma página manualmente, pode transferi-la e editá-la à mão.

Se tiver curiosidade em saber o que acontece nos bastidores, clique na ligação “Processo de pensamento” no chat. Para cada passo, são apresentados o prompt do sistema, a sua entrada e o resultado devolvido pela IA. Uma secção de estatísticas acrescenta o tempo e o número de tokens consumidos pelo passo.

![Processo de pensamento da IA no chat de IA](Thought_process_AI_chat.png)

No SeaTable Cloud, a geração de páginas é executada num potente modelo de pesos abertos alojado pelo nosso parceiro de infraestrutura Exoscale, que também opera os servidores do SeaTable Cloud. Por conseguinte, os seus prompts e os esquemas das suas bases não são processados por nenhum outro terceiro. Os dados armazenados nas suas bases nunca são enviados para o modelo de IA. Quem auto-alojar o SeaTable pode utilizar um modelo na nuvem de um dos principais laboratórios de IA ou ligar um modelo auto-alojado à sua escolha. O SeaTable suporta todos os LLM com um endpoint compatível com a OpenAI.

{{< warning headline="Infraestrutura de IA melhorada" >}}
O modelo de IA por detrás da geração de páginas HTML é o Qwen 3.8 27B, um grande modelo de linguagem multimodal com 27 mil milhões de parâmetros desenvolvido pela Alibaba. Foi concebido para raciocínio avançado, programação, investigação, processamento de documentos e tarefas complexas de vários passos, e é disponibilizado ao abrigo da licença Apache 2.0. O Qwen 3.8 27B substitui ainda o modelo de pesos abertos [Gemma 4 E4B da Google DeepMind]({{< relref "posts/seatable-releases/seatable-release-6-0" >}}), que até agora alimentava as ações de IA automatizadas do SeaTable.
{{< /warning >}}

## SDK melhorado para páginas HTML

O SDK do SeaTable para páginas HTML liga as suas páginas personalizadas aos dados da sua base, quer as escreva você mesmo, quer as gere com IA. Com base nos comentários dos utilizadores, o SeaTable 7.0 acrescenta quatro melhorias que o tornam consideravelmente mais potente.

Em primeiro lugar, o SDK trabalha agora com os nomes dos utilizadores. Até agora, só conseguia ler os dados das linhas da base e não tinha forma de consultar nomes, pelo que as páginas apenas podiam apresentar nomes de utilizador internos como `a1b2c3…@auth.local`. Agora, as suas páginas podem mostrar rapidamente quem é quem.

Em segundo lugar, o SDK consegue identificar o utilizador com sessão iniciada. Até agora, uma página não tinha forma de saber quem a estava a ver. Com o novo método `getCurrentUser()`, as páginas podem filtrar os dados pelo utilizador atual, por exemplo, para mostrar a cada membro da equipa apenas as suas próprias tarefas.

Em terceiro lugar, o SDK disponibiliza novos métodos para adicionar e remover ligações individuais em colunas de ligação. Até agora, o método `updateRow()` só podia atualizar uma coluna de ligação no seu todo, substituindo todas as ligações existentes. Os novos métodos facilitam adicionar uma tarefa a um projeto, incluir um artigo num orçamento ou remover um participante de um seminário, sem tocar nas restantes ligações.

Em quarto lugar, o SDK suporta três novas ações: enviar um e-mail, enviar uma notificação e executar um script. Com elas, as páginas HTML podem enviar mensagens e executar scripts com um simples clique num botão, por exemplo, para confirmar uma reserva por e-mail diretamente a partir da página. As contas de e-mail e os scripts que pretende utilizar têm de estar configurados na base.

![Três novas ações em páginas HTML: enviar e-mail, enviar notificação e executar script](Action_permissions_HTML_page.png)

## Plugin de Chat IA pronto para produção

O plugin de Chat IA foi apresentado como função beta no [SeaTable 6.1]({{< relref "posts/seatable-releases/seatable-release-6-1" >}}). Permite editar e analisar bases em linguagem natural: criar registos, alterar valores, ligar linhas ou analisar dados, em português, inglês, alemão, francês e noutros idiomas. (Não são suportadas alterações ao esquema da base.)

Com o SeaTable 7.0, o plugin sai da fase beta. Com base nos comentários dos utilizadores, melhorámos tanto o plugin como o servidor MCP que utiliza. Os pedidos são agora consideravelmente mais eficientes, o que reduz significativamente o consumo de tokens. Atualizámos também a lista de modelos de IA na nuvem suportados.

O plugin tornou-se também muito mais fácil de utilizar. Durante a fase beta, tinha de fornecer o seu próprio token de API para um LLM suportado. No SeaTable Cloud, o plugin utiliza agora por predefinição o nosso próprio modelo de IA alojado na Exoscale. Os tokens consumidos são convertidos em créditos de IA e deduzidos do seu saldo de créditos de IA: 1 milhão de tokens de entrada equivale a 500 créditos de IA e 1 milhão de tokens de saída equivale a 1500 créditos de IA. Se preferir não utilizar o modelo predefinido, pode escolher outro dos modelos suportados dos principais laboratórios de IA.

{{< warning headline="Em breve para sistemas auto-alojados" >}}
O plugin de Chat IA está atualmente disponível apenas para clientes do SeaTable Cloud e do SeaTable Dedicated. Iremos disponibilizá-lo para sistemas auto-alojados nos próximos meses.
{{< /warning >}}

## Regras de automatização melhoradas

O SeaTable 7.0 traz duas novas ações de automatização, torna duas ações existentes mais versáteis e acrescenta mais detalhe ao registo de automatização.

A primeira nova ação, “Adicionar registro a uma tabela ligada”, funciona de forma muito semelhante à ação existente “Adicionar uma nova entrada a outra tabela”: cria um novo registo noutra tabela. Além disso, liga o novo registo ao registo que acionou a automatização. A segunda nova ação, “Modificar registro ligado noutra tabela”, complementa a primeira e modifica registos ligados existentes noutras tabelas. Por exemplo, quando o estado de um registo muda, todos os registos ligados dependentes podem ser atualizados de imediato. Ambas as novas ações estão disponíveis com o acionador “Quando uma linha é alterada”.

![Nova ação de automatização para registos ligados no SeaTable 7.0](New_automated_actions.png)

A ação “Converter página em PDF” gera um PDF a partir de um modelo de design de página e guarda-o numa coluna de ficheiros. No SeaTable 6.x, só estava disponível com o acionador de hora programada. Agora pode utilizá-la com todos os acionadores que têm contexto de linha: “Quando uma linha é alterada”, “Quando uma linha é adicionada” e “Numa hora programada para entradas que preencham determinadas condições”. Isto abre a porta a fluxos de trabalho totalmente automatizados. Por exemplo, um cliente envia um pedido de orçamento, o SeaTable gera o orçamento (com ou sem a ajuda da IA) e este é enviado ao cliente por e-mail.

A ação “Gerir eventos no Google Calendar” pode agora também eliminar eventos de um calendário.

Por último, o registo de automatização é mais informativo: além da hora de acionamento, indica agora também quando terminou a execução.

## E muito mais

Os formulários de várias páginas podem agora apresentar uma barra de progresso, para que quem os preenche veja quanto falta. Além disso, as mensagens de confirmação de envio suportam agora texto formatado.

As estatísticas nas aplicações SeaTable foram reconstruídas com D3.js, uma biblioteca JavaScript potente e amplamente utilizada para visualização de dados. Esta alteração técnica abre caminho a gráficos mais personalizáveis no futuro. As estatísticas na base seguir-se-ão na próxima versão menor.

Ao configurar a autenticação de dois fatores, o SeaTable apresenta agora a chave secreta, para que a possa guardar no seu gestor de palavras-passe.

E mais uma coisa: as aplicações nativas do SeaTable para iOS e Android chegam em breve. Os testes finais já estão a decorrer. Fique atento!

## Função retirada: aplicações de consulta de dados

Com o SeaTable 7.0, retirámos o construtor de aplicações de consulta de dados. Já não é possível criar novas aplicações deste tipo. As aplicações de consulta de dados existentes não são afetadas e continuam a funcionar normalmente.

Para novas aplicações, utilize as aplicações universais. Podem oferecer as mesmas funções que as aplicações de consulta de dados, e muito mais. Saiba como criá-las nas [páginas de ajuda sobre aplicações universais]({{< relref "help/app-builder/seitentypen-in-universellen-apps/ueberblick" >}}).
