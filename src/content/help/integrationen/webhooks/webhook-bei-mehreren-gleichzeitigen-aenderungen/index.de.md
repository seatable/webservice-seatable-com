---
title: "Webhook bei mehreren gleichzeitigen Änderungen"
date: 2024-02-13
lastmod: "2026-11-05"
categories: 
  - "webhooks"
author: "cdb"
url: "/de/hilfe/webhook-bei-mehreren-gleichzeitigen-aenderungen"
seo:
    title: 'Webhooks bei mehreren gleichzeitigen Änderungen'
    description: 'Erfahren Sie, wie SeaTable Webhooks bei mehreren Änderungen zusammenfasst, was der Parameter row_count bedeutet und wie Sie alle geänderten Zeilen abfragen.'

---

SeaTable schickt üblicherweise für jede Änderung an einer Zeile einen Webhook. Verändert ein Vorgang jedoch mehrere Zeilen gleichzeitig, wird nur ein Webhook mit dem zusätzlichen Parameter _row\_count_ erzeugt. Das gilt auch für die API: Ein API-Aufruf erzeugt einen Webhook, egal ob er eine oder mehrere Zeilen ändert.

Im Web-Editor tritt dieser Fall z.B. ein, wenn Sie einen Wert mit {{< key "STRG" >}}+{{< key "C" >}} in die Zwischenablage legen und dann mit {{< key "STRG" >}}+{{< key "V" >}} in mehreren anderen Zeilen einfügen. Dieser Vorgang erzeugt nur einen Webhook. Die folgende Grafik zeigt den entsprechenden Webhook.

![Mehrere gleichzeitige Änderungen per Webhook.](images/webhook_multiple_changes.jpg)

## Was der Webhook enthält

Der Parameter _row\_count_ nennt die Anzahl der betroffenen Zeilen. Die übrigen Angaben wie _row\_id_, _row\_name_ und _row\_data_ beziehen sich dagegen nur auf eine einzige Zeile, in der Regel die erste des Vorgangs. Auch _op\_type_ bleibt in der Einzahl, also _insert\_row_, _modify\_row_ oder _delete\_row_.

Aktuell gibt es keine Möglichkeit, dass für jede Zeile ein eigener Webhook erzeugt wird. Der Webhook enthält auch keine Liste aller betroffenen Zeilen.

## Geänderte Zeilen nach einem Webhook abfragen

{{< warning headline="Webhooks sind nicht für die Synchronisation gedacht" text="Wenn Sie Daten mit einem anderen System synchronisieren möchten, sollte der Webhook nur der Auslöser für den Abgleich sein. Er enthält nicht alle Änderungen, und seine Zustellung ist nicht garantiert." />}}

Fragen Sie die geänderten Zeilen nach dem Webhook über die [SQL-Schnittstelle](https://developer.seatable.com/sql/select/) ab:

```sql
SELECT * FROM Table1 WHERE _mtime >= '2026-11-05T18:30:00+01:00' ORDER BY _mtime, _id LIMIT 1000 OFFSET 0
```

Beachten Sie dabei die folgenden Punkte:

- **Vergleich mit `>=`:** Die Spalte _\_mtime_ ist in der Regel nur sekundengenau. Mit `>` würden Sie Änderungen übersehen, die in derselben Sekunde wie Ihr letzter Abgleich erfolgt sind. Da `>=` manche Zeilen erneut liefert, muss Ihr System doppelte Treffer verarbeiten können.
- **Zeitzone angeben:** Ein Zeitpunkt ohne Zeitzone wird nicht als UTC interpretiert. Geben Sie deshalb immer den Versatz an, z.B. `+01:00`.
- **Ergebnisse seitenweise abrufen:** Ohne `LIMIT` liefert eine SQL-Abfrage höchstens 100 Zeilen, das Maximum pro Abfrage sind 10.000 Zeilen. Erhöhen Sie `OFFSET` so lange, bis eine Abfrage weniger Zeilen liefert als das gesetzte `LIMIT`.
- **Gelöschte Zeilen und Verknüpfungen:** Gelöschte Zeilen tauchen in dieser Abfrage nicht auf, und das Hinzufügen einer Verknüpfung verändert _\_mtime_ nicht. Vergleichen Sie deshalb von Zeit zu Zeit die Zeilen-IDs und die Verknüpfungsspalten in beiden Systemen.

## Zusätzlich regelmäßig abgleichen

Webhooks garantieren keine lückenlose Zustellung: Fehlgeschlagene Zustellungen werden nicht wiederholt, ein Webhook kann [nach Fehlern deaktiviert werden]({{< relref "help/integrationen/webhooks/deaktivierung-eines-webhooks-bei-fehlern" >}}) und in Einzelfällen kann er auch ganz ausbleiben. Führen Sie den Abgleich deshalb zusätzlich nach einem festen Zeitplan aus und prüfen Sie regelmäßig, ob der Webhook noch aktiv ist.
