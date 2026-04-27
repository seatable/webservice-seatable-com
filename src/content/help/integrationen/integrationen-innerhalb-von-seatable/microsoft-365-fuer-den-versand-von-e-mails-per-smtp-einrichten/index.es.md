---
title: 'Configurar Microsoft 365 para enviar correos electrónicos a través de SMTP'
date: 2023-04-28
lastmod: '2025-03-07'
categories:
    - 'integrationen-innerhalb-von-seatable'
author: 'nsc2'
url: '/es/ayuda/microsoft-365-smtp-envio-correo'
aliases:
    - '/es/ayuda/microsoft-365-fuer-den-versand-von-e-mails-per-smtp-einrichten'
seo:
    title: 'Configura Microsoft 365 para enviar correos desde SeaTable vía SMTP y OAuth2'
    description: 'Descubre cómo vincular Microsoft 365 con SeaTable: autentica tu cuenta y configura el envío seguro de correos por SMTP con una guía paso a paso.'
---

**Microsoft 365**, el popular servicio en línea para las aplicaciones Office de Microsoft, puede utilizarse para **enviar correos electrónicos desde SeaTable**. La autenticación contra su Microsoft 365 debe realizarse mediante la autenticación moderna de Microsoft. (La autenticación mediante nombre de usuario y contraseña de usuario no es posible con Microsoft 365).

{{< warning headline="Cuentas de Outlook" text="Estas instrucciones explican el procedimiento utilizando una cuenta de Microsoft 365. Sin embargo, el procedimiento también se aplica a las cuentas de correo electrónico gratuitas de Outlook." />}}

## Preparación en el Entra Admin Centre

Para poder utilizar su cuenta de Microsoft 365 en SeaTable para enviar correos electrónicos, primero debe crear y configurar una aplicación en el Entra Admin Centre de Microsoft.

1. Inicie sesión en el [Centro de administración de Microsoft Entra](https://entra.microsoft.com/). El usuario necesita derechos de administrador para la cuenta que se va a utilizar para el envío.
2. Haz clic en **Registros de aplicaciones** en el menú de navegación de la página.
3. Crea una nueva cuenta haciendo clic en **\+ Nuevo registro**. Introduce un nombre (por ejemplo, 'SeaTable') y selecciona **Cualquier inquilino de Entra ID + cuentas personales de Microsoft** como tipo de cuenta. Registra el siguiente URI de redireccionamiento para una aplicación de tipo **Web**:

    ```
    https://cloud.seatable.io/oauth/third-party-email-accounts/callback/
    ```

    Si no utiliza SeaTable Cloud, sustituya cloud.seatable.io por el nombre de host de su instancia de SeaTable. Complete la creación del registro de la app haciendo clic en **Registrar**.

4. Anote el **ID de aplicación (cliente)** en la página de resumen de la aplicación que acaba de registrar. Es necesario para configurar la cuenta de correo electrónico en SeaTable.
5. Para generar la clave de cliente, ve a **Certificados y secretos** en el menú de navegación de la aplicación. Haz clic en **Nuevo secreto de cliente**. Introduce una descripción y una fecha de caducidad para la clave.

    ![Creación de un secreto de cliente para una aplicación registrada en Microsoft Entra](images/Creating_Client_Secret_Microsoft_Entra.gif)

6. Copia el valor de la clave creada en el portapapeles.

Ya ha realizado todos los preparativos para poder utilizar su cuenta de Microsoft 365 como cuenta de correo electrónico en SeaTable.

## Creación de la cuenta de correo electrónico en SeaTable

Ahora necesitas añadir tu cuenta de Microsoft 365 a tu Base SeaTable. Para ello, es necesario seguir los siguientes pasos:

1. Abra las opciones de la base ampliada haciendo clic en el **icono de tres puntos** {{< seatable-icon icon="dtable-icon-more-level" >}} situado en la esquina superior derecha.
2. Seleccione la opción **Integración de terceros**.
   ![Integración de terceros mediante las opciones avanzadas de la base](images/Integration-von-Drittanbietern-ueber-die-erweiterten-Base-Optionen.png)
3. Haga clic en **Añadir cuenta de correo electrónico**.
4. Seleccione **Microsoft (Microsoft 365 and Outlook)** como proveedor de servicios.
5. Introduzca la siguiente información y haga clic en el botón **Enviar** situado en la esquina superior derecha:
    - **Nombre de la cuenta**: una breve descripción de la cuenta (por ejemplo, "Microsoft 365")
    - **ID de aplicación (cliente)**: el ID de aplicación (cliente) de la aplicación creada.
    - **Clave cliente**: la clave cliente secreta de la aplicación creada desde el portapapeles
6. Concede los permisos solicitados haciendo clic en **Aceptar**.
   ![Screencast aceptar permisos solicitados](images/Accept-Permissions-Requested-Microsoft.gif)

## Enviar correos electrónicos mediante automatización o botón

A continuación, puede utilizar la cuenta de correo electrónico creada en su Base SeaTable para enviar correos electrónicos mediante [automatización]({{< relref "help/base-editor/schaltflaechen/eine-e-mail-per-schaltflaeche-verschicken" >}}) o botón.

Si quieres saber más sobre esta útil función, lee el artículo [Configurar una cuenta de correo electrónico en una Base]({{< relref "help/base-editor/weitere-optionen/einrichtung-eines-e-mail-kontos-in-einer-base" >}}).
