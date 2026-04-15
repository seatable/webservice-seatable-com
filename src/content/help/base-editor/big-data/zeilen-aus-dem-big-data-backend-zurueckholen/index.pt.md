---
title: 'Recuperar linhas da memória de big data'
date: 2023-05-11
lastmod: '2024-05-13'
categories:
    - 'big-data'
author: 'nsc2'
url: '/pt/ajuda/restaurar-linhas-big-data'
aliases:
    - '/pt/ajuda/zeilen-aus-dem-big-data-backend-zurueckholen'
seo:
    title: 'Restaurar linhas do armazenamento Big Data SeaTable'
    description: 'Saiba como restaurar linhas arquivadas do Big Data do SeaTable e devolvê-las a uma vista normal com eficiência.'

---

Para recuperar linhas da memória de big data, é necessária uma [vista de big data]({{< relref "help/base-editor/big-data/so-erstellen-sie-eine-big-data-ansicht" >}}). Nesta vista, pode [selecionar as linhas]({{< relref "help/base-editor/zeilen/mehrere-zeilen-selektieren" >}}) e movê-las de volta para uma **vista normal**.

1. Abrir uma **vista de big data**.
2. **Clique com o botão direito do rato numa linha arquivada**.
3. Seleccione a opção **Recuperar linha do arquivo**.

![Recuperar entradas do backend de Big Data](images/unarchive-rows-out-of-the-big-data-backend.png)

Em poucos segundos, as linhas seleccionadas são reescritas da memória de big data para a vista normal, perdendo assim o seu **triângulo cinzento** , que identifica as linhas como entradas de big data.
