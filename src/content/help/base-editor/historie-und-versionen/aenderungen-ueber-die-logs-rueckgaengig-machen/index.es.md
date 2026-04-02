---
title: 'Deshacer cambios a través de los registros'
date: 2023-01-11
lastmod: '2023-06-22'
categories:
    - 'historie-und-versionen'
author: 'kgr'
url: '/es/ayuda/deshacer-cambios-log-seatable'
aliases:
    - '/es/ayuda/aenderungen-ueber-die-logs-rueckgaengig-machen'
seo:
    title: 'Deshacer cambios por logs en SeaTable: recuperación'
    description: 'Restaure valores, filas o columnas desde el registro de cambios SeaTable. Guía fácil para ver logs, revertir y conocer límites de restauración.'

---

SeaTable registra todas las actividades dentro de una base en un registro. Este registro puede utilizarse para restaurar no sólo valores individuales, sino también filas, columnas y tablas. Los registros permiten ver los cambios con más detalle y deshacer más que a través de la papelera de reciclaje.

## Para abrir el registro de una base

Puede abrir los registros del mismo modo que la papelera de reciclaje, haciendo clic en el icono de versiones de la esquina superior derecha.

![Abrir registros en Base](images/Logs-in-der-Base-oeffnen.png)

En el panel que se abre, encontrará los cambios más recientes que se han realizado en la base **por orden anticronológico**. Cada entrada del registro contiene la siguiente información:

- Nombre del editor
- Naturaleza del cambio
- Tabla correspondiente
- Fecha del cambio
- Descripción del cambio

![Cambios en los registros](images/Aenderungen-in-den-Logs.png)

## Cargar entradas de registro antiguas

Si se está trabajando intensamente en una base, el registro contiene un gran número de entradas y puede ser necesario **desplazarse hacia abajo en el registro**. Al desplazarse hacia abajo se cargan sucesivamente las entradas más antiguas del registro, en las que se puede buscar.

Puede ver **un máximo de las últimas 1.000 entradas** en el registro para cada base. La documentación de los cambios realizados más atrás en el tiempo se elimina y, por lo general, ya no es necesaria.

## Filtrar entradas de registro

Si desea rastrear o deshacer ciertos cambios en una base con muchos usuarios, puede volverse confuso rápidamente. Para acotar quién hizo cambios, dónde y cuándo, los registros pueden filtrarse por **usuario**, **tabla** y **periodo**. También es posible utilizar filtros combinados.

## Deshacer cambios

Puede deshacer un cambio haciendo clic en **Restaurar** mediante el **icono de tres puntos** a la derecha de la entrada del registro. La restauración se realiza inmediatamente en la tabla correspondiente y se confirma con un breve mensaje.

Una acción deshecha permanece documentada en el registro, pero no puede volver a realizarse. Un intento de hacerlo se reconoce con un mensaje de error.

{{< warning  headline="Nota"  text="Hay acciones que **no se pueden** deshacer a través de los registros. Entre ellas se incluyen, por ejemplo, los comentarios o las filas y columnas recién insertadas. Si de todas formas hace clic en el icono de los tres puntos, sólo aparecerán **Sin opciones** en lugar de la opción Restaurar." />}}
