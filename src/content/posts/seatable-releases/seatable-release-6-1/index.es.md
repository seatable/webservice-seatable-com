---
title: 'SeaTable 6.1: Más potencia para aplicaciones, bases e integraciones'
description: 'SeaTable 6.1 aporta nuevas funciones para el App Builder, el Base Editor y en el ámbito de las integraciones. Hay para todos los gustos.'
date: 2026-03-20
author: 'rdb'
url: '/es/seatable-release-6-1'
color: '#fad102'
categories:
    - 'product-features'
seo:
    title: 'SeaTable 6.1: Más potencia para aplicaciones, bases e integraciones'
    description: 'SeaTable 6.1 aporta nuevas funciones para el App Builder, el Base Editor y en el ámbito de las integraciones. Hay para todos los gustos.'
register:
    show: true
---

En el **App Builder**, el número de [tipos de página]({{< relref "help/app-builder/seitentypen-in-universellen-apps/ueberblick" >}}) aumenta a 10; el tipo de página **Mapa** es nuevo. SeaTable 6.1 amplía las opciones para las columnas de enlace en los demás tipos de página. Ahora se pueden configurar de manera uniforme y asignarles autorizaciones finamente graduadas. Los usuarios de aplicaciones pueden esperar una **opción de impresión para los cuadros de mando**, así como funciones ampliadas de filtrado y clasificación.

En el **Base Editor**, la [columna Enlace]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}}) adquiere protagonismo gracias a una actualización funcional: las reglas de filtrado dinámico permiten controlar las filas seleccionables en función de la fila de origen respectiva: cada fila obtiene así su propia selección individual. También son nuevos los dos [tipos de vista]({{< relref "help/base-editor/ansichten/was-ist-eine-ansicht" >}}) **Árbol** y **Línea de tiempo**, que sustituyen a los plugins del mismo nombre. En los registros de la base, los filtros proporcionan una mejor visión general de las actividades de una base.

También ha ocurrido mucho en el área de **Integraciones**: SeaTable 6.1 introduce una conexión con Google Calendar y una función de importación desde Airtable. Junto al plugin mejorado de relaciones entre tablas se encuentra el nuevo [plugin de Chat IA]({{< relref "help/ai/ai-chat/introduction" >}}), que permite realizar análisis y cambios en los datos mediante el lenguaje natural.

SeaTable 6.1 ya está disponible para su descarga en el conocido [Repositorio Docker](https://hub.docker.com/r/seatable/seatable-enterprise); en el [Changelog](https://cloud.seatable.io/dtable/view-external-links/c9124bcd934b47bc8f30/) encontrará -como siempre- la lista completa de todos los cambios.

La nueva versión se desplegará en [SeaTable Cloud]({{< relref "pages/product/seatable-cloud" >}}) el 25 de marzo. La actualización va acompañada de una mejora de las suscripciones Free y Plus. **Las automatizaciones**, antes exclusivas de la suscripción Enterprise, también estarán disponibles en [Free y Plus]({{< relref "pages/prices" >}}). Los equipos Free reciben 100 ejecuciones de automatización al mes; los equipos Plus reciben 500 ejecuciones al mes y un miembro del equipo. El precio de la suscripción Plus no cambia y la Free sigue siendo gratuita.

## Aplicaciones más potentes

Las distribuciones espaciales pueden visualizarse en Bases con el [map plugin]({{< relref "help/base-editor/plugins/anleitung-zum-karten-plugin" >}}). El nuevo tipo de página **Mapa** ahora también lo hace posible en las aplicaciones. Al igual que en otras páginas, los preajustes de página pueden utilizarse para ocultar registros de datos y limitar el alcance de los registros de datos mostrados. También pueden configurarse el valor de visualización y el efecto hover.

![nuevo tipo de página para mapas geográficos](map-page-app-builder-seatable-6-1.png)

{{< warning headline="Nota para autoalojadores" >}}

Debe almacenarse un **token de la API de Google** en la configuración del SeaTable Server para que el tipo de página pueda mostrarse y utilizarse en el App Builder. Encontrará más detalles en el [Manual del administrador](https://admin.seatable.com/configuration/plugins/#map-plugin).

{{< /warning >}}

SeaTable 6.1 estandariza las opciones de configuración y el concepto de autorización para **columnas de enlace en el App Builder**. Se pueden activar individualmente tres autorizaciones en las páginas de tipo Galería, Kanban, Calendario, Línea de tiempo y Registro único:

- Crear y vincular nuevas entradas
- Vincular entradas existentes
- Editar entradas vinculadas

En SeaTable 6.2, se añadirá la cuarta autorización **Eliminar enlaces existentes**. Los ajustes de los enlaces seguirán sin estar disponibles en las páginas del panel de control y de consulta, ya que estos dos tipos de página no permiten la edición.

Los **Ajustes de columna para la tabla vinculada** permiten adaptar individualmente estas autorizaciones al caso de uso específico. El administrador de la aplicación puede definir qué columnas se muestran en la tabla vinculada, cuáles son editables y cuáles son campos obligatorios.

En la nueva versión, se han añadido **funciones de clasificación y filtrado** a los tipos de página Galería, Kanban y Calendario. Éstas permiten a los usuarios de la app personalizar el alcance de los datos mostrados y su presentación, lo que supone una notable ganancia de claridad en cuanto aumenta la cantidad de datos.

La **nueva función de impresión en la página del Cuadro de mandos** ofrece más flexibilidad. Una vez activada, permite imprimir fácilmente una página en papel.

## Editor de bases más potente

### Dos nuevos tipos de vista

El nuevo tipo de **Vista de árbol** muestra los registros de datos en una estructura jerárquica con nodos expandibles y plegables -una estructura de árbol- y permite así una visualización intuitiva de las relaciones entre los registros de datos. La **jerarquía de los registros de datos** resulta de los vínculos entre las tablas. La vista de árbol es especialmente adecuada para gestionar categorías de productos y organizaciones de proyectos.

{{< warning headline="Nota de uso" >}}
Actualmente, la nueva vista de árbol está limitada a **tres niveles jerárquicos** y no admite enlaces dentro de una tabla.
{{< /warning >}}

El segundo nuevo tipo de **Vista de línea de tiempo** organiza los registros de datos en una línea de tiempo y, por lo tanto, es la primera opción cuando las relaciones y dependencias temporales están en primer plano.

![Nuevos tipos de vista](two-new-views-seatable-6-1.png)

Las nuevas vistas **reemplazarán a los plugins del mismo nombre**. Sin embargo, la reimplementación como vistas es algo más que un cambio en la interfaz de usuario. Como vistas de pleno derecho, pueden compartirse específicamente a través de las vistas y tenerse en cuenta en las acciones definidas por el usuario, lo que simplemente no es posible con un plugin. La vista de árbol también añade funcionalidad. Las columnas que se mostrarán pueden seleccionarse para cada nivel jerárquico. Con el [plugin de árbol]({{< relref "help/base-editor/plugins/anleitung-zum-tree-plugin" >}}) esto se limitaba al nivel superior.

### Reglas de filtrado en las columnas de enlaces

Una de las novedades más útiles está algo escondida en los ajustes de la columna de enlaces: La opción **Restringir enlaces con una regla de filtrado**. Esto le permite restringir la selección de filas enlazables basándose en reglas simples o complejas. Los propios filtros pueden ser estáticos o dinámicos:

- Con un **filtro estático**, se utiliza un valor de filtro normalizado para filtrar las filas de la tabla enlazada (por ejemplo, sólo se pueden enlazar las filas que no tengan el valor "archivado"). El efecto es, por tanto, similar al de la opción **Restringir los enlaces a una vista**.
- Con un **filtro dinámico**, el valor de filtro utilizado para filtrar las filas de la tabla vinculada es un valor de columna de la fila activa (por ejemplo, sólo pueden vincularse las filas cuyo estado sea idéntico al estado de la fila activa). **Las filas con diferentes valores de filtro** tienen, por tanto, diferentes filas vinculables.

![Reglas de filtrado en columnas enlazables](dynamic-link-selection-filters-seatable-6-1.png)

### Opciones de filtro en los Base Logs

Los administradores estarán encantados con las opciones de filtro en los [Base Logs]({{< relref "help/base-editor/historie-und-versionen/aenderungen-ueber-die-logs-rueckgaengig-machen" >}}). Ahora los registros pueden filtrarse por usuario, tabla y periodo de tiempo. Por supuesto, también son posibles los filtros combinados. Cualquiera que desee **realizar un seguimiento o deshacer cambios** en una base con muchos usuarios apreciará rápidamente la nueva claridad.

## Más integraciones

Pasar de Airtable a SeaTable es más fácil que nunca con SeaTable 6.1: Al crear una nueva base, simplemente seleccione **Importar base desde Airtable**, introduzca un ID de base de Airtable y un Token de acceso personal en el diálogo de importación y listo. SeaTable hace el resto.

La segunda nueva integración se refiere a Google Calendar. La nueva acción de automatización **Gestionar citas en Google Calendar** permite crear citas directamente desde SeaTable en un Google Calendar y actualizar las existentes.

### Actualización del plugin de relaciones entre tablas

El [plugin de relaciones entre tablas]({{< relref "help/base-editor/plugins/anleitung-zum-tabellenbeziehungen-plugin" >}}) es un viejo conocido y recibe una amplia actualización con SeaTable 6.1:

- Las tablas pueden ocultarse individualmente
- Las columnas mostradas pueden controlarse seleccionando una vista
- Los enlaces dentro de una tabla pueden ocultarse
- Amplias funciones de formato
- Función de exportación
- Función de reinicio del diagrama
- Función de nota

Esto le permite crear diagramas de relaciones claros incluso para bases complejas.

![Plugin de relaciones de tablas mejorado](table-relationship-plugin-seatable-6-1.png)

### Chat con inteligencia artificial

Totalmente nuevo es el **plugin de Chat IA**. Le permite editar y analizar bases en lenguaje natural. Cree registros de datos, modifique valores, vincule filas, cree análisis... en alemán, inglés, francés y otros idiomas. El plugin realmente da lo mejor de sí con análisis ad hoc que van más allá de las funciones estándar.

Un ejemplo de solicitud de análisis de una lista de datos de direcciones sería: "Haga una lista de todas las personas de la lista de datos de direcciones que viven en una ciudad con más de 1 millón de habitantes." A continuación, el modelo analiza las direcciones residenciales, determina la población del lugar de residencia y genera la lista de resultados sobre esta base.

![plugin de chat AI](chat-ai-plugin-seatable-6-1.png)

Para utilizar el plugin, debe almacenar un **token de API para uno de los LLM compatibles** en la [Configuración]({{< relref "help/ai/ai-chat/setup" >}}) del plugin. Los [modelos soportados]({{< relref "help/ai/ai-chat/supported-models" >}}) incluyen los de Anthropic, OpenAI y Mistral. Pronto se añadirán más modelos.

{{< warning headline="Fase beta" >}}
El plugin de Chat IA se encuentra actualmente en fase beta. Estaremos encantados de que comparta sus experiencias con nosotros en el [Foro de SeaTable](https://forum.seatable.com/t/we-need-your-feedback-ai-chat-for-seatable/7265).
{{< /warning >}}

## Y más

- Los [formularios]({{< relref "help/base-editor/webformulare/webformulare" >}}) – tanto los formularios clásicos como los de las aplicaciones – pueden diseñarse ahora con **páginas múltiples**. Esto aumenta notablemente la claridad en cuanto intervienen muchos campos.

- [Columnas de correo electrónico]({{< relref "help/base-editor/spaltentypen/die-e-mail-spalte" >}}) permiten almacenar direcciones de correo electrónico con el formato 'Nombre para mostrar < mail@example.com >'. El envío de correos electrónicos a este tipo de direcciones fallaba anteriormente, tanto en las reglas de automatización como en los botones. Esto es historia con SeaTable 6.1.

- La nueva [Acción de automatización]({{< relref "help/base-editor/automationen/automations-aktionen" >}}) **Archive** le permite automatizar el traslado de registros de datos desde el Base Editor al [backend de Big Data]({{< relref "help/base-editor/big-data/zeilen-ins-big-data-backend-verschieben" >}}). La acción se ofrece para ambos activadores periódicos.

## Discontinuaciones

SeaTable 6.2 elimina dos funciones de SeaTable.

1. La función de **sincronización de correos electrónicos a través de IMAP** se eliminará de SeaTable con SeaTable 6.2. Pedimos a los usuarios afectados que repliquen la sincronización a través de una de las plataformas de automatización compatibles: Make, n8n o Zapier.
2. SeaTable 6.2 también pone fin a la compatibilidad con las aplicaciones basadas en el [constructor de aplicaciones de galería o consulta de datos]({{< relref "help/app-builder/app-verwaltung/datenabfrage-app" >}}) de la versión 4.3 de SeaTable y anteriores. Recomendamos migrar estas aplicaciones al [Universal App Builder]({{< relref "help/app-builder/app-verwaltung/universelle-app" >}}), que ofrece bastantes más opciones.

Se espera que SeaTable 6.2 salga a la venta a mediados/finales de mayo de 2026.
