---
title: 'Guía del complemento de consulta SQL'
date: 2023-05-04
lastmod: '2023-05-15'
categories:
    - 'plugins'
author: 'nsc2'
url: '/es/ayuda/guia-plugin-consulta-sql'
aliases:
    - '/es/ayuda/anleitung-zum-sql-abfrage-plugin'
seo:
    title: 'Guía del plugin de consulta SQL – comandos y ejemplos'
    description: 'Descubre cómo usar el plugin SQL de SeaTable: SELECT, DELETE, exportar resultados y tips para el backend de Big Data.'
---

El complemento de consulta SQL está perfectamente adaptado para la **ejecución** directa **de comandos SQL**, por lo que resulta interesante sobre todo para usuarios que ya tienen experiencia con bases de datos.

Una gran ventaja del plugin es que accede tanto al backend normal como al [de Big Data]({{< relref "help/base-editor/big-data/potenzial-big-data" >}}) en el curso de la consulta a la base de datos.

{{< warning  headline="Especialmente útil con grandes cantidades de datos"  text="El acceso directo a los datos de SeaTable mediante comandos SQL tiene poco sentido para pequeñas cantidades de datos. Las posibilidades de crear una vista y establecer los filtros, la ordenación y la agrupación adecuados permitirán a la mayoría de los usuarios alcanzar su objetivo más rápidamente. La consulta SQL es especialmente relevante para grandes cantidades de datos y usted ya debería estar familiarizado con la sintaxis SQL." />}}

## Ejemplos de aplicación

### El comando SQL SELECT

Probablemente el comando SQL más utilizado es el comando **SELECT**, que se utiliza para consultar entradas. Una consulta simple de las columnas _Nombre_ y _Número_ de la tabla _Tiempo_ tendría el siguiente aspecto:

```
SELECT Nombre, Número FROM Tiempo
```

Tras introducir el comando, se buscan en la base de datos los **valores definidos** y los resultados se muestran automáticamente en forma de tabla.

![Resultados de una consulta de datos mediante el comando SQL SELECT](images/results-data-sql-query.png)

### Transferencia de los resultados como una nueva tabla

Mediante la función **Exportar a nueva tabla**, puede exportar los datos encontrados a una nueva tabla dentro de la misma base.

![Exportación de los valores encontrados mediante la consulta de datos SQL a una nueva tabla](images/export-data-sql-query-to-a-new-table.png)

![Tabla recién creada con los datos encontrados previamente mediante comando SQL con el plugin](images/new-table-with-sql-data.png)

### El comando SQL DELETE

**DELETE** es otro comando de uso frecuente que se utiliza para **borrar entradas** rápidamente. Por ejemplo, el siguiente comando borra todos los datos de la tabla _Hora_.

```
DELETE FROM Tiempo
```

Después de introducir el comando, se borran **todas las** entradas de la tabla **Horarios**. Sin embargo, puede restaurar las filas a través del [registro base]({{< relref "help/base-editor/historie-und-versionen/historie-und-logs" >}}#base-log).

![Introducción del comando SQL DELETE para eliminar datos de una tabla](images/query-delete-from-table.png)

## Resumen de los comandos SQL compatibles

SeaTable no soporta todos, pero sí la mayoría de los comandos SQL. Para obtener una lista completa y más detalles, consulte el [Manual de programación de Sea](https://developer.seatable.com/scripts/) Table.
