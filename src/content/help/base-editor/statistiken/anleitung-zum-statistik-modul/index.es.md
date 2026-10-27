---
title: 'Instrucciones para el módulo estadístico'
date: 2023-02-06
lastmod: '2024-03-18'
categories:
    - 'statistiken-und-datenanalyse'
author: 'vge'
url: '/es/ayuda/modulo-estadisticas-guia-seatable'
aliases:
    - '/es/ayuda/anleitung-zum-statistik-modul'
seo:
    title: 'Estadísticas y gráficos en SeaTable: guía del módulo'
    description: 'Genere dashboards y gráficos en SeaTable con el módulo de estadísticas. Analice y visualice datos fácilmente con opciones de personalización en tiempo real.'
weight: 1
---

El **módulo de estadísticas** le permite visualizar los datos de su tabla en forma de diversos **gráficos** y **diagramas**. Esto es extremadamente útil para su trabajo en SeaTable: gracias a los **cuadros de mando**, siempre tendrá una visión general de las cifras y la evolución estadística de su base.

![Módulo estadístico](images/erweitertes-statistik-plugin-release-notes.gif)

## Abrir el módulo de estadísticas

El módulo de estadísticas está configurado por defecto en todas las bases. Siempre puedes acceder a él a través del botón "Estadísticas" de la **cabecera de** la base.

![Módulo de estadísticas en la cabecera base](images/statistic-plugin-in-base-header.jpg)

## Crear un gráfico

1. Abra el módulo de estadísticas y pulse el botón {{< seatable-icon icon="dtable-icon-add-table" >}} **Añadir gráfico** en la esquina superior derecha.

Puede elegir entre distintos **tipos de** gráficos y diagramas. Desplácese por la selección o haga clic en los iconos etiquetados de la barra de opciones para saltar directamente a la ubicación deseada.

![Navegue por el módulo de estadísticas.](images/Navigieren-im-Statistik-Plugin-1.png)

2. Seleccione el **tipo** adecuado para sus estadísticas y haga clic en **Enviar**.

### Configuración de datos

3. Determine de qué **tabla** y **vista** debe obtener los datos el gráfico.
4. Dependiendo del gráfico, puede realizar diferentes **configuraciones de datos**: para un gráfico de barras, por ejemplo, qué valores desea mostrar en los **ejes X e Y**.

![Crear nuevo gráfico en el módulo de estadísticas.](images/Dateneinstellungen.png)

El trabajo detallado en un gráfico de columnas se inicia seleccionando la columna que debe proporcionar los **valores para el eje X**. Haga clic en el campo desplegable correspondiente y seleccione la **columna**. Con un control deslizante puede establecer si desea considerar **filas vacías** en el gráfico.

A continuación, elija cómo se mostrarán los valores en **el eje Y**. Puede elegir entre el **número de** entradas que tienen un determinado valor en la columna seleccionada y la opción del **campo Suma**, donde puede evaluar la suma, la media, el número de valores únicos, el máximo o el mínimo en **columnas numéricas**. Para los gráficos **agrupados** o **apilados**, puede especificar una columna de opciones por la que desee agrupar.

Todos los cambios de ajuste se realizan **en tiempo** real, es decir, el diagrama se **actualiza** inmediatamente **con** cada cambio de ajuste. De este modo, puede ver directamente si ha logrado el resultado deseado o necesita reajustarlo.

### Ajustes de estilo

5. Póngale un **título** al gráfico. Para ello, haga clic en la pestaña **Estilo del gráfico** e introduzca el nombre deseado.
6. Si el gráfico que ha elegido permite **ajustes de estilo**, puede configurar, por ejemplo, los **títulos de los ejes X e Y**, los **colores** o las **etiquetas de los datos**.

![Ajustes al añadir un nuevo gráfico en el módulo de estadísticas.](images/Stileinstellungen.png)

## Gráficos en el salpicadero

7. Después de cerrar la ventana de configuración, el gráfico guardado aparecerá en su **panel de control**.

Puede crear **varios cuadros de** mando y crear tantos gráficos como desee en cada uno de ellos. Para cambiar el **orden de los gráficos**, arrástrelos **y suéltelos** en el lugar deseado. Para ello, mueva el puntero del ratón sobre el **título de** un gráfico hasta que aparezca una **cruz en forma de flecha** y mantenga pulsado el **botón del ratón**.

![Mover gráficos en el módulo de estadísticas.](images/Dashboard_Sortierung_Statistik-Plugin.gif)

## Opciones para un gráfico

Al mover el puntero del ratón sobre un gráfico, aparecen en la esquina superior derecha los símbolos de una **flecha doble** {{< seatable-icon icon="dtable-icon-open" >}} y **de tres puntos** {{< seatable-icon icon="dtable-icon-more-level" >}}. Seleccione la flecha doble para visualizar un gráfico a **pantalla completa**. Puede acceder a todas las demás opciones a través de los tres puntos:

- Editar gráfico
- Copiar gráfico
- Exportar como imagen
- Borrar gráfico

![Módulo de estadísticas Opciones gráficas](images/Statistik-Plugin-Grafik-Optionen.gif)

## Otras opciones de visualización

Haciendo clic en {{< seatable-icon icon="dtable-icon-full-screen" >}} puede visualizar toda la ventana del módulo de estadísticas a **pantalla completa**.

![Módulo de estadísticas a pantalla completa](images/Statistik-Plugin-Vollbildmodus.gif)

Puede cambiar entre los **modos claro y** oscuro utilizando los símbolos {{< seatable-icon icon="dtable-icon-night-mode" >}} y {{< seatable-icon icon="dtable-icon-day-mode" >}}.

![Módulo de estadísticas del modo nocturno](images/Statistik-Plugin-dark-mode.png)
