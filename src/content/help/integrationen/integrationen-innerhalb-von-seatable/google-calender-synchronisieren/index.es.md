---
title: 'Sincronizar citas en SeaTable con un calendario de Google'
date: 2026-03-23
lastmod: '2026-03-23'
categories:
    - 'integrationen-innerhalb-von-seatable'
author: 'rdb'
url: '/es/ayuda/sincronizar-citas-con-google-calendario'
seo:
    title: 'Sincronizar citas en SeaTable con un calendario de Google'
    description: 'Instrucciones paso a paso para sincronizar las citas de SeaTable con un calendario de Google.'
---

Las citas de una base SeaTable pueden sincronizarse automáticamente con uno o varios **calendarios de Google**. Esto significa que siempre tendrá sus citas actuales disponibles en su calendario de Google en su PC y dispositivos móviles.

Antes de configurar la sincronización de citas, debe configurar la **cuenta de Google** del calendario al que desea transferir las citas de SeaTable. Esto se hace en dos pasos: En primer lugar, cree **credenciales OAuth** en Google Cloud Console. A continuación, cree una cuenta de terceros en SeaTable con los datos de acceso y conéctela a Google. Esto es muy fácil con estas instrucciones paso a paso.

## Creación de los datos de acceso en la Google Cloud Console

Como plataforma para desarrolladores, Google Cloud Console parece inicialmente confusa para los usuarios normales. No deje que eso le impresione. La siguiente guía paso a paso le ayudará a configurarla sin quebraderos de cabeza.

1. Abra [Google Cloud Console](https://console.cloud.google.com/) e inicie sesión con su **cuenta de Google** cuando se le solicite.
2. Haga clic en **Seleccionar proyecto** en la parte superior junto al logotipo de Google Cloud y cree un **Proyecto nuevo**. Todos los ajustes que se explican a continuación se realizan en este proyecto.
   ![Selección de proyecto en Google Cloud](images/GoogleConsole_CreateNewProject_723.png)
3. Introduzca un **nombre de proyecto** (por ejemplo, SeaTable Base XY) y seleccione la **ubicación de almacenamiento**. Si no hay organizaciones definidas, mantenga "Sin organización". Confirme con **Crear**.
   ![crear nuevo proyecto en Google Cloud Console](images/GoogleConsole_NewProject_723.png)
4. Permita que el proyecto creado utilice la API de Google Calendar. Para ello, haga clic con el ratón en el **campo de búsqueda** de la parte superior de la página, introduzca **Google Calendar API** y haga clic en el resultado de búsqueda correspondiente. A continuación, active la API del Calendario de Google.
   ![Activar la API del Calendario de Google](images/GoogleConsole_EnableCalendarAPI_722.gif)
5. Haga clic en el icono del menú de la hamburguesa en la esquina superior izquierda para mostrar la navegación y, a continuación, seleccione la opción **Todos los productos** en la sección "Soluciones". En la página de productos, haga clic en **Google Auth Platform**.
   ![llame a Google Auth Platform](images/GoogleConsole_SwitchAuthPlatform_722.gif)
6. Realice las configuraciones necesarias en la Google Auth Platform haciendo clic en **Primeros pasos**: Introduzca un **Nombre de la aplicación** y una **Dirección de correo electrónico de soporte** (por ejemplo, su dirección de Gmail). Seleccione **Externo** como grupo destinatario. Introduzca una **Dirección de correo electrónico de contacto** (por ejemplo, su dirección de Gmail). Acepte las **Condiciones de uso** y finalice la configuración.
7. Haga clic en **Grupo objetivo** en la navegación lateral de la plataforma Google Auth. Añada su dirección de correo electrónico de Google como **usuario de prueba**.
8. Haga clic en **Clientes** en la navegación lateral de la plataforma Google Auth y cree un cliente OAuth 2.0. Seleccione la opción "Aplicación web" como **Tipo de aplicación** para el cliente OAuth e introduzca un **Nombre** (por ejemplo, SeaTable). Omita "Fuentes JavaScript autorizadas" e inserte la siguiente URI como **URI de redirección autorizada** antes de hacer clic en **Crear**:

    ```
    https://cloud.seatable.io/oauth/google-calendar/callback/
    ```

    Si utiliza su propio sistema en lugar de SeaTable Cloud, sustituya cloud.seatable.io por el nombre de host de su instancia de SeaTable.

   ![crear cliente OAuth](images/GoogleConsole_CreateClient_722.gif)

9. El cliente recién creado aparece ahora en la lista de clientes OAuth 2.0. La configuración del cliente puede visualizarse pulsando sobre su nombre. El **identificador del cliente** y la **clave del cliente** mostrados son esenciales para la siguiente configuración en SeaTable.

{{< warning headline="Que no cunda el pánico" text="Si ha cometido un error durante la configuración y ya no sabe dónde se encuentra, haga clic en el icono del menú hamburguesa situado en la esquina superior izquierda. Desde ahí puede navegar de vuelta a la plataforma Google Auth a través de **Accedido recientemente**." />}}

## Creación de la cuenta Google en SeaTable

Ahora necesita añadir su cuenta de Google como **cuenta de terceros en su Base SeaTable**. Para ello es necesario seguir los siguientes pasos:

1. Abra las opciones avanzadas de la base haciendo clic en el **icono de los tres puntos** {{< seatable-icon icon="dtable-icon-more-level" >}} en la esquina superior derecha.
   ![abrir el menú para la integración de terceros](images/third-party-integration.png)
2. Seleccione la opción **Integración de terceros**.
3. Haga clic en **Google Calendar** en la navegación de la izquierda y después en **Añadir cuenta de Google Calendar** en la esquina superior derecha.
   ![añadir cuenta de Google Calendar](images/add-google-calendar-account-in-seatable.png)
4. Introduzca la siguiente información:
    - **Nombre de la cuenta**: cualquier nombre para la cuenta, por ejemplo, Google
    - **ID del cliente**: el ID del cliente OAuth creado
    - **Clave de cliente**: la clave del cliente OAuth creado
5. Tras hacer clic en **Submitir**, se abrirá una ventana del navegador. Haga clic en **Siguiente** si se le informa de que esta aplicación no ha sido verificada y permita el acceso a la cuenta de Google.
6. Puede encontrar la cuenta creada del mismo modo en **Cuentas de Google Calendar**.

## Transferir citas automáticamente a Google Calendar

Si ha configurado la cuenta de Google, puede transferir y actualizar automáticamente las citas desde SeaTable a su calendario en la nube de Google. La configuración de la transferencia de datos de SeaTable a Google Calendar se realiza a través de una [acción]({{< relref "help/base-editor/automationen/automations-aktionen" >}}) en una regla de automatización.
