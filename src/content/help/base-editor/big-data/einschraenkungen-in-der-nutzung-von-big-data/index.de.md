---
title: 'Einschränkungen in der Nutzung von Big Data'
date: 2023-05-11
lastmod: '2024-12-16'
categories:
    - 'big-data'
author: 'nsc2'
url: '/de/hilfe/einschraenkungen-in-der-nutzung-von-big-data'
seo:
    title: 'Big Data in SeaTable: Alle Einschränkungen im Überblick'
    description: 'Informieren Sie sich über die wichtigsten Einschränkungen bei SeaTable Big Data: Synchronisation, Bearbeitung, Freigabe, Operationsmöglichkeiten und Tipps zur Nutzung.'

---

Eine normale Ansicht in SeaTable erlaubt das **kollaborative** Arbeiten **in Echtzeit** für **bis zu 100.000 Zeilen**. Big Data ermöglicht Ihnen die **unbegrenzte Speicherung** von Zeilen, reduziert jedoch Ihre Möglichkeiten zur kollaborativen Zusammenarbeit. Werfen Sie vor der Nutzung von Big Data unbedingt einen Blick in diesen Hilfeartikel, um zu erfahren, mit welchen Einschränkungen Sie bei der Nutzung von Big Data rechnen müssen.

## Einschränkungen von Big Data

Der Big-Data-Speicher bietet Ihnen die weitestgehend **unlimitierte Speicherung von Zeilen**, bringt allerdings auch gewisse Einschränkungen mit sich. Im Folgenden finden Sie die **Einschränkungen** in der Übersicht:

- Änderungen an einem Big-Data-Eintrag werden **nicht in Echtzeit** im Browser eines anderen Users **synchronisiert**. Die Änderungen werden für andere User erst nach einem **Reload** der Seite sichtbar.
- Big-Data-Ansichten können Sie **nicht freigeben** – weder einzeln noch in [benutzerdefinierten Freigabeberechtigungen]({{< relref "help/startseite/freigaben/benutzerdefinierte-freigabe-erstellen" >}}).
- In einer Big-Data-Ansicht können Sie **keine neuen Zeilen** anlegen. Dies muss immer in einer [normalen Ansicht]({{< relref "help/base-editor/zeilen/sperren-einer-zeile" >}}).
- In einer Big-Data-Ansicht können Sie nicht den [Spaltentyp anpassen]({{< relref "help/base-editor/spalten/spaltenberechtigungen-festlegen" >}}) bearbeiten.
- [Verknüpfte Einträge]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}}) können Sie bei Big-Data-Einträgen **nicht verändern**. Verlinkungen mit Zeilen im Big-Data-Speicher werden in normalen Ansichten **nicht angezeigt** – in einer Big-Data-Ansicht hingegen schon.
- Bedingte Formatierungen ([Zeilen farblich hervorheben]({{< relref "help/base-editor/ansichten/einfaerben-von-zellen" >}}).
- [Datenverarbeitungsoperationen]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitungsoperationen-in-seatable" >}}) stehen bei Big Data **nicht** zur Verfügung. Einzige Ausnahme ist [Vergleichen und verknüpfen]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-vergleichen-und-verknuepfen" >}}). Diese Operation kann Einträge im Big-Data-Speicher mit Zeilen in jeder anderen Tabelle verknüpfen, egal ob die Zeilen in der Base oder im Big-Data-Speicher gespeichert sind.
- Die Funktion [Suchen und Ersetzen]({{< relref "help/base-editor/tabellen/suchen-und-ersetzen-von-werten-in-seatable" >}}) steht **nicht** zur Verfügung.

{{< warning  headline="Viele dieser Einschränkungen von Big Data gelten nicht für die SeaTable App" >}}

Die meisten Nutzer des Big-Data-Speichers fühlen sich durch diese Einschränkungen nicht in ihrer Arbeit beeinträchtigt. Sollten Sie jedoch davon betroffen sein, können Sie einen Blick auf die [SeaTable App]({{< relref "help/app-builder/app-verwaltung/universelle-app" >}}) werfen. Dort gelten einige der genannten Einschränkungen nicht.

{{< /warning >}}
