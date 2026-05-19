---
title: 'Миграция с баз Airtable на SeaTable'
date: 2023-07-30
lastmod: '2024-11-21'
categories:
    - 'import-von-daten'
author: 'fsa'
url: '/ru/pomoshch/migratsiya-baz-airtable-v-seatable'
aliases:
    - '/ru/pomoshch/migration-von-airtable-bases-zu-seatable'
seo:
    title: 'Миграция баз Airtable в SeaTable: пошаговая инструкция'
    description: 'Узнайте, как быстро перенести базы Airtable в SeaTable: скрипт, настройка, перенос данных, советы и готовое руководство для успешной миграции.'
---

Вы хотите перенести свои базы Airtable на SeaTable и боитесь, что это будет сложно? Не волнуйтесь! Даже базы со сложной структурой данных и многими тысячами записей могут быть быстро перенесены в SeaTable.

Мы разработали скрипт миграции для переноса данных Airtable в SeaTable. Он переносит все данные из базы Airtable - таблицы, колонки, записи данных - в базу SeaTable за один раз. После переноса вы можете продолжать работу в SeaTable с данными, которые вы в последний раз использовали в Airtable. После выполнения сценария необходимо выполнить лишь несколько настроек.

Скрипт может быть использован любым человеком - как техническим, так и нетехническим. Для того чтобы сделать скрипт готовым к использованию, необходимо сделать всего несколько **ручных записей**. В этой статье мы объясним, как это сделать.

{{< warning  headline="Важное замечание"  text="Скрипт миграции является функциональным, но все еще бета-версией. Мы постоянно адаптируем и оптимизируем его. Если у вас возникли проблемы, пожалуйста, оставьте сообщение на [форуме SeaTable](https://forum.seatable.com/)." />}}

## Как перенести базу из Airtable в SeaTable

### 1\. создать базу

Создайте [новую базу]({{< relref "help/startseite/bases/eine-neue-base-erstellen" >}}) в SeaTable. Имя базы SeaTable не обязательно должно совпадать с именем импортируемой базы Airtable. Вы можете выбрать имя произвольно.

### 2\. вставить скрипт

{{< seatable-icon icon="dtable-icon-script" >}} В новой базе откройте [боковую панель сценариев]({{< relref "help/skripte/allgemein/anlegen-und-loeschen-eines-skriptes" >}}), нажав на значок сценария в заголовке базы в правом верхнем углу. Затем выберите **Добавить сценарий**. Сценарий миграции написан на языке программирования Python. Поэтому выберите **Python**.

Теперь выделите следующий блок кода, скопируйте его в буфер обмена, а затем вставьте в левое окно редактора сценариев:

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

Не волнуйтесь, если вам непонятен код, который вы только что скопировали. Мы объясним его. Комментарии в коде должны немного помочь в интерпретации. Комментарии - это все строки с ведущим хэш-знаком ('#'). Эти строки игнорируются при выполнении скрипта, то есть вы можете изменять, удалять или добавлять комментарии, не влияя на функциональность скрипта.

В отличие от комментариев, отступы в коде очень важны при выполнении скрипта. Пожалуйста, не изменяйте их.

### 3\. укажите URL-адрес сервера SeaTable и API-токен базы

Добавьте URL-адрес сервера SeaTable в комментарий **SeaTable - Destination** и введите [API-токен]({{< relref "help/integrationen/seatable-api/erzeugen-eines-api-tokens" >}}). API-токен должен предоставлять права на чтение и запись. Если вы используете SeaTable Cloud, то правильным будет предварительно заполненный URL "https://cloud.seatable.io". Если вы используете другой сервер SeaTable, введите его URL. (URL всегда должен вводиться с https:// или http://.) URL и маркер должны быть заключены в одинарные инвертированные запятые.

Это пример конфигурации для импорта данных в базу в SeaTable Cloud:  
![](images/SeaTable_Server_URL_and_API_Token.png)

### 4\. введите токен персонального доступа Airtable и идентификатор базы

Добавить комментарий ниже **Airtable - Источник** сайт [Airtable Personal Access Token (PAT)](https://support.airtable.com/docs/creating-personal-access-tokens) и [Идентификатор базы Airtable](https://support.airtable.com/docs/finding-airtable-ids)оба значения снова в одинарных инвертированных запятых. PAT должен обладать полномочиями `data.records:read` и `schema.bases:read` в наличии.

Вот как это должно выглядеть, хотя ваши значения, конечно, будут отличаться:  
![](images/Airtable_Base_ID_and_PAT.png)

Используйте ссылки в скрипте на документацию Airtable, чтобы узнать, где можно получить PAT и Base ID.

### 5\. введите имена таблиц и столбцов

Теперь укажите скрипту, какие таблицы вы хотите импортировать из базы Airtable. Сделайте это в строке "table_names". Добавьте имена таблиц в квадратных скобках - каждое из них заключено в одну перевернутую запятую и разделено запятой.

Для базы с двумя таблицами "table1" и "table2" строка должна выглядеть, например, так:  
![](images/Airtable-tables_names_500.png)

Если ваша база airtable состоит более чем из двух таблиц, просто расширьте список в скобках. Если вы не хотите переносить все таблицы базы, просто опустите названия таблиц, которые не будут скопированы.

В связи с ограничением API Airtable необходимо также указывать имена первых столбцов таблиц. Это делается в строке "first_columns" или в следующих строках.

Для базы Airtable с двумя таблицами "table1" и "table2" это может выглядеть следующим образом:  
![](images/Airtable-first_columns_500.png)

### 6\. определить колонки ссылок

Для того чтобы SeaTable корректно импортировал данные, необходимо выполнить еще один шаг: указать [колонки связей]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}) в Airtable Base.

Для этого предназначена переменная "links". Например, если столбец "link to table2" в таблице "table1" представляет собой ссылку на таблицу "table 2", то сценарий должен быть параметризован следующим образом:

![](images/Airtable-links_500.png)

Каждую пару столбцов ссылок необходимо указывать только один раз. Не обязательно указывать связь в обоих направлениях.

Если в базу Airtable Base не поступают колонки ссылок, то квадратную скобку можно оставить пустой:  
![](images/Airtable-linksEmpty_500.png)

### 7\. исключить столбцы или типы столбцов (необязательно)

Если вы не хотите копировать все столбцы или типы столбцов из Airtable в SeaTable, вы можете исключить их. Исключение столбца или типа столбца гарантирует, что столбец будет создан в базе SeaTable, но содержащиеся в нем данные не будут перенесены. Исключив столбцы с очень большим объемом данных - в частности, речь идет о файловых столбцах, - вы можете значительно сократить время выполнения сценария. Исключение столбцов с большим объемом данных особенно полезно при тестировании миграции.

Типы столбцов можно исключить с помощью переменной "excluded_column_types". Чтобы указать типы исключаемых столбцов, используйте константы Python, предусмотренные для этой цели. Отдельные столбцы можно исключить с помощью переменной "excluded_columns". Она аналогична переменной "first_columns" в формате ('имя таблицы', 'имя столбца'). Если вы хотите исключить несколько столбцов, значения должны быть разделены запятыми.

### 8\. импорт таблиц и столбцов

Скрипт может быть выполнен в двух режимах: "import-header" и "import-rows". Во-первых, скрипт всегда должен выполняться в режиме "import-header". В этом режиме в SeaTable Base создаются таблицы и колонки и импортируются 10 тестовых строк.

Режим выполнения задается через одноименную переменную:  
![](images/SeaTable-modeImportHeader_500.png)

Теперь выполните сценарий, нажав на кнопку **Execute script**. Во время выполнения сценария в редакторе справа видны шаги, которые были выполнены. В фоновом режиме также видно, как создаются таблицы и столбцы.

{{< warning  headline="Важное замечание"  text="Не закрывайте окно во время импорта, иначе процесс будет прерван." />}}

### 9\. проверка тестовых линий

Теперь проверьте, есть ли

- все таблицы и все столбцы были импортированы,
- правильный первый столбец был создан во всех таблицах и
- столбцы ссылок корректны.

Поскольку типы столбцов Airtable и SeaTable не полностью совпадают, некоторые типы столбцов в базе SeaTable будут отличаться от типов столбцов в базе Airtable. В следующей таблице показано, как типы столбцов из Airtable переносятся в SeaTable.

| **Тип колонны с воздушным столом** | **Импорт в SeaTable Тип столбца** |
| ---------------------------------- | --------------------------------- |
| Приложение                         | Файл                              |
| Автонумерация                      | Текст                             |
| Штрих-код                          | Текст                             |
| Кнопка                             | \-                                |
| Флажок                             | Флажок                            |
| Граф                               | \-                                |
| Создано                            | Текст                             |
| Время создания                     | Дата                              |
| Валюта                             | Номер                             |
| Дата                               | Дата                              |
| Продолжительность                  | Продолжительность                 |
| Электронная почта                  | Электронная почта                 |
| Формула                            | Формула (с формулой-заместителем) |
| Последнее изменение                | Текст                             |
| Время последнего изменения         | Дата                              |
| Ссылка на другую запись            | Ссылка на другие записи           |
| Длинный текст                      | Форматированный текст             |
| Поиск                              | \-                                |
| Множественный выбор                | Множественный выбор               |
| Номер                              | Номер                             |
| Процент                            | Номер                             |
| Номер телефона                     | Текст                             |
| Рейтинг                            | Рейтинг                           |
| Рулонный                           | \-                                |
| Однострочный текст                 | Текст                             |
| Однократный выбор                  | Одиночный выбор                   |
| Пользователь                       | Текст                             |
| URL                                | URL                               |

Особую роль играют столбцы формул и столбцы Airtable типов Count, Lookup и Rollup. Для первых в базе SeaTable создается колонка формул с результатом "Формула должна быть определена". К сожалению, в настоящее время невозможно автоматически преобразовать формулу Airtable в формулу SeaTable. Аналогичная ситуация и с другими упомянутыми типами колонок. Они не создаются автоматически скриптом. Те колонки, которые не создаются скриптом, перечислены в отдельной таблице "Колонки, которые нужно перенести вручную".

Если что-то не так, удалите таблицы, созданные скриптом, и проверьте записи в шагах 5 и 6. Затем снова запустите скрипт в режиме "import-header". Вы можете запускать скрипт так часто, как вам удобно.

![](images/Vorschaueintraege_Member_bearbeitet-1088x212.png)

### 10\. Импорт всех записей данных

Если вы удовлетворены проверкой на шаге 9, все записи данных можно переносить.

В скрипте измените режим с "import-header" на "import-rows":

![](images/SeaTable-modeImportRows_500.png)

Снова выполните сценарий, нажав на кнопку **Run Script**. Вновь можно наблюдать выполнение сценария в правой части и видеть действия в фоновом режиме.

{{< warning  headline="Важное замечание"  text="Не закрывайте окно во время импорта, иначе процесс будет прерван." />}}

![](images/Migration_final-1088x348.png)

Теперь вы должны увидеть все записи из базы Airtable в новой базе SeaTable. Поздравляем, миграция наборов данных завершена!

Если вас не устраивает конечный результат, [удалите все таблицы]({{< relref "help/base-editor/tabellen/loeschen-einer-tabelle-aus-einer-base" >}}) и начните с шага 5.

### 11\. завершить миграцию

Сценарий миграции перенес все данные. Может потребоваться некоторая ручная доработка.

Сначала нужно добавить формулы в столбцы формул и добавить столбцы, которые не были созданы автоматически и перечислены в таблице "Столбцы, которые нужно перенести вручную".

С другой стороны, вы также должны сами создавать представления, поскольку они не передаются из Airtable Base. То же самое относится к автоматизациям, интерфейсам и скриптам.

## Область часто задаваемых вопросов

{{< faq "Изменяет ли скрипт данные в моей базе Airtable?" >}}Нет. Скрипт считывает только вашу базу airtable. Данные в базе airtable не изменяются.
{{< /faq >}}

{{< faq "Что делать, если появляется сообщение об ошибке?" >}}Сообщение об ошибке при первом выполнении вовсе не является маловероятным. Причин для этого может быть множество, например, неправильный токен, неправильная последовательность в указании ссылок, опечатки, пропущенные запятые или неправильный отступ. Одна-единственная ошибка может привести к тому, что выполнение скрипта будет отменено.  
Если вы получаете сообщение об ошибке, это, как правило, не проблема. Данные не могут быть потеряны. Чтобы найти причину ошибки, выполните следующие действия:

- В большинстве случаев в сообщении об ошибке будет дана подсказка, где искать ошибку. Следуя ей, исправьте введенные параметры и запустите скрипт снова. Например, ошибка отступа указывает на то, что отступ не соответствует синтаксису Python.
- Если сообщение об ошибке непонятно, проверьте правильность всех записей и повторите попытку.
- Если ни один из советов не помог, обратитесь за помощью в [Форум SeaTable](https://forum.seatable.com/).

> **Важное замечание**: Пожалуйста, удалите API-токен, PAT и ID базы, прежде чем публиковать скриншоты или скрипты на форуме.

{{< /faq >}}

{{< faq "Можно ли переносить базы Airtable любого размера?" >}}В принципе, да. Однако представленная в этой статье процедура с использованием встроенного редактора Python имеет ограничение на максимальное время выполнения в 15 минут, то есть скрипты, выполняющиеся дольше 15 минут, отменяются. На практике этого достаточно для подавляющего большинства баз. Однако это ограничение может сыграть свою роль для баз с большим количеством вложенных файлов. В этом случае время выполнения можно сократить, исключив столбцы. Если вы не хотите исключать столбцы, вы должны запустить Python-скрипт локально на компьютере, где нет ограничений по времени выполнения.
{{< /faq >}}

{{< faq "Можно ли импортировать таблицы в существующую базу?" >}}Скрипт не требует, чтобы база была пустой. Поэтому скрипт можно запускать и в базе с существующими заполненными таблицами. Единственное, чего следует избегать, - это дублирования имен таблиц.
{{< /faq >}}
