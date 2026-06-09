---
title: 'Die Spalten Ersteller und Erstellt'
date: 2023-01-20
lastmod: '2023-08-04'
categories:
    - 'datum-dauer-und-personen'
author: 'nsc2'
url: '/de/hilfe/die-spalten-ersteller-und-erstelldatum'
seo:
    title: 'Die Spalten „Ersteller“ und „Erstellt“ in SeaTable: Automatisierte Dokumentation'
    description: 'SeaTable nutzt „Ersteller“ & „Erstellt“, um Nutzer und Zeitpunkte automatisch zu protokollieren. Beide Spalten sind nicht editierbar.'
weight: 21
---

Die Spalten **Ersteller** und **Erstellt** werden von SeaTable ausschließlich **automatisch** gefüllt und stellen daher besondere Spaltentypen dar. Während SeaTable die Ersteller-Spalte mit dem **Namen des Benutzers** füllt, der eine Zeile angelegt hat, wird in der Erstellt-Spalte der **Zeitpunkt** (Datum und Uhrzeit) festgehalten, wann der Benutzer die Zeile angelegt hat.

![Die Spalten "Ersteller und Erstellt" nach dem Anlegen](images/column-creator-and-created-time.png)

## Besonderheiten der beiden Spaltentypen

- Die automatisch erfassten Werte in den Spalten Ersteller und Erstellt können **nicht** bearbeitet werden.
- Bei der **Erstellung** der beiden Spaltentypen stehen, abgesehen vom Spaltennamen, **keine** Optionen zur Verfügung.
- Pro Tabelle kann nur **je eine** Ersteller- und Erstellt-Spalte angelegt werden. Wenn Sie versuchen, eine weitere Spalte desselben Typs anzulegen, erscheint der Hinweis "Eine andere Spalte hat diesen Spaltentyp."

![Fehlermeldung bei weiterer Ersteller-Spalte](images/Fehlermeldung-bei-weiterer-Ersteller-Spalte.png)

- Aus diesem Grund können Sie Ersteller- und Erstellt-Spalten **nicht duplizieren und deren Spaltentyp nicht anpassen**.
