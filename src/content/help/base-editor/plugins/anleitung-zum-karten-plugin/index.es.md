---
title: 'Guía de plugins de mapas'
date: 2023-02-06
lastmod: '2023-06-29'
categories:
    - 'plugins'
author: 'vge'
url: '/es/ayuda/plugin-mapas-seatable'
aliases:
    - '/es/ayuda/anleitung-zum-karten-plugin'
seo:
    title: 'Guía del plugin de mapas SeaTable: funciones detalladas'
    description: 'Visualiza ubicaciones en SeaTable: instala el plugin de mapas, configura marcadores, imágenes y opciones avanzadas para geolocalización.'


---

Si ha creado una columna de texto con direcciones o topónimos en su tabla o ha utilizado el tipo de columna [Geoposición]({{< relref "help/base-editor/spaltentypen/die-geopositions-spalte" >}}), puede utilizar el **complemento de mapa** para mostrar las ubicaciones introducidas en la columna.

Para activar el plugin, siga las instrucciones del artículo [Activar un plugin en una base]({{< relref "help/base-editor/plugins/aktivieren-eines-plugins-in-einer-base" >}}).

## Funciones del complemento de mapas

### Zoom

Para hacer zoom, utilice el **símbolo más/menos** situado en la esquina superior izquierda o simplemente gire la **rueda del ratón**.

![Zoom en el plugin de mapas](images/zoom.png)

### Cambiar la sección del mapa

Mueva la sección del mapa **haciendo clic y arrastrando** con el ratón.

![Plugin de mapas en movimiento](images/Karten-Plugin.gif)

### Descargar mapa

Descargue la sección del mapa como archivo de imagen pulsando el **botón de descarga**.

![El botón de descarga del plugin de mapas](images/download-button.png)

### Modo de pantalla completa

Amplíe la ventana del complemento cartográfico para que ocupe toda la interfaz de usuario pulsando {{< seatable-icon icon="dtable-icon-full-screen" >}}.

![Visualización a pantalla completa en el complemento de mapas](images/ganzer-bildschirm.png)

## Opciones de configuración del complemento de mapas

Haga clic en el **símbolo de la rueda dentada** para abrir los ajustes.

![Configuración del plugin de mapas](images/setting.png)

Dispone de las siguientes opciones de configuración:

- Tipo de mapa
- Tabla y vista
- Dirección
- Color del marcador
- Campo de visualización

### Tipo de mapa

Decida entre la visualización estándar con **chinchetas de ubicación** o utilizar **imágenes** para marcar las ubicaciones.

![Mapa plugin el mapa por defecto](images/default-map.png)

Si decide mostrar imágenes, debe especificar la [columna de]({{< relref "help/base-editor/spaltentypen/die-bild-spalte" >}}) imágenes desde la que se mostrarán las imágenes.

![La visualización de imágenes en el complemento de mapas](images/bildanzeige.png)

### Tabla y vista

Si ha creado varias tablas en su base, puede seleccionar en este punto qué tabla se va a utilizar. Lo mismo ocurre con las vistas.

{{< warning  headline="Nota"  text="También puede crear **varios mapas** para una base si ha creado más de una tabla o varias vistas de una tabla." />}}

### Dirección

Establezca aquí una columna de texto en la que haya introducido direcciones o topónimos, o una [columna de geoposición]({{< relref "help/base-editor/spaltentypen/die-geopositions-spalte" >}}) a partir de la cual se mostrarán las ubicaciones en el mapa. Tenga en cuenta que el complemento de mapa sólo funciona si ha utilizado una columna de este tipo en su tabla.

### Color del marcador

Si ha [marcado con color las filas]({{< relref "help/base-editor/ansichten/farbliche-markierung-von-zeilen" >}}) o creado [columnas de selección única]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}}) con opciones de color, puede seleccionar en este punto cuál de ellas debe determinar el **color de las marcas del mapa**.

### Campo de visualización

Hasta ahora, había que situar el puntero del ratón sobre un marcador cartográfico para que su **etiqueta** fuera visible. Si desea etiquetar permanentemente las ubicaciones, puede definir aquí una columna a partir de la cual se mostrarán las entradas respectivas junto a las chinchetas de ubicación.

![Campo de visualización del plugin de mapas](images/anzeigefeld-1.png)

## Crear varios mapas

1. Haga clic en el **signo más** situado a la derecha del título del primer mapa.
2. Asigne un **nombre** a la mapa y confirme con **Enviar**.
3. En la **configuración**, defina a qué vista de tabla y a qué columna debe hacer referencia el nuevo mapa.
