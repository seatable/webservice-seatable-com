---
title: 'Paso 2: Crear un formulario - SeaTable'
date: 2024-08-30
lastmod: '2024-09-05'
categories:
    - 'online-kurs'
author: 'cdb'
url: '/es/ayuda/paso-2-crear-formulario-web'
aliases:
    - '/es/ayuda/schritt-2-erstellen-eines-formulars'
seo:
    title: 'Paso 2: Crear y usar un formulario web en SeaTable'
    description: 'Descubra cómo crear y configurar un formulario web en SeaTable para recopilar gastos en su curso online.'
---

Ahora que hemos creado la estructura necesaria para su gestión de gastos en el paso 1, puede introducir nuevos gastos en cualquier momento utilizando su navegador. Probablemente lo recuerde: Cada línea representa un nuevo registro de datos y, en su caso, una operación de pago.

Pero, por supuesto, estaría bien que también pudieras registrar otros gastos en tu teléfono móvil mientras estás fuera de casa. O también le gustaría registrar los gastos de compañeros de equipo o familiares. Para estos casos, lo ideal es un formulario web, que puede crear fácilmente con SeaTable, puesto que ya ha definido las posibilidades del formulario de entrada a través de los tipos de columna. Pero, ¿qué tengo que explicar largo y tendido? Construyamos el formulario y probémoslo.

## Adjuntar el formulario web

Encontrará muchas funciones adicionales en la zona de cabecera de su base. Detrás del botón `Formularios` SeaTable le ofrece la posibilidad de crear nuevos formularios web.

![Gestión de formularios con botón «Forms» y nuevo formulario web](images/level1-create-webform.png)

1. Crear un nuevo formulario web con el nombre `Expense Tracking`. El nombre no importa, pero ¿por qué no ponerle un nombre bonito?
2. Se abre una nueva interfaz de usuario en la que puede diseñar el formulario web.
3. Arrastre los cuatro campos de la tabla `Reason`, `Date`, `Amount` y `Category` mediante arrastrar y soltar en el formulario.

![Formulario web «Expense Tracking» con campos Reason, Date, Amount, Category](images/level1-webform.png)

## Otros ajustes del formulario web

Su formulario web está casi listo y ya se puede utilizar. Sin embargo, todavía hay tres ajustes que yo recomendaría. Para ajustar la configuración de un campo de entrada, debe hacer clic en el campo de entrada del formulario, lo que mostrará inmediatamente las opciones de configuración para este campo de entrada en el lado derecho. Las opciones de configuración varían en función del campo de entrada en el que haga clic.

- `Category`: elija la visualización `Lista`
- `Date`: establezca la fecha de hoy como `Valor por defecto`
- `Amount`: active la opción `Necesario`

La configuración del formulario web ya está completa y podemos utilizarlo para introducir los primeros registros de datos.

## Probar el formulario web

Utilice los botones naranjas de la esquina superior derecha para obtener la URL del formulario web o un código QR.

Verás que cada vez que envías el formulario, se escribe inmediatamente un nuevo registro de datos en tu base. No es necesario recargar la página en el navegador.

Siéntete libre de experimentar con el formulario web durante unos minutos y disfruta de los progresos que acabas de hacer: **A partir de ahora, tú y cualquier otra persona con la que compartas el enlace a este formulario web podréis crear nuevas entradas en tu base.**

Es importante señalar que sólo pueden crearse nuevas entradas a través del formulario web y que las entradas existentes no pueden editarse ni visualizarse.

Tómese unos minutos para explorar las posibilidades adicionales del formulario web.

## Artículo de ayuda con más información

- [Formularios web]({{< relref "help/base-editor/webformulare/webformulare" >}})
- [Creación de un formulario web]({{< relref "help/base-editor/webformulare/anlegen-eines-webformulars" >}})
- [Opciones de configuración de un formulario web]({{< relref "help/base-editor/webformulare/konfigurationsmoeglichkeiten-eines-webformulars" >}})
