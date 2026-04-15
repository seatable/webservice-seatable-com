---
title: 'Récupérer des lignes dans le stockage de big data'
date: 2023-05-11
lastmod: '2024-05-13'
categories:
    - 'big-data'
author: 'nsc2'
url: '/fr/aide/recuperer-lignes-big-data'
aliases:
    - '/fr/aide/zeilen-aus-dem-big-data-backend-zurueckholen'
seo:
    title: 'Récupérer des lignes du stockage Big Data SeaTable'
    description: 'Apprenez à récupérer les lignes archivées du stockage Big Data dans SeaTable et à les remettre dans une vue normale rapidement.'

---

Pour récupérer des lignes de la mémoire Big Data, vous avez besoin d'une [vue Big Data]({{< relref "help/base-editor/big-data/so-erstellen-sie-eine-big-data-ansicht" >}}). Dans cette vue, vous pouvez [sélectionner les lignes]({{< relref "help/base-editor/zeilen/mehrere-zeilen-selektieren" >}}) et les déplacer à nouveau vers une vue **normale**.

1. Ouvrez une **vue Big Data**.
2. Faites un **clic droit sur une ligne archivée**.
3. Sélectionnez l'option **Récupérer la ligne dans les archives**.

![Récupérer des entrées dans le backend Big Data](images/unarchive-rows-out-of-the-big-data-backend.png)

En l'espace de quelques secondes, les lignes sélectionnées sont réécrites de la mémoire Big Data vers la vue normale et perdent ainsi leur **triangle gris** , qui identifie les lignes comme des entrées Big Data.
