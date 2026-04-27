---
title: 'Установка значения по умолчанию для столбца'
date: 2023-11-07
lastmod: '2024-06-11'
categories:
    - 'arbeiten-mit-spalten'
author: 'kgr'
url: '/ru/pomoshch/ustanovit-znachenie-po-umolchaniyu-dlya-stolbtsa'
aliases:
    - '/ru/pomoshch/standardwert-fuer-eine-spalte-festlegen'
seo:
    title: 'Значения по умолчанию для столбцов в SeaTable'
    description: 'Узнайте, как задавать значения по умолчанию для столбцов в SeaTable. Новые строки автоматически заполняются, что экономит время и сокращает ошибки.'
---

Если вы зададите **значение по умолчанию** для столбца, оно будет **автоматически вводиться в каждую новую строку** таблицы. Благодаря предопределенным значениям по умолчанию вы можете сэкономить несколько кликов при [добавлении новых строк]({{< relref "help/base-editor/zeilen/hinzufuegen-einer-zeile" >}}). Разумеется, впоследствии вы можете вручную скорректировать автоматически введенные значения.

## Как установить значения по умолчанию

![Установка значения по умолчанию для столбца](images/Standardwert-festlegen.gif)

1. Щелкните на треугольном **значке** {{< seatable-icon icon="dtable-icon-drop-down" color="grey" >}} справа от названия столбца, для которого нужно задать значение по умолчанию.
2. Выберите опцию **Установить значение по умолчанию**.
3. Введите желаемое **значение по умолчанию**. В зависимости от типа столбца можно выбрать различные варианты.
4. Подтвердите процесс **кнопкой Enter** или **щелчком** мыши вне диалогового окна.
5. Если теперь **создать новую строку**, SeaTable автоматически введет соответствующие значения. После этого можно **корректировать** данные обычным образом.

{{< warning  headline="Внимание"  text="Значения по умолчанию используются **повсеместно** при создании новых строк, т. е. строки, созданные с помощью автоматического или кнопочного действия, также содержат значения по умолчанию." />}}

Вы также можете задать значение по умолчанию непосредственно при [создании нового столбца]({{< relref "help/base-editor/spalten/hinzufuegen-einer-spalte" >}}).

## Для каких типов столбцов можно задать значения по умолчанию

Значения по умолчанию могут быть определены для многих, но не для всех [типов столбцов SeaTable]({{< relref "help/base-editor/spalten/uebersicht-alle-spaltentypen" >}}). Колонки, содержимое которых автоматически генерируется SeaTable[(формулы]({{< relref "help/base-editor/spaltentypen/die-bild-spalte" >}}), [файлами]({{< relref "help/base-editor/spaltentypen/die-datei-spalte" >}}) и [подписями]({{< relref "help/base-editor/spaltentypen/die-signatur-spalte" >}}).

**Ниже приведен обзор типов столбцов, для которых можно задать значения по умолчанию:**

| Тип колонки              | Поддерживает значения по умолчанию                            |
| ------------------------ | ------------------------------------------------------------- |
| Автоматический номер     | {{< icon "circle-xmark" >}}                                   |
| Изображение              | {{< icon "circle-xmark" >}}                                   |
| Флажок                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Файл                     | {{< icon "circle-xmark" >}}                                   |
| Дата                     | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Продолжительность        | {{< icon "circle-xmark" >}}                                   |
| Одиночный выбор          | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Электронная почта        | {{< icon "circle-xmark" >}}                                   |
| Создатель                | {{< icon "circle-xmark" >}}                                   |
| Создано                  | {{< icon "circle-xmark" >}}                                   |
| Форматированный текст    | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Формула                  | {{< icon "circle-xmark" >}}                                   |
| Формула для ссылок       | {{< icon "circle-xmark" >}}                                   |
| Геопозиция               | {{< icon "circle-xmark" >}}                                   |
| Последний редактор       | {{< icon "circle-xmark" >}}                                   |
| Множественный выбор      | {{< icon "circle-xmark" >}}                                   |
| Сотрудники               | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Рейтинг                  | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Кнопка                   | {{< icon "circle-xmark" >}}                                   |
| Подпись                  | {{< icon "circle-xmark" >}}                                   |
| Текст                    | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| URL                      | {{< icon "circle-xmark" >}}                                   |
| Номер                    | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Последнее редактирование | {{< icon "circle-xmark" >}}                                   |

## Ссылающиеся значения по умолчанию в текстовых колонках

Если в качестве значения по умолчанию в [текстовом столбце]({{< relref "help/base-editor/spaltentypen/die-spalten-text-und-formatierter-text" >}}) указать ссылку **{creator.name}** или **{creator.id}**, то автоматически вводится **имя** или **идентификатор пользователя**, добавившего строку.

![Ссылка на имя пользователя со значением по умолчанию](images/Set-creator-name-as-default-value.png)

## Область применения значений по умолчанию

Значения по умолчанию применяются **везде, где** можно создавать новые строки:

- в [таблице]({{< relref "help/base-editor/zeilen/hinzufuegen-einer-zeile" >}})
- в [колонке ссылок]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}})
- через [кнопку]({{< relref "help/base-editor/schaltflaechen/zeilen-per-schaltflaeche-in-eine-andere-tabelle-kopieren" >}}) (действие: "Скопировать строку в другую таблицу")
- с помощью [автоматизации]({{< relref "help/base-editor/automationen/automations-aktionen" >}}) (действия: "Добавить строку" и "Добавить новую запись в другую таблицу")
- в [представлении Календарь, Канбан, Галерея и Дерево]({{< relref "help/base-editor/ansichten/was-ist-eine-ansicht" >}})
- через [веб-формы]({{< relref "help/base-editor/webformulare/webformulare" >}})
- на [страницах]({{< relref "help/app-builder/seitentypen-in-universellen-apps/tabellenseiten-in-universellen-apps" >}}), [форм]({{< relref "help/app-builder/seitentypen-in-universellen-apps/formularseiten-in-universellen-apps" >}}) и [Kanban]({{< relref "help/app-builder/seitentypen-in-universellen-apps/kanbanseiten-in-universellen-apps" >}}) в приложениях

![Значение по умолчанию применяется везде для новых строк](images/Standardwert-greift-ueberall-bei-neuen-Zeilen.gif)

## Значения по умолчанию в веб-формах

Помимо значений по умолчанию, заданных в таблице, [веб-формы]({{< relref "help/base-editor/webformulare/webformulare" >}}) также позволяют задать значения по умолчанию для полей формы, связанных с колонками. Вы также можете установить, разрешено ли пользователям **изменять** эти значения по умолчанию при заполнении формы.

![Установка значений по умолчанию в веб-формах](images/Set-default-values-in-web-forms.png)

{{< warning  headline="Важное замечание"  text="Если значение по умолчанию определено и в таблице, и в веб-форме, значение из формы применяется ко всем строкам, созданным с помощью веб-формы. Значения по умолчанию, заданные в таблице, действуют **только** в том случае, если вы не задали никаких значений по умолчанию в редакторе формы." />}}

## Значения по умолчанию в приложениях

Значения по умолчанию, заданные в базе, также влияют на строки, которые вводятся на **страницах таблиц, форм и Kanban** в [приложениях]({{< relref "help/app-builder/app-verwaltung/universelle-app" >}}). Единственный [тип страницы]({{< relref "help/app-builder/seitentypen-in-universellen-apps/ueberblick" >}}), для которого вы все еще можете задать значения по умолчанию в приложении, - это [страница формы]({{< relref "help/app-builder/seitentypen-in-universellen-apps/formularseiten-in-universellen-apps" >}}). Настройки работают точно так же, как и для веб-форм: Для этого активируйте ползунки, как показано на скриншоте выше.
