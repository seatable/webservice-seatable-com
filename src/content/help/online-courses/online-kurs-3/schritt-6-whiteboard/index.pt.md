---
title: 'Passo 6: Quadro branco'
date: 2026-10-08
lastmod: '2026-10-08'
categories:
    - 'online-kurs-3'
author: 'bha'
url: '/pt/ajuda/curso-3-passo-6-quadro-branco'
seo:
    title: 'Passo 6 do Curso SeaTable 3: o quadro branco'
    description: 'Colabore em tempo real no quadro branco do SeaTable, na base do marketing (cursores e mensagens em direto), e combine algumas regras gráficas para mostrar o que é de quem.'
---

Nem toda a colaboração acontece numa tabela. Por vezes, uma equipa precisa de esboçar um processo, desenvolver uma ideia ou rascunhar uma disposição em conjunto: o tipo de reflexão que pertence a uma tela partilhada, e não a linhas e colunas. O SeaTable tem precisamente uma ferramenta para isso: o plugin de quadro branco.

Ao contrário de tudo o que vimos até agora, o quadro branco não contém nenhum dos seus dados e, o que determina todo este passo, não guarda nenhum registo de quem fez o quê: não há registo de atividades para um desenho. O que faz de forma brilhante é a outra metade da colaboração: trabalhar em conjunto, em direto, no mesmo espaço e ao mesmo tempo.

## A base certa para o quadro

Um quadro branco precisa de uma base que todos os que nele desenham possam editar. Acabou de passar quatro passos a aprender a não dar esse tipo de acesso a uma base cheia de dados sensíveis, e o mesmo hábito aplica-se aqui: mantenha a coordenação e os esboços fora das suas tabelas de produção, tal como a sua lista de referência de clientes fica separada da cópia de trabalho do marketing. O quadro vai para uma base que a sua colega pode editar, nunca para `Sales CRM`.

Essa base é `Campaign Hub`. É a base do próprio marketing, todos os membros do grupo `Marketing` podem editá-la, e os seus valores confidenciais nunca lá chegaram: o conjunto de dados comum deixou-os em `Sales CRM`. Também contém o quadro que lhe pertence: `Customers data flow`, o diagrama do marketing que mostra como os dados dos clientes lhe chegam, e portanto uma imagem desta mesma base. Mas ainda mostra a forma antiga, do tempo em que o marketing trabalhava a partir de uma cópia manual. Agora que os dados chegam através de um conjunto de dados comum, o diagrama tem de ser redesenhado e, como foi quem montou esse novo circuito, cabe-lhe a si atualizá-lo.

O plugin de quadro branco já está configurado em `Campaign Hub`, por isso não há nada a instalar: abra `Customers data flow` a partir da área de plugins da base. Num servidor auto-hospedado, o quadro branco é um componente à parte: se não abrir, o seu administrador de sistema poderá ter primeiro de [o instalar](https://admin.seatable.com/installation/components/whiteboard/).

Repare que uma partilha de apenas leitura não teria funcionado aqui: desenhar num quadro branco exige permissão de edição.

## Trabalhar em conjunto

Abra o quadro e está numa tela partilhada: todos os que a têm aberta ao mesmo tempo estão lá presentes, juntos. O cursor de cada pessoa desloca-se pelo quadro nas janelas dos outros, um ponteiro laser deixa um rasto que se desvanece ao longo de uma forma, e uma mensagem curta pode aparecer por momentos por baixo de um cursor. O cursor que se desloca, o rasto do laser que se desvanece, a mensagem breve: é esta a colaboração no momento que uma tabela não lhe pode dar. A animação abaixo mostra-o, com duas pessoas no mesmo quadro.

{{< zoom image="images/lvl3-whiteboard-collab.gif" alt="Dois cursores no quadro branco partilhado a fazerem sinais um ao outro, com um rasto de laser e uma mensagem por baixo de um dos cursores" >}}

## O quadro não se lembra de nada

{{< warning headline="O quadro branco não guarda histórico" text="Ao contrário da sua base, o quadro branco não guarda registo de quem desenhou o quê, nem permite anular por autor. O registo de atividades do passo 4 não tem equivalente aqui. Se for importante saber quem acrescentou alguma coisa, tem de ser o próprio quadro a mostrá-lo." />}}

Como o quadro não guarda nenhum registo, vale a pena combinar algumas regras gráficas antes de o preencher, tal como uma equipa combina regras de nomes para os seus dados. O quadro inicial usa duas:

- uma cor por departamento, para ver num relance a que equipa pertence cada elemento;
- retângulos sem preenchimento à volta do que vai junto, aqui um por base.

São apenas um ponto de partida: a sua equipa pode adotar as suas. Mantenha-as simples e poucas, e procure cumpri-las. Pode até criar um quadro à parte só para estas regras, para que todos possam consultá-las mais tarde.

## Atualizar o quadro

O quadro inicial ainda mostra a forma antiga: a lista de clientes chega ao marketing através de uma exportação manual (`manual export`) para `Customers list (manual)`. Passou o curso inteiro a substituir exatamente isso, por isso atualize o quadro: mude o nome de elementos e altere cores para que mostre como os dados dos clientes chegam hoje ao marketing. Neste caso simplificado, o objetivo é pôr as mãos nas ferramentas do quadro branco, por isso faça todas as alterações sozinho, respeitando as regras acima.

Eis o conjunto completo de ferramentas de colaboração. É altura de rever tudo o que aprendeu, e de o pôr à prova.

## Para ir mais longe

Experimente por si o lado em direto, com a Malika. Abra uma janela privada (anónima) no seu navegador, inicie aí sessão com a conta dela e abra o mesmo quadro: ela tem acesso, porque é membro do grupo `Marketing`. Uma janela privada mantém as duas sessões separadas, por isso continua com a sua própria sessão iniciada na janela habitual. Coloque as duas janelas lado a lado e, na sua, desloque o cursor pelo quadro, passe o ponteiro laser ao longo de uma forma ou deixe uma mensagem curta por baixo do cursor, e veja cada uma destas ações aparecer na janela dela no mesmo instante.

## Artigo de ajuda com mais informações

- [Instruções para o plug-in do quadro branco (tldraw)]({{< relref "help/base-editor/plugins/anleitung-zum-whiteboard-plugin-tldraw/" >}})
