---
title: 'Envío automatizado de correos electrónicos'
date: 2023-03-03
lastmod: '2023-03-03'
categories:
    - 'beispiel-automationen'
author: 'nsc2'
url: '/es/ayuda/enviar-correos-automaticos-por-automatizacion'
aliases:
    - '/es/ayuda/e-mail-versand-per-automation'
seo:
    title: 'Enviar correos automáticos en SeaTable – guía completa'
    description: 'Aprende a automatizar el envío de correos en SeaTable con reglas, activadores y cuentas externas de correo mediante SMTP.'
---

Con la ayuda de las automatizaciones, ya no tendrá que enviar correos electrónicos manualmente a los usuarios seleccionados, sino que podrá hacer que se envíen automáticamente. Basta con definir la automatización correspondiente para cualquier vista de tabla.

## Envío automatizado de correos electrónicos

![Envío automatizado de correos electrónicos](images/how-to-use-automations-for-locking-rows-3.png)

1. Haga clic en {{< seatable-icon icon="dtable-icon-rule" >}} en la cabecera Base y luego en **Reglas de automatización**.
2. Haga clic en **Añadir Regla**.
3. **Asigne un nombre a la** automatización y defina la **tabla** y la **vista en las** que debe funcionar.
4. Defina un **evento desencadenante que active** la automatización.
5. Haga clic en **Añadir acción** y seleccione **Enviar correo electrónico** como acción automatizada.
6. Confirme con **Enviar**.

## Creación de la automatización

En primer lugar, defina un **evento desencadenante** para la automatización.

![Eventos desencadenantes básicamente disponibles para su selección](images/trigger-options-for-archivating-rows.png)

{{< warning headline="Nota" >}}

La acción automatizada **Enviar correo electrónico** está disponible después de todos los eventos desencadenantes:

- Las entradas cumplen determinadas condiciones tras la edición
- Se añade una nueva entrada
- Activador periódico
- Activación periódica de las entradas que cumplan determinadas condiciones

{{< /warning >}}

A continuación, seleccione **Enviar correo electrónico** como acción automatizada.

![Añadir la acción automatizada](images/add-an-action.png) ![Añadir la acción automatizada](images/example-send-email-action.png)

En el siguiente paso, seleccione en primer lugar una **cuenta de correo electrónico** desde la que desee enviar los correos. Para poder utilizar su cuenta de correo electrónico para el envío, **debe** primero **añadirla** como tercero en su base de SeaTable. Puede encontrar instrucciones detalladas para este paso [aquí]({{< relref "help/integrationen/integrationen-innerhalb-von-seatable/gmail-fuer-den-versand-von-e-mails-per-smtp-einrichten" >}}).

{{< warning  type="warning" headline="Nota importante"  text="Si **no** ha añadido ninguna cuenta de correo electrónico como tercero en su base de SeaTable, **no** se mostrará ninguna cuenta. Añadir una cuenta de correo electrónico constituye, por tanto, un **requisito** importante para la automatización." />}}

![Selección de una cuenta de correo electrónico para el envío](images/select-email-account.png)

Tras seleccionar la cuenta de correo electrónico, defina el **asunto**, el **destinatario** y el **contenido** del correo. Puede introducir **varias direcciones de correo electrónico** separadas por comas y en CC. Además, tiene la posibilidad de añadir **archivos adjuntos** desde una [columna de archivo]({{< relref "help/base-editor/spaltentypen/die-datei-spalte" >}}).

![Definición del correo electrónico que se enviará mediante la automatización](images/define-email.png)

Finalmente, confirme la automatización haciendo clic en **Enviar**.

![Confirmación de la automatización](images/confirm-the-automation.jpg)

## Ejemplo de aplicación

Un **caso de uso** concreto de este tipo de automatización podría darse, por ejemplo, si trabaja en el comité de empresa de una compañía. Desea informar automáticamente al departamento de Recursos Humanos de que ha aprobado el despido de un empleado.

En su caso, esto puede ponerse en práctica con una tabla en la que se mantienen distintos **datos** de todos los empleados de su empresa. En este contexto podría registrar, entre otras cosas, los **nombres** de los empleados, su **situación laboral** y el estado de sus **pagos salariales**.

![Tabla de ejemplo del caso de uso concreto](images/example-table-email-automation.png)

Con la ayuda de una automatización, SeaTable debe enviar ahora automáticamente un **correo electrónico** al departamento de Recursos Humanos tan pronto como haya aprobado el despido de un empleado en el comité de empresa.

### Creación de la automatización

En primer lugar, asigne un **nombre** a la automatización y seleccione tanto la **tabla** (employee list) como la **vista** (employees ressort marketing) en la que debe actuar la automatización.

![Configuración básica de la automatización](images/basic-settings-automation.png)

Como **evento desencadenante** de la automatización, seleccione la opción **Las entradas cumplen determinadas condiciones tras la edición**. Para que los correos electrónicos se envíen **únicamente** en caso de despido de un empleado, añada como **condición de filtro** que la entrada en la columna **status of employment** deba cambiar a **terminated**.

![Definición del evento desencadenante](images/condition-of-the-trigger-event.png)

Como **acción automatizada**, defina la acción **Enviar correo electrónico**.

![Añadir la acción automatizada](images/example-send-email-action.png)

En el siguiente paso, seleccione una **cuenta de correo electrónico** desde la que desee enviar los correos al departamento de Recursos Humanos. Para poder utilizar su cuenta de correo electrónico para el envío, **debe** primero **añadirla** como tercero en su base de SeaTable. Puede encontrar instrucciones detalladas para este paso [aquí]({{< relref "help/integrationen/integrationen-innerhalb-von-seatable/gmail-fuer-den-versand-von-e-mails-per-smtp-einrichten" >}}).

{{< warning  type="warning" headline="Nota importante"  text="Si **no** ha añadido ninguna cuenta de correo electrónico como tercero en su base de SeaTable, en este paso **no** se mostrará ninguna cuenta. Añadir una cuenta de correo electrónico constituye, por tanto, un **requisito** importante para la automatización." />}}

![Selección de una cuenta de correo electrónico para el envío](images/select-email-account-1.png)

Tras seleccionar su cuenta de correo electrónico, defina el **asunto**, el **destinatario** y el **contenido** de los correos. Puede introducir **varias direcciones de correo electrónico** separadas por comas y en CC. Por último, tiene la posibilidad de añadir **archivos adjuntos** desde una [columna de archivo]({{< relref "help/base-editor/spaltentypen/die-datei-spalte" >}}).

{{< warning  headline="Consejo"  text="Mediante llaves puede citar **contenidos de columnas de la tabla** en el texto del correo. Utilice esta función para insertar automáticamente los **nombres** de los empleados despedidos en el texto." />}}

![Definición del correo electrónico para la automatización del caso de uso](images/definition-email-example.png)

Cuando haya terminado el correo electrónico que desea enviar, confirme la automatización con **Enviar**.

### Probar la automatización

Si a continuación, en la tabla seleccionada, cambia la situación laboral de un empleado a **terminated**, el **correo electrónico** preparado se enviará automáticamente al departamento de Recursos Humanos para informarle del despido.

![Una vez cambiada la situación laboral de un empleado a "terminated", el correo preparado se envía automáticamente a los destinatarios seleccionados ](images/test-automation-email.jpg)

### Más ejemplos interesantes de automatizaciones:

- [Bloquear filas mediante automatización]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-sperren" >}})
- [Vincular entradas mediante automatización]({{< relref "help/base-editor/automationen/beispiel-verlinken-von-eintraegen-per-automation" >}})
- [Añadir filas mediante automatización]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-hinzufuegen" >}})
- [Añadir entradas a otras tablas mediante automatización]({{< relref "help/base-editor/automationen/beispiel-eintraege-in-andere-tabellen-per-automation-hinzufuegen" >}})
- [Enviar notificaciones mediante automatización]({{< relref "help/base-editor/automationen/benachrichtigungen-per-automation-versenden" >}})
