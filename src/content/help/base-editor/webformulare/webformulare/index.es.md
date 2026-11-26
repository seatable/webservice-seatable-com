---
title: 'Formularios web'
date: 2022-08-25
lastmod: '2026-11-26'
categories:
    - 'webformulare'
author: 'cdb'
url: '/es/ayuda/formularios-web-seatable'
aliases:
    - '/es/ayuda/webformulare'
seo:
    title: 'Formularios web SeaTable: creación, personalización y uso sencillo'
    description: 'Formularios web en SeaTable: cree, configure y pruebe formularios para captar datos fácilmente de usuarios internos y externos.'
weight: 1
star: true
---

Los **formularios web** son la herramienta preferida para que los miembros del equipo y terceros externos introduzcan nuevos registros en sus tablas. Los usuarios acceden a un formulario a través de un **enlace**, por lo que **no es necesario compartir** la tabla. Por ello, los formularios web son especialmente adecuados para la recopilación de datos por parte de un gran número de **personas dentro y fuera de su equipo**.

Familiarícese con la función de formularios de SeaTable para recopilar datos cómodamente a través de formularios web.

## Funcionamiento de los formularios web

El formulario web clásico es ideal para **encuestas en línea**, **solicitudes** y la recopilación estructurada de nuevos datos. Las columnas de la tabla se integran mediante **campos de formulario** y los usuarios son guiados a través del proceso de cumplimentación. Para el acceso, usted crea un enlace que permite a los usuarios **sin cuenta de usuario de SeaTable** rellenar el formulario web. Un formulario web cumplimentado corresponde a **un nuevo registro** o a una fila añadida en la tabla correspondiente.

Los formularios web siempre hacen referencia a una **tabla** de la base abierta. Por lo tanto, debe seleccionar primero la tabla correspondiente antes de crear un formulario. Puede crear y guardar **cualquier número** de formularios web en cada base.

## Crear un formulario

Abra la gestión de formularios a través del botón {{< seatable-icon icon="dtable-icon-form" >}} **Formularios** situado en la parte superior derecha de la cabecera de la base. Si aún no se ha creado ningún formulario en la base, la gestión de formularios aparecerá como una lista vacía. En caso contrario, los formularios existentes se mostrarán en la ventana abierta.

![Crear un formulario clásico](images/create-a-web-form.gif)

Para crear un [nuevo formulario web]({{< relref "help/base-editor/webformulare/anlegen-eines-webformulars" >}}), haga clic en **Crear formulario web** en la parte inferior de la gestión de formularios y, a continuación, seleccione **Formulario clásico**.

Introduzca ahora el **nombre** del nuevo formulario web que también debe mostrarse en la gestión de formularios. Utilice un nombre conciso para no perder la visión de conjunto si tiene muchos formularios. Por supuesto, puede modificar el nombre más adelante.

Al hacer clic en el **icono del lápiz** {{< seatable-icon icon="dtable-icon-rename" >}} se abre el **editor de formularios web** con su vista en dos partes: a la izquierda se muestra el formulario web en modo borrador; a la derecha se encuentran los **ajustes**.

Existen numerosas [opciones de configuración]({{< relref "help/base-editor/webformulare/konfigurationsmoeglichkeiten-eines-webformulars" >}}) para adaptar rápida y fácilmente un formulario web a sus deseos e ideas.

En los **ajustes del formulario web** de la derecha puede tomar las siguientes decisiones:

- ¿A qué **tabla** está vinculado el formulario?
- ¿Qué **elementos estáticos** y **campos de tabla** desea incluir en el formulario?
- ¿Desea crear un **formulario de varias páginas** mediante saltos de página?
- ¿Debe enviarse una **notificación** (a usted) cuando se envíe el formulario?
- ¿Quién puede **acceder** al formulario?
- ¿Deben ser **obligatorios** todos los campos?
- ¿Debe mostrarse una **barra de progreso** a las personas que rellenan formularios de varias páginas?
- ¿Debe aparecer "Powered by"?
- ¿Qué **mensaje** se muestra al participante después de enviar el formulario?
- ¿Desea **redirigir** al participante a **un sitio web** después de enviar el formulario?
- ¿Tiene el formulario una **fecha límite de envío**?
- ¿Tiene el formulario un **límite de envíos**?

Los campos disponibles en el formulario dependen de las **columnas** de la tabla seleccionada. Si añade o elimina columnas en la tabla, los campos disponibles en los ajustes se adaptan automáticamente. Los **nombres** y el **orden** de los campos de tabla se toman directamente de la tabla subyacente.

![Añadir y configurar campos en un formulario web](images/Add-fields-to-a-web-form.gif)

**Arrastre y suelte** los campos de la tabla en su borrador o haga clic en el **símbolo más** a la derecha del nombre de la columna. Puede cambiar el orden de los campos en el formulario web como desee haciendo clic en el **símbolo de seis puntos** {{< seatable-icon icon="dtable-icon-drag" >}} en la esquina derecha de un campo y arrastrando y soltando el campo en la posición deseada.

{{< warning  type="warning" headline="Tipos de columnas no seleccionables"  text="Las columnas del tipo Colaborador, Fórmula, Fórmula para enlaces, Creador, Fecha de creación, Último modificador, Última modificación, Autonumeración y Botón no pueden incluirse en un formulario web." />}}

En el borrador, puede hacer clic en cada campo, lo que le llevará a los **ajustes del campo**. Para cada campo puede especificar si...

- se debe mostrar en el formulario un **nombre de campo** distinto del nombre de la columna,
- un campo recibe un **texto de ayuda** complementario como indicación para rellenarlo,
- un campo es **obligatorio**,
- un campo debe contener un **valor por defecto**,
- la visualización del campo depende de una **condición**.

{{< warning  headline="Campos de selección"  text="Para los campos de selección única y múltiple, también puede especificar si los valores se muestran como una **lista** o como un **desplegable**." />}}

Para comprobar qué aspecto tiene el formulario para el destinatario, haga clic en el botón **Página del formulario web** de la esquina superior derecha. El formulario se abrirá en una nueva pestaña tal y como lo vería otro usuario.

## Compartir el formulario

Para que otras personas puedan acceder al formulario, necesita un **enlace**. Puede obtener el enlace del formulario en el editor de formularios web a través del botón {{< seatable-icon icon="dtable-icon-share" >}} **Compartir**. Puede utilizar el **enlace generado automáticamente** o crear **sus propios enlaces** y ampliarlos con [valores prerrellenados]({{< relref "help/base-editor/webformulare/formularfelder-per-url-vorbefuellen" >}}).

![Nuevo diálogo de enlace de formularios en SeaTable 4.3](images/Formularlink-Dialog.gif)

{{< warning  headline="Enlaces propios"  text="La parte definida por el usuario que se añade al enlace debe tener **entre 5 y 30 caracteres** y solo puede contener **letras**, **números** y **guiones**. Además, cada URL debe ser única: si una URL definida por el usuario ya está en uso, aparece un mensaje de error." />}}

Antes de enviar el enlace del formulario o hacerlo accesible al público, debe probar el formulario exhaustivamente.

## Probar el formulario

Las pruebas exhaustivas evitan la frustración de los destinatarios. Los problemas pueden deberse a ambigüedades o conflictos en el formulario. En el peor de los casos, un formulario no puede enviarse porque no se puede rellenar un campo obligatorio (por ejemplo, si no se han definido valores para una selección única).

Abra el formulario web para probarlo. Desde el editor de formularios web, esto se hace a través del botón **Página del formulario web**. Desde la vista de tabla, abra primero la gestión de formularios y, a continuación, haga clic en el nombre del formulario web. En ambos casos, el formulario web se abre en una nueva pestaña del navegador.

![Probar un formulario web](images/Test-a-web-form.gif)

Los valores introducidos en el formulario se guardan en la tabla vinculada. No olvide borrar los datos de prueba de la tabla antes de la recopilación de datos propiamente dicha.

## Modificar el formulario

Puede modificar los formularios web en cualquier momento utilizando el editor de formularios web. Para volver al editor, abra la gestión de formularios, sitúe el puntero del ratón sobre el nombre del formulario y, a continuación, haga clic en el **icono del lápiz** {{< seatable-icon icon="dtable-icon-rename" >}} situado a la derecha del nombre.

## Copiar el formulario

Si ya ha creado un formulario que solo desea modificar ligeramente para otro caso de uso, puede copiar el formulario. Para ello, sitúe el puntero del ratón sobre el nombre del formulario y haga clic en el **icono de copia** {{< seatable-icon icon="dtable-icon-copy" >}} situado a la derecha del nombre.

## Eliminar el formulario

Puede eliminar formularios web en cualquier momento a través de la gestión de formularios. Sitúe el puntero del ratón sobre el nombre del formulario y, a continuación, haga clic en el **icono de la papelera** {{< seatable-icon icon="dtable-icon-delete" >}} situado a la derecha del nombre.

![Opciones de la gestión de formularios](images/form-management-options.png)
