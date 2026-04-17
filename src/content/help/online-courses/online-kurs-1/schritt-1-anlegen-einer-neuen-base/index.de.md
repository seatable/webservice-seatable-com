---
title: 'Schritt 1: Anlegen einer neuen Base'
date: 2024-08-30
lastmod: '2024-09-04'
categories:
    - 'online-kurs'
author: 'cdb'
url: '/de/hilfe/schritt-1-anlegen-einer-neuen-base'
seo:
    title: 'Schritt 1 im SeaTable Kurs 1: Neue Base für Ausgaben'
    description: 'Start des Onlinekurses: Legen Sie eine neue Base in SeaTable an, passen Sie Spalten sowie Kategorien an und bereiten Sie alles für Ihr Ausgaben-Tracking vor.'
---

In diesem Kurs wollen wir ein einfaches Tool zur Erfassung und Verwaltung Ihrer persönlichen oder beruflichen Ausgaben erstellen. Wenn Sie fertig sind, können Sie zu jeder Zeit entweder über Ihren Computer oder auch mit Ihrem Mobiltelefon Ausgaben erfassen. Jedes Mal, wenn Sie Ihren Geldbeutel zücken, sollten Sie anschließend diese Ausgabe dokumentieren. Der Lohn für diese Mühe ist, dass Sie auf einen Blick sehen können, wofür Sie wie viel Geld ausgegeben haben.

Beginnen wir diesen Online Kurs also damit, dass wir die notwendige Struktur anlegen, um diese Ausgaben speichern zu können. Hierfür werden Sie eine erste Base und anschließend einige Spalten anlegen. Sie werden sehen, dass die folgenden Schritte fast schon selbsterklärend sind.

{{< warning  type="warning" headline="Ein kleiner Tipp zum effizenten Arbeiten mit diesem Online Kurs"  text="Ich möchte Ihnen empfehlen, dass Sie auf Ihrem Monitor zwei Browserfenster offen haben und diese nebeneinander stellen. Im einen Browser-Fenster öffnen Sie diesen Artikel und im anderen Fenster öffnen Sie Ihr SeaTable. So können Sie viel einfacher den Schritten in diesem Kurs folgen, ohne ständig das Fenster wechseln zu müssen." />}}

![](images/level1-browser-window-setup.png)

## Neue Base anlegen

Wir beginnen auf der Startseite von SeaTable. Legen Sie eine neue Base mit dem Namen `Expense Tracking` an. Klicken Sie anschließend auf diese Base, um zum Base Editor zu gelangen.

## Ändern Sie den Namen der ersten Tabelle

Jede Base beinhaltet standardmäßig eine Tabelle mit dem Namen `Table 1`, die eine Spalte mit drei Zeilen besitzt.

- Löschen Sie die drei Zeilen
- Ändern Sie anschließend den Namen der Tabelle auf `Expenses`

{{< warning  type="warning" headline="Hilfe, wenn Sie nicht weiterkommen"  text="Die Bedienung von SeaTable sollte in den meisten Fällen intuitiv sein. Zum Beispiel können Sie Zeilen auf die gleiche Weise löschen, wie Sie es von vielen anderen Softwarelösungen gewohnt sind: Markieren Sie die Zeilen und machen Sie einen Rechtsklick. Sollten Sie dennoch Unterstützung benötigen, denken Sie an die Hilfeartikel, die wir am Ende der Seite für Sie zusammengestellt haben. Dort finden Sie zu jedem Schritt dieses Online-Kurses die passenden Anleitungen." />}}

## Passen Sie die Spalten der Tabelle an und fügen Sie neue hinzu

Als Nächsten wenden wir uns den Spalten der Tabelle zu, damit unsere Base die gewünschten Daten aufnehmen kann.

- Ändern Sie den Namen der ersten Spalte von `Name` auf `Reason`
- Fügen Sie nun drei weitere Spalten hinzu

**Spalte 1:**

> Name: `Date`
>
> Spaltentyp: `{{< seatable-icon icon="dtable-icon-calendar-alt-solid" >}} Date`
>
> Format: beliebig
>
> Minutengenau: `Yes`

**Hinweis:** Anstelle des Spaltentyps `{{< seatable-icon icon="dtable-icon-calendar-alt-solid" >}} Date` hätte man hier auch den Spaltentyp `{{< seatable-icon icon="dtable-icon-creation-time" >}} Created time` verwenden können. Während Sie die Datumsspalte händisch ausfüllen müssen, würde diese automatisch mit dem aktuellen Datum gefüllt werden. Das spart natürlich Zeit. Der Nachteil wäre aber, dass Sie den Datumswert nicht mehr verändern können und z.B. rückwirkend keine Ausgaben mehr für andere Tage erfassen könnten.

---

**Spalte 2:**

> Name: `Amount`
>
> Spaltentyp: `{{< seatable-icon icon="dtable-icon-number" >}} Number`
>
> Format: `Euro`

---

**Spalte 3:**

> Name: `Category`
>
> Spaltentyp: `{{< seatable-icon icon="dtable-icon-single-election" >}} Single select`

---

{{< warning  headline="26 Spaltentypen"  text="Bisher haben Sie nur einen Bruchteil der möglichen Spaltentypen kennengelernt. Eine der größten Stärken von SeaTable ist es, dass Sie aufgrund der aktuell 26 Spaltentypen wirklich jede Art von Information speichern können." />}}

## Einfachauswahl Optionen hinzufügen

Aktuell hat Ihre Einfachauswahl noch keine Auswahlmöglichkeiten. Legen Sie deshalb als Nächstes, für die Spalte `Category` die folgenden vier Optionen fest:

- Clothing
- Groceries
- Leisure
- Travel

## Kurzer Qualitätscheck

Fantastisch. Wenn Sie der Anleitung genau gefolgt sind, sollte ihre Base nun so aussehen:

![](images/level1-expenses-table.png)

Rekapitulieren wir kurz, was Sie gerade mit wenigen Mausklicks erschaffen haben: **Sie haben nun eine Base, in der Sie zukünftig alle Ihre Ausgaben erfassen können.**

Gleichzeitig haben Sie durch die Wahl der Spaltentypen sichergestellt, dass in den Spalten nur die passenden Informationen erfasst werden können.

Das war auch schon Schritt 1 dieses Online Kurses. Scrollen Sie bis ans Ende dieses Artikels und springen Sie zu **Schritt 2: Erstellen eines Formulars**.

## Hilfeartikel mit weiteren Informationen

- [Eine neue Base erstellen]({{< relref "help/startseite/bases/eine-neue-base-erstellen" >}})
- [Wie man den Spaltentyp anpasst]({{< relref "help/base-editor/spalten/wie-man-den-spaltentyp-anpasst" >}})
- [Löschen einer Zeile]({{< relref "help/base-editor/zeilen/das-loeschen-von-zeilen" >}})
- [Hinzufügen einer Spalte]({{< relref "help/base-editor/spalten/hinzufuegen-einer-spalte" >}})
- [Hinzufügen von Optionen zu einer Einfachauswahl-Spalte]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}})
- [Besonderheiten der ersten Spalte]({{< relref "help/base-editor/spalten/die-besonderheiten-der-ersten-spalte" >}})
- [Aussehen einer Base anpassen (Icon und Farbe)]({{< relref "help/startseite/bases/aussehen-einer-base-anpassen-icon-und-farbe" >}})
