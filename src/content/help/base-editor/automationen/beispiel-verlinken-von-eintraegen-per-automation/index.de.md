---
title: 'Verlinken von Einträgen per Automation'
date: 2023-01-30
lastmod: '2023-04-06'
categories:
    - 'beispiel-automationen'
author: 'nsc2'
url: '/de/hilfe/verlinken-von-eintraegen-per-automation'
seo:
    title: 'Einträge automatisch verlinken: SeaTable Automation'
    description: 'Verlinken Sie Datensätze gezielt per Automation: Setzen Sie Trigger, wählen Sie Spalten, und lassen Sie Einträge in SeaTable vollautomatisch zusammenführen.'


---

Mithilfe von Automationen müssen Sie Einträge in Ihren Tabellen nicht mehr manuell miteinander verknüpfen, sondern können diese Schritte automatisch ausführen lassen. Definieren Sie hierfür einfach eine entsprechende Automation für eine beliebige Tabellenansicht.

## Verlinken von Einträgen per Automation

![Zeilen sperren und archivieren mit einer Automation](images/how-to-use-automations-for-locking-rows-3.png)

1. Klicken Sie im Base-Header auf {{< seatable-icon icon="dtable-icon-rule" >}} und im Anschluss auf **Automatisierungsregeln**.
2. Klicken Sie auf **Regel hinzufügen**.
3. **Benennen** Sie die Automation und legen Sie die **Tabelle** und **Ansicht** fest, in der diese wirken soll.
4. Definieren Sie ein **Trigger-Ereignis**, welches die Automation auslöst.
5. Klicken Sie auf **Aktion hinzufügen** und wählen Sie als automatisierte Aktion **Links hinzufügen** aus.
6. Bestätigen Sie mit **Abschicken**.

## Anlegen der Automation

Definieren Sie für die Automation zunächst ein **Trigger-Ereignis**.

![Trigger-Ereignisse zur Sperrung und Archivierung von Zeilen](images/trigger-options-for-archivating-rows.png)

{{< warning type="warning" headline="Wichtiger Hinweis" >}}

Die automatisierte Aktion **Links hinzufügen** steht Ihnen **ausschließlich** bei folgenden Trigger-Ereignissen zur Verfügung:

- "Einträge erfüllen nach Bearbeitung bestimmte Bedingungen
- "Ein neuer Eintrag wird hinzugefügt
- "Periodischer Trigger

{{< /warning >}}

Wählen Sie anschließend als automatisierte Aktion **"Links hinzufügen"** aus.

![Hinzufügen der automatisierten Aktion](images/add-an-action.png) ![Hinzufügen der automatisierten Aktion: "Links hinzufügen"](images/add-action-add-links.png)

Wählen Sie abschließend eine **Spalte** aus, die mit der ausgewählten Tabelle verknüpft werden soll, und definieren Sie eine **spezifische Bedingung**, die erfüllt sein muss, damit die Automation durchgeführt wird.

![Definition der automatisierten Aktion](images/automated-actions-add-links.png)

Bestätigen Sie abschließend die Automation mit einem Klick auf **Abschicken**.

![Bestätigung der Automation](images/confirm-the-automation.jpg)

## Anwendungsbeispiel

Ein konkreter **Anwendungsfall** für diese Art von Automation könnte beispielsweise auftreten, wenn Sie in der Buchhaltung eines Unternehmens arbeiten. Dabei möchten Sie sowohl eine Tabelle mit allen Zahlungen pflegen, die auf ein Konto des Unternehmens eingehen (**Payments**), als auch eine Tabelle mit allen Rechnungen, die an das Unternehmen gezahlt werden müssen (**Invoices**).

In der Tabelle **Payments** erfassen Sie neben den **Transaktionsnummern** der Zahlungen (P-0001 etc.) bereits die **Beträge** der verschiedenen Zahlungen (Spalte **"Value"**).

![Beispiel-Tabelle Payments](images/Table-Payments-1.png)

Ihre Tabelle **Invoices** enthält derweil die **Rechnungsnummern** (Spalte **"Invoice-No"**) und die jeweiligen **Rechnungsbeträge** (Spalte **"Price Total"**).

![Beispiel-Tabelle "Invoices"](images/Table-Invoices.png)

Mithilfe einer **Automation** möchten Sie nun die beiden Tabellen **Payments** und **Invoices** miteinander **verlinken**, damit Sie die eingegangenen **Zahlungen** anhand ihrer Rechnungsnummern automatisch einer **Rechnung** zuordnen können.

### Vorbereitung der Automation

Bevor Sie die Automation anlegen können, müssen Sie in der Tabelle **Payments** zunächst noch zwei Spalten hinzufügen. In der Spalte **"Inv-No"** tragen Sie manuell die Rechnungsnummern ein, die zu den jeweiligen Zahlungen gehören – was später die Automation **auslösen** soll. In der Spalte **"Invoices"** werden nach Anlegen der Automation automatisch die **verlinkten Einträge** aus der Tabelle **Invoices** hinzugefügt.

![Manuelle Erweiterung der Tabelle "Payments" um zwei Spalten](images/Manuelle-Erweiterung-der-Tabelle-22Payments22.png)

In der Tabelle **Invoices** benötigen Sie ebenfalls noch eine Spalte (**"Collected Payments"**), in der im Zuge der Automation die verlinkten Einträge der Tabelle **Payments** hinzugefügt werden.

![](images/Hinzufuegen-der-Spalte-22Collected-PAyments22.png)

Im Anschluss können Sie für die Tabelle **Payments** eine **Automation** anlegen.

### Anlegen der Automation

Als Erstes geben Sie der Automation einen Namen und wählen die Tabelle **Payments** mit der gleichnamigen Ansicht aus, in der diese wirken soll.

![Definition der Automation des Anwendungsfalls](images/definition-of-the-automation-1.png)

Als **Trigger-Ereignis** der Automation wählen Sie die Option **"Einträge erfüllen nach Bearbeitung bestimmte Bedingungen"** aus. Dabei fügen Sie als Filterbedingung hinzu, dass die beiden Spalten **"Inv-No"** und **"Value"** der Tabelle "Payments" **nicht leer** sind. Diese Bedingung ist sinnvoll, da die Automation ausgelöst werden soll, sobald in diesen Spalten Einträge vorhanden sind.

![Definition des Trigger-Ereignisses des Anwendungsfalls ](images/trigger-example-1-1.png) ![Definition des Trigger-Ereignisses des Anwendungsfalls ](images/trigger-example-2-1.png)

Als **automatisierte Aktion** der Automation definieren Sie abschließend die Aktion **"Hinzufügen einer verlinkten Spalte in die Tabelle"**.

![Hinzufügen der automatisierten Aktion: "Links hinzufügen"](images/add-action-add-links.png)

Die Spalte **"Invoices"** ist die Spalte, in welche die verlinkten Einträge im Zuge der Automation hinzugefügt werden sollen.

![Auswahl der Spalte, in welche die verlinkten Einträge hinzugefügt werden](images/automated-action-example-1.png)

Im letzten Schritt der Definition der Automation sollten Sie noch eine weitere **Bedingung** festlegen, die erfüllt werden muss, damit der Spalte ein verlinkter Eintrag hinzugefügt wird. In diesem Beispiel wird dabei definiert, dass jeder **Eintrag**, der in der Spalte **"Inv-No"** hinzugefügt wird, auch in der Spalte **"Invoice-No"** der Tabelle **Invoices** zu finden sein muss.

Konkret bedeutet dies, dass jede **Rechnungsnummer**, die Sie einer Zahlung in der Tabelle **Payments** manuell zuordnen, bereits in der Tabelle **Invoices** zu finden sein muss, damit die entsprechenden **Einträge** beider Tabellen miteinander **verlinkt** werden können.

![Definiton der abschließenden Bedingung zum Auslösen der Automation](images/automated-action-example-2-1.png)

### Testen der Automation

Wenn Sie daraufhin in der Tabelle **Payments** in der Spalte **"Inv-No"** eine Rechnungsnummer eintragen, die bereits in der Tabelle **Invoices** zu finden ist, wird der entsprechende **verlinkte Eintrag** automatisch der Tabelle in der Spalte **"Invoices"** hinzugefügt.

![Hinzufügen der verlinkten Einträge durch Auslösen der Automation](images/Ausloesen-der-Automation-Beispiel-1-1-1.png)

{{< warning  type="warning" headline="Wichtiger Hinweis"  text="Wenn Sie in der Spalte **\\"Inv-No\\"** Rechnungsnummern hinzufügen, die **noch nicht** in der Tabelle **Invoices** zu finden sind, wird die Automation **nicht** ausgelöst und der Spalte wird dementsprechend auch **kein** verlinkter Eintrag hinzugefügt, da es den dazugehörigen Eintrag in der Tabelle **Invoices** schlichtweg noch nicht gibt." />}}

Mit einem Klick auf den verlinkten Eintrag öffnet sich ein Fenster, in dem Sie die Inhalte des **verlinkten Eintrags** aus der Tabelle **Invoices** einsehen können.

![Mit einem Klick auf den verlinkten Eintrag lassen sich die Inhalte der verlinkten Spalte in der anderen Tabelle einsehen.](images/Informationen-der-verlinkten-Spalte.png)

Zusätzlich werden durch das Auslösen der Automation auch in der Tabelle **Invoices** die **verlinkten Einträge** aus der Tabelle **Payments** hinzugefügt. Dabei wird in der Spalte **"Collected Payments"** automatisch jeder Rechnungsnummer die dazugehörige **Zahlungsnummer (P-000X)** zugeordnet. Durch die **Automation** können Sie folglich für jede Rechnung die dazugehörige **Zahlung** einsehen und schnell feststellen, welche Rechnungen beglichen und welche Rechnungen noch offen sind.

![Hinzufügen der verlinkten Einträge durch Auslösen der Automation](images/Ausloesen-der-Automation-Beispiel-2.png)

Auch in dieser Tabelle können Sie mit einem Klick auf den verlinkten Eintrag ein Fenster öffnen, in dem Sie die Inhalte des **verlinkten Eintrags** aus der Tabelle **Payments** einsehen können.

![Mit einem Klick auf einen verlinkten Eintrag lassen sich die Inhalte der verlinkten Spalte in der anderen Tabelle einsehen.](images/Informationen-der-verlinkten-Spalte-2.png)

### Weitere hilfreiche Artikel in der Rubrik Automationen:

- [Übersicht über Automationen]({{< relref "help/base-editor/automationen/uebersicht-ueber-automationen" >}})
- [Funktionsweise von Automationen]({{< relref "help/base-editor/automationen/funktionsweise-von-automationen" >}})
- [Anlegen einer Automation]({{< relref "help/base-editor/automationen/anlegen-einer-automation" >}})
- [Automationen verwalten und gruppieren]({{< relref "help/base-editor/automationen/automationen-verwalten-und-gruppieren" >}})
- [Automationen stoppen]({{< relref "help/base-editor/automationen/automationen-stoppen" >}})
- [Automationen löschen]({{< relref "help/base-editor/automationen/automationen-loeschen" >}})
- [Ausführungslog einer Automation anzeigen]({{< relref "help/base-editor/automationen/ausfuehrungslog-einer-automation-anzeigen" >}})
- [Automations-Trigger]({{< relref "help/base-editor/automationen/automations-trigger" >}})
- [Automations-Aktionen]({{< relref "help/base-editor/automationen/automations-aktionen" >}})
- [Zeilen per Automation sperren]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-sperren" >}})

### Weitere interessante Beispiele von Automationen:

- [Zeilen per Automation sperren]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-sperren" >}})
- [Zeilen per Automation hinzufügen]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-hinzufuegen" >}})
- [Einträge in andere Tabellen per Automation hinzufügen]({{< relref "help/base-editor/automationen/beispiel-eintraege-in-andere-tabellen-per-automation-hinzufuegen" >}})
- [Benachrichtigungen per Automation versenden]({{< relref "help/base-editor/automationen/benachrichtigungen-per-automation-versenden" >}})
- [E-Mail-Versand per Automation]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}})
