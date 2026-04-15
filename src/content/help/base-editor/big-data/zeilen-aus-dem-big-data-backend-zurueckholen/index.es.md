---
title: 'Recuperar filas del almacén de big data'
date: 2023-05-11
lastmod: '2024-05-13'
categories:
    - 'big-data'
author: 'nsc2'
url: '/es/ayuda/recuperar-filas-big-data'
aliases:
    - '/es/ayuda/zeilen-aus-dem-big-data-backend-zurueckholen'
seo:
    title: 'Recuperar filas del almacenamiento Big Data SeaTable'
    description: 'Descubra cómo recuperar filas archivadas en el almacenamiento Big Data de SeaTable y devolverlas a vistas normales fácilmente.'

---

Para recuperar filas del almacén de big data, se necesita una [vista de big data]({{< relref "help/base-editor/big-data/so-erstellen-sie-eine-big-data-ansicht" >}}). En esta vista, puede [seleccionar las filas]({{< relref "help/base-editor/zeilen/mehrere-zeilen-selektieren" >}}) y moverlas de nuevo a una vista **normal**.

1. Abra una **vista de big data**.
2. **Haga clic con el botón derecho del ratón en una fila archivada**.
3. Seleccione la opción **Recuperar fila del archivo**.

![Recuperar entradas del backend de Big Data](images/unarchive-rows-out-of-the-big-data-backend.png)

En unos segundos, las filas seleccionadas se vuelven a escribir desde el almacén de big data a la vista normal y pierden así su **triángulo gris** , que identifica las filas como entradas de big data.
