---
title: 'Typische Fehler beim Arbeiten mit Formeln'
date: 2023-05-03
lastmod: '2023-05-03'
categories:
    - 'formeln'
author: 'nsc2'
url: '/de/hilfe/typische-fehler-beim-arbeiten-mit-formeln'
seo:
    title: 'Typische Fehler beim Arbeiten mit Formeln in SeaTable'
    description: 'Erkennen und beheben Sie häufige Fehler bei SeaTable-Formeln: Setzen Sie Anführungszeichen, Klammern, Kommas und Spaltenverweise richtig.'

---

Die [Formel-Spalte]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}}) eröffnet Ihnen viele Möglichkeiten in der Arbeit mit Ihren Daten. Mithilfe von Formeln können Sie beispielsweise Werte von unterschiedlichen Spalten miteinander in Beziehung setzen und mit ihnen Berechnungen vornehmen. Da die Arbeit mit komplexeren Formeln jedoch vor allem am Anfang schwierig sein kann, geben wir Ihnen in diesem Artikel **Lösungen für die bekanntesten Probleme** an die Hand.

## Anführungszeichen bei Textelementen fehlen

Jedes Textelement in Ihren Formeln **muss** zwingend in Anführungszeichen gesetzt werden, damit es vom Formeleditor erkannt wird. Ist ein Text **nicht** in Anführungszeichen gesetzt, kann folgende **Fehlermeldung** erscheinen:

![Fehlermeldung, die bei fehlenden Anführungszeichen um Textelementen erscheint](images/Fehlermeldung-fehlende-Anfuehrungszeichen-bei-Textelementen.png)

#### Fehlerhafte Eingabe:

![Fehlerhafte Eingabe von Textelementen](images/fehlerhafte-eingabe-anfuehrungszeichen.png)

#### Korrekte Eingabe:

![Korrekte Eingabe von Textelementen](images/richtige-eingabe-anfuehrungszeichen.png)

{{< warning  headline="Tipp"  text="Textelemente sind in einer Formel stets **rot** markiert und können so von anderen Elementen unterschieden werden. Ist ein Textelement im Formeleditor **nicht rot** markiert, bedeutet dies, dass es **fehlerhaft** eingegeben wurde." />}}

## Klammern bei Funktionen fehlen oder sind falsch gesetzt

**Nach jeder Funktion** muss im Formeleditor zunächst eine **öffnende runde Klammer** folgen, bevor Sie weitere Elemente hinzufügen. Haben Sie alle Elemente einer Funktion zur Formel hinzugefügt, muss diese zudem mit einer **schließenden Klammer** enden. Werden **keine** Klammern gesetzt, kann der Formeleditor die Funktion **nicht** erkennen und folgende Fehlermeldungen können erscheinen:

![Fehlermeldung, die erscheint, wenn nach einer Funktion keine öffnende runde Klammer gesetzt wird](images/Fehlermeldung-bei-fehlender-Klammer-nach-einer-Funktion.png)

![Fehlermeldung, die erscheint, wenn die Klammern bei einer Funktion fehlerhaft gesetzt werden](images/fehlermeldung-klammern-bei-funktion-falsch-gesetzt.png)

#### Fehlerhafte Eingabe:

![Fehlerhafte Eingabe einer Funktion](images/fehlerhafte-eingabe-funktion-1.png)

#### Korrekte Eingabe:

![Korrekte Eingabe einer Funktion](images/korrekte-eingabe-funktion-1.png)

{{< warning  headline="Tipp"  text="Funktionen werden in einer Formel stets **blau** markiert. Wenn Sie im Formeleditor auf eine öffnende oder schließende Klammer klicken, wird **die zugehörige Klammer hervorgehoben**. So können Sie einfacher fehlende oder falsche Klammersetzungen bei der Eingabe von Funktionen erkennen." />}}

## Fehlerhafte Klammersetzung allgemein

Das korrekte Setzen von Klammern ist eine der größten Herausforderungen bei der Eingabe von Formeln. Egal ob **runde oder geschweifte Klammern** – sie müssen stets an der **richtigen Stelle** in einer Formel gesetzt werden, damit diese vom Formeleditor erkannt wird.

### Runde Klammern

Wie Sie runde Klammern bei der Eingabe von Funktionen korrekt setzen, erfahren Sie im **vorherigen Abschnitt** dieses Artikels.

### Geschweifte Klammern

Geschweifte Klammern nutzen Sie, wenn Sie auf bestimmte **Tabellenspalten** verweisen möchten. Dabei muss der **Name** der gewünschten Spalte stets von **zwei geschweiften Klammern** umgeben sein. Werden **keine** oder **falsche** Klammern gesetzt, kann der Spaltenverweis **nicht** vom Formeleditor erkannt werden und folgende Fehlermeldungen können erscheinen:

![Fehlermeldung die erscheint, wenn keine geschweiften Klammern beim Verweis auf Spaltennamen gesetzt werden](images/fehlermeldung-keine-geschweiften-klammern.png)

![Fehlermeldung die erscheint, wenn geschweiften Klammern beim Verweis auf Spaltennamen fehlerhaft gesetzt werden](images/fehlermeldung-geschweifte-klammern-falsch-gesetzt-1.png)

#### Fehlerhafte Eingabe:

![Fehlerhafte Eingabe von geschweiften Klammern beim Verweisen auf Spaltennamen](images/fehlerhafte-eingabe-geschweifte-klammern-1.png)

#### Korrekte Eingabe:

![Korrekte Eingabe von geschweiften Klammern beim Verweisen auf Spaltennamen](images/korrekte-eingabe.geschweifte-klammern.png)

### Spaltenreferenzen innerhalb von Funktionen

Wenn Sie innerhalb einer Funktion auf Spaltennamen verweisen möchten, müssen Sie besonders auf eine korrekte Klammersetzung achten. Beachten Sie dabei die individuellen Regeln zur Klammersetzung bei Funktionen und Spaltenreferenzen. Falls Sie sich unsicher sind, ob eine Umklammerung vollständig ist, denken Sie daran, dass Ihnen die zweite Klammer immer hervorgehoben wird, wenn Sie im Formeleditor auf eine Klammer klicken.

#### Fehlerhafte Eingabe:

![Fehlerhafte Eingabe einer Funktion mit Spaltenverweis](images/fehlerhafte-eingabe-einer-funktion-mit-spaltenverweis.png)

#### Korrekte Eingabe:

![Korrekte Eingabe einer Funktion mit Spaltenverweis](images/korrekte-eingabe-einer-funktion-mit-spaltenverweis.png)

## Mehrere Funktionen hintereinanderschalten

Wenn Sie **mehrere Funktionen** in Ihre Formel einbauen möchten, müssen Sie darauf achten, die einzelnen Funktionen stets mit einem **Komma** zu trennen.

Darüber hinaus müssen Sie Formeln, die mehrere Funktionen enthalten, auch mit **mehreren schließenden Klammern** beenden. Enthält Ihre Formel z. B. drei Funktionen, muss diese im Formeleditor auch mit drei schließenden Klammern beendet werden.

Werden die genannten Punkte **nicht** beachtet, kann der Formeleditor die eingegebene Formel **nicht** erkennen und folgende Fehlermeldungen können erscheinen:

![Fehlermeldung die erscheint, wenn eine Formel, die mehrere Funktionen beinhaltet nicht mit der erforderlichen Zahl an schließenden Klammern beendet wird](images/fehlermeldung-zu-weinge-klammern-am-ende-der-formel.png)

![Fehlermeldung, die erscheint, wenn keine Kommas zwischen den verschiedenen Funktionen einer Formel gesetzt werden oder diese falsch gesetzt werden](images/fehlermeldung-falsche-kommasetzung.png)

#### Fehlerhafte Eingabe:

![Fehlerhafte Eingabe einer Formel, in der mehrere Funktionen hintereinandergeschaltet wurden ](images/fehlerhafte-eingabe-einer-formel-mit-mehreren-funktionen.png)

#### Korrekte Eingabe:

![Korrekte Eingabe einer Formel, in der mehrere Funktionen hintereinandergeschaltet wurden ](images/korrekte-eingabe-formel-mit-mehreren-funktionen.png)

{{< warning  headline="Tipp"  text="Arbeiten Sie bei komplexeren Formeln stets mit **Leerzeichen und Zeilenumbrüchen**, damit Sie die einzelnen Funktionen Ihrer Formel getrennt voneinander betrachten können und Fehler leichter ins Auge fallen." />}}

## Mehrere Textelemente in einer Formel miteinander verketten

Um mehrere Textelemente in Ihrer Formel miteinander zu verketten, müssen Sie die einzelnen Textelemente jeweils mit einem **&-Symbol** voneinander trennen. Werden **keine &-Symbole** zwischen den Textelementen hinzugefügt, kann der Formeleditor die eingegebene Formel **nicht** erkennen und folgende Fehlermeldung erscheint:

![Fehlermeldung die erscheint, wenn mehrere Textelemente in einer Formel nicht durch & getrennt werden.](images/Fehlermeldung-bei-fehlendenen-zwischen-Textelementen.png)

#### Fehlerhafte Eingabe:

![Fehlerhafte Eingabe von mehreren Textelementen in einer Formel](images/fehlerhafte-Eingabe-mehrere-Textelemente.png)

#### Korrekte Eingabe:

![Korrekte Eingabe von mehreren Textelementen in einer Formel](images/korrekte-Eingabe-mehrere-Textelemente.png)

{{< warning headline="Tipp" text="Damit die verschiedenen Textelemente jeweils durch ein Leerzeichen getrennt werden, fügen Sie jeweils zwischen den Textelementen **zwei &-Symbole** und **zwei Anführungszeichen (oben)** hinzu." />}}

![Bearbeiten der Formel, so dass die Textelemente jeweils durch ein Leerzeichen getrennt sind](images/Leerzeichen-zwischen-Textelementen.png)
