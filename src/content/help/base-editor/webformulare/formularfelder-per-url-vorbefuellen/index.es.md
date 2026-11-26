---
title: 'Rellenar campos de formulario'
date: 2023-01-08
lastmod: '2024-03-18'
categories:
    - 'webformulare'
author: 'vge'
url: '/es/ayuda/prellenar-campos-formulario-url'
aliases:
    - '/es/ayuda/formularfelder-per-url-vorbefuellen'
seo:
    title: 'Formularios web SeaTable: prellenar campos con enlaces personalizados o URLs'
    description: 'Formularios web de SeaTable: prellenar campos por enlace con valores estándar. Guía sobre tipos de columna y modos de lectura.'
weight: 5
---

Para **prellenar formularios web**, tiene la opción de definir valores por defecto en los campos del formulario. Puede hacerlo directamente en la URL o mediante una función fácil de usar en SeaTable.

## Generar un enlace de formulario con valores por defecto en SeaTable

SeaTable ofrece una función con la que puede generar cómodamente **enlaces de formulario** en los que los valores por defecto ya están definidos de antemano.

1. Cree un [formulario web]({{< relref "help/base-editor/webformulare/webformulare" >}}).
2. En el editor de formularios web, haga clic en el botón {{< seatable-icon icon="dtable-icon-share" >}} **Compartir** de la esquina superior derecha.
3. Ahora haga clic en el botón **Añadir enlace de formulario** y aparecerá la siguiente máscara de entrada:
   ![Valores prellenados en los enlaces de formulario personalizados](images/Vorbefuellte-Werte-in-benutzerdefinierten-Formularlinks.png)
4. Asigne un **nombre** al nuevo enlace. En **URL personalizada**, puede definir usted mismo una parte de la URL.
5. Para prellenar un campo de formulario con un valor por defecto, haga clic en **Añadir campo**. Seleccione el **campo de formulario** en el menú desplegable e introduzca el **valor por defecto** deseado.
6. Por último, puede decidir si el valor por defecto puede modificarse al rellenar el formulario. Para ello, seleccione **Lectura y escritura**. Si selecciona **Solo lectura**, el valor no podrá modificarse en el formulario.
7. Haga clic en **Crear** para generar el enlace.

![Enlace de formulario personalizado con valor prellenado](images/Benutzerdefinierter-Formularlink-mit-vorausgefuelltem-Wert.png)

El resultado, es decir, la URL ampliada, es el mismo que con el procedimiento manual descrito a continuación.

## Prellenar un formulario web directamente a través de la URL

![Prellenar formulario web](images/prefill.png)

1. Cree un [formulario web]({{< relref "help/base-editor/webformulare/webformulare" >}}).
2. Haga clic en el botón {{< seatable-icon icon="dtable-icon-share" >}} **Compartir** del editor de formularios web para obtener el enlace al formulario web.
3. **Copie** el enlace y péguelo en una nueva pestaña en la **barra de direcciones del navegador**, donde podrá editarlo y probarlo.
4. Para prellenar un campo de formulario con un valor por defecto, añada la cadena **/?prefill_COLUMNNAME=PREFILLVALUE** al enlace del formulario.

En lugar de **COLUMNNAME**, introduzca el nombre del campo que desea rellenar; en lugar de **PREFILLVALUE**, introduzca el valor por defecto deseado. Los espacios deben escribirse como **%20**. Preste atención a las mayúsculas y minúsculas.

**Ejemplo**: Si desea enviar a Joe Smith un formulario web personalizado en el que su nombre ya esté introducido, añada la cadena **/?prefill_Name=Joe%20Smith** al enlace del formulario.

Para utilizar **varios valores por defecto**, encadene las entradas de prellenado con el carácter **&**: /?prefill_COLUMNNAME=PREFILLVALUE**&**prefill_COLUMNNAME=PREFILLVALUE

Una vez que haya terminado, puede probar el enlace pulsando la **tecla Intro** y abriendo el formulario web. Si todo ha funcionado, podrá ver los valores por defecto prellenados en esta **vista previa**.

## Campos de formulario prellenables

Dependiendo del tipo de columna en el que se base un campo de formulario, no siempre es posible prellenarlo. En el siguiente resumen puede ver qué tipos de columna permiten el prellenado mediante URL y cuáles no.

| Tipo de columna          | Admite prellenado                                             |
| ------------------------ | ------------------------------------------------------------- |
| Número automático        | {{< icon "circle-xmark" >}}                                   |
| Imagen                   | {{< icon "circle-xmark" >}}                                   |
| Casilla de verificación  | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Archivo                  | {{< icon "circle-xmark" >}}                                   |
| Fecha                    | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Duración                 | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Selección única          | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Correo electrónico       | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Creador                  | {{< icon "circle-xmark" >}}                                   |
| Creado                   | {{< icon "circle-xmark" >}}                                   |
| Texto con formato        | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Fórmula                  | {{< icon "circle-xmark" >}}                                   |
| Fórmula de vínculo       | {{< icon "circle-xmark" >}}                                   |
| Geoposición              | {{< icon "circle-xmark" >}}                                   |
| Último editor            | {{< icon "circle-xmark" >}}                                   |
| Selección múltiple       | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Colaborador              | {{< icon "circle-xmark" >}}                                   |
| Valoración               | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Botón                    | {{< icon "circle-xmark" >}}                                   |
| Firma                    | {{< icon "circle-xmark" >}}                                   |
| Número de teléfono       | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Texto                    | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| URL                      | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Número                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Última modificación      | {{< icon "circle-xmark" >}}                                   |
