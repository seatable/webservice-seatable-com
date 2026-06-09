---
title: 'Filtern von Einträgen in einer Ansicht'
date: 2022-11-16
lastmod: '2025-02-25'
categories:
    - 'ansichtsoptionen'
author: 'kgr'
url: '/de/hilfe/filtern-von-eintraegen-in-einer-ansicht'
seo:
    title: 'Einträge in SeaTable-Ansichten filtern: Schritt-für-Schritt und Optionen'
    description: 'Lernen Sie, wie Sie mit Filtern gezielt Einträge in einer SeaTable-Ansicht anzeigen lassen, mehrere Filtergruppen anwenden und Bedingungen nach Spaltentyp setzen.'
weight: 21
---

Mit der Filterfunktion von SeaTable können Sie über **Filterregeln** die gewünschten Einträge aus einer Tabelle herausfiltern und nur die Einträge anzeigen lassen, die bestimmte Kriterien erfüllen. Der eingestellte Filter bezieht sich lediglich auf **die aktive Ansicht**.

{{< warning headline="Wichtiger Hinweis" text="Mit Filtern ändern Sie nur, wie viele Datensätze in Ihrer Ansicht angezeigt werden! Die Datengrundlage bleibt durch das Filtern unverändert und die unsichtbaren Zeilen sind nicht gelöscht. Wenn also Datensätze verschwunden sind, prüfen Sie, ob Sie in der richtigen Ansicht sind oder ob Sie Datensätze mit einem Filter ausgeblendet haben." />}}

## Einträge in einer Ansicht filtern

![Filtern von Einträgen](images/Filtern-von-Eintraegen-1.gif)

1. Wählen Sie die **Ansicht** aus, in der Sie einen Filter setzen wollen.
2. Klicken Sie in den Ansichtsoptionen über der Tabelle auf **Filtern**.
3. Gehen Sie auf **Filter hinzufügen** oder **Filtergruppe hinzufügen**.
4. Wählen Sie im ersten Feld die **Spalte** aus, für die Sie eine Filterregel definieren wollen.
5. Legen Sie im mittleren Feld fest, nach welcher **Bedingung** die Einträge gefiltert werden sollen.
6. Entscheiden Sie im letzten Feld, auf welche **Option** oder welchen **Wert** sich die Bedingung beziehen soll. Bei einigen Filterkriterien wie z. B. "ist leer" ist dies aus logischen Gründen nicht nötig.

## Die verschiedenen Bedingungen beim Filtern

SeaTable unterstützt die Filterung nach allen [Spaltentypen]({{< relref "help/base-editor/spalten/uebersicht-alle-spaltentypen" >}}) außer Schaltflächen.

Je nachdem, nach welchem **Spaltentyp** Sie filtern möchten, passen sich auch die Bedingungen an, die Sie auswählen können.

### Hier einige Beispiele

Diese Optionen haben Sie bei einer [Text-Spalte]({{< relref "help/base-editor/spaltentypen/die-text-spalte" >}}): 

![Filtern Textspalte](images/filtern-von-eintraegen-5.png)

Diese Optionen haben Sie bei einer [Einfachauswahl-Spalte]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}}): 

![Filter einzelauswahl-Spalte](images/filtern-von-eintraegen-6.png)

Diese Optionen haben Sie bei einer [Bild-Spalte]({{< relref "help/base-editor/spaltentypen/die-bild-spalte" >}}): 

![Filtern Bildspalte](images/filtern-von-eintraegen-7.png)

Zeilen **mit leeren Zellen** in der Filterungsspalte werden grundsätzlich nicht angezeigt, es sei denn, es wird explizit nach "ist leer" gesucht.

## Einen Filter entfernen

Sie können erstellte Filter wieder **löschen**, indem Sie auf das **x-Symbol** klicken.

![Entfernung eines Filters einer Ansicht](images/filtern-von-eintraegen.png)

## Mehrere Filter anwenden

Sie können einen oder mehrere Filter erstellen, welche die erste Bedingung weiter einschränken. Lesen Sie im Artikel [Filter-Regeln mit UND und ODER verknüpfen]({{< relref "help/base-editor/ansichten/filter-regeln-mit-und-und-oder-verknuepfen" >}}) mehr darüber.

## Filter neu anordnen

Sie können Filter verschieben und neu anordnen, indem Sie die linke Maustaste auf der **Sechs-Punkte-Greiffläche** gedrückt halten, ziehen und loslassen. 

![Filtern von Einträgen sortieren](images/Filtern-von-Eintraegen-2.gif)
