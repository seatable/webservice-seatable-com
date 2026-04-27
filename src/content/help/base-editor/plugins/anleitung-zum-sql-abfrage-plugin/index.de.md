---
title: 'Anleitung zum SQL-Abfrage-Plugin'
date: 2023-05-04
lastmod: '2023-05-15'
categories:
    - 'plugins'
author: 'nsc2'
url: '/de/hilfe/anleitung-zum-sql-abfrage-plugin'
seo:
    title: 'Anleitung SQL-Abfrage-Plugin – Befehle & Beispiele'
    description: 'So nutzen Sie das SQL-Abfrage-Plugin in SeaTable: SELECT, DELETE, Export als Tabelle – optimale Auswertung auch fürs Big Data Backend.'
---

Das SQL-Abfrage-Plugin eignet sich perfekt für die direkte **Ausführung von SQL-Befehlen** und ist daher primär für Nutzer interessant, die bereits Erfahrung mit Datenbanken besitzen.

Ein großer Vorteil des Plugins besteht darin, dass es im Zuge der Datenbankabfrage sowohl auf das normale Backend als auch auf das [Big Data Backend]({{< relref "help/base-editor/big-data/potenzial-big-data" >}}) zugreift.

{{< warning  headline="Besonders hilfreich bei großen Datenmengen"  text="Der direkte Zugriff auf die SeaTable Daten per SQL-Befehl macht bei kleinen Datenmengen wenig Sinn. Die Möglichkeiten, eine Ansicht anzulegen und entsprechende Filter, Sortierungen und Gruppierungen zu setzen, wird die meisten Anwender schneller ans Ziel bringen. Die SQL-Abfrage ist besonders für große Datenmengen relevant und Sie sollten sich bereits mit der SQL-Syntax auskennen." />}}

## Anwendungsbeispiele

### Der SQL-Befehl SELECT

Der wohl am häufigsten genutzte SQL-Befehl ist der **SELECT** Befehl, der zur Abfrage von Einträgen verwendet wird. Eine einfache Abfrage der Spalten _Name_ und _Number_ aus der Tabelle _Time_ würde so aussehen:

```
SELECT Name, Number FROM Time
```

Nach der Eingabe des Befehls wird die Datenbank nach den **definierten Werten** durchsucht und die Ergebnisse werden automatisch in Tabellenform dargestellt.

![Ergebnisse einer Datenabfrage anhand des SQL-Befehls SELECT](images/results-data-sql-query.png)

### Übernahme der Ergebnisse als neue Tabelle

Mithilfe der Funktion **Exportieren in eine neue Tabelle** können Sie die gefundenen Daten in eine neue Tabelle innerhalb der gleichen Base exportieren.

![Export der per SQL-Datenabfrage gefundenen Werte in eine neue Tabelle](images/export-data-sql-query-to-a-new-table.png)

![Neu angelegte Tabelle mit den Daten, die zuvor per SQL-Befehl mit dem Plugin gefunden wurden](images/new-table-with-sql-data.png)

### Der SQL-Befehl DELETE

**DELETE** ist ein weiterer häufig genutzter Befehl, der zum schnellen **Löschen von Einträgen** verwendet wird. Der folgende Befehl löscht beispielsweise alle Daten aus der Tabelle _Time_.

```
DELETE FROM Time
```

Nach der Eingabe des Befehls werden **alle** Einträge aus der Tabelle **Time** gelöscht. Über das [Base-Log]({{< relref "help/base-editor/historie-und-versionen/historie-und-logs" >}}#base-log) können Sie die Zeilen aber wiederherstellen.

![Eingabe des SQL-Befehls DELETE zum Löschen von Tabellendaten](images/query-delete-from-table.png)

## Übersicht über die unterstützten SQL-Befehle

SeaTable unterstützt nicht alle, aber einen Großteil der SQL-Befehle. Eine vollständige Liste und weitere Details finden Sie im [SeaTable Programming Manual](https://developer.seatable.com/scripts/).
