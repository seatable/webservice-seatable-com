---
title: 'Comparación entre las ediciones Developer y Enterprise de SeaTable'
description: 'SeaTable está disponible en dos ediciones diferentes: La Enterprise Edition ofrece toda la gama de funciones. SeaTable Cloud también se basa en la Enterprise Edition. La Developer Edition tiene funcionalidad limitada, pero destaca como base de datos flexible para proyectos web. La Enterprise Edition requiere una licencia de pago, mientras que la Developer Edition puede utilizarse de forma gratuita y sin restricciones.'
color: '#069214'
categories:
    - 'product-features'
date: 2022-02-03
lastmod: '2025-07-22'
author: 'cdb'
url: '/es/comparacion-ediciones'
aliases:
    - /es/editionsvergleich
seo:
    title: 'SeaTable Developer vs Enterprise Edition: comparación'
    description: 'SeaTable ofrece dos ediciones No-Code: Enterprise y Developer. Descubra detalles sobre las funciones y los casos de uso de la plataforma.'
---

[SeaTable Server]({{< relref "pages/product/seatable-server" >}}) es SeaTable para su propio servidor. Al instalar SeaTable en su propia infraestructura, tendrá un control total sobre dónde se almacenan sus datos y quién puede acceder a ellos. Por ello, SeaTable también es recomendable para casos de uso en los que no quiera sacar sus datos de la empresa. También puede operar SeaTable Server exclusivamente en la red local sin posibilidad de acceso a través de Internet.

## Comparación breve

### SeaTable Enterprise Edition

La SeaTable Enterprise Edition (SeaTable EE) es la solución [No-Code]({{< relref "posts/20250307-low-code" >}}) perfecta para equipos y organizaciones de cualquier tamaño que busquen una potente base de datos No-Code y no quieran renunciar a la plena [soberanía de los datos]({{< relref "posts/digitale-souveraenitaet" >}}). Los usuarios pueden implementar también casos de uso exigentes gracias a los permisos avanzados de uso compartido, las automatizaciones, el App Builder integrado y el backend Big Data. Funciones empresariales como la autenticación externa (AD/LDAP, SAML), la gestión de permisos basada en roles, la comprobación de malware y el registro de auditoría harán las delicias de los administradores.

Obtendrá gratis una licencia SeaTable EE para hasta tres usuarios. Para más usuarios se necesita una [licencia de pago]({{< relref "pages/prices" >}}). Gracias a [Docker Compose](https://admin.seatable.com), la instalación se realiza en pocos minutos.

### SeaTable Developer Edition

La SeaTable Developer Edition (SeaTable DE) está dirigida a los desarrolladores que deseen utilizar SeaTable como una base de datos flexible y para quienes las funciones del frontend tengan una importancia secundaria. En estos casos de uso, SeaTable DE destaca por su compatibilidad con numerosos tipos de datos, una potente [REST API](https://api.seatable.com/) y aplicaciones para conocidas plataformas de automatización como Zapier, Make y n8n.

SeaTable DE no requiere ninguna licencia de pago. Encontrará las instrucciones de instalación [aquí](https://admin.seatable.com/installation/basic-setup/).

## Comparación funcional

|                                              | Developer Edition                                                                                          | Enterprise Edition                                                  |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **Plataforma y entorno**                     |                                                                                                            |                                                                     |
| Sistema operativo del servidor               | Linux                                                                                                      | Linux                                                               |
| Método de instalación                        | Docker                                                                                                     | Docker                                                              |
| Imágenes Docker                              | [Docker Hub](https://hub.docker.com/r/seatable/seatable-developer)                                         | [Docker Hub](https://hub.docker.com/r/seatable/seatable-enterprise) |
| **Licencia**                                 |                                                                                                            |                                                                     |
| Tipo de licencia                             | [híbrida (código abierto y propietaria)](https://admin.seatable.com/introduction/dtable-server-license/)   | [propietaria]({{< relref "pages/legal/terms-of-service" >}})        |
| Modelo de precios de la licencia             | gratis                                                                                                     | basado en el usuario                                                |
| **Límites**                                  |                                                                                                            |                                                                     |
| Bases ilimitadas                             | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Tablas ilimitadas                            | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Filas ilimitadas                             | {{< icon icon="circle-check" class="text-seatable-orange" >}} (pero sin backend de archivo)                | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Almacenamiento ilimitado                     | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Usuarios ilimitados                          | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}} (se requiere licencia) |
| Control de versiones (instantáneas)          | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| **Captura y edición de datos**               |                                                                                                            |                                                                     |
| 26 tipos de columnas                         | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| 6 tipos de vistas                            | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Vistas privadas                              | {{< icon "circle-xmark" >}}                                                                                | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Filtro                                       | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Agrupación                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Clasificación                                | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Formato condicional                          | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Formularios web                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Registros compartidos                        | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Procesamiento de datos                       | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Estadísticas                                 | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Importación desde CSV y XLSX                 | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Exportación a CSV y XLSX                     | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Notificaciones                               | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Automatizaciones                             | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Backend Big Data                             | {{< icon "circle-xmark" >}}                                                                                | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Compatibilidad con JavaScript                | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Compatibilidad con Python (instalación independiente) | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                     | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| **Colaboración**                             |                                                                                                            |                                                                     |
| Colaboración en tiempo real                  | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Enlaces externos                             | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Enlaces de invitación                        | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Compartir bases                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Compartir vistas                             | {{< icon "circle-xmark" >}}                                                                                | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Permisos de compartición individuales        | {{< icon "circle-xmark" >}}                                                                                | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Permisos de tabla                            | {{< icon "circle-xmark" >}}                                                                                | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Permisos de columna                          | {{< icon "circle-xmark" >}}                                                                                | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Bloqueo de filas                             | {{< icon "circle-xmark" >}}                                                                                | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| **Construcción de aplicaciones**             |                                                                                                            |                                                                     |
| App Builder universal                        | {{< icon "circle-xmark" >}}                                                                                | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| App Builder de consulta de datos             | {{< icon "circle-xmark" >}}                                                                                | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| **Plugins y extensiones**                    |                                                                                                            |                                                                     |
| Mapas                                        | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Diseño de página                             | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Diseño de informes                           | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Consulta SQL                                 | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Integración con Google Calendar              | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}} (se requiere una instalación independiente) |
| Integración con ONLYOFFICE                   | {{< icon "circle-xmark" >}}                                                                                | {{< icon icon="circle-check" class="text-seatable-orange" >}} (se requiere una instalación independiente) |


|                                               | Developer Edition                                             | Enterprise Edition                                            |
| --------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| **API y opciones de integración**             |                                                               |                                                               |
| REST API                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Zapier                                        | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Make                                          | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| n8n                                           | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Integrately                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| **Marca y personalización**                   |                                                               |                                                               |
| Plantillas propias                            | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| URL propia                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Logotipo propio                               | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Logotipo en el formulario web                 | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Imagen de portada en el formulario web        | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Ocultar “Powered by”                          | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| **Gestión de usuarios y permisos**            |                                                               |                                                               |
| Base de datos local de usuarios               | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Autenticación de dos factores                 | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Autenticación mediante AD/LDAP                | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Inicio de sesión único mediante SAML/OAuth2   | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Roles de usuario                              | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| **Backend y escalabilidad**                   |                                                               |                                                               |
| Soporte S3                                    | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Soporte de clústeres                          | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |

## Diferencias entre versiones

Tanto la SeaTable Enterprise Edition como la Developer Edition se pueden descargar cómodamente desde Docker Hub:

- https://hub.docker.com/r/seatable/seatable-enterprise
- https://hub.docker.com/r/seatable/seatable-developer

**Las ediciones se diferencian sobre todo en sus versiones:**

La Developer Edition proporciona únicamente una versión base, por ejemplo **5.3.0**, basada en la primera versión Enterprise correspondiente. La Enterprise Edition se desarrolla y actualiza continuamente. Allí siempre encontrará la versión más reciente, como **5.3.12**.

Los problemas detectados en la Developer Edition solo se corrigen con la siguiente versión principal (por ejemplo, de 5.3.0 a 5.4.0).

## Diferencias en pruebas y soporte

La **SeaTable Enterprise Edition** se prueba exhaustivamente para garantizar una experiencia lo más estable y libre de errores posible. En cambio, **no se realizan pruebas sistemáticas** para la **Developer Edition**.

El **soporte de pago** está disponible únicamente para la edición Enterprise; **no se proporciona soporte oficial** para la Developer Edition.

Si tiene preguntas sobre la Developer Edition, le recomendamos utilizar el [foro de la comunidad SeaTable](https://forum.seatable.com). Sin embargo, tenga en cuenta que la mayoría de las consultas se refieren a la Enterprise Edition, ya que es más utilizada y está oficialmente soportada.
