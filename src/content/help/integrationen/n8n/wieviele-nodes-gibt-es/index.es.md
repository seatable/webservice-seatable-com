---
title: 'Las razones de dos Community Nodes: SeaTable y SeaTable-Admin'
date: '2025-10-03'
seo:
    title: 'Nodos SeaTable en n8n: diferencia entre el nodo de usuario y el nodo de administrador'
    description: 'SeaTable en n8n: usa el nodo de usuario para operaciones de datos con token API y el nodo de administrador para tareas de gestión con permisos de admin.'
categories:
    - 'n8n-integration'
url: '/es/ayuda/por-que-hay-dos-community-nodes'
---

En n8n existen dos Community Nodes de SeaTable distintos, cada uno desarrollado para diferentes áreas de uso, lo que te permite diseñar tus flujos de trabajo de forma precisa y segura.

## 1. Nodo SeaTable – Interacción con tus datos

El nodo SeaTable es el estándar probado cuando se trata de trabajar con los datos de tus bases SeaTable. Ya sea que quieras agregar nuevos registros, actualizar los existentes o eliminar entradas, este nodo lo hace posible.

Está disponible tanto en versión Core como Community en n8n. Más detalles en [este artículo]({{< relref "help/integrationen/n8n/n8n-community-vs-core" >}}).

Para usarlo, solo necesitas un **token API de SeaTable** que te da acceso a los datos de tu base.

## 2. Nodo SeaAdmin – Control administrativo

Si deseas realizar tareas administrativas en SeaTable, el nodo SeaAdmin es la opción perfecta.

Con él puedes cómodamente:

- Ver todas las bases disponibles o consultar específicamente las bases de un usuario determinado
- Revisar los registros del sistema
- Crear, eliminar cuentas de usuario o restablecer contraseñas

Para estas funciones necesitas un **token de cuenta con permisos de administrador**.

## ¿Por qué esta separación clara?

Al dividir las funciones en dos nodos, cada función se mantiene exactamente donde corresponde: las **operaciones de datos para usuarios** y la **gestión y control para administradores**. Esto garantiza mayor claridad, seguridad y facilidad de uso en tus flujos de trabajo de n8n.

## Conclusión

- El **nodo SeaTable** es tu herramienta para todas las operaciones de datos diarias con un token API.
- El **nodo SeaAdmin** te apoya en tareas administrativas con un token de cuenta de administrador.

Así ofreces en n8n la solución óptima para ambos roles: eficiente, segura y claramente estructurada.
