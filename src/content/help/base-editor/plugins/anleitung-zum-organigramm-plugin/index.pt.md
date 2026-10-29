---
title: 'Guia para o plugin do organigrama'
date: 2024-07-18
lastmod: '2025-02-28'
categories:
    - 'plugins'
author: 'kgr'
url: '/pt/ajuda/guia-plugin-organograma'
aliases:
    - '/pt/ajuda/anleitung-zum-organigramm-plugin'
seo:
    title: 'Plugin organograma: hierarquia e equipes visuais'
    description: 'Plugin de organograma: crie hierarquias, visualize equipes ou estruturas em árvore no SeaTable. Prático e personalizável.'
---

Pode utilizar o plugin do organigrama para apresentar **hierarquias** entre os registos de dados de uma tabela. Isto é útil, por exemplo, para visualizar os cargos numa empresa ou as [tarefas superiores e subordinadas num projeto]({{< relref "templates/projects/work-breakdown-structure" >}}).

**Veja o nosso vídeo explicativo com legendas em português.**
{{< youtube OD71y5CJ7vo >}}

Pode descobrir como ativar o plugin numa base [aqui]({{< relref "help/base-editor/plugins/aktivieren-eines-plugins-in-einer-base" >}}).

![Plugin de organograma](images/Organigramm-Plugin.png)

## Requisitos e funcionalidade do plugin do organigrama

Para definir quais os registos de dados que são dependentes uns dos outros, é necessária uma [ligação que se refira a uma e à mesma tabela]({{< relref "help/base-editor/tabellen/verknuepfungen-innerhalb-einer-tabelle" >}}). A entrada que se liga nesta coluna a outra linha na mesma tabela é exibida como um **registo de dados superior**.

![Coluna de ligação para um organigrama](images/Verknuepfungsspalte-fuer-ein-Organigramm.png)

> No exemplo de aplicação com as posições numa empresa, o utilizador ligaria o respetivo gerente do empregado na coluna de ligação. Isto resulta nos níveis do organigrama: Os chefes de departamento estariam no segundo nível e o diretor-geral no topo.

Se quiser ilustrar os registos de dados no organigrama com imagens, também precisa de uma [coluna de imagens]({{< relref "help/base-editor/spaltentypen/die-bild-spalte" >}}) na tabela onde possa carregar fotografias e gráficos.

## Definir opções para um organigrama

Por defeito, já é criado um organigrama vazio quando abre o plugin do organigrama pela primeira vez. {{< seatable-icon icon="dtable-icon-add-table" >}} Se quiser criar outro organigrama, clique em **Adicionar organigrama**. Isto abre um campo de entrada no qual pode introduzir o **nome** pretendido.

![Opções para organigramas](images/Optionen-fuer-Organigramme.png)

{{< seatable-icon icon="dtable-icon-drag" >}} Para **alterar a ordem dos organogramas**, mantenha premido o botão esquerdo do rato na **área de aperto** e arraste **e largue** o organograma para a posição pretendida. Também é possível **renomear**, **duplicar** ou **eliminar** organogramas.

{{< warning  headline="Nota"  text="Se apenas tiver sido criado um organigrama no plugin, **não é possível** apagá-lo." />}}

{{< seatable-icon icon="dtable-icon-set-up" >}} Pode definir o seguinte para o organigrama através das **definições**, às quais pode aceder clicando no **símbolo da roda dentada**:

- **Tabela**: Seleccione a tabela a partir da qual o SeaTable deve gerar o organigrama.
- **Vista**: Selecionar a vista com os registos de dados a apresentar no organigrama.
- **Relação**: Seleccione a coluna de relação na qual a hierarquia se baseia.
- **Título**: Seleccione uma coluna cujos valores devem ser apresentados como um título.
- **Imagem de capa**: Seleccione uma coluna de imagens para ilustrar os registos de dados.
- **Outras colunas**: Selecionar colunas adicionais cujos valores devem ser apresentados.

![Definições do organigrama](images/Einstellungen-eines-Organigramms.png)

{{< warning  headline="Nota"  text="Atualmente, o organigrama só pode ter **um chefe** no nível superior da hierarquia. Se a sua empresa tiver vários diretores executivos, por exemplo, deve colocar o nome da empresa no topo." />}}
