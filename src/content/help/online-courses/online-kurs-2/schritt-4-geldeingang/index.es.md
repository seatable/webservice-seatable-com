---
title: 'Paso 4: Recibo de caja'
date: 2024-09-19
lastmod: '2024-09-24'
categories:
    - 'online-kurs-2'
author: 'cdb'
url: '/es/ayuda/paso4-pago-recibido-seatable'
aliases:
    - '/es/ayuda/schritt-4-geldeingang'
seo:
    title: 'Paso 4 Curso SeaTable 2: pago recibido – automatización'
    description: 'El cuarto paso utiliza botones para registrar pagos y enviar emails en SeaTable: automatiza y actualiza tu proceso comercial online con facilidad.'
---

Una vez que los participantes en el curso hayan recibido la solicitud de pago por correo electrónico, transferirán el importe del curso a su cuenta bancaria. En este punto no automatizaremos más la verificación de los pagos entrantes. No obstante, tendría sentido integrar un botón adicional en su base que realice dos tareas:

1. Confirmación de la recepción del pago y, por tanto, de la inscripción completa del participante en el curso.
2. Documentación del proceso de pago en la base.

## Múltiples acciones en un solo botón

Esto es fácil de implementar en SeaTable. En la tabla, añada `Registrations` añade un nuevo botón que realiza dos acciones:

- Enviar un correo electrónico con la confirmación del pago al participante.
- En `Payment Status` en `Paid` set.

Con tus conocimientos recién adquiridos, esto no debería ser un problema. Puede utilizar el siguiente texto para su correo electrónico:

> Subject: Payment Confirmation and Online Meeting Details
>
> Hey,
>
> Thank you for your payment! We’re excited to confirm that we’ve successfully received it.
>
> You can join the online meeting using the link below:  
> – https://meet.jit.si/{Course-ID}
>
> We look forward to seeing you there!  
> Best regards

## Artículo de ayuda con más información

- [Configurar una cuenta de correo electrónico en una Base]({{< relref "help/base-editor/weitere-optionen/einrichtung-eines-e-mail-kontos-in-einer-base" >}})
- [Configurar Gmail para enviar correos electrónicos a través de SMTP]({{< relref "help/integrationen/integrationen-innerhalb-von-seatable/gmail-fuer-den-versand-von-e-mails-per-smtp-einrichten" >}})
- [El botón]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}})
- [Enviar un correo electrónico por botón]({{< relref "help/base-editor/schaltflaechen/eine-e-mail-per-schaltflaeche-verschicken" >}})
- [Envío automatizado de correos electrónicos]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}})
