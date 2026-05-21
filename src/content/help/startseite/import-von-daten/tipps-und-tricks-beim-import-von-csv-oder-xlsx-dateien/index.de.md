---
title: 'Tipps und Tricks beim Import von CSV- oder XLSX-Dateien'
date: 2022-10-15
lastmod: '2023-01-19'
categories:
    - 'import-von-daten'
author: 'nsc2'
url: '/de/hilfe/tipps-und-tricks-beim-import-von-csv-oder-xlsx-dateien'
seo:
    title: 'Tipps für den Import von CSV- & XLSX-Dateien in SeaTable'
    description: 'Importieren Sie Daten fehlerfrei nach SeaTable: Nur Tabellenstrukturen nutzen, Import splitten, Datenqualität sichern und Ergebnis kontrollieren!'
---

In SeaTable haben Sie die Möglichkeit, sowohl **CSV-** als auch **Excel-Dateien (.xlsx)** in Ihre Bases zu **importieren**. Damit beim Daten-Import auch alles nach Plan läuft und keine Daten verloren gehen, haben wir die wichtigsten **Tipps und Tricks** beim Import von CSV- oder XLSX-Dateien für Sie zusammengefasst. Wenn Sie diese Tipps und Tricks befolgen, werden Sie erfolgreich Ihre Daten in SeaTable importieren:

- Nur Tabellenstrukturen importieren
- Die Tabellenstruktur in SeaTable vor dem Import anlegen
- Den Import aufteilen
- Die Datenqualität sicherstellen
- Den Import kontrollieren

## Importieren Sie nur Tabellenstrukturen

Häufig treten Probleme beim Import von Excel-Dateien auf, wenn diese **Strukturen** und Inhalte enthalten, **die nicht zur Tabelle gehören**. Die folgende Grafik zeigt einen solchen Fall. Die Überschrift, das Datum und die Spalten A und D gehören nicht zur Tabelle und müssen vor dem Import entfernt werden.

![Excel list with bad elements](images/tipps-import.png)

Auch **Grafiken** werden bei einem Import nicht berücksichtigt und sollten somit vor dem Importversuch gelöscht werden.

## Legen Sie die Tabellenstruktur in SeaTable vor dem Import an

Wenn SeaTable eine Excel-Liste importiert, versucht es anhand der **importierten Daten** zu ermitteln, welcher **Spaltentyp** angelegt werden muss. Probleme entstehen zwangsläufig immer dann, wenn SeaTable den Spaltentyp falsch ermittelt und die Daten nicht mit dem Spaltentyp kompatibel sind. Wenn SeaTable z. B. eine Zahl erkennt und daher eine Zahlspalte anlegt, können Texte und Wörter in dieser Spalte nicht mehr importiert werden und die Zellen bleiben gleich.

Auch wenn die Spaltenerkennung typischerweise zuverlässig funktioniert, können Sie ein mögliches Auftreten dieses Problems leicht vermeiden. Anstatt eine neue Base per Import anlegen zu lassen, legen Sie zuerst selbst die Base mit allen Tabellenspalten an und importieren dann nur noch die Inhalte.

## Teilen Sie den Import auf

Die Importfunktion von SeaTable kann Excel-Dateien mit **mehreren Tabellenblättern** und **Zehntausenden Zeilen** importieren. Die Erfahrung zeigt jedoch: Je mehr Daten Sie versuchen auf einen Schlag zu importieren, umso wahrscheinlicher treten Probleme auf.

Versuchen Sie deshalb, wann immer es möglich ist, den Import in **kleinere Datenpakete** aufzuteilen. Importieren Sie die Tabellenblätter lieber separat und nacheinander und teilen Sie große Tabellen in kleine Tabellen auf. So haben Sie eine bessere Kontrolle über den Import und freuen sich am Ende über vollständig importierte Daten.

## Stellen Sie die Datenqualität sicher

Die **Aufbereitung der Daten** ist für einen reibungslosen Import essenziell. Bevor Sie CSV- oder XLSX-Dateien in eine Base importieren, sollten Sie stets sicherstellen, dass die Daten bereinigt sind und die Anforderungen zum Import erfüllen. Welche **Limitationen** es bezüglich der Daten beim CSV- bzw. Excel-Import gibt, können Sie im entsprechenden Hilfe-Artikel [Limitationen beim CSV/Excel-Import]({{< relref "help/startseite/import-von-daten/limitationen-beim-csv-excel-import" >}}) nachlesen.

## Kontrollieren Sie den Import

Zu jedem Daten-Import gehört immer auch die **Erfolgskontrolle**. Verlassen Sie sich nicht darauf, dass alles funktioniert hat, nur weil Sie keine Fehlermeldungen bekommen. Kontrollieren Sie die importierten Daten auf **Vollständigkeit** und **Fehlerfreiheit**, bevor Sie mit der Bearbeitung beginnen.
