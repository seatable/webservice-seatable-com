---
title: 'Páginas de consulta en aplicaciones de SeaTable'
date: 2023-12-08
lastmod: '2025-02-27'
categories:
    - 'seitentypen-in-universellen-apps'
author: 'kgr'
url: '/es/ayuda/paginas-consulta-apps-seatable'
aliases:
    - '/es/ayuda/abfrageseiten-in-universellen-apps'
    - '/es/ayuda/paginas-consulta-apps-universales'
seo:
    title: 'Páginas de consulta en SeaTable Apps'
    description: 'Busque y filtre grandes conjuntos de datos en aplicaciones de SeaTable: defina filtros, ordenaciones y campos de consulta para resultados propios.'
weight: 9
---

Con este tipo de página puede buscar en sus registros de datos valores específicos en determinados campos. Este tipo de página es especialmente útil para registros de **datos extensos**, como catálogos de productos o bibliotecas. Un caso de uso específico podría ser, por ejemplo, la consulta de un directorio de empleados.

![Páginas de consulta en aplicaciones](images/Abfrageseiten-in-Universellen-Apps.png)

## Configuración de página

Si desea cambiar la configuración de una página, haga clic en el **símbolo de rueda dentada** {{< seatable-icon icon="dtable-icon-set-up" >}} correspondiente en la barra de navegación.

![Cambiar la configuración de la página de consulta](images/Einstellungen-der-Abfrageseite-aendern.png)

## Filtros preestablecidos, clasificación y columnas ocultas

En la **configuración de la página**, defina primero la **tabla** en la que se va a buscar.

A continuación, puede definir **filtros** preestablecidos, **clasificar** y **ocultar columnas** para limitar y organizar los datos que se muestran a los usuarios. Para filtrar u ordenar, haga clic en **Añadir filtro** o **Añadir ordenación**, seleccione la **columna** y la **condición** deseadas y confirme con **Enviar**.

![Añadir filtro en páginas de consulta](images/Add-filter-on-query-pages-in-Universal-Apps.png)

Los usuarios pueden ver toda la información de los registros de datos aplicables en los **resultados de la consulta** si usted no los restringe. Por lo tanto, decida qué datos deben ser **visibles** y muestre u oculte las columnas correspondientes utilizando los **controles deslizantes**.

![Ocultar columnas en páginas de consulta](images/Hide-columns-on-query-pages-in-Universal-Apps.png)

{{< warning  headline="Nota importante"  text="Los usuarios de la aplicación **no pueden cambiar** los **filtros preestablecidos** ni las **columnas ocultas**. Por lo tanto, sólo verán las entradas filtradas, como deseen. Sin embargo, los usuarios pueden personalizar la **altura de las filas** y la **ordenación** de los registros de datos consultados." />}}

## Añadir campos de consulta

Los **campos de consulta** tienen una importancia fundamental en este tipo de páginas. Los usuarios pueden utilizarlos para buscar valores específicos en las columnas de la tabla seleccionada y **encontrar así registros de datos**. Haga clic en {{< seatable-icon icon="dtable-icon-enlarge" >}} **Añadir campo** en la configuración de la página para definir un campo de consulta.

![Añadir campos a las páginas de consulta](images/Felder-auf-Abfrageseiten-hinzufuegen.png)

A continuación, puede seleccionar la **columna** deseada y establecer si el campo de consulta debe ser **obligatorio**, si es posible realizar una **búsqueda difusa** y si se tienen en cuenta las **mayúsculas y minúsculas** al realizar las entradas.

## Añadir nota

Puede añadir una **nota** introductoria a su página de consulta, que puede contener explicaciones sobre cómo rellenar los campos de consulta, por ejemplo. Para ello, basta con activar el **control deslizante** en la configuración de la página y escribir la nota en el cuadro de texto que aparece.

![Añadir referencia a las páginas de consulta de la aplicación](images/Hinweis-auf-Abfrageseiten-der-Universellen-App-hinzufuegen.png)

## Editar los resultados de la consulta

Para poder utilizar esta función, debe **activar** el control deslizante en la configuración de la página en **¿Es editable el resultado de la consulta**?

![Hacer editable el resultado de la consulta](images/Abfrageergebnis-bearbeitbar-machen.png)

A continuación, todos los usuarios con acceso a la página de consulta pueden **editar los registros de datos** buscados.

![Editar los resultados de la consulta en las páginas de consulta de la aplicación](images/Abfrageergebnisse-bearbeiten-auf-Abfrageseiten-der-App.gif)

- Realizar una **consulta de datos con éxito**.
- Desplace el ratón hasta la **numeración de líneas** de la lista de aciertos y haga clic en el **símbolo de la doble flecha** situado delante del registro de datos que desea editar.
- Realice los cambios deseados en **los detalles de la fila** abierta.
- Haga clic en el **símbolo x** para cerrar la ventana y guardar los cambios.

{{< warning  type="warning" headline="Columnas de sólo lectura" text="Puede definir de antemano columnas que no se puedan editar. Para ello, vaya a la configuración de la página y marque las casillas de las columnas que deben ser de **sólo lectura** para los usuarios. Puede reconocer las columnas de sólo lectura por el hecho de que los campos de los detalles de la fila aparecen resaltados en gris." />}}

## Autorizaciones de páginas

En la parte inferior de la configuración de la página, puede restringir quién puede ver la página de consulta.

![Autorización para páginas de consulta de la aplicación](images/Berechtigung-fuer-individuelle-Seiten-der-Universellen-App.png)

Esta es la única [autorización de página]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}) que puede seleccionar aquí. No puede añadir o eliminar filas en la tabla a través de páginas de consulta.

Sin embargo, tras una consulta de datos satisfactoria, los usuarios de la aplicación pueden hacer clic en [los botones]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}}) de la lista de aciertos mostrada para realizar determinadas **acciones**.

![Botones de ejecución en las páginas de consulta](images/Schaltflaechen-auf-Abfrageseiten-ausfuehren.gif)

Un ejemplo de aplicación es una bolsa de trabajo interna: la página de consulta permite buscar rápidamente puestos relevantes. Si se encuentra un puesto interesante, basta con hacer clic en el botón de los resultados de la búsqueda para solicitarlo directamente.

{{< warning  headline="Atención con los botones" >}}

[Los botones]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}}) **siempre** se pueden pulsar independientemente de las autorizaciones de la página. Esto significa que todos los usuarios de la app pueden realizar determinados cambios en los registros de datos que hayas definido previamente, aunque las columnas afectadas estén bloqueadas para ellos o el usuario no esté autorizado a editar los resultados de la consulta.

{{< /warning >}}
