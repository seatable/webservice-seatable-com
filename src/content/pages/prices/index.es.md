---
title: 'Precios SeaTable: Tarifas transparentes para todos los tamaños de equipo'
description: ''
date: '2025-03-30'
url: '/es/precio'
aliases:
    - '/es/preise/'
    - '/es/prices/'
seo:
    title: 'Precios de SeaTable: Tarifas para todos los equipos'
    description: 'Consulta precios flexibles, compara planes de SeaTable y elige la solución ideal para tus datos.'

sections:
    - name: hero-price
      weight: 1
      title: SeaTable Cloud. Hecho a tu medida.
      subtitle: Lo que ofrecemos
      text: Empieza gratis y obtén más funciones y límites más altos desde 7€ por usuario al mes cuando lo necesites
      title2: SeaTable Server. Control total para su organización.
      subtitle2: Lo que obtiene
      text2: Instale SeaTable en su propio servidor y benefíciese de la máxima soberanía de datos, personalización individual y todas las funciones empresariales.


    - name: 'price-1'
      weight: 2
      xshow: 'showCloud'

    - name: price-table
      weight: 3
      xshow: 'showCloud'
      classes:
        - curved
        - bg-gray-100
      title: Compare todos los detalles
      table:
        head: ['Gratis', 'Plus', 'Enterprise', 'Dedicado']
        rows:
          - type: section
            label: 'Precio (por usuario, sin IVA)'
          - key: 'Facturación anual'
            values: ['0€', '7€', '14€', '*']
          - key: 'Facturación mensual'
            values: ['0€', '9€', '18€', '*']
          - type: section
            label: 'Uso (total por equipo)'
          - key: 'Bases'
            values: ['∞', '∞', '∞', '∞']
          - key: 'Tablas'
            values: ['∞', '∞', '∞', '∞']
          - key: 'Líneas máximas en una base'
            values: ['10.000', '50.000', '∞', '∞']
          - key: 'Número máximo de líneas en una base'
            values: ['10.000', '50.000', '100.000', '200.000']
          - key: 'Espacio de almacenamiento'
            values: ['2 GB', '50 GB', '100 GB', '∞']
          - key: 'Período de retención de instantáneas'
            values: ['1 mes', '6 meses', '12 meses', '24 meses']
          - key: 'Ejecuciones de JavaScript (por mes)'
            values: ['∞', '∞', '∞', '∞']
          - key: 'Ejecuciones de Python (por mes)'
            values: ['100', '5.000', '∞', '∞']
          - key: 'Llamadas API (por mes y usuario)'
            values: ['3.000 (fijo)', '10.000', '50.000', '∞']
          - key: 'Tamaño máximo del equipo'
            values: ['25', '∞', '∞', '∞']
          - type: section
            label: 'Funciones'
          - key: '26 tipos de columnas'
            values: ['+', '+', '+', '+']
          - key: 'Filtrar, agrupar y ordenar'
            values: ['+', '+', '+', '+']
          - key: 'Vistas'
            values: ['+', '+', '+', '+']
          - key: 'Vistas privadas'
            values: ['-', '+', '+', '+']
          - key: 'Compartir vistas'
            values: ['-', '+', '+', '+']
          - key: 'Formularios web'
            values: ['+', '+', '+', '+']
          - key: 'Conjuntos de datos compartidos'
            values: ['+', '+', '+', '+']
          - key: 'Importar / Exportar (CSV, XLSX y DTABLE)'
            values: ['+', '+', '+', '+']
          - key: 'Notificaciones'
            values: ['+', '+', '+', '+']
          - key: 'Plugins'
            values: ['+', '+', '+', '+']
          - key: 'Soporte de Javascript y Python'
            values: ['+', '+', '+', '+']
          - key: 'App Builder'
            values: ['+', '+', '+', '+']
          - key: 'Permisos de compartición individual (Base)'
            values: ['-', '+', '+', '+']
          - key: 'Permisos de tabla, vista y columna (Base)'
            values: ['-', '+', '+', '+']
          - key: 'Bloqueo de filas'
            values: ['-', '+', '+', '+']
          - key: 'Permisos de página (App)'
            values: ['-', '-', '+', '+']
          - key: 'Personalización de formularios web (logo, imagen de cabecera)'
            values: ['-', '-', '+', '+']
          - key: 'Automatizaciones (por mes y usuario)'
            values: ['100 (fijo)', '500', '5.000', '∞']
          - key: 'Créditos de IA (por mes y usuario)'
            values: ['12,5 (fijo)', '50', '500', '∞']
          - key: 'Almacenamiento de Big Data'
            values: ['-', '-', '+', '+']
          - type: section
            label: 'Soporte'
          - key: 'Centro de ayuda'
            values: ['+', '+', '+', '+']
          - key: 'Foro de SeaTable'
            values: ['+', '+', '+', '+']
          - key: 'Soporte por correo electrónico'
            values: ['-', '-', '+', '+']
          - key: 'Servicios profesionales (de pago)'
            values: ['-', '-', '+', '+']
          - type: section
            label: 'Administración y seguridad'
          - key: 'Autenticación de dos factores'
            values: ['+', '+', '+', '+']
          - key: 'Panel de administración empresarial'
            values: ['-', '-', '-', '+']
          - key: 'Autenticación mediante AD/LDAP, SAML u OAuth'
            values: ['-', '-', '-', '+']
          - type: section
            label: 'Facturación'
          - key: 'Pago con tarjeta de crédito'
            values: ['+', '+', '+', '+']
          - key: 'Pago por transferencia bancaria (mín. 10 usuarios, pago anual)'
            values: ['-', '-', '+', '+']


    # details on-premise
    - name: 'content-9'
      weight: 3
      classes:
          - bg-gray-100
          - curved
      xshow: '!showCloud'
      title: Ventajas de tener su propio servidor
      subtitle: Razones para on-premises
      items:
          - headline: Funcionalidades Enterprise
            text: Con su propio servidor, no hay diferentes versiones. Siempre obtiene la gama completa de funciones de SeaTable Enterprise.
            icon: robot
          - headline: Soporte Enterprise
            text: El precio de la licencia de SeaTable Enterprise siempre incluye nuestro soporte Enterprise.
            icon: award
          - headline: Personalización
            text: Con su sistema SeaTable Enterprise, puede utilizar su propia URL, plantillas personalizadas, códigos de color individuales, así como roles y permisos.
            icon: paint-roller
          - headline: Máxima Protección de Datos
            text: SeaTable es una de las pocas soluciones en la nube que también puede obtener como solución on-premises.<br><br>Usted licencia un SeaTable Enterprise Server y puede instalar y operar el software del servidor donde quiera.
            icon: file-shield
          - headline: Autenticación
            text: SeaTable es compatible con todos los métodos de autenticación comunes como SAML, OAuth, Shibboleth, Active Directory y LDAP. Permite la autenticación de dos factores y el inicio de sesión único (Single Sign-On).
            icon: fingerprint
          - headline: Límites Personalizados
            text: En su sistema, usted decide qué límites de API deben aplicarse o si debe aplicarse alguno.
            icon: compass

    - name: 'customer-1'
      weight: 9
      title: 'Empresas y equipos de todos los tamaños confían en SeaTable en todo el mundo'
      subtitle: 'Estás en buena compañía'
      show_numbers: 'no'
      buttons: []

    - name: content-11
      weight: 10
      title: Descuentos para organizaciones sin fines de lucro
      subtitle: Asequible para todos
      items:
          - text: Nos complace apoyar a personas en proyectos extraordinarios. Las organizaciones sin fines de lucro y las instituciones educativas reciben un 50% de descuento. En casos excepcionales, las asociaciones locales pueden obtener hasta un 75% de descuento en las suscripciones de SeaTable Plus y SeaTable Enterprise. Envíenos [su solicitud de descuento a través de la administración del equipo]({{< relref "help/teamverwaltung/abonnement/rabatte" >}}).
      image: /images/image-341.png
      image_alt: 'Gráfico de SeaTable sobre descuentos para organizaciones sin ánimo de lucro, instituciones educativas y organismos públicos'

    - name: platform-selector
      weight: 18

    - name: faq
      weight: 19
      xshow: '!showCloud'
      title: Preguntas Frecuentes
      items:
          - q: ¿Qué es un usuario?
            a: 'Un usuario significa una cuenta de usuario (activa) en una instancia del Servidor SeaTable. Una cuenta de usuario (activa) permite la autenticación y el inicio de sesión en el sistema.<br><br>
            Se requiere un inicio de sesión y, por lo tanto, una cuenta de usuario para las siguientes acciones:<br>
            – Crear, editar y eliminar bases, apps y formularios web<br>
            – Introducir, editar y borrar datos en bases y apps<br><br>
            No es necesario iniciar sesión y, por tanto, no se requiere cuenta de usuario para estas acciones:<br>
            – Uso de apps públicas<br>
            – Acceso a bases/vistas a través de enlaces externos<br>
            – Envío de formularios web públicos'
          - q: ¿Qué es un usuario inactivo?
            a: Por usuario inactivo se entiende una cuenta de usuario que se ha configurado como inactiva y que no permite iniciar sesión en el sistema. Los usuarios inactivos no cuentan para la licencia y ésta no limita el número de usuarios inactivos. El estado de actividad de un usuario puede ser modificado por un administrador del sistema en cualquier momento.
          - q: ¿Qué métodos de pago puedo utilizar?
            a: Puedes pagar con tarjeta de crédito, Apple Pay y Google Pay. También puedes pagar licencias para 50 usuarios y más mediante transferencia bancaria.
          - q: ¿Puedo adquirir una licencia para SeaTable Server sin renovación automática?
            a: Si desea adquirir una licencia de SeaTable Server sin renovación automática de la licencia, adquiera una licencia con renovación automática y desactive la renovación automática en el [Portal de Gestión de Suscripciones de SeaTable Server](https://licenses.seatable.com/p/login/5kA4j61uU641eqY000) inmediatamente después de la compra.
          - q: ¿Cómo puedo cancelar la renovación automática de la licencia SeaTable Server?
            a: Puede desactivar la renovación automática en cualquier momento en el [Portal de Gestión de Suscripciones de SeaTable Server](https://licenses.seatable.com/p/login/5kA4j61uU641eqY000).
          - q: ¿Cómo puedo personalizar la dirección de facturación?
            a: Puede cambiar la dirección de facturación en cualquier momento en el [Portal de Gestión de Suscripciones de SeaTable Server](https://licenses.seatable.com/p/login/5kA4j61uU641eqY000).<br><br>No es posible modificar una factura a posteriori.
          - q: ¿Puedo cambiar el tamaño de una licencia de SeaTable Server en funcionamiento?
            a: Puede ampliar una licencia de SeaTable Server para 50 usuarios o más en cualquier momento. Póngase en contacto con sales@seatable.com e indique la clave de licencia y el número de usuarios deseado. El precio de la licencia para los usuarios adicionales se calcula pro rata temporis.<br><br>Una licencia SeaTable Server para 10 y 25 usuarios no puede aumentarse durante el periodo de vigencia. Si necesita más usuarios, deberá adquirir una nueva licencia.<br><br>No es posible combinar varias licencias. Una instancia de SeaTable Server solo puede conectarse a una licencia.
          - q: ¿Puedo combinar varias licencias de SeaTable Server?
            a: No es posible combinar varias licencias de SeaTable Server. Sólo se activa una licencia en una instancia de SeaTable Server.
          - q: ¿Cómo funciona la renovación automática?
            a: Recibirá un correo electrónico unos 30 días antes de que caduque su licencia de SeaTable Server informándole de la próxima renovación. El correo electrónico explicará cuándo tendrá lugar la renovación y qué método de pago se utilizará. El correo electrónico también contendrá un enlace al [Portal de Gestión de Suscripciones de SeaTable Server](https://licenses.seatable.com/p/login/5kA4j61uU641eqY000). Allí podrá cambiar la dirección de facturación y el método de pago. Tras la renovación, recibirá la factura y los documentos de la licencia por correo electrónico. Para activar la licencia renovada, cargue el archivo de licencia en su instancia de SeaTable Server.
          - q: ¿Puedo especificar un número de pedido o un centro de costes al comprar una licencia?
            a: "Si necesita una referencia en la factura, póngase en contacto con sales@seatable.com. Incluya la siguiente información en su consulta: Número de usuarios, dirección de facturación, NIF, correo electrónico de contacto y correo electrónico de facturación, si procede. Recibirá una oferta por correo electrónico. Indíquenos la referencia al confirmar la oferta. La referencia se mencionará en la factura."
          - q: ¿Tengo descuento como organismo público o como organización sin ánimo de lucro?
            a: Las instituciones públicas y las organizaciones sin ánimo de lucro disfrutan de un descuento en las licencias de SeaTable Server. Póngase en contacto con [nuestro departamento de ventas]({{< relref "pages/contact" >}}).<br><br>Las licencias SeaTable Server para 10 y 25 usuarios no suelen estar sujetas a ningún descuento.
          - q: ¿Para qué periodos de licencia puedo adquirir una licencia para SeaTable Server?
            a: La duración mínima de una licencia de software para SeaTable Server es de 1 año. También puede adquirir licencias con plazos de 2 y 3 años. Ahorra un 5% o un 10% en licencias con plazos de 2 o 3 años.<br><br>Por lo general, el canon de licencia se factura y vence al principio del periodo de licencia por la totalidad del plazo.<br><br>Para licencias con un plazo más largo, póngase en contacto con [nuestro departamento de ventas]({{< relref "pages/contact" >}}) e indique el plazo deseado y el número de usuarios. Recibirá una oferta por correo electrónico.
          - q: ¿Cómo activo la licencia para SeaTable Server?
            a: Debe tomar medidas para activar la licencia. Inicie sesión en su instancia de SeaTable Server como usuario con derechos de administrador y acceda a la administración del sistema. Para ello, haga clic en su avatar en la esquina superior derecha de la página de inicio. Puede cargar el archivo de licencia en el área de información de la administración del sistema. El periodo de validez de la licencia se mostrará inmediatamente en el área de información.<br><br>Si la interfaz web de su instancia de SeaTable Server ya no es accesible, debe guardar el archivo de licencia en el sistema de archivos del host. Encontrará más información en el [Manual de administración de SeaTable](https://admin.seatable.com).
          - q: ¿Qué derechos me otorga la licencia del software SeaTable Server?
            a: Una licencia de software para SeaTable es la autorización para que el licenciatario utilice SeaTable Server. Los derechos de uso otorgados por la licencia y otros derechos se pueden encontrar en el [EULA de SeaTable Server Enterprise Edition]({{< relref "pages/legal/eula" >}}).
          - q: ¿Es transferible una licencia?
            a: El [EULA de SeaTable Server Enterprise Edition]({{< relref "pages/legal/eula" >}}) excluye la transferencia de derechos de uso. No podrá vender ni ceder una licencia.
          - q: ¿Puedo adquirir también una licencia para SeaTable Server a través de un distribuidor?
            a: Sólo puede adquirir licencias de SeaTable Server directamente de SeaTable GmbH.
          - q: ¿Cuáles son los requisitos mínimos para utilizar SeaTable Server?
            a: Consulte el [Manual de administración de SeaTable](https://admin.seatable.com) para todas las cuestiones técnicas.

    - name: faq
      weight: 20
      xshow: 'showCloud'
      title: Preguntas Frecuentes
      items:
          - q: ¿Puedo usar SeaTable Cloud gratis?
            a: 'Con nuestra suscripción Free puedes usar SeaTable Cloud permanentemente con hasta 25 usuarios sin costo. Al registrarte, activas esta suscripción.<br><br>Si los límites o funciones de la suscripción Free son insuficientes, puedes actualizar en cualquier momento a la suscripción de pago Plus o Enterprise con mayores límites y funciones extendidas.'

          - q: ¿Puedo probar las funciones Enterprise?
            a: Podemos actualizar tu suscripción Free o Plus a Enterprise por tiempo limitado sin costo. [Envía una solicitud a través de la administración de equipo](https://account.seatable.com/).

          - q: ¿Qué es un equipo y qué es un usuario?
            a: En SeaTable Cloud colaboras en equipos. Cada miembro tiene una cuenta de usuario (un equipo puede tener solo un miembro).<br><br>Al registrarte se crea un equipo donde eres el administrador. Puedes agregar más usuarios y asignar otros administradores.<br><br>Los usuarios se identifican por email y solo pueden estar en un equipo.

          - q: ¿Puedo cambiar el número de usuarios en mi equipo?
            a: 'Puedes ajustar el número de usuarios en cualquier momento.<br><br>En los planes Free, Plus y Enterprise hazlo desde la [administración de equipo](https://account.seatable.com/). Para SeaTable Dedicated contacta a tu representante.<br><br>El plan Free limita a 25 usuarios. Plus, Enterprise y Dedicated no tienen límite.'

          - q: ¿Puedo combinar diferentes suscripciones en mi equipo?
            a: 'No es posible combinar suscripciones en un mismo equipo.<br><br>Pero puedes distribuir usuarios en varios equipos con diferentes suscripciones.'

          - q: ¿Puedo combinar diferentes períodos de facturación?
            a: 'No se pueden combinar períodos de facturación. Un equipo se factura completamente mensual o anual.<br><br>El pago anual ofrece un 20% de descuento.'

          - q: ¿Cómo cancelo una suscripción Plus o Enterprise?
            a: 'Cancela desde la [administración de equipo](https://account.seatable.com/). Podrás usar las funciones hasta el final del período.<br><br>Luego volverás al plan Free, que podría limitar tu acceso a solo lectura.'

          - q: '¿Qué pasa si alcanzo los límites de mi suscripción?'
            a: 'Te notificaremos. Podrás acceder a tus bases pero no añadir filas ni archivos.'

          - q: '¿Qué métodos de pago aceptan?'
            a: 'Tarjetas, Apple Pay y Google Pay. Clientes Enterprise con pago anual y 10+ usuarios pueden pagar por transferencia.'

          - q: '¿Cómo cambio la dirección de facturación?'
            a: 'Ajústala en cualquier momento desde la [administración de equipo](https://account.seatable.com/).<br><br>No se pueden modificar facturas emitidas.'

          - q: '¿Qué hay sobre privacidad y seguridad?'
            a: 'Son prioridad absoluta. Tus datos se procesan exclusivamente en centros de datos alemanes con monitoreo continuo. Más detalles en [Privacidad]({{< relref "pages/legal/data-privacy" >}}) y [Seguridad]({{< relref "pages/legal/security" >}}).'

          - q: '¿Cómo elimino mi cuenta?'
            a: 'El administrador puede eliminar usuarios o equipos completos desde la [administración](https://account.seatable.com). Si eres el único usuario, eres administrador.<br><br>Lamentamos que dejes SeaTable. [Comparte tus razones]({{< relref "pages/contact" >}}).<br><br>Los [Términos de Servicio]({{< relref "pages/legal/terms-of-service" >}}) detallan el tratamiento de datos tras la eliminación.'
---
