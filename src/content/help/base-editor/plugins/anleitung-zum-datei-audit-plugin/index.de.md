---
title: 'Anleitung zum Datei-Audit-Plugin'
date: 2026-11-26
lastmod: '2026-11-26'
categories:
    - 'plugins'
author: 'bha'
url: '/de/hilfe/anleitung-zum-datei-audit-plugin'
seo:
    title: 'Anleitung Datei-Audit-Plugin in SeaTable'
    description: 'Das Datei-Audit-Plugin von SeaTable findet Dateien, die eine Base nicht mehr nutzt, Verweise auf fehlende Dateien und zeigt, was den Speicher belegt.'
---

Das **Datei-Audit-Plugin** untersucht die **in Ihrer Base gespeicherten Dateien**: alles, was in die Base hochgeladen wurde – in Datei-, Bild- und Signatur-Spalten, in formatiertem Text, in Kommentaren, Webformularen und Apps –, sowie die Dateien in Ihren eigenen benutzerdefinierten Ordnern der [Dateiverwaltung]({{< relref "help/base-editor/dateien/das-dateimanagement-einer-base" >}}). Es vergleicht, was im Speicher liegt, mit dem, worauf Ihre Base tatsächlich verweist, und meldet die Lücke in beide Richtungen: **Dateien, die niemand mehr nutzt**, und **Verweise auf Dateien, die es nicht mehr gibt**. Außerdem zeigt es Ihnen, wo der Speicherplatz bleibt.

Der Speicher füllt sich in SeaTable unbemerkt, denn wenn Sie eine Datei aus einer Zelle entfernen, **wird sie nicht gelöscht**: Die Datei bleibt in der Dateiverwaltung der Base, damit sie [wiederhergestellt]({{< relref "help/haeufig-gestellte-fragen/wissen-und-tipps/zugriff-auf-geloeschte-anhaenge" >}}) werden kann. Mit der Zeit speichert eine Base so womöglich weit mehr, als ihre Zeilen zeigen.

Das Plugin muss nicht eingerichtet werden: Wenn Sie es zum ersten Mal öffnen, startet das Audit von selbst. Das Audit selbst ändert nichts – Dateien werden nur gelöscht und Verweise nur entfernt, wenn Sie es ausdrücklich veranlassen, Eintrag für Eintrag oder gruppenweise.

{{< zoom image="images/file-audit-plugin.png" alt="Das Datei-Audit-Plugin zeigt den Speicher einer Base nach Ordner und ihre verwaisten Assets" >}}

Wie Sie ein Plugin in einer Base aktivieren, erfahren Sie [hier]({{< relref "help/base-editor/plugins/aktivieren-eines-plugins-in-einer-base" >}}).

## So funktioniert das Audit {#how-the-audit-works}

Ein Audit erledigt drei Dinge:

1. Es **listet den Speicher der Base auf**: jede Datei mit ihrem Ordner und ihrer Größe.
2. Es sammelt jede Datei, auf die die Base **verweist**, ganz gleich, wo sie verwendet wird:
    - die **Datei- und Bild-Spalten** jeder Tabelle sowie die **Signaturen** der Signatur-Spalten,
    - die in Zellen mit **formatiertem Text** eingefügten Bilder,
    - die Bilder der **Beschreibung der Base** und der **Zeilenkommentare**,
    - die Bilder der **Webformulare** der Base und der Formulare ihrer **Apps**,
    - die **archivierten Zeilen**, die wie alle anderen gelesen werden.
3. Es durchsucht die **anderen Bases, auf die Sie Zugriff haben**, nach Zeilen, die in dieser Base gespeicherte Dateien anzeigen (siehe [Dateien, die mehrere Bases teilen](#files-shared-between-bases) weiter unten).

Anschließend vergleicht es die Listen und zeigt das Ergebnis an. Das Audit läuft mit **Ihren eigenen Rechten** – Sie müssen kein Token erstellen –, und der Bericht wird mit der Base gespeichert: Wenn Sie das Plugin erneut öffnen, finden Sie das letzte Ergebnis mit seinem Datum vor, statt dass ein neuer Durchlauf startet. **Audit erneut ausführen** startet es noch einmal, was Sie nach jeder Änderung tun sollten.

{{< warning type="warning" headline="Skripte werden nicht geprüft" text="Die **Skripte** der Base werden als eigene Dateien gespeichert, doch das Plugin sieht sie überhaupt nicht: Wie in der Dateiverwaltung erscheinen sie nicht in der Ordnerstruktur der Assets der Base, ihre Größe wird nicht mitgezählt, und **ihr Inhalt wird nicht gelesen** – eine Datei, die ein Skript verwendet, gilt nicht als Verweis. Trotzdem gehören Skripte zu den Assets der Base: Beim Export **bleiben sie nur mit der Option *Assets inkludieren* erhalten**." />}}

## Was das Plugin meldet {#what-the-plugin-reports}

### Zusammenfassung und Speicher nach Ordner {#summary-and-storage-by-folder}

Der Anfang des Berichts fasst alles zusammen: **Assets insgesamt im Speicher**, wie viele davon **in der Base referenziert** und wie viele **verwaist** sind und welchen Anteil am Speicher sie ausmachen, dann die Anzahl der **fehlenden Referenzen** und der **externen URLs**.

**Speicher nach Ordner** zeigt, wo der Speicherplatz bleibt. Klicken Sie auf einen Ordner, um ihn aufzuschlüsseln. Ihre eigenen Ordner (**benutzerdefinierte Ordner**) werden getrennt von den **Systemordnern** angezeigt, die SeaTable für Datei- und Bild-Spalten, Signaturen, Webformulare und Apps anlegt. Einige Systemordner enthalten Dateien, die SeaTable zum Betrieb der Base braucht und auf die naturgemäß keine Zeile verweist – Plugin-Dateien, die Seiten und Einstellungen jeder App, Logos und Hintergrundbilder von Webformularen sowie Vorlagen des Seitendesigns: Sie sind mit **Systemordner — NICHT LÖSCHEN** gekennzeichnet und werden nie als verwaist aufgeführt. Dateien, die Benutzer über eine App hochladen, werden dagegen wie jeder andere Upload geprüft.

### Verwaiste Assets {#orphaned-assets}

Ein **verwaistes Asset** ist eine Datei im Speicher, auf die keine Zeile mehr verweist – typischerweise eine aus einer Zelle entfernte Datei oder eine, die von einer gelöschten Zeile übrig geblieben ist. Die Liste ist nach Ordnern gruppiert: Sie können eine einzelne Datei löschen oder alle verwaisten Dateien eines Ordners auf einmal.

Konnte eine der [oben](#how-the-audit-works) genannten Stellen bei einem Durchlauf **nicht gelesen werden** – etwa die Kommentare oder die archivierten Zeilen –, nennt der Abschnitt sie, und **das Löschen ist für diesen Durchlauf deaktiviert**: Andernfalls würde jede Datei, die nur dort verwendet wird, zum Löschen angeboten. Führen Sie das Audit erneut aus, um es noch einmal zu versuchen.

Lesen Sie vor dem Löschen die Warnungen in diesem Abschnitt und die [Einschränkungen](#limitations) weiter unten: Ein verwaistes Asset ist eine Datei, *zu der das Plugin keinen Verweis gefunden hat* – das ist nicht ganz dasselbe wie eine Datei, die niemand braucht.

{{< warning type="warning" headline="Gelöschte Dateien landen im Papierkorb" text="Dateien, die das Plugin löscht, landen im **Papierkorb** der Dateiverwaltung. Dort bleiben sie **60 Tage** lang und lassen sich wiederherstellen. Danach, oder sobald der Papierkorb geleert wird, sind sie endgültig verloren: Snapshots enthalten keine Dateien. Für ein vollständiges Backup **exportieren Sie die Base mit der Option *Assets inkludieren***, bevor Sie etwas löschen." />}}

### Fehlende Referenzen {#missing-references}

Eine **fehlende Referenz** ist das Gegenteil: eine Zeile, deren Datei- oder Bild-Spalte auf eine Datei verweist, die **es im Speicher nicht mehr gibt**. Die Zelle zeigt noch einen Eintrag an, doch dahinter steckt nichts. Sie können den veralteten Verweis aus einer Zeile entfernen, aus allen Zeilen einer Spalte oder überall auf einmal. Der Rest der Zelle bleibt unverändert.

### Externe URLs {#external-urls}

Bild-Spalten können auch Links auf Dateien enthalten, die **außerhalb von SeaTable gespeichert** sind. Das Plugin listet sie nach Tabelle und Spalte gruppiert auf. Beim Audit werden sie nicht geprüft, da es dadurch langsamer würde: Starten Sie die Prüfung selbst mit **Externe URLs prüfen**. Jeder Link ist danach **OK**, **fehlerhaft** oder **nicht prüfbar** – viele Websites erlauben einem Browser nicht, ihre Dateien von einer anderen Website aus zu prüfen, *nicht prüfbar* heißt also nicht, dass der Link fehlerhaft ist. Die fehlerhaften Links können Sie anschließend entfernen.

### Dateien, die mehrere Bases teilen {#files-shared-between-bases}

Die letzten beiden Abschnitte behandeln **Dateien, die von einer Base in eine andere gelangen** – ein Fall, der leicht übersehen wird, und der Grund, warum das Plugin bei jedem Audit Ihre anderen Bases durchsucht.

Wenn Sie **eine Zelle oder eine Zeile** von einer Base in eine andere **kopieren**, kopiert SeaTable den Verweis auf die Datei, **nicht die Datei selbst**. Die Datei bleibt in der ursprünglichen Base gespeichert, und die andere Base zeigt sie von dort an – selbst wenn sie in einem anderen Arbeitsbereich liegt. Nichts in den beiden Bases zeigt, dass sie nun miteinander verbunden sind. **Das Importieren einer Tabelle** aus einer anderen Base funktioniert anders: Dabei werden auch die Dateien kopiert, sodass die beiden Bases danach unabhängig voneinander sind. **Wählen Sie diesen Weg**, wann immer Sie die Dateien in beiden Bases brauchen.

- **Von anderen Bases genutzte Dateien** listet die in *dieser* Base gespeicherten Dateien auf, die Zeilen in *einer anderen* Base anzeigen. Sie sind von der Liste der verwaisten Assets ausgenommen, auch wenn in dieser Base nichts mehr auf sie verweist: Eine davon zu löschen würde die andere Base beschädigen.
- **Verweise auf Dateien in anderen Bases** ist das Gegenstück: Zeilen in *dieser* Base, die eine in *einer anderen* Base gespeicherte Datei anzeigen. Sie gelten hier weder als verwaist noch als fehlende Referenzen, und das Plugin kann nicht prüfen, ob diese Dateien noch existieren.

Eine so angezeigte Datei behält die **Berechtigungen der Base, in der sie gespeichert ist**. Wer keinen Zugriff auf diese Base hat, sieht eine **leere Zelle**, wo Sie die Datei sehen – dieselbe Zeile kann für zwei Personen also unterschiedlich aussehen.

## Berechtigungen und Sicherheit {#permissions-and-safety}

- Mit **Lesezugriff** auf die Base können Sie den gesamten Bericht lesen, die Schaltflächen zum Löschen und Entfernen stehen Ihnen aber nicht zur Verfügung.
- In einer **Gruppe**, die Sie nicht verwalten, können Sie trotzdem Dateien löschen. Das Plugin weist Sie jedoch darauf hin, dass sie von anderen Mitgliedern hochgeladen worden sein können, und verlangt eine ausdrückliche Bestätigung.
- Bevor es zum ersten Mal eine Zeile ändert – beim Entfernen einer fehlenden Referenz oder eines fehlerhaften Links –, erstellt das Plugin einen **Snapshot** der Base. Damit können Sie die **Zellinhalte** zurückholen, die das Plugin entfernt hat: die Dateinamen und Links, nicht die Dateien selbst. Das Löschen von Dateien ändert keine Zeile und ist nicht abgedeckt: Snapshots enthalten keine Dateien (siehe die Warnung [oben](#orphaned-assets)).

## Einschränkungen {#limitations}

{{< warning type="warning" headline="Nur die Bases, auf die Sie Zugriff haben, werden geprüft" text="Die Suche nach Verweisen in anderen Bases umfasst die Bases, die Sie sehen: die in Ihren Arbeitsbereichen und Gruppen sowie die für Sie freigegebenen. Die Base eines Kollegen, auf die Sie keinen Zugriff haben, kann durchaus eine Datei aus Ihrer Base anzeigen, ohne dass das Plugin davon erfahren kann. **Ein verwaistes Asset im Bericht ist daher nie ein Beweis dafür, dass eine Datei ungenutzt ist.** Solche Bases erscheinen nie im Bericht, da das Plugin nichts von ihrer Existenz weiß. Nur die Bases, die Sie sehen, die das Plugin bei einem Durchlauf aber nicht lesen konnte – zum Beispiel nach einem Fehler –, werden im Bericht mit dem Grund genannt." />}}

Das Audit hat noch einige weitere blinde Flecken, die Sie vor dem Löschen kennen sollten:

- **Nur die [oben](#how-the-audit-works) genannten Stellen werden gelesen.** Eine Datei, auf die auf andere Weise verwiesen wird, gilt nicht als referenziert und kann daher als verwaist aufgeführt werden – zum Beispiel eine Datei, deren Adresse in einer Text- oder URL-Spalte steht oder die in einem Skript oder über ein externes Tool (Orchestrator usw.) verwendet wird.
- **Ihre eigenen Ordner zählen wie alle anderen.** Eine Datei, die Sie in einen benutzerdefinierten Ordner der Dateiverwaltung hochgeladen haben, um sie dort aufzubewahren, wird als verwaist aufgeführt, solange keine Zeile auf sie verweist.
- **Dateien in benutzerdefinierten Ordnern werden nicht über Bases hinweg verfolgt.** Eine Zeile verweist auf sie über eine Kennung, aus der nicht hervorgeht, in welcher Base sie gespeichert sind. Das Plugin kann daher nicht feststellen, ob eine andere Base sie verwendet.
- **Eine importierte oder kopierte Base kann weiterhin Dateien der ursprünglichen Base verwenden.** Wenn Sie eine Base aus einer `.dtable`-Datei importieren oder kopieren, werden ihre Dateien mitkopiert, doch manche Stellen behalten ihre Links zur ursprünglichen Base – je nachdem, wie die Base erstellt wurde, die Bilder der Base-Beschreibung, von Webformularen und App-Formularen oder die Dateien archivierter Zeilen. Das Plugin führt diese Links unter **Verweise auf Dateien in anderen Bases** auf, und die Kopien, die dadurch in dieser Base ungenutzt bleiben, erscheinen als verwaist. Ihre Bilder werden aus der ursprünglichen Base geladen, und manche werden anderen Personen möglicherweise nicht angezeigt, selbst wenn sie Zugriff auf diese Base haben. Auch Zeilenkommentare werden weder exportiert noch kopiert, sodass die darin eingefügten Bilder in der neuen Base ebenfalls verwaist sind.
- **Der Bericht beschreibt den Zeitpunkt seines Durchlaufs.** Danach kann jeder einen Verweis hinzufügen oder entfernen, in dieser Base oder in einer anderen: Führen Sie das Audit vor dem Löschen erneut aus.
- Bei einem Konto mit vielen Bases **dauert es eine Weile**, sie alle zu prüfen.

## Weitere hilfreiche Artikel

- [Alle Plugins in der Übersicht]({{< relref "help/base-editor/plugins/alle-plugins-in-der-uebersicht" >}})
- [Die Dateiverwaltung einer Base]({{< relref "help/base-editor/dateien/das-dateimanagement-einer-base" >}})
- [Zugriff auf gelöschte Dateien und Bilder]({{< relref "help/haeufig-gestellte-fragen/wissen-und-tipps/zugriff-auf-geloeschte-anhaenge" >}})
- [Wie man Dateien dauerhaft entfernt]({{< relref "help/base-editor/dateien/wie-man-dateien-dauerhaft-entfernt" >}})
- [Aktivieren eines Plugins in einer Base]({{< relref "help/base-editor/plugins/aktivieren-eines-plugins-in-einer-base" >}})
