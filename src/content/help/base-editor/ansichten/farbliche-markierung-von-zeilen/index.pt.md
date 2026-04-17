---
title: 'Marcação a cores das filas'
date: 2022-11-16
lastmod: '2025-02-25'
categories:
    - 'ansichtsoptionen'
author: 'vge'
url: '/pt/ajuda/marcacao-colorida-linhas-seatable'
aliases:
  - '/pt/ajuda/farbliche-markierung-von-zeilen'
seo:
    title: 'Marcação colorida de linhas no SeaTable: tutorial'
    description: 'Marque linhas com cores usando seleção simples, regras ou para duplicidades. Melhore o status visual e a análise rápida dos dados em qualquer tabela.'
weight: 27
---

A **marcação a cores das filas** serve para identificar rapidamente certos registos de dados. Isto não deve ser confundido com [colorir células]({{< relref "help/base-editor/ansichten/einfaerben-von-zellen" >}}), o que lhe permite destacar células individuais.

## A ferramenta de cores de linha

Nas opções de visualização acima de uma tabela encontrará o seguinte símbolo:

![Ferramenta de marcação a cores](images/Farbliche-Markierung-von-Zellen-1.png)

Depois de clicar na ferramenta de cores de linha, pode escolher entre **três opções** para a marcação a cores:

- Utilizar uma coluna de seleção única 
- Regras de utilização
- Destacar duplicados

![Marcação a cores das células](images/Farbliche-Markierung-von-Zellen-2.png)

A ferramenta de cores de linha está disponível não apenas nas vistas de tabela, mas também nas [vistas de calendário]({{< relref "help/base-editor/ansichten/die-kalender-ansicht" >}}) e de [linha do tempo]({{< relref "help/base-editor/ansichten/die-zeitleisten-ansicht" >}}). No entanto, nestas últimas só pode utilizar colunas de seleção única para definir a cor das linhas.

## Utilizar uma coluna de seleção única 

Para a opção **Utilizar coluna de seleção única**, é necessária uma coluna deste tipo na tabela. Isto permite-lhe marcar cada linha no **início da linha** com a cor da respectiva opção que é introduzida nesta coluna.

![Marcação a cores das células](images/Farbliche-Markierung-von-Zellen-3.png)

{{< warning  headline="Criar uma coluna de seleção única" >}}

Descubra [aqui]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}}) como criar novas colunas de seleção única.

{{< /warning >}}

## Regras de utilização

A opção **Regras de Utilização** permite-lhe definir condições para a marcação por cor.

- Clique no botão **símbolo de triângulo colorido**para mudar a cor do marcador.
  ![Marcação a cores das células](images/Farbliche-Markierung-von-Zellen-5.png)
- Determine qual dos seus **Colunas** a condição deve referir-se a.
  ![Marcação a cores das células](images/Farbliche-Markierung-von-Zellen-6.png)
- Decidir a favor do **Tipo de condição**.
  ![Marcação a cores das células](images/Farbliche-Markierung-von-Zellen-7.png)

{{< warning  headline="Selecção dos tipos de condições dependendo do tipo de coluna"  text="Note que o tipo de coluna seleccionada determina que opções tem para selecção nas condições." />}}

### Usar exemplo de regra

Neste exemplo, todas as linhas de um plano editorial que estão marcadas como concluídas na [coluna da caixa de verificação]({{< relref "help/base-editor/spaltentypen/die-checkbox-spalte" >}}) devem ser destacadas. Para tal, foi selecionada a **coluna "Publicado"**, foi utilizada a condição **"é"** e foi especificado que as linhas **com um visto** devem ser marcadas.

![Marcação a cores das linhas](images/Farbliche-Markierung-von-Zellen-9.png)

### Exemplo de uma regra com várias condições

Neste exemplo, só queremos destacar as linhas do plano editorial a cores se o **estado** da publicação não estiver "terminado", se a **data de publicação** estiver no futuro e se já existir uma **imagem** disponível.

![Regra com várias condições para a marcação de linhas coloridas](images/Regel-mit-mehreren-Bedingungen-fuer-die-farbliche-Zeilenmarkierung.png)

## Destacar duplicados

Pode destacar linhas com um ou mais valores de coluna idênticos utilizando a opção **Destacar Duplicações**. Para o fazer, seleccione a coluna que pretende verificar se existem duplicados. Desta forma pode facilmente identificar duplicados na sua tabela e corrigi-los ou eliminá-los, se necessário.

![Destacar as células duplicadas a cores](images/Farbliche-Markierung-von-Zellen-9-1.png)
