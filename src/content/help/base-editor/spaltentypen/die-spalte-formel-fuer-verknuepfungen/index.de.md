---
title: 'Die Spalte Formel für Verknüpfungen'
date: 2025-07-18
lastmod: '2026-10-08'
categories:
    - 'formeln'
author: 'kgr'
url: '/de/hilfe/die-spalte-formel-fuer-verknuepfungen'
seo:
    title: 'Formel für Verknüpfungen: Lookup, Rollup und mehr in SeaTable'
    description: 'Werte aus verknüpften Datensätzen nutzen: mit Lookup, Rollup, Countlinks, Findmax und Findmin, auch über mehrere Ebenen hinweg.'
weight: 18
---

Mit einer Formel für Verknüpfungen können Sie **Daten aus verknüpften Tabellen** in Ihrer aktuellen Tabelle **darstellen, zusammenfassen oder miteinander in Beziehung setzen**: Werte per **Lookup** nachschlagen, per **Rollup** zusammenfassen oder verknüpfte Datensätze zählen. Hierbei spielt SeaTable seine Vorteile als [relationale Datenbank]({{< relref "posts/relationale-datenbank" >}}) aus.

Für den Spaltentyp stehen Ihnen insgesamt **fünf verschiedene Formeln** zur Verfügung. Voraussetzung für die Verwendung der Spalte ist das Vorhandensein von mindestens einer Spalte des Typs [Verknüpfung zu anderen Einträgen]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}) in Ihrer Tabelle.

## Anlegen einer Formel-für-Verknüpfungen-Spalte

Um eine Formel anzuwenden, müssen Sie zunächst eine neue Formel-für-Verknüpfungen-Spalte zu Ihrer Tabelle hinzufügen.

![Auswahl einer Formel für Verknüpfungen](images/add-a-link-formula.png)

1. Klicken Sie auf das **Plus-Symbol** rechts neben der letzten Spalte.
2. Geben Sie der Spalte einen **Namen**.
3. Wählen Sie als Spaltentyp **Formel für Verknüpfungen** aus.
4. Entscheiden Sie sich für eine **Formel** (z. B. Rollup).
5. Wählen Sie die **Verknüpfungsspalte** der Tabelle, aus der Sie Daten verwenden möchten.
6. Geben Sie die **Spalte in der verknüpften Tabelle** an, auf die sich die Formel beziehen soll.
7. Je nach gewählter Formel können Sie **weitere Einstellungen** vornehmen.
8. Legen Sie die Spalte mit **Abschicken** an.

## 5 Formeln für Verknüpfungen

Die Beispiele beziehen sich auf eine Base mit den Tabellen Kunden und Aufträge, wie in der Anleitung zur [Verknüpfungsspalte]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}). Weitere Informationen finden Sie in den Artikeln zu den einzelnen Formeln:

| Formel | Was sie tut | Beispiel |
|---|---|---|
| [Lookup]({{< relref "help/base-editor/formeln/die-lookup-funktion" >}}) | holt die Werte einer Spalte aus den verknüpften Einträgen | Telefonnummer des Kunden im Auftrag anzeigen |
| [Rollup]({{< relref "help/base-editor/formeln/die-rollup-formel" >}}) | fasst die Werte der verknüpften Einträge zusammen, z. B. als Summe oder Durchschnitt | Umsatz pro Kunde aus allen Aufträgen |
| [Countlinks]({{< relref "help/base-editor/formeln/die-countlinks-formel" >}}) | zählt die verknüpften Einträge | Anzahl der Aufträge pro Kunde |
| [Findmax]({{< relref "help/base-editor/formeln/die-findmax-formel" >}}) | findet den verknüpften Eintrag mit dem größten Wert | letzter Auftrag eines Kunden |
| [Findmin]({{< relref "help/base-editor/formeln/die-findmin-formel" >}}) | findet den verknüpften Eintrag mit dem kleinsten Wert | erster Auftrag eines Kunden |

## Formeln über mehrere Ebenen

Ein Lookup kann auch auf eine Lookup- oder Rollup-Spalte der verknüpften Tabelle zugreifen. So arbeiten Sie über mehrere verknüpfte Tabellen hinweg: Ein Auftrag holt per Lookup den Namen des Kunden, und eine Auftragsposition, die mit dem Auftrag verknüpft ist, greift per Lookup auf diese Spalte zu.

Welche Tabellen über welche Formeln miteinander verbunden sind, zeigt das [Tabellenbeziehungen-Plugin]({{< relref "help/base-editor/plugins/anleitung-zum-tabellenbeziehungen-plugin" >}}) als Diagramm.

## Formatierung der Ergebnisse

Jede Formel in SeaTable hat eine **Zahl**, ein **Datum** oder einen **Text/String** als Ergebnis. Die Ergebnisse in einer Formel-für-Verknüpfungen-Spalte bekommen automatisch ein bestimmtes **Format** zugewiesen. Wenn Sie mit diesem nicht zufrieden sind, können Sie es **neu ermitteln**. Klicken Sie dazu auf den **Drop-down-Pfeil** rechts neben dem Spaltennamen und dann auf **Formateinstellungen bearbeiten**.

![Formatierung von Formelergebnissen](images/format-settings-of-the-link-formula-column.png)

Bei Countlinks- und Rollup-Spalten stehen Ihnen zudem unterschiedliche **Formateinstellungen für Zahlen** zur Verfügung: Prozent, Währungen oder Dauer sowie Dezimaltrennzeichen, Tausendertrennzeichen und Nachkommastellen.