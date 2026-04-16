---
title: 'Inicio de sesión único: significado, ventajas y configuración'
description: 'Docenas de contraseñas, constantes solicitudes de inicio de sesión, empleados frustrados y equipos de TI que gestionan a diario el restablecimiento de contraseñas. El inicio de sesión único pone fin a este caos. Pero, ¿cómo funciona? ¿Qué protocolos existen? ¿Y hasta qué punto es segura realmente la autenticación centralizada? Descubra por qué el SSO es indispensable para las empresas modernas.'
seo:
    title: 'Autenticación de inicio de sesión único para una mayor seguridad informática'
    description: 'Explicación del inicio de sesión único: cómo el SSO pone fin al caos de las contraseñas, maximiza la seguridad informática y ahorra un tiempo valioso al iniciar sesión.'
date: 2026-02-04
url: '/es/inicio-de-sesion-unico/'
categories:
    - 'best-practice'
tags:
    - 'Seguridad informática y privacidad de datos'
    - 'Transformación digital'
color: '#3962d2'
register:
   show: true 
--- 

## ¿Qué significa SSO? 

Los empleados de las empresas tienen que cambiar a diario entre diferentes aplicaciones. Cada una de ellas requiere una contraseña segura y única que debe cambiarse periódicamente, y lo que esto significa exactamente varía de una herramienta a otra. Los gestores de contraseñas son una forma probada de evitar que sus empleados olviden constantemente sus contraseñas, pero también requieren una contraseña. El resultado son tickets de asistencia técnica innecesarios, pérdidas de productividad y también problemas de seguridad. El inicio de sesión único resuelve este problema al permitir a los usuarios **acceder a varias aplicaciones o sistemas a través de un inicio de sesión centralizado**.

### Puntos clave

* El inicio de sesión único (SSO) **aumenta la seguridad informática** en su [ITSM]({{< relref "pages/landing-pages/industry-solutions/software-development" >}}) mediante una autenticación centralizada de usuarios y una supervisión simplificada del acceso. 
* El uso de procedimientos de inicio de sesión único **aumenta la productividad** al reducir los inicios de sesión con contraseña.
* Los protocolos habituales, como SAML, OAuth y LDAP, permiten una **integración flexible** en entornos híbridos y en la nube, como SeaTable. 
* Las soluciones SSO con sede en la UE o locales cumplen los requisitos del RGPD y evitan la transferencia de datos a terceros países.

## ¿Cómo funciona la autenticación SSO?

El procedimiento SSO se basa básicamente en una comunicación basada en tokens entre la aplicación web y un **proveedor de identidad central** (IdP).

![El inicio de sesión único simplifica el proceso de registro de los usuarios.](single-sign-on.png)


* Los usuarios se autentican una sola vez en un IdP, por ejemplo, Okta o [Authentik](https://goauthentik.io/). A continuación, el administrador del sistema responsable concede acceso a todos los servicios autorizados sin necesidad de volver a introducir contraseñas. 
* Tras la autenticación SSO satisfactoria, el IdP genera un token SSO, una especie de certificado de seguridad, por ejemplo, como una aserción SAML (basada en XML) o como un JWT (JSON Web Token), y lo almacena en el sistema SSO o en el navegador web. Los tokens SSO contienen información sobre el usuario correspondiente, por ejemplo, el nombre de usuario y una dirección de correo electrónico. 
* Si el usuario desea iniciar sesión en una aplicación web como SeaTable mediante el procedimiento SSO, la aplicación envía un token al IdP, que se compara con el token SSO existente. Si se puede identificar al usuario y está autorizado para la aplicación, la solución SSO valida el token de autenticación y el usuario obtiene acceso a la aplicación.

Todo el proceso de inicio de sesión solo dura unos segundos, sin que el usuario se dé cuenta del proceso de autenticación que se lleva a cabo en segundo plano. Si más tarde su empleado inicia sesión en otra aplicación integrada, esta comprueba primero si ya existe un token válido del IdP. Si es así, **el usuario iniciará sesión automáticamente** sin tener que volver a introducir sus datos. Eso es lo que se entiende por «único» en el inicio de sesión único. Y también existe el cierre de sesión único: cuando el usuario cierra sesión en una aplicación web, el token se invalida y también se cierran todas las demás aplicaciones vinculadas.

## ¿Por qué deberían las empresas implementar SSO? Las ventajas concretas

* **Una administración centralizada en lugar de silos de contraseñas**: en lugar de gestionar los derechos de acceso en diferentes herramientas, sus responsables de TI gestionan las funciones y los permisos desde un lugar centralizado. Esto no solo es una bendición para su personal de TI, sino que también reduce la superficie de ataque y los errores manuales.
    
* **Mayor aceptación de los procesos de transformación digital**: si la transición a las nuevas herramientas se realiza sin problemas, sin discusiones sobre contraseñas, sin frustraciones al iniciar sesión y sin preocupaciones por la seguridad, sus empleados aceptarán los cambios más rápidamente y, según las estimaciones, ahorrarán unos 30 minutos de trabajo al día al no tener que introducir o restablecer contraseñas. Tras solo dos semanas con el inicio de sesión SSO, esto supone un día completo de trabajo ganado para tareas productivas. 
    
* **Mayor seguridad informática y cumplimiento normativo**: muchas soluciones SSO requieren autenticación multifactorial y los registros de auditoría muestran de forma completa quién ha accedido a qué sistemas y cuándo.

* **Evitar la TI en la sombra**: al permitir que los empleados accedan de forma fácil y cómoda a las aplicaciones autorizadas, el departamento de TI reduce el uso de herramientas no autorizadas y potencialmente inseguras. De este modo, el SSO puede ayudar a evitar la aparición de [estructuras de TI en la sombra]({{< relref "posts/schatten-it" >}}). 

![El inicio de sesión único aumenta la seguridad informática.](single-sign-on-it-security.png)    

## ¿Cuáles son los protocolos de inicio de sesión único más comunes?

La seguridad de los sistemas SSO se basa en diversos protocolos que regulan el intercambio de información entre la aplicación y el proveedor de identidad. El protocolo más adecuado para una empresa depende en gran medida del entorno informático y de los requisitos. A continuación, presentamos los protocolos más importantes para facilitar su comprensión.

### SAML 2.0: el estándar empresarial

SAML (Security Assertion Markup Language) lleva años dominando los entornos empresariales y es **el estándar de facto para el SSO en toda la empresa**, además de ser compatible con la [gestión de equipos en SeaTable]({{< relref "help/teamverwaltung/abonnement" >}}). En este caso, el token SSO es una aserción basada en XML, es decir, una carta de certificación digital, que se firma con un certificado. Las ventajas del inicio de sesión único con SAML son considerables:

* SAML se basa en el navegador y funciona a la perfección con las aplicaciones empresariales clásicas. 
* SAML también admite el cierre de sesión único: cuando un usuario cierra la sesión, el IdP puede finalizar todas las sesiones al mismo tiempo. 
* Para sectores regulados, como la administración pública, SAML supone una gran ventaja gracias a sus registros fáciles de auditar.    

Pero SAML también tiene desventajas: 

* El formato XML es difícil de depurar en comparación con JSON. 
* SAML no es compatible con dispositivos móviles.
    
### OAuth 2.0: moderno y nativo para dispositivos móviles

OAuth 2.0 ha sido diseñado específicamente como **SSO para la nube** y es adecuado para entornos con microservicios o conexiones API. Conocido por el lema «Iniciar sesión con Google» o «Iniciar sesión con Facebook», OAuth concede derechos de acceso delegados sin revelar la contraseña real. Es nativo para dispositivos móviles: las aplicaciones de smartphones y tabletas funcionan a la perfección con OAuth. Al igual que con SAML, este protocolo también permite definir derechos de acceso granulares.

DEl punto débil: OAuth se diseñó originalmente solo para la autorización, no para la autenticación. Para solucionar esto, se inventó OpenID Connect (OIDC), que amplía OAuth y ofrece autenticación real. Otra desventaja es la **gestión de tokens de actualización, algo más compleja**, para evitar que los usuarios tengan que volver a iniciar sesión cuando caduca un token.

![El inicio de sesión único permite un registro cómodo..](single-sign-on-protokolle.png)

### LDAP: el clásico

LDAP (Lightweight Directory Access Protocol) es anterior a SAML y OAuth y se utiliza desde la década de 1990. LDAP almacena directorios de usuarios en una estructura de árbol y se utiliza habitualmente en Microsoft Active Directory (AD) en entornos Windows. Por lo tanto, si utiliza un entorno exclusivamente Windows con servidores locales, esta solución es ideal.

Una verdadera desventaja: **LDAP se desarrolló antes de la era de la nube** y no está optimizado para el SSO web.

### JWT: el token descentralizado

Los tokens web JSON (JWT) son más bien una tecnología, no principalmente un protocolo SSO, pero cada vez son más importantes para las autenticaciones modernas. Un JWT es un token firmado basado en texto que contiene información sobre el usuario, como su ID, sus roles y su tiempo de caducidad. Dado que cada token contiene toda la información y los tokens web JSON son compatibles con dispositivos móviles, **esta solución es ideal para sistemas escalables y descentralizados y microservicios**, también porque las API pueden validar muy fácilmente la autenticación JWT.

Por supuesto, también hay una desventaja: los tokens web JSON no se pueden eliminar y son válidos hasta su fecha de caducidad. Por ejemplo, no es tan fácil retirar inmediatamente los derechos de acceso a un usuario tras un incidente de seguridad o un despido inmediato.

### Kerberos: el clásico de las redes Windows

Kerberos fue la respuesta de Microsoft a la autenticación segura de red en dominios Windows. Se basa en un sistema de tickets: el cliente obtiene un ticket del servidor Kerberos que le permite acceder a un servicio específico sin compartir la contraseña. En un dominio Windows puro, puede utilizar Kerberos sin problemas para el inicio de sesión SSO.

Sin embargo, la estricta orientación hacia Windows local también supone una desventaja decisiva. Su uso como SSO en la nube o en entornos híbridos solo funciona con soluciones complementarias. ¿Y las aplicaciones móviles modernas? Kerberos no está diseñado para eso.  

## ¿Qué proveedores de identidad existen para los procedimientos de inicio de sesión único?

Si desea utilizar el procedimiento de inicio de sesión único para su empresa, necesita una herramienta de gestión de identidades y accesos, o lo que es lo mismo, un proveedor de identidades. Allí podrá definir las aplicaciones a las que tendrá acceso cada usuario autenticado. Entretanto, el mercado de herramientas de este tipo se ha consolidado y se ha reducido a unos pocos proveedores, de los cuales le presentamos aquí los más importantes:  

* **Okta**: el líder del mercado nativo en la nube con más de 7000 integraciones de aplicaciones preconfiguradas. Okta destaca por sus **amplias funciones** (MFA adaptativa, políticas basadas en el riesgo, análisis) y su sólido servicio de asistencia, pero tiene su sede en EE. UU., por lo que **su uso solo se recomienda con restricciones en materia de protección de datos**.  
    
* **Microsoft Entra ID** (antes Azure AD): Entra ha crecido mucho y ahora es **el mayor rival de Okta**. El sistema es gratuito para los usuarios de Microsoft 365 y está profundamente integrado en Microsoft. Sin embargo, al ser una solución estadounidense, al igual que Okta, **plantea dudas en materia de protección de datos**. Además, la integración de aplicaciones ajenas al mundo Microsoft resulta complicada.
    
* **Authentik**: esta **solución de código abierto** destaca en todos los aspectos (y la utilizamos en SeaTable como IdP). Authentik **se puede alojar en su propio servidor, es de uso gratuito** y es compatible con la autenticación SAML, OAuth y LDAP. La desventaja: la configuración requiere conocimientos técnicos y el soporte solo lo proporciona la comunidad.
   
![Los proveedores de identidad permiten el inicio de sesión único.](single-sign-on-identity-provider.png)
    
* **OneLogin**: OneLogin ofrece funciones sólidas y cuenta con una **infraestructura global con servidores en Alemania**. La desventaja: OneLogin solo es compatible con aproximadamente la mitad de aplicaciones que Okta y no ofrece asistencia técnica gratuita.
    
* **Authelia**: la solución más ligera entre las soluciones de código abierto para procesos SSO. Authelia **se basa en proxys** y es ideal si solo necesita una solución rápida y sencilla para la autenticación SSO. La gran desventaja: Authelia no es, en sentido estricto, **un IdP completo**, sino que utiliza la autenticación directa a través de proxys inversos, en lugar de protocolos independientes.    

## ¿Es realmente seguro el inicio de sesión único?

Si un sistema SSO es pirateado, los atacantes pueden tener acceso a toda la información de acceso. ¿No supone esto un riesgo de seguridad desproporcionadamente alto? La objeción es totalmente válida, pero no se puede responder con un sí o un no rotundos.

No hay duda: con las soluciones de inicio de sesión único, se concentra el riesgo, por lo que un IdP pirateado es un asunto muy serio. Sin embargo, los procedimientos SSO también ofrecen ventajas que compensan este riesgo: 

1\. **Con SSO hay menos contraseñas en circulación**. Cada contraseña almacenada de forma descentralizada aumenta el riesgo de intrusiones de piratas informáticos.

2\. El IdP puede exigir que cada usuario utilice un segundo factor de autenticación. **La autenticación multifactorial (MFA) bloquea el 99 % de todos los ataques de phishing**.

3\. **Los tokens SSO tienen una vida útil corta**. Por ejemplo, un token SAML o JWT robado solo es válido durante una hora y luego caduca. Una contraseña robada puede seguir funcionando durante meses. 

Por lo tanto, sí, el uso del inicio de sesión único no garantiza una seguridad total, especialmente si no se requiere MFA. Sin embargo, si se implementa correctamente, el SSO ofrece **un nivel de protección que difícilmente se puede alcanzar de forma generalizada con contraseñas gestionadas de forma descentralizada**.

![El inicio de sesión único suele requerir MFA.](single-sign-on-mfa.png)

## SSO y protección de datos: ¿qué deben tener en cuenta los usuarios?

Las soluciones de inicio de sesión único también se pueden utilizar en las instalaciones. Sin embargo, la autenticación SSO se utiliza con mayor frecuencia en entornos en la nube. Por lo tanto, los responsables de TI deben tener siempre en cuenta la protección de datos y el cumplimiento legal a la hora de seleccionar una solución adecuada. Los siguientes puntos son especialmente importantes:

1\. ¿Qué datos se transfieren? Al utilizar SSO en la nube, la información de los usuarios fluye desde el IdP a la aplicación. Estos datos son personales y, por lo tanto, relevantes desde el punto de vista de la protección de datos. En lo que respecta al RGPD europeo, resulta especialmente crítico si el IdP se encuentra en EE. UU. y los datos se transfieren allí. Por lo tanto, recomendamos utilizar un proveedor de identidad europeo o una solución local como Authentik. 
    
2\. Preste atención al consentimiento y a la minimización de datos. El RGPD exige que los usuarios den su consentimiento expreso para la transferencia de sus datos a terceros. Por lo tanto, un buen IdP debe indicar de forma transparente qué datos se comparten con las diferentes aplicaciones.
    
3\. Trabaje con registros de auditoría bien mantenidos. El artículo 5 del RGPD obliga a las empresas que recopilan datos personales a rendir cuentas sobre el tratamiento legal y seguro de los mismos. En concreto, esto significa que los responsables deben poder demostrar quién ha iniciado sesión, cuándo y dónde. La buena noticia es que, por lo general, los proveedores de identidad registran esto automáticamente de forma seudonimizada. 
    
4\. Debe poder eliminar usuarios. El artículo 17 del RGPD regula el derecho de supresión. Independientemente de ello, sin embargo, debería ser interés de toda empresa conceder a los empleados solo los accesos que realmente necesitan y bloquear los accesos de los antiguos empleados. Por lo tanto, un sistema SSO debería facilitarle la eliminación de un usuario, incluso de forma inmediata si es necesario. 

{{< youtube HUIJ8k2zlgY >}}

## SSO en SeaTable

SeaTable es más que una **solución no-code, alojada en Alemania y conforme al RGPD**, para bases de datos flexibles, automatizaciones asistidas por IA y creación de aplicaciones. Como herramienta para la transformación digital de los procesos empresariales, ya se integra a la perfección en los entornos informáticos existentes gracias a la **API de SeaTable**. 

Los suscriptores empresariales de [SeaTable Cloud]({{< relref "pages/product/seatable-cloud" >}}) y los usuarios de la oferta local [SeaTable Server]({{< relref "pages/product/seatable-server" >}}) pueden configurar el inicio de sesión mediante el inicio de sesión único y, de este modo, garantizar una seguridad aún mayor. La integración es sencilla y solo lleva unos minutos. Para ello, los usuarios de la nube deben registrarse en un proveedor de identidad que admita SAML 2.0, que es el protocolo de autenticación utilizado por SeaTable. En nuestro [artículo de ayuda sobre el inicio de sesión único]({{< relref "help/teamverwaltung/sso/konfiguration" >}}) encontrarán todos los pasos descritos. Los clientes del servidor también pueden utilizar LDAP o JWT y encontrarán información detallada en el [manual de administración](https://admin.seatable.com/configuration/authentication/ldap/).

{{< newsletter title="Manténgase informado" subtitle="" submit="Suscríbase ahora" >}}

¡Suscríbase a nuestro **boletín informativo** y manténgase al día sobre temas relacionados con la seguridad informática y la protección de datos!

{{< /newsletter >}}

## Preguntas frecuentes: inicio de sesión único

{{< faq "¿Qué necesito para utilizar SSO?" >}} 
Solo necesita un dominio de correo electrónico empresarial y un proveedor de identidad de inicio de sesión único, como Okta o Authentik. 
{{< /faq >}} 

{{< faq "¿Se pueden revocar fácilmente los derechos de acceso de inicio de sesión único concedidos?" >}}
En principio, puede invalidar los tokens SSO y eliminar usuarios, de modo que, por ejemplo, los antiguos empleados ya no tengan acceso. Sin embargo, en el caso de la autenticación mediante JWT, el token no se puede eliminar inmediatamente, sino que permanece activo hasta la fecha de caducidad especificada. 
{{< /faq >}}

{{< faq "¿Puedo utilizar el procedimiento de inicio de sesión único con varios proveedores de identidad?" >}} 
No, eso no es posible. Todos los usuarios de los dominios que haya configurado deben gestionarse en el mismo proveedor de identidad. 
{{< /faq >}} 

{{< faq "¿Qué es un token SSO?" >}}
Un token SSO es un conjunto de datos o información que se transmite de un sistema a otro durante el proceso SSO. Los tokens son firmados digitalmente por los proveedores de identidad, de modo que el destinatario del token puede verificar si proviene de una fuente fiable. El certificado de seguridad necesario para esta firma digital se proporciona durante la configuración inicial del IdP.
{{< /faq >}} 

{{< faq "¿Qué proveedores de identidad pueden comunicarse con SeaTable Cloud?" >}} 
Le recomendamos que utilice Okta, Authentik o Microsoft Entra ID. {{< /faq >}}