---
title: 'Como funcionam as automatizações'
date: 2023-01-31
lastmod: '2025-12-01'
categories:
    - 'automationen'
author: 'kgr'
url: '/pt/ajuda/funcionamento-automacoes-seatable'
aliases:
    - '/pt/ajuda/funktionsweise-von-automationen'
seo:
    title: 'Como funcionam as automações no SeaTable?'
    description: 'Saiba como as automações otimizam processos no SeaTable: gatilhos, ações, condições e exemplos práticos de workflows eficientes.'
weight: 4
---

As automatizações são uma característica poderosa do SeaTable que lhe permite automatizar processos. Ao automatizar passos, não só poupa tempo, como também minimiza o erro humano ao trabalhar com dados.

## Informação básica

- As automatizações são sempre criadas como regras de automatização individuais que se relacionam com uma **vista de tabela** específica.
- Os dois componentes mais importantes de uma automatização são o **evento de disparo** e **as acções automatizadas**.

## Eventos de desencadeamento

O chamado gatilho é um evento que actua como um **acionador** para a automatização. Define-se este evento individualmente para cada regra de automatização. O facto de **linhas terem sido adicionadas ou editadas** numa vista de tabela pode funcionar como um acionador. Uma **hora** específica num intervalo definido (diário, semanal ou mensal) também pode acionar uma automatização.

Para certos eventos, tais como a adição de entradas, também é possível fazer outras **configurações**. Por exemplo, pode determinar se **todas as colunas** da vista de tabela ou apenas as colunas seleccionadas devem ser **monitorizadas** para a ocorrência do evento de disparo. Se seleccionar colunas individuais neste contexto, a automatização só é accionada se o evento ocorrer nas colunas seleccionadas.

Além disso, é possível limitar as **condições do** evento de disparo para que a automatização só seja disparada se **determinados dados** forem encontrados em determinadas colunas. Por exemplo, é possível definir valores exactos que devem estar presentes numa coluna seleccionada após adicionar ou alterar uma entrada para que a automatização seja accionada.

Pode descobrir tudo o resto no artigo [Acionadores de automatização]({{< relref "help/base-editor/automationen/automations-trigger" >}}).

## Acções automatizadas

As acções automatizadas são aquelas **acções** que são **desencadeadas** pela ocorrência do evento de desencadeamento especificado. As acções automatizadas são portanto sempre uma **consequência** de eventos de desencadeamento e **só** ocorrem quando esses eventos ocorrem sob as condições especificadas.

Dependendo do evento seleccionado, pode escolher entre diferentes acções, tais como **enviar um e-mail** ou **notificação** a um ou mais utilizadores, **acrescentar, alterar ou bloquear um registro** ou **executar de scripts Python ou funções de IA**.

Para muitas acções, também tem de cumprir **requisitos** adicionais. Por exemplo, precisa de determinados tipos de colunas, uma conta de correio eletrónico ou modelos no plug-in de design de página ou de design de relatório para tornar possíveis automações mais complexas.

{{< warning  headline="Nota"  text="É claro que tem a opção de atribuir **várias acções** a um único evento de disparo." />}}

Se quiser saber mais sobre acções automatizadas, leia o artigo [Acções de Automatização]({{< relref "help/base-editor/automationen/automations-aktionen" >}}).

## Funcionalidade das automatizações

A funcionalidade das automatizações é explicada mais pormenorizadamente a seguir, através de um exemplo.

{{< warning  headline="Nota importante"  text="O exemplo fictício destina-se a ilustrar o **funcionamento básico** das automatizações com complexidade reduzida e, portanto, contém apenas uma quantidade relativamente pequena de dados. Como regra geral, as automatizações têm um efeito muito maior em **conjuntos de dados mais extensos**." />}}

![Tabela de exemplo](images/example-for-a-simple-automation-1.jpg)

Pode utilizar a tabela de exemplo apresentada na imagem no departamento de RH de uma empresa para registar o **estado de emprego** e o estado dos **pagamentos salariais**, para além dos dados dos empregados.

Em seguida, crie uma **automação** para a vista de tabela para automatizar uma etapa de trabalho. Especificamente, quando um empregado deixa a empresa, ou seja, sempre que a entrada na coluna **Status** muda de "empregado" ou "freelancer" para "terminado", "licença parental" ou "reformado", a entrada na coluna **Payroll** deve ser definida de "ativo" para "inativo".

![Exemplo de automatização](images/example-for-a-simple-automation-2.jpg)

Para automatizar esta etapa do processo, defina primeiro o evento "Quando uma linha é alterada" como um **acionador**. Nas definições do acionador, selecione a **tabela** e a **vista** e introduza a coluna "Estado" como a **coluna monitorizada**. Como **condição** específica para acionar a automatização, especifique que a linha editada na coluna correspondente deve ter o valor "terminado", "licença parental" ou "reformado".

![definição do evento de acionamento](images/example-for-a-simple-automation-3.jpg)

Em seguida, selecione a opção **Modificar registro** como **ação automatizada**. Especificamente, a entrada na coluna "Payroll" deve ser definida de "ativa" para "inativa" depois de o evento de disparo ter sido acionado.

![definição da ação automática do exemplo de automatização](images/example-for-a-simple-automation-4.jpg)

Depois de ter criado a automatização, a alteração manual da coluna "Estado" **automaticamente** despoleta o desejado **ajuste do registo** na coluna "Payroll".

![execução do exemplo de automatização](images/example-for-a-simple-automation.gif)