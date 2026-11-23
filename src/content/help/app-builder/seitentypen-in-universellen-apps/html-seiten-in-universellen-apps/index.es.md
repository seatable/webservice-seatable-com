---
title: 'Páginas HTML en aplicaciones de SeaTable'
date: 2026-08-11
lastmod: '2026-11-20'
categories:
    - 'seitentypen-in-universellen-apps'
author: 'kgr'
url: '/es/ayuda/paginas-html-apps-seatable'
seo:
    title: 'Añadir páginas HTML en SeaTable Apps: guía'
    description: 'Añada a su aplicación páginas totalmente personalizadas basadas en HTML, JavaScript y CSS para diseñar usted mismo la interfaz.'
weight: 12
---

Los demás [tipos de página de una aplicación]({{< relref "help/app-builder/seitentypen-in-universellen-apps/ueberblick" >}}) ofrecen numerosas opciones de configuración, pero predeterminan la estructura y el comportamiento de una página. Con las **páginas HTML** puede añadir a su aplicación páginas totalmente personalizadas basadas en HTML, JavaScript y CSS. De este modo, puede diseñar sus aplicaciones exactamente según sus ideas e implementar sin problemas incluso interacciones complejas. Los **casos de uso típicos** son:
- Formularios, listas y páginas informativas con un diseño individual
- Tipos de gráficos o diagramas propios con elementos en los que se puede hacer clic
- Vistas combinadas, p. ej. una tabla y un registro individual en una misma página

![Ejemplo de una página HTML](images/html-page.png)

Las páginas HTML pueden mostrar **contenidos estáticos**, pero desarrollan todo su potencial en combinación con los **datos de una base**. Al igual que los demás tipos de página del App Builder, pueden recuperar datos de una base y modificar registros en una base. En el **diseño de la interfaz de usuario** no existen prácticamente limitaciones. Todo lo que se pueda realizar con HTML, CSS y JavaScript también lo puede integrar en su aplicación como página HTML.

{{< warning headline="No es un enfoque no-code" >}}

Tenga en cuenta que este tipo de página está dirigido a **usuarios con experiencia en programación**. Todo el código de la página debe crearse fuera de SeaTable y, a continuación, cargarse en la aplicación como un paquete. Si no tiene conocimientos de programación, es preferible que cree una **página generada con IA**, con la que una IA puede generar páginas HTML a partir de sus indicaciones en lenguaje natural.

{{< /warning >}}

## Cómo crear una página HTML

1. Abra una aplicación en el **modo de edición**. Para ello, pase el ratón por encima de la aplicación y haga clic en el **icono del lápiz** {{< seatable-icon icon="dtable-icon-rename" >}}.
   ![Editar aplicaciones](images/edit-apps.png)
2. Haga clic arriba a la izquierda en **el círculo naranja con el icono del signo más** y seleccione a continuación **Añadir página HTML**.
   ![Añadir página HTML](images/add-html-page.png)
3. Asigne un **nombre** a la página y defina opcionalmente un **icono** para la página.
   ![Crear página HTML](images/create-html-page.png)
4. Confirme con **Enviar**.
5. Cree en su dispositivo un **archivo zip** que contenga los archivos HTML, JavaScript y CSS.
6. **Cargue el archivo** haciendo clic en el área prevista para ello o arrastrando el archivo hasta allí.
   ![Cargar archivo zip](images/upload-zip-file.png)
7. A continuación, SeaTable renderiza el archivo como **página en la aplicación**.

{{< warning headline="Atención" >}}

El archivo zip puede tener un tamaño **máximo de 10 MB** y debe contener un archivo HTML llamado **index.html**.

{{< /warning >}}

## Cómo crear los archivos necesarios

Hay **dos formas** de crear una página HTML y proporcionarla como archivo zip:
- El **enfoque low-code**: Diseñe la página en un **editor HTML visual**, vincúlela con su base mediante **fragmentos de código** predefinidos, añada opcionalmente **imágenes y gráficos** y empaquételo todo como **archivo zip**. Este procedimiento es ideal para formularios, cuadros de mando y páginas con diseño individual y con operaciones sencillas de lectura y escritura.
- El **enfoque para desarrolladores**: En cuanto desee crear páginas HTML más grandes con una lógica más compleja, p. ej. cuando los elementos de la página deban interactuar entre sí, necesitará la **cadena de herramientas de JavaScript completa**. Para el desarrollo se requieren **Node.js** y **npm**, un **servidor de desarrollo** con recarga en vivo, así como un **token API** generado en la base.

Encontrará más información, ejemplos y plantillas en nuestro [manual para desarrolladores](https://developer.seatable.com/html-pages/).
