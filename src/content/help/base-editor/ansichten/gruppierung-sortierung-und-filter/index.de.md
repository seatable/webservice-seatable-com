---
title: 'Gruppierung, Sortierung und Filter'
date: 2022-08-25
lastmod: '2025-12-03'
categories:
    - 'grundlagen-von-ansichten'
author: 'cdb'
url: '/de/hilfe/gruppierung-sortierung-und-filter'
seo:
    title: 'Gruppieren, sortieren & filtern in SeaTable richtig nutzen'
    description: 'Filtern, Sortieren und Gruppieren in SeaTable: So organisieren Sie Ihre Tabellen effizient und erhalten die gewünschten Daten in wenigen Klicks.'
weight: 20
---

SeaTable bietet diverse Methoden, um Daten auszuwerten und aufzubereiten. **Filter, Sortierungen und Gruppierungen** sind einfache Werkzeuge, mit denen Sie in wenigen Klicks Ihre Daten strukturieren und schnell die gewünschten Informationen erhalten. Richtig angewendet, bieten Filter, Sortierungen und Gruppierungen vielfältige Auswertungsmöglichkeiten.

Die Filterung, Sortierung und Gruppierung von Datensätzen erfolgt über **Regeln**. Eine Regel besteht immer aus einer Anweisung und der Spalte, auf die sie angewendet wird. Bei Sortierungen und Gruppierungen ist die Anweisung, unabhängig vom Spaltentyp, die Reihenfolge (aufsteigend oder absteigend), in der die Datensätze aufgelistet werden. Eine Filteranweisung hat weitere Komponenten, die abhängig vom Spaltentyp sind.

Klingt kompliziert? Keineswegs – in SeaTable ist das Gruppieren, Sortieren und Filtern ein Kinderspiel!

## Gruppieren

Mit der Gruppierungsfunktion können Sie **die Zeilen einer Tabelle in Gruppen zusammenfassen** und einfache deskriptive Statistiken wie die Anzahl der Zeilen in einer Gruppe oder die Summe und den Durchschnittswert von zahlenbasierten Spalten ermitteln. Die Gruppierung erfolgt über **identische Werte in der für die Gruppierung gewählten Spalte**. Organisieren Sie beispielsweise die Aufgaben in Ihrem Team, indem Sie mit einer Gruppierung über die Mitarbeiter-Spalte die anstehenden Aufgaben für jedes Teammitglied bündeln.

Möchten Sie Ihre Daten noch genauer darstellen, dann nutzen Sie **verschachtelte Gruppierungen**. Sie können bis zu drei Gruppierungsmerkmale auswählen, um untergeordnete Gruppierungen vorzunehmen. Zum Beispiel können Sie Aufgaben zuerst nach dem Verantwortlichen, dann nach Priorität und dann nach Datum gruppieren. Damit erschließen sich Ihnen neue Möglichkeiten der Datenstrukturierung.

[Erfahren Sie hier mehr zur Gruppierungsfunktion]({{< relref "help/base-editor/ansichten/gruppieren-von-eintraegen-in-einer-ansicht" >}})

## Sortieren

Mit der Sortierungsfunktion können Sie die ungeordneten Einträge in einer Tabelle **in einer geordneten Reihenfolge** anzeigen lassen.

Legen Sie eine Regel an, um die Datensätze aufsteigend bzw. absteigend nach den Werten in einer Spalte zu sortieren. Bei großen Datensätzen können auch **mehrere Sortierungsregeln** zum Einsatz kommen. Bei mehreren Sortierungsregeln werden die Zeilen zunächst nach der ersten Regel sortiert. Zeilen mit identischen Werten nach der ersten Sortierungsregel werden dann nach der zweiten Regel sortiert.

[Erfahren Sie hier mehr zur Sortierungsfunktion]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}})

## Filtern

Mit der Filterfunktion von SeaTable können Sie über Filterregeln **bestimmte Datensätze aus einer Tabelle herausfiltern** und nur die Zeilen anzeigen lassen, die ein gewünschtes Kriterium bzw. die gewünschten Kriterien erfüllen. So reduzieren Sie die Zeilen in der Ansicht auf das Mindestmaß, das Sie gerade benötigen, und behalten immer den Überblick.

Bei Filterregeln besteht die Anweisung – anders als Gruppierungs- und Sortierungsregeln – normalerweise aus zwei Komponenten:
- **Filterkriterium**: Beziehung zwischen gefilterter Spalte und Filterwert (z. B. "ist", "enthält", "ist leer")
- **Filterwert**: Der Wert nach dem gefiltert wird (z. B. "123", "erledigt")

Filterregeln lassen sich darüber hinaus mit den beiden Boole'schen Operatoren UND und ODER verknüpfen. Bei einer **UND-Verknüpfung** werden nur die Einträge angezeigt, die alle definierten Bedingungen erfüllen. Mit der **ODER-Verknüpfung** kann man die Ansicht so filtern, dass alle Zeilen angezeigt werden, die mindestens eine der definierten Bedingungen erfüllen. Mithilfe von **Filtergruppen** lassen sich die Operatoren UND und ODER auch gemeinsam verwenden.

[Erfahren Sie hier mehr zur Filterungsfunktion]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}})

## Sperren von Filter-, Sortierungs- und Gruppierungseinstellungen

Die von Ihnen vorgenommenen Einstellungen mittels Filtern, Gruppierungen und Sortierungen werden jeweils in der aktuellen Ansicht gespeichert. Wenn Sie diese für eine zukünftige Verwendung sichern wollen, können Sie die [Ansicht sperren]({{< relref "help/base-editor/ansichten/ansicht-sperren" >}}), damit niemand die Ansicht verändert.

{{< warning headline="Wichtiger Hinweis" text="Mit Filtern, Gruppierungen und Sortierungen ändern Sie nur, wie die Daten in Ihrer Ansicht angezeigt werden! Die Datengrundlage bleibt unverändert. Wenn also Datensätze verschwunden sind, prüfen Sie, ob Sie in der richtigen Ansicht sind oder ob Sie Datensätze mit einem Filter ausgeblendet haben." />}}

## Unterschiede je nach Ansichtstyp

Nicht alle [Ansichtstypen]({{< relref "help/base-editor/ansichten/was-ist-eine-ansicht" >}}) erlauben Gruppierung, Sortierung und Filterung gleichermaßen. Verschaffen Sie sich einen Überblick mithilfe dieser Tabelle:

| Ansichtstyp        | Filtern                        | Sortieren                      | Gruppieren                 |
| ------------------ | ------------------------------ | ------------------------------ | -------------------------- |
| **Tabelle**        | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| **Kanban**         | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}  |
| **Kalender**       | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}  |
| **Galerie**        | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}  |
| **Zeitleiste**     | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| **Baum**           | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}  |
| **Big Data**       | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |