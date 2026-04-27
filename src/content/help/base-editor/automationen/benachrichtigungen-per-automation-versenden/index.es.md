---
title: 'Enviar notificaciones mediante automatización'
date: 2023-02-27
lastmod: '2023-03-31'
categories:
    - 'benachrichtigungen'
author: 'nsc2'
url: '/es/ayuda/enviar-notificaciones-automatizacion'
aliases:
    - '/es/ayuda/benachrichtigungen-per-automation-versenden'
seo:
    title: 'Enviar notificaciones por automatización en SeaTable'
    description: 'Automatiza las notificaciones en SeaTable: crea reglas para alertar a usuarios en alemán, inglés, español, francés, portugués, ruso y chino fácilmente.'

---

Si dispone de una suscripción Enterprise, también puede enviar notificaciones a usuarios seleccionados mediante automatización. Basta con definir una regla de automatización correspondiente para cualquier vista de tabla.

## Enviar notificaciones mediante automatización

![Envío automatizado de correos electrónicos](images/how-to-use-automations-for-locking-rows-3.png)

1. Haga clic en {{< seatable-icon icon="dtable-icon-rule" >}} en la cabecera Base y luego en **Reglas de automatización**.
2. Haga clic en **Añadir Regla**.
3. Dé un **nombre** a la automatización y defina la **tabla** y la **vista en la** que debe funcionar.
4. Defina un **evento desencadenante que active** la automatización.
5. Haga clic en **Añadir acción** y seleccione **Enviar notificación** como acción automatizada.
6. Confirme con **Enviar**.

## Creación de la automatización

En primer lugar, defina un **evento desencadenante** para la automatización.

![Eventos desencadenantes básicamente disponibles para su selección](images/trigger-options-for-archivating-rows.png)

Las **cuatro opciones** son:

- Las entradas cumplen determinadas condiciones tras la edición
- Se añade una nueva entrada
- Activador periódico
- Activación periódica de entradas que cumplen una determinada condición

A continuación, seleccione **Enviar notificación** como acción automatizada. Esto está disponible como acción para las cuatro opciones de activación.

![Añadir la acción automatizada](images/add-an-action.png)  
![Añadir la acción automatizada](images/send-notification.png)

En el siguiente paso, seleccione los **usuarios** a los que se notificará cuando se produzca el evento desencadenante. Tenga en cuenta que sólo puede seleccionar usuarios que tengan al menos **acceso de lectura a** la tabla o vista.

![Selección de usuarios a notificar ](images/select-users-to-get-notified.png)

En el último paso, inserte el **contenido de** la notificación en el **campo de** texto previsto. Para hacer referencia a las entradas de la tabla, basta con escribir el nombre de las columnas entre llaves en el texto.

![Añadir el contenido de las notificaciones a enviar ](images/content-of-the-notification.png)

Guarde la automatización haciendo clic en **Enviar**.

## Ejemplo de aplicación

Un **caso de uso** concreto para este tipo de automatización podría darse, por ejemplo, si usted trabaja como directivo en una empresa y desea ordenar la reserva de varios cursos de formación para sus empleados. Le gustaría informar automáticamente al departamento de RRHH, que en última instancia es el que reserva la formación, sobre a qué formación les gustaría asistir a sus empleados.

En concreto, esto puede llevarse a cabo con la ayuda de una tabla en la que se mantengan diversos **datos de** los empleados de su empresa. En este contexto, podrías recoger, entre otras cosas, los **nombres de** los empleados, el **departamento** y la última formación que reservaron.

![Cuadro de ejemplo del caso de uso específico de la automatización](images/beispieltabelle-anwendungsfall.png)

Con la ayuda de una automatización, ahora se enviará automáticamente una **notificación** a los empleados seleccionados del departamento de RR.HH. por cada nueva reserva solicitada en la tabla, para que inicien la reserva de la formación solicitada para el empleado correspondiente.

### Creación de la automatización

En primer lugar, dé un **nombre** a la automatización (por ejemplo, notificación si se ha reservado una formación) y seleccione tanto la tabla (aquí: empleados y formaciones) como la vista en la que debe funcionar la automatización.

![Dar un nombre a la automatización y definir la tabla y la vista en las que debe funcionar](images/definition-of-the-automation-1.png)

Como **evento desencadenante de** la automatización, seleccione la opción "Las entradas cumplen determinadas condiciones tras el procesamiento".

![Selección del evento desencadenante](images/trigger-condition.png)

Para que las notificaciones se envíen sólo en caso de solicitud de un nuevo entrenamiento, añada como **condición de** filtro que la entrada de la columna "último entrenamiento reservado" se cambie por una de las posibles **opciones de selección** de esta columna.

![Añadir una condición de filtro](images/set-filter-condition.png)

A continuación, defina la acción "Enviar notificación" como acción **automatizada**.

![Añadir la acción automatizada](images/send-notification.png)

En el siguiente paso, seleccione en el campo desplegable los miembros del **personal** del departamento de RRHH a los que debe enviarse la **notificación** cuando se active el activador.

![Selección de usuarios a notificar ](images/select-users-to-get-notified-example.png)

En el último paso, puede escribir el **contenido de** la notificación que se enviará en el campo de texto proporcionado.

![Añadir el contenido de la notificación ](images/content-of-the-notification-example.png)

{{< warning  headline="Consejo"  text="Puede utilizar llaves para citar el **contenido de las columnas de la tabla** en la notificación. Utilice esta función para añadir a la notificación los **nombres de** los miembros del personal y el nombre de la **formación** solicitada." />}}

### Probar la automatización

Si posteriormente solicita una nueva formación para un empleado en la tabla seleccionada, es decir, cambia la entrada de la columna**"última formación reservada**" por la última formación solicitada, la **notificación** prefabricada se envía automáticamente a los usuarios seleccionados del departamento de RRHH.

Los empleados del departamento de RRHH reciben la información de que se ha solicitado una formación en la notificación, a la que llegan a través del símbolo de campana {{< seatable-icon icon="dtable-icon-notice" >}}, y pueden iniciar la formación seleccionada para el empleado correspondiente.

![Notificación enviada a los usuarios seleccionados tras activarse el evento desencadenante.](images/notification-after-trigger.png)

### Otros ejemplos interesantes de automatización:

- [Bloquear líneas mediante automatización]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-sperren" >}})
- [Vinculación de entradas mediante automatización]({{< relref "help/base-editor/automationen/beispiel-verlinken-von-eintraegen-per-automation" >}})
- [Añadir líneas mediante automatización]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-hinzufuegen" >}})
- [Añadir entradas a otras tablas mediante automatización]({{< relref "help/base-editor/automationen/beispiel-eintraege-in-andere-tabellen-per-automation-hinzufuegen" >}})
- [Envío automatizado de correos electrónicos]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}})
