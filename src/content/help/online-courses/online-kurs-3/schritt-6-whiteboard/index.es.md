---
title: 'Paso 6: Pizarra'
date: 2026-10-08
lastmod: '2026-10-08'
categories:
    - 'online-kurs-3'
author: 'bha'
url: '/es/ayuda/curso-3-paso-6-pizarra'
seo:
    title: 'Paso 6 del curso SeaTable 3: la pizarra'
    description: 'Colabore en tiempo real en la pizarra de SeaTable, en la base de marketing (cursores y mensajes en directo), y acuerde después algunas reglas gráficas para saber qué es de quién.'
---

No toda colaboración ocurre en una tabla. A veces un equipo necesita esbozar un proceso, plasmar una idea o bosquejar una maqueta en común: el tipo de reflexión que tiene su sitio en un lienzo compartido, más que en filas y columnas. SeaTable tiene precisamente la herramienta para ello: el plugin de pizarra.

A diferencia de todo lo visto hasta ahora, la pizarra no contiene ninguno de sus datos y, lo que condiciona todo este paso, no guarda constancia de quién hizo qué: un dibujo no tiene registro de actividades. Lo que hace de maravilla es la otra mitad de la colaboración: trabajar juntos en directo, en el mismo espacio y al mismo tiempo.

## La base adecuada para la pizarra

Una pizarra necesita una base que todos los que dibujan en ella puedan modificar. Acaba de dedicar cuatro pasos a aprender a no dar ese tipo de acceso a una base llena de datos sensibles, y el mismo hábito vale aquí: mantenga la coordinación y los bocetos fuera de sus tablas de producción, igual que su lista de referencia de clientes se mantiene separada de la copia de trabajo de marketing. La pizarra va en una base que su compañera puede modificar, nunca en `Sales CRM`.

Esa base es `Campaign Hub`. Es la de marketing, todos los miembros del grupo `Marketing` pueden modificarla y sus cifras confidenciales nunca llegaron a ella: el conjunto de datos común las dejó en `Sales CRM`. Además contiene la pizarra que le corresponde: `Customers data flow`, el diagrama de marketing que muestra cómo le llegan los datos de clientes, y por tanto una representación de esta misma base. Pero todavía muestra la forma antigua de trabajar, cuando marketing partía de una copia manual. Ahora que los datos llegan mediante un conjunto de datos común, hay que volver a dibujar el diagrama, y como fue usted quien puso en marcha este nuevo flujo, le toca a usted actualizarlo.

El plugin de pizarra ya está configurado en `Campaign Hub`, así que no hay nada que instalar: abra `Customers data flow` desde la zona de plugins de la base. En un servidor autoalojado, la pizarra es un componente aparte: si no se abre, quizá su administrador del sistema tenga que [instalarla](https://admin.seatable.com/installation/components/whiteboard/) primero.

Observe que un acceso de solo lectura no habría servido aquí: dibujar en una pizarra requiere permiso de edición.

## Trabajar juntos

Abra la pizarra y estará en un lienzo compartido: todos los que la tienen abierta al mismo tiempo están presentes en ella a la vez. El cursor de cada persona se desplaza por la pizarra en las ventanas de los demás, un puntero láser deja un rastro que se desvanece a lo largo de una forma, y un mensaje breve puede aparecer un momento bajo un cursor. El cursor que se desplaza, el rastro del láser que se desvanece, el mensaje fugaz: esta es la colaboración en el momento que una tabla no le puede ofrecer. El vídeo de abajo lo muestra con dos personas en la misma pizarra.

{{< zoom image="images/lvl3-whiteboard-collab.gif" alt="Dos cursores en la pizarra compartida haciéndose señas, con un rastro de láser y un mensaje bajo uno de los cursores" >}}

## La pizarra no recuerda nada

{{< warning headline="La pizarra no guarda historial" text="A diferencia de su base, la pizarra no guarda ningún registro de quién dibujó qué, ni permite deshacer por autor. El registro de actividades del paso 4 no tiene equivalente aquí. Si importa quién añadió algo, tiene que mostrarlo la propia pizarra." />}}

Como la pizarra no guarda constancia de nada, conviene acordar algunas reglas gráficas antes de llenarla, igual que un equipo acuerda reglas para nombrar sus datos. La pizarra de partida aplica dos:

- un color por departamento, para saber de un vistazo a qué equipo pertenece cada elemento;
- rectángulos sin relleno alrededor de lo que va junto, aquí uno por base.

Son solo un punto de partida: su equipo puede adoptar las suyas. Que sean pocas y sencillas, e intente atenerse a ellas. Puede incluso crear una pizarra aparte solo para estas reglas, para que todos puedan consultarlas más adelante.

## Actualizar la pizarra

La pizarra de partida todavía muestra la forma antigua: la lista de clientes llega a marketing mediante una exportación manual (`manual export`) hacia `Customers list (manual)`. Ha dedicado todo este curso a sustituir precisamente eso, así que actualice la pizarra: cambie el nombre de algunos elementos y sus colores para que muestre cómo llegan ahora los datos de clientes a marketing. En este caso simplificado, se trata de familiarizarse con las herramientas de la pizarra, así que haga usted mismo todos los cambios, respetando las reglas anteriores.

Ya tiene en sus manos todas las herramientas de colaboración. Es hora de repasar todo lo que ha aprendido y de ponerlo a prueba.

## Para profundizar

Compruebe usted mismo el trabajo en directo, con Malika. Abra una ventana privada (de incógnito) en su navegador, inicie sesión en ella con la cuenta de Malika y abra la misma pizarra: ella tiene acceso, porque es miembro del grupo `Marketing`. Una ventana privada mantiene separadas las dos sesiones, así que usted sigue con su propia sesión en su ventana habitual. Coloque las dos ventanas una al lado de la otra y, en la suya, desplace el cursor por la pizarra, pase el puntero láser a lo largo de una forma o deje un mensaje breve bajo el cursor, y observe cómo cada acción aparece en la ventana de Malika en el mismo momento.

## Artículo de ayuda con más información

- [Instrucciones para el plugin de pizarra (tldraw)]({{< relref "help/base-editor/plugins/anleitung-zum-whiteboard-plugin-tldraw/" >}})
