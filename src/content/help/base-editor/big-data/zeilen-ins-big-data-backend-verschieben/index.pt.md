---
title: 'Mover linhas para o armazenamento de big data'
date: 2022-09-23
lastmod: '2024-05-13'
categories:
    - 'big-data'
author: 'cdb'
url: '/pt/ajuda/transferir-linhas-big-data-backend'
aliases:
    - '/pt/ajuda/zeilen-ins-big-data-backend-verschieben'
seo:
    title: 'Transferir linhas para Big Data no SeaTable – tutorial completo'
    description: 'Veja como arquivar, transferir e recuperar linhas para o Big Data do SeaTable e ative essa função. Dicas para configurar e identificar dados.'

---

{{< required-version "Empresa" >}}

Só é possível criar **novas linhas** em **vistas normais** do SeaTable. Em seguida, é necessário mover manualmente ou automaticamente as linhas desejadas para a memória de big data.

{{< warning  headline="Pré-requisito" >}}

Só é possível deslocar linhas para a memória de big data se a [memória de big data já tiver sido activada]({{< relref "help/base-editor/big-data/aktivieren-des-big-data-backends-in-einer-base" >}}) na base.

{{< /warning >}}

## Mover linhas para a memória de big data

![Mover linhas para a memória de big data](images/move-rows-to-big-data.gif)

1. Clique nos **três pontos** nas opções de vista.
2. Seleccione a opção **Vista de arquivo**.
3. **Confirmar** a deslocação de todas as linhas visíveis para o armazenamento de big data.

{{< warning  headline="Dica" >}}

Por exemplo, se pretender **arquivar entradas antigas**, pode filtrar previamente a vista com os tipos de colunas [Criado]({{< relref "help/base-editor/spaltentypen/die-spalten-ersteller-und-erstelldatum" >}}) ou [Última modificação]({{< relref "help/base-editor/spaltentypen/die-spalten-letzter-bearbeiter-und-bearbeitungsdatum" >}}).

{{< /warning >}}

As linhas são então transferidas para a memória de big data. Como resultado, elas não são mais visíveis na vista normal. [Crie uma vista de big data]({{< relref "help/base-editor/big-data/so-erstellen-sie-eine-big-data-ansicht" >}}) para exibir dados no armazenamento de big data.

## Arquivamento automático

Também pode criar uma regra de **automatização com a ação "Arquivar"** para que SeaTable mova automaticamente as linhas de uma vista para o armazenamento de big data num momento específico.

Pode obter mais informações sobre isto em [Acções de automatização]({{< relref "help/base-editor/automationen/automations-aktionen" >}}).

## Como é que se pode reconhecer se os dados estão ou não no armazenamento de big data?

As linhas que estão armazenadas na memória de big data têm um pequeno **triângulo cinzento na coluna de numeração**.

**É bom saber:**

- Numa [vista normal]({{< relref "help/base-editor/ansichten/anlegen-einer-neuen-ansicht" >}}), **não** são apresentadas **quaisquer linhas da memória de big data**.
- Numa [vista de big data]({{< relref "help/base-editor/big-data/so-erstellen-sie-eine-big-data-ansicht" >}}), **todas as linhas** podem ser apresentadas, independentemente do local onde estão atualmente armazenadas.

## Recuperar registos da memória de big data

Pode descobrir como recuperar entradas da memória de big data [neste artigo]({{< relref "help/base-editor/big-data/zeilen-aus-dem-big-data-backend-zurueckholen" >}}).
