---
title: 'Python-Beispiel: Ein paar zufällige Einträge erstellen'
date: 2023-03-02
lastmod: '2023-03-22'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/de/hilfe/python-beispiel-ein-paar-zufaellige-eintraege-erstellen'
seo:
    title: 'Python: Zufällige Einträge in SeaTable automatisch erzeugen'
    description: 'Mit diesem Python-Skript erstellen Sie viele zufällige Beispielzeilen direkt in SeaTable. Ideal zum Testen, Vorfühlen und schnellen Füllen neuer Datenbanken.'

---


Manchmal möchte man in einer Base ein paar Beispieleinträge generieren. Mit diesem Python-Skript können Sie in kürzester Zeit von einigen wenigen bis zu viele Tausende Einträge erzeugen.

Dieser Artikel führt Sie durch die verschiedenen Abschnitte des Skriptes, sodass Sie die Funktionsweise verstehen und es bei Bedarf an Ihre Bedürfnisse anpassen können. Das vollständige Skript finden Sie am Ende dieses Artikels.

## 1) Laden der Module

Jedes Python-Skript beginnt mit dem Laden der verwendeten Python-Module, wobei wir _Base_ und _context_ aus der Klasse _seatable_api_ verwenden werden. Das Modul _random_ in der zweiten Zeile benötigen Sie nur, wenn Sie Zufallszahlen erzeugen wollen.

```python
from seatable_api import Base, context
import random
```

## 2) Authentifizierung

Die nächsten zwei Zeilen sind notwendig, um die Verbindung zur aktuellen Base aufzubauen. Nach dieser Authentifizierung können wir über das _base_\-Objekt entweder Informationen auslesen, löschen oder manipulieren.

```python
base = Base(context.api_token, context.server_url)
base.auth()
```

## 3) Neue Zeileninhalte definieren

Nachdem wir nun Zugriff auf die aktuelle Tabelle haben, können wir die anzulegenden Datensätze definieren. Der folgende Code geht davon aus, dass Sie Spalten mit den Namen _Name_, _single_, _random_, _rating_ haben. Wenn Ihre Spalten anders heißen, müssen Sie die Namen entsprechend anpassen.

```python
# define the data for two new rows
rows_data = [
  {
    'Name': "I am new Row",
    'single': "new",
    'random': random.randint(0,100000000),
    'rating': random.randint(0,5)
  },
  {
    'Name': "I am second new row",
    'single': "other value",
    'random': random.randint(0,100000000),
    'rating': random.randint(0,5)
  },
]
```

## 4) Neue Zeilen schreiben

Mit dem letzten Code-Block wurden die Inhalte der neuen Zeilen zwar definiert und in der Variable _rows_data_ gespeichert, aber bisher noch nicht in die Base geschrieben. Dies machen wir jetzt mit dem folgenden Aufruf.

```python
# append the two rows
  base.batch_append_rows(context.current_table, rows_data)
```

## 5) Wenn Sie mehr Zeilen möchten

Selbstverständlich können Sie auch mehr als zwei Zeilen schreiben. Dies erreichen Sie entweder dadurch, dass Sie einfach weitere Zeileninhalte definieren oder indem Sie den Schreibvorgang mithilfe einer Schleife mehrfach ausführen lassen.

```python
# execute batch append 10 times
for i in range(10):

  # define the data for two new rows
  ...

  # append the two rows
  ...
```

{{< warning  type="warning" headline="Einrückungen bei Python beachten"  text="In Python wird die Einrückung von Zeilen zur Strukturierung des Codes verwendet. Das führt dazu, dass der Code kurz und übersichtlich bleibt, gleichzeitig müssen Sie genau auf die Einrückungen achten, da diese festlegt, wo die _for_\-Schleife endet." />}}

## Das komplette Skript

Das vollständige Skript sollte ohne große Anpassungen unmittelbar bei Ihnen lauffähig sein. Ändern Sie die vier Spaltennamen und schon sollte das Skript in Ihrer Tabelle neue Zeilen erzeugen können.

```python
from seatable_api import Base, context
import random

base = Base(context.api_token, context.server_url)
base.auth()

# execute batch append multiple times
for i in range(10):

  # define the data for two new rows
  rows_data = [
    {
      'Name': "I am new Row",
      'single': "new",
      'random': random.randint(0,100000000),
      'rating': random.randint(0,5)
    },
    {
      'Name': "I am second new row",
      'single': "more than new",
      'random': random.randint(0,100000000),
      'rating': random.randint(0,5)
    },
  ]

  # append the two rows
  base.batch_append_rows(context.current_table, rows_data)
```

Das Skript kann sowohl manuell als auch über eine Schaltfläche oder per Automation gestartet werden. Mehr dazu erfahren Sie [hier]({{< relref "help/skripte/allgemein/skript-manuell-per-schaltflaeche-oder-automation-ausfuehren" >}}).
