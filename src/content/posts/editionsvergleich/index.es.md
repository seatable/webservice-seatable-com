---
title: 'Comparación entre las ediciones Developer y Enterprise de SeaTable'
description: 'SeaTable está disponible en dos ediciones diferentes. Mientras que la edición Enterprise ofrece la gama completa de funciones y, por tanto, se utiliza para la nube SeaTable y los sistemas dedicados, la edición Developer puede utilizarse de forma gratuita y es ideal para los desarrolladores como base de datos flexible.'
color: '#069214'
categories:
    - 'product-features'
lastmod: '2025-07-22'
url: '/es/comparacion-ediciones'
aliases:
    - /es/editionsvergleich
seo:
    title: 'SeaTable Developer y Enterprise Edition comparadas'
    description: 'SeaTable ofrece dos ediciones No-Code autoalojadas: Enterprise y Developer. Descubra características y casos de uso de cada edición.'
---

SeaTable Server es SeaTable para su propio servidor. Al instalar SeaTable en su propia infraestructura, tiene un control total sobre dónde están sus datos y quién accede a ellos. SeaTable también se recomienda para los casos de uso en los que no se desea llevar los datos fuera de las instalaciones. También puede operar SeaTable Server exclusivamente en la red local sin acceso a través de Internet.

## SeaTable Server está disponible en dos ediciones diferentes:

### SeaTable Server Enterprise Edition

SeaTable Server Enterprise Edition es la solución perfecta [sin código]({{< relref "posts/20250307-low-code" >}}) para equipos y organizaciones de todos los tamaños que desean una funcionalidad completa y un control de los datos. Sólo la edición Enterprise ofrece la posibilidad de utilizar la autenticación externa mediante LDAP o SAML. Los permisos y automatizaciones de la versión ampliada también están disponibles únicamente en esta edición.  
Puede obtener una licencia SeaTable Enterprise para un máximo de tres usuarios en cualquier momento. Encontrará el formulario de inscripción correspondiente [en este enlace]({{< relref "pages/product/seatable-server" >}}). La instalación se realiza según el [manual de administración](https://admin.seatable.com) utilizando Docker.

### SeaTable Server Developer Edition

La edición para desarrolladores de SeaTable Server está dirigida principalmente a los desarrolladores que desean utilizar SeaTable como una base de datos flexible y que pueden no utilizar el frontend en absoluto. En este caso, la edición para desarrolladores se caracteriza por la potente [API de SeaTable](https://api.seatable.com/), las aplicaciones para las distintas plataformas de automatización y la total compatibilidad con todos los tipos de columnas. La edición para desarrolladores se puede utilizar de forma gratuita. Puede encontrar las instrucciones de instalación [aquí](https://admin.seatable.com).

## Diferencias en la comparación

|                                           | Edición para desarrolladores                                                                                | Edición para empresas                                                                                       |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Plataforma y entorno                      |                                                                                                             |                                                                                                             |
| Sistema operativo del servidor            | Linux                                                                                                       | Linux                                                                                                       |
| Método de instalación                     | Docker                                                                                                      | Docker                                                                                                      |
| Docker Imágenes                           | [Docker Hub](https://hub.docker.com/r/seatable/seatable-developer)                                          | [Docker Hub](https://hub.docker.com/r/seatable/seatable-enterprise)                                          |
| Licencia                                  |                                                                                                             |                                                                                                             |
| Tipo de licencia                          | [híbrido (código abierto y propietario)](https://admin.seatable.com/introduction/requirements/#license)                          | [propietario]({{< relref "pages/legal/terms-of-service" >}})                                                |
| Modelo de precio de la licencia           | Gratis                                                                                                      | Basado en el usuario                                                                                        |
| Límites                                   |                                                                                                             |                                                                                                             |
| Bases ilimitadas                          | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               |
| Mesas ilimitadas                          | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               |
| Líneas ilimitadas                         | {{< icon icon="circle-check" class="text-seatable-orange" >}} **(pero sin backend de archivo)**             | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               |
| Memoria ilimitada                         | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               |
| Usuarios ilimitados                       | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               | {{< icon icon="circle-check" class="text-seatable-orange" >}} **(se requiere licencia)**                    |
| Control de versiones (instantáneas)       | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               |
| Adquisición y procesamiento de datos      |                                                                                                             |                                                                                                             |
| 24 tipos de columnas                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               |
| Vistas                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               |
| Vistas privadas                           |                                                                                                             | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               |
| Filtro                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               |
| Agrupación                                | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               |
| Clasificación                             | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               |
| Formato condicional                       | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               |
| Formularios web                           | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               |
| Conjuntos de datos compartidos            | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               |
| Procesamiento de datos                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               |
| Estadísticas                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               |
| Importación desde CSV y XLSX              | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               |
| Exportación a CSV y XLSX                  | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               |
| Notificaciones                            | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               |
| Automatizaciones                          | {{< icon "circle-xmark" >}}                                                                                 | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               |
| Función de archivo                        | {{< icon "circle-xmark" >}}                                                                                 | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               |
| Compatibilidad con JavaScript             | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               |
| Soporte de Python                         | {{< icon icon="circle-check" class="text-seatable-orange" >}} _(se requiere una instalación independiente)_ | {{< icon icon="circle-check" class="text-seatable-orange" >}} _(se requiere una instalación independiente)_ |
| Colaboración                              |                                                                                                             |                                                                                                             |
| Colaboración en tiempo real               | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               |
| Enlaces externos                          | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               |
| Enlaces de invitación                     | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               |
| Liberación de la base                     | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               |
| Ver el comunicado                         | {{< icon "circle-xmark" >}}                                                                                 | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               |
| Autorizaciones individuales de liberación | {{< icon "circle-xmark" >}}                                                                                 | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               |
| Autorizaciones de mesa                    | {{< icon "circle-xmark" >}}                                                                                 | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               |
| Permisos de columna                       | {{< icon "circle-xmark" >}}                                                                                 | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               |
| Bloqueo de líneas                         | {{< icon "circle-xmark" >}}                                                                                 | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               |
| Plugins y extensiones                     |                                                                                                             |                                                                                                             |
| Calendario                                | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               |
| Línea de tiempo                           | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               |
| Galería                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               |
| Kanban                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               |
| Mapas                                     | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               |
| Diseño de la página                       | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               |
| Estadísticas avanzadas                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               |
| Consulta SQL                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                               |
| Integración de ONLYOFFICE                 | {{< icon "circle-xmark" >}}                                                                                 | {{< icon icon="circle-check" class="text-seatable-orange" >}} _(se requiere una instalación independiente)_ |

---

|                                                        | Edición para desarrolladores                                  | Edición para empresas                                         |
| ------------------------------------------------------ | ------------------------------------------------------------- | ------------------------------------------------------------- |
| API y opciones de integración                          |                                                               |                                                               |
| API REST                                               | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Zapier                                                 | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Integromat                                             | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| n8n                                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Locoia                                                 | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Marca y personalización                                |                                                               |                                                               |
| Plantillas propias                                     | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| URL propia                                             | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Logotipo propio                                        | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Logotipo en el formulario web                          | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Foto de portada en el formulario web                   | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| "Ocultar" "Desarrollado por                            | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Administración de usuarios y gestión de autorizaciones |                                                               |                                                               |
| Base de datos local de usuarios                        | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Autenticación de 2 factores                            | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Autenticación mediante AD/LDAP                         | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Inicio de sesión único mediante SAML                   | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Funciones de los usuarios                              | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Backend y escalabilidad                                |                                                               |                                                               |
| Soporte S3                                             | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Apoyo a los clústeres                                  | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |

## Diferencias entre versiones

Tanto la **SeaTable Enterprise Edition** como la **Developer Edition** se pueden descargar fácilmente desde Docker Hub:

- https://hub.docker.com/r/seatable/seatable-enterprise
- https://hub.docker.com/r/seatable/seatable-developer

**La principal diferencia entre ambas ediciones está en sus versiones:**

La Developer Edition ofrece únicamente una versión base, por ejemplo **5.3.0**, basada en la primera versión correspondiente de la Enterprise Edition. En cambio, la Enterprise Edition se desarrolla y actualiza de forma continua. Por lo tanto, siempre encontrará la versión más reciente disponible, como **5.3.12**.

Los problemas detectados en la Developer Edition solo se corrigen con la siguiente versión principal (por ejemplo, de 5.3.x a 5.4.0).

## Diferencias en pruebas y soporte

La **SeaTable Enterprise Edition** se prueba exhaustivamente para garantizar una experiencia lo más estable y libre de errores posible. En cambio, no se realizan **pruebas sistemáticas** para la **Developer Edition**.

El **soporte de pago** está disponible únicamente para la edición Enterprise; no se proporciona **soporte oficial** para la Developer Edition.

Si tiene preguntas sobre la Developer Edition, le recomendamos utilizar el [foro de la comunidad SeaTable](https://forum.seatable.com). Sin embargo, tenga en cuenta que la mayoría de las consultas se refieren a la Enterprise Edition, ya que es más utilizada y está oficialmente soportada.
