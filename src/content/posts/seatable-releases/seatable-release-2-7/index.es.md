---
title: 'SeaTable 2.7: Formato de celdas condicional, fijación flexible de columnas y práctico valor por defecto de la fecha - SeaTable'
description: 'Controla fácilmente los datos: reglas visuales por celda, relajate fijando columnas clave, asigna fechas automáticas y habilita protección por contraseña en bases sensibles. Encuentra entradas y enlaces más rápido, administra autenticación 2FA y explora mejoras de búsqueda y recuperación de vínculos.'
date: 2022-02-02
lastmod: '2022-02-03'
author: 'rdb'
url: '/es/seatable-release-2-7'
color: '#c29eca'
categories:
    - 'product-features'
seo:
    title: 'SeaTable 2.7: Formato condicional de celdas y fijación'
    description: 'Formato condicional, congelar columnas, valores por defecto — SeaTable 2.7 potencia la gestión de datos y la seguridad del acceso.'
---

Esta mañana, [SeaTable Cloud](https://cloud.seatable.io) se ha actualizado a la versión 2.7. Esto significa que todos los usuarios de Cloud pueden disfrutar también de las nuevas funciones y mejoras de la nueva versión, que ya está disponible para su descarga para los auto-alojadores en Docker Hub desde hace unos días. El editor de tablas es el que más se ha beneficiado del cambio de versión: el formato condicional de las celdas, la nueva operación de tratamiento de datos "Calcular clasificación", la fijación ampliada de las columnas y la función de valor por defecto para las columnas de fecha ofrecen una gran cantidad de nuevas funcionalidades. Fuera del editor de tablas, las bases protegidas por contraseña son una mejora importante. Todos los cambios se pueden encontrar - como siempre - en el [registro de cambios de SeaTable]({{< relref "pages/changelog" >}}).

## Formato condicional de las columnas

Cualquiera que trabaje habitualmente con [Excel]({{< relref "pages/landing-pages/alternatives/excel-alternative" >}}) conoce la función de formato condicional. Con la versión 2.7, esta función también está disponible en SeaTable. Con el formato condicional, se formatean o colorean las celdas en función de su valor (o de la ausencia de dicho valor) y se puede realizar así una estructuración visual de los datos y un análisis de los mismos.

Para todas las columnas, SeaTable ofrece un formato condicional basado en reglas. Una regla es la descripción de un contenido hipotético de una celda (por ejemplo, valor > 50 o fecha posterior al 31.12.2021) y una instrucción de formato. Si la regla se cumple, la celda se formatea según la instrucción. Unas reglas bien elegidas pueden, entre otras cosas, hacer fácilmente reconocibles los valores estadísticos atípicos o inusuales. Por supuesto, también puede definir varias reglas por columna para asignar requisitos exigentes.

![Formato condicional de celdas con degradado de color y reglas para valores de una columna](Conditional_cell_formatting2.png)

Si una columna tiene valores de celda numéricos, SeaTable ofrece formato por valores además de formato basado en reglas. Este formato condicional colorea las celdas con un gradiente de color. Los valores grandes se colorean con el extremo superior del gradiente, los pequeños con el extremo inferior. Esto hace que la magnitud del valor de una celda quede clara de un vistazo.

## Secuencia de valores

Si no sólo quiere mostrar el orden de magnitud de los valores de las celdas de una columna, sino que también necesita la clasificación de los valores, la nueva operación de tratamiento de datos Calcular clasificación es exactamente lo que necesita. Calcula la clasificación y escribe el resultado en una columna separada. El valor más grande obtiene la clasificación 1. Si dos o más valores de celda tienen la misma cantidad, entonces todas las celdas obtienen la misma clasificación y se saltan una o más posiciones de clasificación posteriores. La operación funciona para las columnas con contenido numérico, pero también para los tipos de columna fecha, duración y valoración.

## Fijación de columnas

En las tablas con muchas columnas, suele darse el problema de que las primeras columnas desaparecen de la pantalla al desplazarse hacia la derecha. Hasta ahora, la primera columna podía fijarse y, por tanto, mostrarse permanentemente incluso en tablas grandes. Esta función muestra un lado más flexible en la nueva versión: a partir de la versión 2.7, se pueden fijar columnas adicionales a la izquierda. De esta manera, incluso cuando se navega en tablas grandes, se sabe en qué entrada se está.

![Vista de tabla con varias columnas fijadas a la izquierda y el resto desplazable](Freeze-columns.png)

Para fijar varias columnas, basta con utilizar el ratón: mueva el puntero del ratón a la línea vertical que separa la numeración de las filas de la primera columna. Ahora arrastre el ratón hacia la derecha para establecer el número de columnas fijas. Si desea eliminar la fijación de la columna, mueva el puntero del ratón al marco entre la última columna fijada y su siguiente columna y arrastre la línea hasta la izquierda.

## Valores por defecto para la columna de fecha

![Configuración de columna de fecha con selección de fecha predeterminada estática o dinámica](Default_value_date_column.png)

Repetidamente solicitada, ahora cumplida: Después de las columnas de texto, números y selección simple, SeaTable 2.7 también ofrece a la columna de fecha una función de valor estándar. Con él se añade automáticamente un valor de fecha estático o dinámico a las nuevas entradas.

La fecha de lanzamiento de SeaTable 2.7, 2 de febrero de 2022, es un ejemplo de valor de fecha estático. Los valores de fecha dinámicos establecen una referencia relativa y cambian con el tiempo. Además de la fecha actual ("Hoy"), x días antes o después de la fecha actual también es un valor de fecha dinámico. Ambos pueden asignarse ahora en la columna de fecha con la función de valor estándar. En combinación con las funciones de fecha de la columna de fórmulas, pueden generarse automáticamente prácticamente todos los valores de fecha para las nuevas entradas, que a su vez pueden utilizarse para automatizaciones.

## Bases protegidas por contraseña

En el caso de las bases con datos confidenciales, muchos clientes quieren una protección de acceso ampliada. SeaTable 2.7 ofrece ahora dicha protección con la protección opcional por contraseña para las bases. Sólo después de introducir la contraseña se accederá a la base y se mostrarán los datos. La protección por contraseña puede ser configurada y eliminada por los propietarios para sus propias bases y por los administradores de grupo para las bases del grupo.

Las bases protegidas por contraseña se pueden compartir con otros usuarios. Por supuesto, también deben introducir la contraseña al llamar a la base. Lo mismo ocurre al copiar una base protegida por contraseña. La protección de acceso adicional no se produce a costa de una menor flexibilidad.

## ... y mucho más

Como la mayoría de las nuevas versiones, la versión 2.7 vuelve a contener más funciones dignas de mención de las que las notas de la versión pueden digerir con una extensión aceptable. Por lo tanto, a continuación se presenta una visión general de otras innovaciones:

Al enlazar entradas, el asistente de enlaces de SeaTable 2.7 ofrece una mejor función de búsqueda. Al introducir varios términos de búsqueda separados por espacios, SeaTable busca en todas las columnas de la tabla vinculada. Concretamente: si busca una determinada entrada en una fecha determinada, simplemente introduzca la fecha y, separada por espacios, otra propiedad de la entrada que busca. El asistente sólo mostrará las entradas correspondientes y le ahorrará mucho trabajo de búsqueda manual. Hasta ahora, SeaTable buscaba la entrada como un todo en una columna.

Los formularios web pueden ahora adornarse con una imagen de portada o una combinación de colores. Junto con un logotipo insertado, se pueden construir formularios atractivos e individuales. (Esta función está reservada a los abonados de la empresa).

Los administradores de equipo pueden ahora imponer la autenticación de 2 factores a los miembros de su equipo y también desactivarla individualmente. De esta forma, el administrador del equipo puede reaccionar individualmente ante el aumento de los requisitos de seguridad y desactivar más fácilmente las situaciones en las que los usuarios han perdido su segundo factor.

Hasta ahora, los enlaces de las filas borradas y luego restauradas seguían perdiéndose. Con la versión 2.7, los enlaces también se vuelven a crear cuando se restaura una fila.

La función de archivo introducida con la [versión 2.3]({{< relref "posts/seatable-releases/seatable-release-2-3" >}}) ha dado un paso más hacia el uso productivo: ahora se pueden borrar entradas del archivo y también se pueden editar. (Los enlaces, sin embargo, aún no pueden ser creados o modificados).
