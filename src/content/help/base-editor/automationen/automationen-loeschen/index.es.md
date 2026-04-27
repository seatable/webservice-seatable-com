---
title: 'Borrar automatizaciones'
date: 2022-12-06
lastmod: '2025-11-05'
categories:
    - 'automationen'
author: 'kgr'
url: '/es/ayuda/eliminar-automatizaciones-seatable'
aliases:
    - '/es/ayuda/automationen-loeschen'
seo:
    title: 'Eliminar automatizaciones en SeaTable: guía completa'
    description: 'Sepa cómo borrar automatizaciones en SeaTable, cuáles son los efectos para acciones y cómo administrar reglas paso a paso.'
weight: 10
---

Puede **eliminar reglas de automatización** ya creadas en cualquier momento. Tenga en cuenta qué efectos tiene la supresión en las distintas **acciones automatizadas**.

## Para eliminar una automatización

![eliminar una automatización](images/delete-automation-rule.gif)

1. Abra una **base** en la que desee eliminar una automatización ya creada.
2. En la cabecera de la base, haga clic en {{< seatable-icon icon="dtable-icon-rule" >}} y después en **Reglas de automatización**.
3. Desplace el puntero del ratón sobre la regla de automatización correspondiente, haga clic en los tres puntos y, a continuación, en {{< seatable-icon icon="dtable-icon-delete" >}} **Borrar regla** .
4. Confirme con **Borrar**.

{{< warning type="warning" headline="El borrado es definitivo" text="La regla de automatización borrada habrá **desaparecido definitivamente y no podrá restaurarse**." />}}

## Efectos

Dependiendo de las acciones que hubiera definido para una automatización, la eliminación de una regla de automatización puede tener **diferentes consecuencias**. En principio, sin embargo, el evento desencadenante definido **ya no desencadenará ninguna acción** tras la eliminación – a menos que se siga utilizando como desencadenante de otra automatización existente.

Especialmente en el caso de acciones complejas como el envío de correos electrónicos, scripts de Python o funciones de IA, debería considerar sólo [pausar la automatización]({{< relref "help/base-editor/automationen/automationen-stoppen" >}}) en lugar de borrarla definitivamente.