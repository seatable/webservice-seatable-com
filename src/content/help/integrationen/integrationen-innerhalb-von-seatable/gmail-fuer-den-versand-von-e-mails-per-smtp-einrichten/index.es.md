---
title: 'Configurar Gmail para enviar correos electrónicos a través de SMTP'
date: 2023-01-10
lastmod: '2025-03-07'
categories:
    - 'integrationen-innerhalb-von-seatable'
author: 'cdb'
url: '/es/ayuda/configurar-gmail-envio-smtp-seatable'
aliases:
    - '/es/ayuda/gmail-fuer-den-versand-von-e-mails-per-smtp-einrichten'
seo:
    title: 'Configure Gmail para envío SMTP en SeaTable'
    description: 'Configure plataformas para enviar correos desde SeaTable por SMTP mediante Gmail, paso a paso, para mayor integración y seguridad.'

---

Gmail, el popular servicio de correo electrónico de Google, puede utilizarse para enviar correos electrónicos desde SeaTable. La autenticación contra la cuenta de Google se puede hacer ya sea a través de una contraseña de la aplicación oa través de OAuth. OAuth es el método preferido por Google, pero también es mucho más difícil de configurar. (La autenticación a través de nombre de usuario y contraseña de usuario no es posible con Gmail).

{{< warning headline="Atención a las cuentas del espacio de trabajo" text="Estas instrucciones explican el procedimiento utilizando una cuenta sencilla de Gmail. Sin embargo, el procedimiento aquí descrito también se aplica a las cuentas de Google Workspace. Si tienes una cuenta de Workspace, solo tienes que asegurarte de que la verificación en dos pasos está activada." />}}

## Autenticación mediante contraseña de la aplicación

Una [contraseña](https://support.google.com/accounts/answer/185833?hl=de) de [aplicación](https://support.google.com/accounts/answer/185833?hl=de) es un código de seguridad de 16 dígitos que las aplicaciones o los dispositivos pueden utilizar para autenticarse ante Google y, de este modo, obtener acceso a tu cuenta de Gmail. Puedes crear contraseñas de aplicaciones en tu [cuenta de Google](https://myaccount.google.com/). Las contraseñas de aplicaciones solo se pueden utilizar en cuentas que tengan habilitada la autenticación de dos factores.

### Creación de una contraseña de aplicación

1. Abre la aplicación de gestión de contraseñas de Google: accede a tu **cuenta de Google** cuando se te solicite.
2. Introduzca un **nombre**, por ejemplo "SeaTable", y haga clic en "Crear".

![Generar una contraseña de aplicación de Google](images/Google_App_Password.gif)

4. Copie la contraseña de la aplicación generada en el portapapeles.

{{< warning headline="Las contraseñas de las aplicaciones son de un solo uso" text="La contraseña de la aplicación sólo se muestra después de haberla creado. No se puede recuperar ni cambiar posteriormente. Si quieres utilizar tu cuenta de Gmail en varias bases para enviar correos electrónicos, te recomendamos crear varias contraseñas de app y dar a cada una un nombre descriptivo." />}}

### Creación de la cuenta de correo electrónico en SeaTable

Ahora tienes que añadir tu cuenta de Gmail como tercero en tu Base SeaTable. Para ello, es necesario seguir los siguientes pasos:

1. Abra las opciones de la base ampliada haciendo clic en el **icono de tres puntos** {{< seatable-icon icon="dtable-icon-more-level" >}} situado en la esquina superior derecha.
2. Seleccione la opción **Integración de proveedores externos**.

![Integración de terceros mediante las opciones avanzadas de la base](images/Integration-von-Drittanbietern-ueber-die-erweiterten-Base-Optionen.png)

4. Haga clic en **Añadir cuenta de correo electrónico**.
5. Seleccione Proveedor de **correo electrónico genérico** como proveedor de servicios.
6. Introduzca la siguiente información:
    - **Nombre de la** cuenta: cualquier nombre para la cuenta, por ejemplo, "Gmail".
    - **Servidor SMTP**: "smtp.gmail.com
    - **Puerto SMTP**: '587
    - **Nombre de usuario**: tu dirección de Gmail, por ejemplo "seatable@gmail.com".
    - **Contraseña**: la contraseña de la aplicación generada a partir de la caché.

![Configuración de Gmail con contraseña de la aplicación para enviar correos electrónicos desde una base SeaTable](images/ThirdPartyIntegration_Gmail.png)

## Autenticación mediante OAuth 2.0

OAuth 2.0, abreviatura de Open Authorisation 2.0, es un protocolo abierto que permite a las aplicaciones (web) acceder de forma segura a las cuentas de usuario de otras aplicaciones. Esto significa que un usuario puede utilizar recursos o servicios de otra aplicación desde una aplicación, por ejemplo, enviar correos electrónicos desde SeaTable a través de Gmail.

Para que SeaTable pueda acceder a una cuenta de Gmail mediante OAuth 2.0, debe crear un ID de cliente y una clave de cliente en [la Cloud Console de Google](<a href=) y guardarlos en SeaTable.

### Creación de datos de acceso en Google Cloud Console

Como plataforma para desarrolladores, la Cloud Console parece confusa para los usuarios normales. No dejes que esto te impresione. Con la siguiente guía paso a paso, cualquiera puede configurarla.

1. Abra [Google Cloud Console](https://console.developers.google.com/) y acceda a su **cuenta de Google** cuando se le solicite.
2. En primer lugar, cree un nuevo proyecto. En este proyecto se realizan todos los ajustes que se describen a continuación. Introduzca un nombre para el proyecto (por ejemplo, "SeaTable") y seleccione el lugar de almacenamiento. (Si no hay organizaciones definidas, mantenga "Sin organización").
3. Permitir que el proyecto creado utilice la API de Gmail. Para ello, haga clic con el ratón en el campo de búsqueda situado en la parte superior de la pantalla, introduzca "Gmail API" y, a continuación, haga clic en el resultado de búsqueda correspondiente. Active la API de Google.
4. Todos los demás pasos tienen lugar en **Google Auth Platform**. Haga clic en el icono del bocadillo situado en la esquina superior izquierda y, a continuación, seleccione "Todos los productos" en la sección "Soluciones". En la página de productos, haga clic en "Google Auth Platform".

![Navegación a Google Auth Platform en Google Cloud Console](images/GoogleAuthPlatform.png)

6. Realice las **configuraciones** necesarias en Google Auth Platform: Introduzca un nombre de aplicación, una dirección de correo electrónico de asistencia y una dirección de correo electrónico de contacto (por ejemplo, su dirección de Gmail). Seleccione "Externo" como grupo de destino. Acepte las condiciones de uso y finalice la configuración.
7. Haga clic en **"Grupo objetivo"** en la página de navegación de Google Auth Platform. Añada su dirección de correo electrónico de Google como usuario de prueba.
8. En la página de navegación de Google Auth Platform, haga clic en **"Clientes"** y cree un cliente OAuth 2.0. Seleccione "Aplicación web" como tipo de aplicación para el cliente OAuth e introduzca un nombre (por ejemplo, "SeaTable"). Omita las "Fuentes JavaScript autorizadas" y añada la siguiente URI como "URI de reenvío autorizada":

    ```
    https://cloud.seatable.io/oauth/third-party-email-accounts/callback/
    ```

    Si no utiliza SeaTable Cloud, sustituya cloud.seatable.io por el nombre de host de su instancia de SeaTable. Desplácese hasta la parte inferior de la página y confirme la creación del cliente OAuth.

![Un cliente OAuth 2.0 configurado en Google Cloud Console](images/Configured_OAuth_Client_GoogleCloudConsole.png)

10. El cliente recién creado aparece ahora en la lista de clientes OAuth 2.0. La configuración del cliente se puede mostrar haciendo clic en su nombre. El ID de cliente mostrado y la clave de cliente son esenciales para la configuración posterior en SeaTable.

Si ha cometido un error durante la configuración y ya no sabe dónde se encuentra, haga clic en el icono del bocadillo situado en la esquina superior derecha. Desde ahí puedes navegar de vuelta a Google Auth Platform.

### Creación de la cuenta de correo electrónico en SeaTable

Ahora tienes que añadir tu cuenta de Gmail como tercero en tu Base SeaTable. Para ello, es necesario seguir los siguientes pasos:

1. Abra las opciones de la base ampliada haciendo clic en el **icono de tres puntos** {{< seatable-icon icon="dtable-icon-more-level" >}} situado en la esquina superior derecha.
2. Seleccione la opción **Integración de proveedores externos**.
3. Haga clic en **Añadir cuenta de correo electrónico**.
4. Selecciona **Gmail** como proveedor de servicios.
5. Introduzca la siguiente información:

    - **Nombre de la** cuenta: cualquier nombre para la cuenta, por ejemplo, "Gmail".
    - **Nombre de usuario**: 'me
    - **ID de cliente**: la clave de cliente del cliente OAuth creado.
    - **Clave** de cliente: la clave de cliente del cliente OAuth creado.

6. Confirme la creación de la cuenta de correo electrónico con autenticación OAuth2.
7. Ahora inicia sesión en tu cuenta de Google en el cuadro de diálogo que se abre.
8. Haz clic en "Siguiente" cuando se te notifique que esta aplicación no ha sido verificada y permite el acceso a la cuenta de Google.

## Envío automatizado de correos electrónicos

A continuación, puede utilizar la cuenta de correo electrónico creada en su Base SeaTable para enviar correos electrónicos mediante automatización o [botón]({{< relref "help/base-editor/schaltflaechen/eine-e-mail-per-schaltflaeche-verschicken" >}}).

Si desea obtener más información sobre esta útil automatización, lea el artículo [Envío de correo electrónico mediante automatización]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}}).
