---
title: 'Ejemplos y consejos'
description: 'Ejemplos prácticos y consejos para el uso eficaz del plugin de chat con IA en SeaTable.'
weight: 4
url: '/es/ayuda/plugin-chat-ia-ejemplos-y-consejos'
seo:
    title: 'Plugin de chat con IA: ejemplos y consejos para buenas preguntas'
    description: 'Aprenda con ejemplos concretos cómo utilizar de forma óptima el plugin de chat con IA en SeaTable: consultar datos, analizarlos y editarlos.'
---

El plugin de chat con IA entiende lenguaje natural y trabaja directamente con los datos de su base. En este artículo encontrará ejemplos concretos para casos de uso típicos, así como consejos con los que obtendrá mejores resultados. También encontrará indicaciones generales sobre cómo formular buenas preguntas en el artículo [Cómo formular buenas preguntas]({{< relref "help/ai/ai-agents/good-questions" >}}).

## Consultar datos

El caso de uso más frecuente: usted hace una pregunta y el chat le devuelve las entradas correspondientes de su base.

> *"Muéstrame todas las tareas abiertas que vencen esta semana."*

> *"¿Cuántos clientes tenemos de España?"*

> *"¿Qué facturas aún no están pagadas?"*

> *"¿Hay proyectos sin un responsable asignado?"*

Cuanto más exactamente mencione los nombres de tablas y columnas, más precisa será la respuesta. Si no está seguro de qué columnas existen, simplemente pregunte:

> *"Describe la estructura de mi base."*

## Analizar datos

El chat no solo puede mostrar sus datos, sino también evaluarlos, agruparlos y resumirlos.

> *"¿Cuál fue la facturación total del último trimestre, desglosada por comercial?"*

> *"Resume las solicitudes de soporte de la última semana."*

> *"¿Qué productos se pidieron con más frecuencia?"*

> *"¿Cómo se distribuyen los tickets abiertos por prioridad?"*

Este tipo de análisis funcionan especialmente bien cuando su base contiene datos bien mantenidos. En caso de valores faltantes o inconsistentes, el chat suele señalarlo.

## Crear y editar datos

El plugin de chat con IA también puede crear, modificar, vincular y eliminar entradas. Para ello, formule de la manera más clara posible qué tabla, qué columnas y qué valores están implicados.

### Crear nuevas entradas

> *"Crea un nuevo contacto: Nombre 'Müller GmbH', Ciudad 'Hamburgo', Estado 'Interesado'."*

> *"Crea una entrada de seguimiento en la tabla Actividades para cada negocio abierto."*

### Modificar entradas existentes

> *"Cambia el estado de todas las tareas vencidas a 'Escalado'."*

> *"Cambia la prioridad del ticket #412 a 'Alta'."*

### Vincular y eliminar entradas

> *"Vincula todas las facturas con el cliente correspondiente de la tabla Contactos."*

> *"Elimina todas las entradas de prueba de la tabla Borradores."*

Al eliminar, el chat solicita confirmación antes de ejecutar la acción. Aun así, compruebe previamente con una consulta de lectura si las entradas correctas están afectadas.

## Consejos para obtener mejores resultados

**Comience con consultas de lectura.** Antes de modificar datos, compruebe primero si el chat encuentra las entradas correctas. Pregunte primero *"¿Qué tareas están vencidas?"*, antes de decir *"Cambia el estado a Escalado."*

**Divida las tareas complejas.** En consultas de varios pasos, llegará más rápido al objetivo si procede paso a paso. El chat recuerda el contexto de la conversación y usted puede basarse en respuestas anteriores.

**Utilice nombres de tablas y columnas.** No es necesaria la escritura exacta, pero los términos correctos ayudan al chat a interpretar su pregunta correctamente.

**Aproveche el contexto.** Después de una consulta, puede hacer referencia a resultados anteriores con "estos", "de ellos" o "los mismos", sin tener que repetir todo.

## Qué no funciona

El plugin de chat con IA trabaja exclusivamente con los datos de su base de SeaTable. Las siguientes acciones no son posibles:

- **Consultar datos inexistentes.** Si una columna o tabla no existe, el chat no puede ofrecer una respuesta. No inventa datos.
- **Acciones fuera de SeaTable.** El chat no puede enviar correos electrónicos, acceder a sistemas externos ni abrir archivos.
- **Operaciones masivas muy grandes.** Las solicitudes individuales que pretenden crear o modificar cientos de entradas simultáneamente pueden alcanzar sus límites. Divida este tipo de tareas en pasos más pequeños.
