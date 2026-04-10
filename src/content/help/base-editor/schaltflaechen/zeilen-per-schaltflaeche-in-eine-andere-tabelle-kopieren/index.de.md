---
title: 'Zeilen per Schaltfläche in eine andere Tabelle kopieren'
date: 2024-02-20
lastmod: '2024-02-20'
categories:
    - 'andere-spalten'
author: 'kgr'
url: '/de/hilfe/zeilen-per-schaltflaeche-in-eine-andere-tabelle-kopieren'
seo:
    title: 'Zeilen per Schaltfläche in andere Tabelle kopieren'
    description: 'Kopieren Sie Datensätze mit einer Schaltfläche in andere Tabellen: So einfach geht’s in SeaTable – mit Filtern, Bedingungen und Automationen.'

---

Mithilfe einer **Schaltfläche** können Sie **Zeilen in andere Tabellen kopieren**. Dies ist hilfreich, wenn Sie bestimmte Datensätze in verschiedenen Tabellen benötigen, aber keine [Verknüpfung]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}}) nutzen möchten. Die folgende Anleitung illustriert den Anwendungsfall anhand eines Beispiels.

## Anwendungsbeispiel

Sie planen eine **Hochzeitsfeier** und haben bereits eine Gästeliste erstellt.

![Beispiel Gästeliste](images/Beispiel-Gaesteliste.png)

Nun möchten Sie auch den anstehenden **Junggesellinnenabschied** für die Braut und den **Junggesellenabschied** für den Bräutigam organisieren. Daher wollen Sie die Daten der Gäste nach deren Zusage in zwei weitere Tabellen kopieren – je nachdem, welches Geschlecht der Gast hat.

## Passende Tabellen anlegen

Legen Sie zwei neue Tabellen für die jeweiligen Party-Gästelisten an.

{{< warning  type="warning" headline="Achtung"  text="Die **Spaltentypen** und die **Spaltennamen** müssen in den Zieltabellen **identisch** mit der Ursprungstabelle sein, sonst funktioniert die Aktion nicht. Alle Spaltenwerte, die SeaTable nicht zuordnen kann, werden **nicht** kopiert und bleiben in den Zieltabellen leer." />}}

**Tipp:** Eine einfache Methode, um die Tabellenstruktur der Ursprungstabelle zu übernehmen, ist **die Tabelle ohne die bestehenden Einträge zu duplizieren**.

![Tabellenstruktur duplizieren](images/Tabellenstruktur-duplizieren.png)

In den leeren Tabellen können Sie die nicht benötigten Spalten selbstverständlich löschen oder nachträglich neue Spalten hinzufügen.

![Leere duplizierte Tabellen](images/Leere-duplizierte-Tabellen.png)

## Die Schaltfläche anlegen

![Schaltfläche anlegen](images/Schaltflaeche-anlegen.gif)

1. Klicken Sie auf das große **Plus-Symbol** am rechten Ende des Tabellenkopfes.
2. Geben Sie der Spalte einen **Namen** und wählen Sie als **Spaltentyp** _Schaltfläche_ aus.
3. Danach legen Sie die **Beschriftung** und **Farbe des Buttons** fest.
4. Im nächsten Schritt definieren Sie eine beliebige Anzahl an **Aktionen**, die durch Aktivierung der Schaltfläche ausgelöst werden sollen. In unserem Fall wählen Sie **Zeile in andere Tabelle kopieren**.
   ![Schaltflächen-Aktion Zeile in andere Tabelle kopieren](images/Schaltflaechen-Aktion-Zeile-in-andere-Tabelle-kopieren.gif)6. Wählen Sie die **Tabelle** aus, in welche die Zeilen kopiert werden sollen.
5. Sie können **Filter** setzen, um die Ausführung der Schaltflächen-Aktionen an **Bedingungen** zu knüpfen.
6. Bestätigen Sie das Anlegen der Schaltfläche mit **Absenden**.

## Bedingte Ausführung der Schaltflächen-Aktionen

In unserem Anwendungsbeispiel sollen bei Knopfdruck weibliche Gäste in die Tabelle "Hen Party Guests" und männliche Gäste in die Tabelle "Stag Party Guests" kopiert werden. Dazu legen Sie **zweimal die gleiche Aktion** an, die Sie mit gegensätzlichen **Filterbedingungen** ausstatten. So können Sie mit einer einzigen Schaltfläche die Gäste abhängig von ihrem Geschlecht in verschiedene Tabellen kopieren.

![Per Schaltfläche kopierte Zeilen](images/Per-Schaltflaeche-kopierte-Zeilen.gif)

{{< warning  type="warning" headline="Hinweis" >}}

Auf [Tabellenseiten in Apps]({{< relref "help/app-builder/seitentypen-in-universellen-apps/tabellenseiten-in-universellen-apps" >}}) wird diese Schaltflächen-Aktion nicht unterstützt. Bei Knopfdruck erscheint eine entsprechende Fehlermeldung.

{{< /warning >}}

## Automation als weitere Option

Wenn Sie über ein SeaTable Enterprise Abo verfügen, können Sie diesen Prozessschritt auch vollständig automatisieren. Dazu konfigurieren Sie eine entsprechende [Automation, mit der Sie Einträge in anderen Tabellen hinzufügen können]({{< relref "help/base-editor/automationen/beispiel-eintraege-in-andere-tabellen-per-automation-hinzufuegen" >}}).
