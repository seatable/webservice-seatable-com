---
title: 'Die Schaltfläche'
date: 2023-01-07
lastmod: '2023-08-23'
categories:
    - 'andere-spalten'
author: 'nsc2'
url: '/de/hilfe/die-schaltflaeche'
seo:
    title: 'Die Schaltfläche in SeaTable – Automatisierung per Klick'
    description: 'Mit der Schaltflächen-Spalte in SeaTable automatisieren Sie Aktionen: Status ändern, Skript starten, PDF erzeugen oder Mail versenden.'
weight: 25
---

Die Schaltflächen-Spalte besitzt eine ähnliche Funktion wie [Automationen]({{< relref "help/base-editor/automationen/anlegen-einer-automation" >}}), wobei Sie Schaltflächen immer **manuell** bedienen müssen. Mithilfe des **Buttons**, den Sie in dieser Spalte Ihren **Zeilen** hinzufügen können, lösen Sie im Vorhinein definierte **Aktionen** aus. Aus diesem Grund eignet sich dieser Spaltentyp besonders gut für die Automatisierung von Prozessschritten.

## Anlegen der Schaltfläche

Als Erstes benennen Sie die **Spalte** und legen die **Beschriftung** und **Farbe des Buttons** fest, den Sie Ihren Zeilen hinzufügen möchten.

![Anlegen einer Schaltfläche](images/create-button-column.png)

Im nächsten Schritt legen Sie eine beliebige Anzahl an **Aktionen** fest, die durch Aktivierung der Schaltfläche ausgelöst werden sollen. Dabei haben Sie die Möglichkeit, **mehrere** Aktionen hintereinanderzuschalten.

![Panel mit neun Schaltflächen-Aktionen](images/New-button-action-modal.png)

Sie können insgesamt zwischen **neun** verschiedenen Aktionen wählen:

- Zeile sperren
- Zeile bearbeiten
- Zeile in eine andere Tabelle kopieren
- URL öffnen
- Plugin öffnen (nur möglich, wenn Sie mindestens ein [Plugin]({{< relref "help/base-editor/plugins/alle-plugins-in-der-uebersicht" >}}) aktiviert haben)
- PDF-Datei in Spalte speichern (nur möglich, wenn das [Seitendesign-Plugin]({{< relref "help/base-editor/plugins/anleitung-zum-seitendesign-plugin" >}}) aktiviert ist)
- Benachrichtigung versenden
- E-Mail versenden
- Skript ausführen

## Anwendungsbeispiel

In diesem Anwendungsbeispiel nutzen wir die Schaltfläche, um bezahlten Rechnungen per Mausklick den Status "paid" zuzuweisen. Hierfür nehmen wir die Aktion **Zeile bearbeiten**.

![Auswahl der Aktion, die durch Aktivierung der Schaltfläche ausgelöst wird](images/modify-row.png)

In den **Spalten-Einstellungen** legen wir fest, dass die Einträge in der Einfachauswahl-Spalte **"status"** durch Aktivierung der Schaltfläche von **"pending"** auf **"paid"** gesetzt werden.

![Definition der Schaltfläche im Anwendungs-Beispiel](images/settings-of-the-button-column-in-the-example.png)

Nach einem Klick auf die Schaltfläche ändert sich der **Status** der ausgewählten Rechnung auf **paid**.

![Ausgelöste Aktion im Anwendungsbeispiel der Schaltfläche](images/example-button-column.gif)

### Zusätzliche Möglichkeit

Um die Automatisierung von Prozessschritten zu erweitern, können Sie Schaltflächen auch in Kombination mit [Automationen]({{< relref "help/base-editor/zeilen/sperren-einer-zeile" >}}).

![Anwendungs-Beispiel für die Nutzung der Schaltfläche in Kombination mit Automationen](images/use-the-button-cplumn-with-automations.gif)
