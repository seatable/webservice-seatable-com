---
title: 'Migración de Airtable Bases a SeaTable'
date: 2023-07-30
lastmod: '2024-11-21'
categories:
    - 'import-von-daten'
author: 'fsa'
url: '/es/ayuda/migrar-bases-airtable-seatable'
aliases:
    - '/es/ayuda/migration-von-airtable-bases-zu-seatable'
seo:
    title: 'Migrar bases de Airtable a SeaTable – guía completa'
    description: 'Descubra cómo migrar sus bases de Airtable a SeaTable de forma sencilla y rápida gracias al script de migración.'
---

¿Quiere trasladar sus Airtable Bases a SeaTable y tiene miedo del esfuerzo? ¡No se preocupe! Incluso bases con estructuras de datos complicadas y muchos miles de registros de datos pueden ser rápidamente transferidos a SeaTable. Para ello dispone de **dos opciones**: una variante sencilla totalmente sin código y un script más flexible para el que resulta útil tener conocimientos básicos de Python.

## Importar bases de Airtable a SeaTable

Para la primera opción de importar bases de Airtable a SeaTable, no necesita ningún conocimiento de programación.

1. Abra la **página de inicio** de SeaTable.
2. Haga clic en **Añadir una base o carpeta** en la sección o grupo donde desee la nueva base.
![Importar desde Airtable](images/import-from-airtable.png)
3. Seleccione **Importar desde Airtable**.
4. Introduzca el [Airtable Personal Access Token (PAT)](https://support.airtable.com/docs/creating-personal-access-tokens) así como el [Airtable Base ID](https://support.airtable.com/docs/finding-airtable-ids). Utilice los enlaces a la documentación de Airtable para saber dónde obtener el PAT y el Base ID. El PAT debe disponer de los permisos **data.records:read** y **schema.bases:read**.
![Cuadro de diálogo de importación de Airtable](images/airtable-import-window.png)
5. Defina el **nombre de la base** que la nueva base recibirá en SeaTable.
6. Confirme con **Importar**.

A diferencia del script que se explica en el siguiente capítulo, con la vía de importación estándar **no dispone de opciones de personalización**. Todas las tablas y filas (incluidos los archivos adjuntos) se importan desde Airtable. Por ello, según el tamaño de la base de Airtable, el proceso de importación puede llevar algún tiempo.

También se importan todas las columnas de Airtable, salvo las columnas de tipo Button, Count, Lookup y Rollup. Más abajo encontrará una visión general de cómo se transfieren los tipos de columna de Airtable a SeaTable. La tabla «Columns to be migrated manually» en la nueva base muestra las columnas que no se importaron desde Airtable.

## Cómo migrar una base de Airtable a SeaTable mediante un script

Para una transferencia más flexible de los datos de Airtable, hemos desarrollado un script de migración. Este transfiere los datos seleccionados de una base Airtable – tablas, columnas, registros de datos – a una base SeaTable. Tras la migración puede seguir trabajando en SeaTable con los datos que utilizó por última vez en Airtable.

Solo se requieren unas pocas **entradas manuales** para poner el script en funcionamiento. Tras la ejecución del script aún serán necesarios algunos ajustes posteriores. En este artículo explicamos cómo hacerlo.

{{< warning  type="warning" headline="Nota importante"  text="El script de migración es funcional, pero aún está en fase beta. Lo estamos adaptando y optimizando constantemente. Si tiene algún problema, por favor deje un mensaje en el [Foro SeaTable](https://forum.seatable.com/)." />}}

### 1\. Crear base

Crear una [nueva base]({{< relref "help/startseite/bases/eine-neue-base-erstellen" >}}) en SeaTable. El nombre de la base SeaTable no tiene que coincidir con el nombre de la base Airtable a importar. Puede elegir el nombre libremente.

### 2\. Insertar script

En la nueva base, abra la barra lateral [Script]({{< relref "help/skripte/allgemein/anlegen-und-loeschen-eines-skriptes" >}}) haciendo clic en el icono de script {{< seatable-icon icon="dtable-icon-script" >}} de la cabecera de la base, arriba a la derecha. A continuación, seleccione **Añadir script**. El script de migración está escrito en el lenguaje de programación Python. Por lo tanto, seleccione **Python**.

Ahora seleccione el siguiente bloque de código, cópielo en el portapapeles y péguelo en la ventana izquierda del editor de scripts:

```
## Parameterize the script

# SeaTable - Destination
server_url = 'https://cloud.seatable.io'
api_token = '...'
# Add an API token of the SeaTable base

# Airtable - Source
airtable_personal_access_token = '...'
# Add a Personal Access Token (PAT)
# PATs are 82-character strings and begin with "pat" (e.g. 'pat544WlSOq6T4Fvv.5710af6611aedbf28493c38084163494e02b24f078cf2d62f07105982a82a64d')
# See https://support.airtable.com/docs/creating-personal-access-tokens/
# for more information on how to create a PAT in Airtable

airtable_base_id = '...'
# Add the Base ID of the Airtable base
# Base IDs are alphanumeric strings and begin with "app" (e.g. 'appRfA3qspH3EJUnV')
# See https://support.airtable.com/docs/finding-airtable-ids/
# for more information on where to find the id of an Airtable base

table_names = ['...', '...']
# Add the names of all tables of the Airtable base, i.e. ['table 1', 'table 2']
# The names must be enclosed in '' and comma-separated

first_columns = [
   ('...', '...'),
   ('...', '...'),
]
# Specify the names of the first columns in every table of the Airtable base
# Use the format ('table_name', 'first_column_name'), i.e. ('table 1', 'ID')
# The table and column name must be enclosed in '' and comma-separated

links = [
]
# Specify the links between the tables in the Airtable base
# Use the format ('table_name', 'column_name', 'other_table_name'), i.e., ('table 1', 'link to table 2', 'table 2')
# The table and column names must be enclosed in '' and comma-separated
# If the Airtable base contains no link columns, just leave the brackets empty

from seatable_api.constants import ColumnTypes
excluded_column_types = [
    ColumnTypes.FILE
]
# Specify the column types which are to be excluded from the data import when running the script in import-rows mode (excluded column types are still created in import-header mode)
# Use the constants from https://developer.seatable.com/scripts/python/objects/constants/, i.e. ColumnTypes.FILE to exclude file columns
# The specified column types must be comma-separated
# If no column types are to be excluded, just leave the brackets empty
# ColumnTypes.LINK_FORMULA are always excluded

excluded_columns = []
# Specify the names of the columns which are to be excluded from the data import when running script in import-rows mode (excluded columns are still created in import-header mode)
# Use the format ('table_name', 'column_name'), i.e. ('table 1', 'column A')
# The table and column names must be enclosed in '' and comma-separated
# If no columns are to be excluded, just leave the brackets empty

mode = 'import-header'
# Specify the run-mode of the script, two options: 'import-header' and 'import-rows'
# Run 'import-header' first to create the data structure in the SeaTable base
# Run 'import-rows' to import all the rows


## No more edits required beyond this row

import sys
from seatable_api import Base, AirtableConvertor

def get_convertor():
    base = Base(api_token, server_url)
    base.auth()
    convertor = AirtableConvertor(
        airtable_api_key=airtable_personal_access_token,
        airtable_base_id=airtable_base_id,
        base=base,
        table_names=table_names,
        first_columns=first_columns,
        links=links,
    )
    return convertor

def import_header():
    convertor = get_convertor()
    convertor.convert_metadata()

def import_rows():
    convertor = get_convertor()
    convertor.convert_data()

if mode == 'import-header':
   import_header()

elif mode == 'import-rows':
   import_rows()

else:
   print('The mode is not properly specified.')

## End script
##
```

No se preocupe si aún no entiende del todo el código que acaba de copiar. Lo explicaremos. Los **comentarios en el código** deberían ayudarle un poco a interpretarlo. Los comentarios son todas las líneas que comienzan con el símbolo de almohadilla (‘#’). Estas líneas no se tienen en cuenta durante la ejecución del script, es decir, puede modificar, eliminar o agregar más comentarios sin afectar la funcionalidad del script.

A diferencia de los comentarios, las **indentaciones en el código** son muy importantes durante la ejecución del script. Por favor, no las modifique.

### 3\. Indicar la URL del servidor de SeaTable y el API Token de la base

Bajo el comentario **SeaTable – Destination**, introduzca la URL del servidor de SeaTable e indique el [API-Token]({{< relref "help/integrationen/seatable-api/erzeugen-eines-api-tokens" >}}). El API-Token debe otorgar permisos de lectura y escritura. Si utiliza SeaTable Cloud, la URL pre-rellenada “https://cloud.seatable.io” es la correcta. Si utiliza otro servidor de SeaTable, introduzca su URL. La URL siempre debe comenzar con https:// o http://. Tanto la URL como el token deben ir entre comillas simples.

Este es un ejemplo de configuración para importar datos a una base en SeaTable Cloud:  
![](images/SeaTable_Server_URL_and_API_Token.png)

### 4\. Introducir el Airtable Personal Access Token y el Base ID

Bajo el comentario **Airtable – Source**, añada el [Airtable Personal Access Token (PAT)](https://support.airtable.com/docs/creating-personal-access-tokens) así como el [Airtable Base ID](https://support.airtable.com/docs/finding-airtable-ids), ambos valores también entre comillas simples. El PAT debe tener los permisos `data.records:read` y `schema.bases:read`.

Debería verse así, aunque sus valores serán diferentes:  
![](images/Airtable_Base_ID_and_PAT.png)

Utilice los enlaces a la documentación de Airtable incluidos en el script para saber dónde obtener el PAT y el Base ID.

### 5\. Introducir los nombres de las tablas y columnas

Ahora indique al script qué tablas de la base de Airtable desea importar. Hágalo en la línea “table_names”. Añada dentro de los corchetes los nombres de las tablas, cada uno entre comillas simples y separados por comas.

Para una base con dos tablas “table1” y “table2”, la línea debería verse así:  
![](images/Airtable-tables_names_500.png)

Si su base de Airtable tiene más de dos tablas, simplemente amplíe la lista dentro del corchete. Si no desea transferir todas las tablas de una base, omita los nombres de las tablas que no desea copiar.

Debido a una limitación de la API de Airtable, también debe indicar los nombres de las primeras columnas de las tablas. Esto se hace en la línea “first_columns” o en las líneas siguientes.

Para la base de Airtable con las dos tablas “table1” y “table2”, podría verse así:  
![](images/Airtable-first_columns_500.png)

### 6\. Definir columnas de enlace

Para que SeaTable pueda importar los datos correctamente, es necesario un paso adicional: la especificación de las [columnas de enlace]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}) en la base de Airtable.

Para ello se utiliza la variable “links”. Por ejemplo, si la columna “link to table2” en la tabla “table1” representa un enlace con la tabla “table 2”, entonces el script debe parametrizarse de la siguiente manera:

![](images/Airtable-links_500.png)

Solo debe indicar cada par de columnas de enlace una vez. No es necesario especificar el enlace en ambas direcciones.

Si la base de Airtable no tiene columnas de enlace, puede dejar el corchete vacío:  
![](images/Airtable-linksEmpty_500.png)

### 7\. Excluir columnas o tipos de columna (opcional)

Si no desea copiar todas las columnas o tipos de columna de Airtable a SeaTable, puede excluirlos. Excluir una columna o tipo de columna hará que la columna se cree en la base de SeaTable, pero los datos que contiene no se transferirán. Excluir columnas con grandes volúmenes de datos – especialmente columnas de archivos – puede reducir significativamente el tiempo de ejecución del script. Especialmente para una prueba de migración, es recomendable excluir columnas con mucho volumen de datos.

Los tipos de columna se pueden excluir usando la variable “excluded_column_types”. Para especificar los tipos de columna a excluir, utilice las constantes de Python correspondientes. Las columnas individuales se pueden excluir usando la variable “excluded_columns”. La especificación es análoga a la variable “first_columns” en el formato (‘NombreTabla’, ‘NombreColumna’). Si desea excluir varias columnas, los valores deben estar separados por comas.

### 8\. Importar tablas y columnas

El script se puede ejecutar en dos modos: “import-header” y “import-rows”. Siempre debe ejecutar primero el script en el modo “import-header”. En este modo, se crean las tablas y columnas en la base de SeaTable y se importan 10 filas de prueba.

El modo de ejecución se define mediante la variable del mismo nombre:  
![](images/SeaTable-modeImportHeader_500.png)

Ejecute el script ahora haciendo clic en **Ejecutar script**. Durante la ejecución, verá los pasos realizados en el lado derecho del editor. En segundo plano, también verá cómo se crean las tablas y columnas.

{{< warning  headline="Aviso importante"  text="No cierre la ventana durante la importación, ya que el proceso se interrumpirá." />}}

### 9\. Comprobar las filas de prueba

Ahora compruebe si

- se importaron todas las tablas y columnas,
- en todas las tablas se creó la primera columna correcta y
- las columnas de enlace son correctas.

Dado que los tipos de columna de Airtable y SeaTable no son completamente congruentes, algunos tipos de columna en la base de SeaTable diferirán de los de la base de Airtable. La siguiente tabla muestra cómo se transfieren los tipos de columna de Airtable a SeaTable.

| **Tipo de columna en Airtable** | **Importación como tipo de columna en SeaTable** |
| ------------------------------- | ------------------------------------------------ |
| Attachment                      | Archivo                                          |
| Autonumber                      | Texto                                            |
| Barcode                         | Texto                                            |
| Button                          | –                                                |
| Checkbox                        | Casilla de verificación                          |
| Count                           | –                                                |
| Created by                      | Texto                                            |
| Created time                    | Fecha                                            |
| Currency                        | Número                                           |
| Date                            | Fecha                                            |
| Duration                        | Duración                                         |
| Email                           | Correo electrónico                               |
| Formula                         | Fórmula (con fórmula de marcador de posición)    |
| Last modified by                | Texto                                            |
| Last modified time              | Fecha                                            |
| Link to another record          | Enlace a otros registros                         |
| Long text                       | Texto con formato                                |
| Lookup                          | –                                                |
| Multiple select                 | Selección múltiple                               |
| Number                          | Número                                           |
| Percent                         | Número                                           |
| Phone number                    | Texto                                            |
| Rating                          | Valoración                                       |
| Rollup                          | –                                                |
| Single line text                | Texto                                            |
| Single select                   | Selección única                                  |
| User                            | Texto                                            |
| URL                             | URL                                              |

Las columnas de tipo fórmula, así como los tipos de columna Count, Lookup y Rollup de Airtable, tienen un papel especial. Para las primeras, se crea en la base de SeaTable una columna de fórmula con el resultado “Formula to be defined”. Lamentablemente, actualmente no es posible traducir automáticamente una fórmula de Airtable a una fórmula de SeaTable. De manera similar ocurre con los otros tipos de columna mencionados. Estos no se crean automáticamente mediante el script. Las columnas que no se crean automáticamente se listan en la tabla separada “Columns to be migrated manually”.

Si algo no es correcto, elimine las tablas creadas por el script y revise las entradas de los pasos 5 y 6. Luego, ejecute nuevamente el script en el modo “import-header”. Puede ejecutar el script tantas veces como desee.

![](images/Vorschaueintraege_Member_bearbeitet-1088x212.png)

### 10\. Importar todos los registros

Si la verificación en el paso 9 es satisfactoria, entonces puede transferir todos los registros.

Cambie en el script el modo de “import-header” a “import-rows”:

![](images/SeaTable-modeImportRows_500.png)

Ejecute nuevamente el script haciendo clic en **Ejecutar script**. Nuevamente podrá observar la ejecución del script en el lado derecho y ver en segundo plano las actividades.

{{< warning  headline="Aviso importante"  text="No cierre la ventana durante la importación, ya que el proceso se interrumpirá." />}}

![](images/Migration_final-1088x348.png)

Ahora debería ver todos los registros de la base de Airtable en la nueva base de SeaTable. **¡Felicidades, la migración de los registros se ha completado!**

Si no está satisfecho con el resultado final, entonces [elimine todas las tablas]({{< relref "help/base-editor/tabellen/loeschen-einer-tabelle-aus-einer-base" >}}) y comience de nuevo desde el paso 5.

### 11\. Finalizar la migración

El script de migración ha transferido todos los datos. Es posible que aún se requieran algunos ajustes manuales.

Por un lado, debe completar las fórmulas en las columnas de fórmula y añadir las columnas que no se crearon automáticamente y que están listadas en la tabla “Columns to be migrated manually”.

Por otro lado, también debe crear las vistas manualmente, ya que estas no se transfieren desde la base de Airtable. Lo mismo aplica para automatizaciones, interfaces y scripts.

## Sección de Preguntas Frecuentes (FAQ)

{{< faq "¿El script modifica datos en mi base de Airtable?" >}}No. El script solo lee su base de Airtable. Los datos en la base de Airtable no se modifican.
{{< /faq >}}

{{< faq "¿Qué debo hacer si recibo mensajes de error?" >}}
Recibir un mensaje de error en la primera ejecución no es inusual. Hay muchas razones posibles, por ejemplo, un token incorrecto, un orden incorrecto en la especificación de los enlaces, errores tipográficos, comas faltantes o una indentación incorrecta. Un solo error puede hacer que la ejecución del script se detenga.  
Si recibe un mensaje de error, no hay problema. No se perderán datos. Siga estos pasos para encontrar la causa del error:

- El mensaje de error generalmente le indica dónde se encuentra el error. Siga la indicación, corrija los parámetros ingresados y ejecute el script nuevamente. Un error de indentación, por ejemplo, indica una indentación que no corresponde a la sintaxis de Python.
- Si el mensaje de error no es claro, revise todas las entradas para asegurarse de que sean correctas e intente de nuevo.
- Si ninguno de los consejos ayuda, solicite ayuda en el [Foro de SeaTable](https://forum.seatable.com/).

> **Aviso importante**: Por favor, elimine el API-Token, el PAT y el Base-ID antes de publicar capturas de pantalla o scripts en el foro.

{{< /faq >}}

{{< faq "¿Se pueden migrar bases de Airtable de cualquier tamaño?" >}}En principio, sí. Sin embargo, el procedimiento presentado en este artículo con el editor de Python integrado tiene una limitación máxima de tiempo de ejecución de 15 minutos, es decir, los scripts que se ejecutan durante más de 15 minutos se interrumpirán. En la práctica, esto es suficiente para la gran mayoría de las bases. Sin embargo, para bases con archivos adjuntos grandes o numerosos, este límite puede ser relevante. En ese caso, puede reducir el tiempo de ejecución excluyendo columnas. Si no desea excluir columnas, debe ejecutar el script de Python localmente en una computadora donde no haya límite de tiempo de ejecución.
{{< /faq >}}

{{< faq "¿Se pueden importar tablas en una base existente?" >}}El script no requiere que una base esté vacía. Por lo tanto, puede ejecutar el script en una base con tablas existentes y llenas. Lo único que debe evitar es la duplicación de nombres de tablas.

{{< /faq >}}
