---
title: 'Der Spaltentyp Automatische Nummer'
date: 2023-01-07
lastmod: '2023-02-10'
categories:
    - 'text-und-zahlen'
author: 'ssc'
url: '/de/hilfe/der-spaltentyp-automatische-nummer'
seo:
    title: 'Spaltentyp Automatische Nummer in SeaTable – erklärt'
    description: 'So nutzen Sie die automatische Nummerierung für eindeutige IDs – Formate, Besonderheiten, Neubeginn und Lücken in der Zählung.'
weight: 24
---

Der Spaltentyp **Automatische Nummer** erzeugt eine automatisch ansteigende Nummer für jede neue Zeile. Dieser Spaltentyp kommt immer dann zum Einsatz, wenn Sie für jeden Datensatz eine eindeutige Kennung benötigen.

Beachten Sie, dass diese Spalte **nicht** dazu gedacht ist, die Anzahl der Datensätze in einer Tabelle zu zählen. Wenn Sie [eine Zeile löschen]({{< relref "help/base-editor/zeilen/das-loeschen-von-zeilen" >}}), werden die verbleibenden Datensätze **nicht** neu nummeriert. Dies kann zu **Lücken** in der Nummerierung führen.

Um Ihre Datensätze **neu** zu nummerieren (z. B. um Lücken zu beseitigen), können Sie entweder die Spalte _Automatische Nummer_ löschen und neu erstellen oder den Spaltentyp ändern und dann erneut in eine _Automatische Nummer_ umwandeln.

![Zeilen mit einer automatischen Nummer](images/auto-number.gif)

## Drei Formate stehen zur Verfügung

Beim Anlegen der Spalte _Automatische Nummer_ legen Sie fest, welches **Format** die Werte in dieser Spalte annehmen sollen. Sie können eine **Zahl** mit einer bestimmten Anzahl von Stellen wählen und dieser Nummer einen **String** aus Buchstaben oder Ziffern (z. B. das aktuelle **Datum**) voranstellen.

![SeaTable Formalmöglichkeiten bei der Automatischen Nummern-Spalte](images/Formatmoeglichkeiten-spalten.png)

## Häufige Fragen

Auch wenn der Spaltentyp _Automatische Nummer_ vergleichsweise einfach wirkt, gibt es ein paar Besonderheiten, die es zu beachten gilt.

{{< faq "Kann man den nächsten verwendeten Wert beeinflussen?" >}}Ja. Die Spalte bietet in den Spalten-Optionen die Möglichkeit, die **automatische Nummer** auf einen bestimmten Wert **zurückzusetzen**, den dann die nächste Zeile erhält.
{{< /faq >}}
{{< faq "Können Werte in der Spalte doppelt vorkommen?" >}}Ja, das kann passieren. Wenn Sie die automatische Nummer zurücksetzen, können Werte auch doppelt vorkommen. Die Werte dieser Spalte sind somit nicht einzigartig.
{{< /faq >}}
{{< faq "Kann die Spalte auch nur einzigartige Werte enthalten?" >}}Ja. Wenn Sie ein Plus- oder Enterprise-Abonnement von SeaTable nutzen, können Sie die **Spalte für die Bearbeitung sperren**. So kann niemand die Nummer zurücksetzen und jeder Wert bleibt einzigartig.

{{< /faq >}}
