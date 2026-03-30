---
title: 'Crear una nueva tabla con un registro común'
date: 2022-12-15
lastmod: '2024-06-12'
categories:
    - 'gemeinsame-datensaetze'
author: 'nsc2'
url: '/es/ayuda/crear-tabla-conj-datos-compartido'
aliases:
    - '/es/ayuda/mit-einem-gemeinsamen-datensatz-eine-neue-tabelle-anlegen'
seo:
    title: 'Crear tabla con conjunto de datos compartido SeaTable '
    description: 'Descubre cómo importar un conjunto de datos común y crear una nueva tabla sincronizada en SeaTable. Requisitos y pasos detallados.'
---

Para utilizar un registro común en otra base, puede importar la vista de tabla correspondiente del registro común a la base deseada. Para ello, cree una nueva tabla en la base con el conjunto de datos correspondiente. A continuación, puede trabajar con los datos del conjunto de datos común o de la vista de tabla, incluidas las condiciones específicas de filtrado y ordenación, en la base seleccionada.

## Requisitos

Para poder crear una nueva tabla en una base con un registro de datos compartido, la base debe cumplir uno de los dos requisitos siguientes:

1. La base debe pertenecer al **grupo** en el que se **creó** el registro de datos compartidos.
2. La base debe pertenecer a un **grupo** al que se haya **liberado** previamente el registro de datos compartidos.

{{< warning  headline="Nota importante"  text="Una base **debe** cumplir uno de estos dos requisitos para que se pueda crear en ella una nueva tabla con un registro de datos compartido. Sin embargo, **si** ninguno de los dos requisitos previos se aplica a una base, **no** es posible crear una nueva tabla con un registro de datos compartido." />}}

## Crear una nueva tabla con un registro común

![Crear una nueva tabla con un registro común](images/image-how-to-create-a-new-table-with-a-common-dataset.png)

1. Abra una **tabla** que esté en una base que cumpla uno de los **requisitos** descritos anteriormente.
2. Haga clic en el **símbolo más** para crear una nueva tabla.
3. Haga clic en **Importar registro compartido**.
4. Seleccione un **registro común**.
5. A continuación, el conjunto de datos comunes se importa a su Base como una **nueva tabla**.

Si la **importación** del conjunto de datos comunes se realiza correctamente, aparece el siguiente mensaje:

![El siguiente mensaje aparece cuando el Conjunto Común de Datos se ha importado correctamente](images/Erfolgsmeldung-beim-Import-eines-GD-.png)

## Características de las tablas creadas con un conjunto de datos común

Las tablas creadas con un registro de datos compartido pueden distinguirse de otras tablas por el símbolo de **pila** delante del nombre de la tabla. Si mueve el puntero del ratón sobre el icono, un breve **texto** informativo indica también que la tabla se ha creado con un registro de datos compartido.

![Icono delante del nombre de las tablas de un conjunto de datos común.](images/icon-table-common-dataset-1.png)

Otra característica es el **carácter** en el icono de las columnas que contienen datos de un conjunto de datos **compartidos**. Las columnas de la tabla que **no** contienen datos de un registro de datos compartidos **no** tienen, por tanto, este etiquetado en el icono de la columna.

![Columna de un conjunto de datos común (izquierda) y columna normal (derecha)](images/icons-of-the-column-of-a-common-dataset-2.png)

## Consecuencias para el tratamiento de datos

La regla fundamental que debe seguir cuando trabaje con registros compartidos es que la información sólo fluya en **una dirección**. En concreto, esto significa que los cambios en los registros compartidos y en las tablas creadas con un registro compartido sólo tienen efecto en una dirección, es decir, hacia las **tablas**.

Si realiza cambios en una vista de tabla que ha publicado como **conjunto** de datos común, estos cambios también se adoptan en todas las tablas que se crearon con el conjunto de datos común correspondiente. El requisito previo para ello es una **sincronización de las tablas respectivas con el conjunto de datos**, que [puede hacerse automática o manualmente]({{< relref "help/startseite/gemeinsame-datensaetze/synchronisation-eines-gemeinsamen-datensatzes" >}}).

Si, por el contrario, realiza cambios en los datos del conjunto de datos común en una tabla que ha creado con un conjunto de datos común, estos cambios **no** afectan a la estructura del conjunto de datos común. Los cambios se aplicarán **exclusivamente** a su tabla y se **sobrescribirán de** nuevo la próxima vez que **sincronice** con el conjunto de datos.

Sin embargo, lo que permanece en su tabla durante la sincronización son los **nombres modificados de las columnas**. Por lo tanto, puede cambiar el nombre de las columnas del registro de datos compartidos de su tabla como desee.
