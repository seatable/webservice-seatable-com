---
title: 'Navigieren in der Benutzeroberfläche von SeaTable'
date: 2024-08-30
lastmod: '2024-09-05'
categories:
    - 'online-kurs'
author: 'cdb'
url: '/de/hilfe/navigieren-in-der-benutzeroberflaeche-von-seatable'
seo:
    title: 'Navigieren in der SeaTable Benutzeroberfläche'
    description: 'Lernen Sie die Navigation und alle Elemente der SeaTable Oberfläche kennen. Schritt-für-Schritt: Startseite, Bases, Tabellen, Ansichten & Funktionen verständlich erklärt.'

weight: 3
---

Lassen Sie uns damit beginnen, wie Sie sich in SeaTable zurechtfinden. SeaTable ist eine Weblösung, welche Sie bequem mit Ihrem Browser bedienen. Wir werden kurz durch die verschiedenen Element der Oberfläche gehen und wir zeigen Ihnen, was die einzelnen Symbole bedeuten und wo Sie die Dinge finden, die Sie beim Erstellen Ihrer Bases benötigen.

Öffnen Sie also Ihren Browser, rufen Sie die Login-Seite von SeaTable auf und melden Sie sich mit Ihren Zugangsdaten an. Die Startseite sollte ungefähr so aussehen:

{{< zoom image="images/elements_seatable_homepage.png" alt="Elemente der SeaTable Startseite" >}}

## Die Startseite

Die Startseite unterteilt sich in zwei Bereiche: Die Navigation (links) und die Übersicht der Bases (rechts). Wahrscheinlich werden Ihnen noch keine oder nur wenige Bases angezeigt. Dies wird sich aber gleich ändern. Eine Base wird immer durch eine farbige Kachel und Ihren Namen, der rechts daneben steht dargestellt.

### Was ist genau eine Base?

Eine Base ist eine Datenbank. Eine Base besteht aus einer oder mehreren Tabellen und kann viele Tausend Zeilen enthalten. Alle Bases, auf die ein Benutzer Zugriff hat, werden Ihnen auf der Startseite angezeigt. Dabei unterscheidet SeaTable unterschiedliche Arbeitsbereiche je nachdem wer die Base erstellt hat oder wer darauf zugriff hat. Die entsprechenden Stichworte sind hier:

- **Meine Bases**: Bases in diesem Bereich haben Sie selbst erstellt und solange Sie nicht explizit die Base an jemanden oder eine Gruppe freigeben, haben nur Sie darauf Zugriff.
- **Favoriten**: Sie können jede beliebige Base als Favorit markieren, um diese immer in diesem Bereich zu finden.
- **Gruppen**: SeaTable lebt von der Zusammenarbeit. Über Gruppen können Sie eine Base einer Personengruppe zugänglich machen.

## Der Base-Editor

Öffnen Sie nun eine Ihrer Bases, indem Sie mit der Maus auf eine Ihrer Bases klicken. Sollten Sie noch keine Base haben, legen Sie einfach eine an. Der Name Ihrer Base ist erstmal egal.

In Ihrer Base werden Sie erstmal nur drei leere Zellen sehen, lassen Sie sich also nicht verwirren, wenn wir die verschiedenen Elemente anhand einer gefüllten Beispielbase erklären.

{{< zoom image="images/elements_seatable_base.png" alt="Elemente der SeaTable Base" >}}

Puh, der erste Anblick einer Base kann ganz schön beängstigend sein. Soviel Schaltflächen und Interaktionsmöglichkeiten warten darauf, genutzt zu werden. Lassen Sie uns die verschiedenen Elemente im Detail ansehen.

### Tabellen

Im Kopfbereich einer jeden Base befinden sich die Tabellen Ihrer Base als Tabs nebeneinander stehen. Tabellen in SeaTable sind vergleichbar mit Tabellenblättern in Excel oder den Tabellen einer Datenbank. Je nachdem, ob Sie das eine oder andere schon kennen. In jeder Tabelle können Sie Spalten anlegen, um die gewünschten Informationen zu erfassen und abzuspeichern. Während in Excel alle Spalten gleich sind, müssen Sie in SeaTable jeweils einen Spaltentyp bei der Anlage auswählen. So legen Sie fest, was für Informationen Sie in dieser Spalte speichern wollen. Hört sich kompliziert an, ist es nicht:

- In einer Zahlenspalte können Sie nur Zahlen speichern, aber keine Bilder
- In einer Datumsspalte können Sie nur Datumswerte speichern, aber keine Zahlen.
- In einer ... - ich glaube, Sie haben das Prinzip verstanden.

### Zeilen

In Zeilen einer Tabelle speichern Sie Ihre Informationen. Jede Zeile steht dabei für einen Datensatz. Wenn Sie also z.B. eine Tabelle `Expenses` mit 50 Zeilen haben, dann haben Sie in jeder der 50 Zeilen eine Ausgabe erfasst.

### Ansichten

Eine Ansicht ist eine benutzerdefinierte Darstellung der Zeilen in einer Tabelle. Jede Ansicht wird durch die genutzten Sortierungen, Filter, Gruppierungen, Spaltenausblendungen sowie weitere Ansichtseinstellungen definiert.

Eine Tabelle kann eine oder mehrere Ansichten enthalten. Alle Ansichten einer Tabelle greifen auf den gleichen Datenbestand zu. Das bedeutet: Wird ein Zellenwert in einer Ansicht geändert, dann wird der Wert in der zugrundeliegenden Tabelle geändert und damit auch in allen Ansichten der Tabelle.

Wir werden das Konzept der Ansichten in diesem Online Kurs noch intensiver beleuchten und mit konkreten Anwendungsfällen verdeutlichen.

## Zusammenfassung

In dieser Lektion haben Sie verschiedene Elemente der SeaTable Oberfläche kennengelernt. Lassen Sie sich nicht einschüchtern von den vielen Möglichkeiten der Benutzeroberfläche. Schon im nächsten Teil dieses Online Kurses werden wir damit beginnen Ihre eigene **Ausgabenverwaltung** zu bauen, wodurch Sie viele der Funktionen von SeaTable einsetzen und kennenlernen werden.

Wenn Sie sich intensiver mit der Benutzeroberfläche und den Begriffen von SeaTable auseinandersetzen wollen, empfehlen wir Ihnen unser [Glossar]({{< relref "help/erste-schritte/einfuehrung-grundlagen/glossar-der-von-seatable-verwendeten-begriffe" >}}). Dort werden die Benutzeroberfläche und die Begrifflichkeiten von SeaTable detailliert erklärt.

## Hilfeartikel mit weiteren Informationen

In den folgenden Artikeln werden wir immer am Ende der Seite einen Abschnitt mit Verweisen auf unseren Hilfebereich einfügen. So werden wir Sie zwar im Rahmen dieses Online Kurses an die Hand nehmen, aber nicht jeden Mausklick per Screenshot visualisieren. Wenn Sie mal nicht weiter wissen, sollten Ihnen die Hilfeartikel weiterhelfen.

- [Eine neue Base erstellen]({{< relref "help/startseite/bases/eine-neue-base-erstellen" >}})
- [Was ist eine Ansicht]({{< relref "help/base-editor/ansichten/was-ist-eine-ansicht" >}}
  )
- [SeaTable Glossar]({{< relref "help/erste-schritte/einfuehrung-grundlagen/glossar-der-von-seatable-verwendeten-begriffe" >}})
- [Eine Base zu den Favoriten hinzufügen]({{< relref "help/startseite/bases/eine-base-zu-den-favoriten-hinzufuegen" >}})
