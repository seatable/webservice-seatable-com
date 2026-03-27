---
title: 'Unterstützte Python Bibliotheken'
date: 2023-05-12
lastmod: '2026-03-27'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/de/hilfe/unterstuetzte-python-bibliotheken'
seo:
    title: 'Unterstützte Python Bibliotheken in SeaTable'
    description: 'Vollständige Liste aller vorinstallierten Python-Bibliotheken in SeaTable Cloud und Server — mit Hinweisen zur Erweiterung auf selbst gehosteten Systemen.'
---

Die Python-Umgebung von SeaTable nutzt **Python 3.12** und enthält die gesamte [Python Standard Library](https://docs.python.org/3.12/library/index.html) (z.B. os, sys, datetime, math, random, json, re, io, smtplib). Diese Module können Sie direkt in Ihren Skripten importieren.

## Vorinstallierte Bibliotheken

Zusätzlich zur Standard Library stehen in SeaTable Cloud und in der Standard-Installation von SeaTable Server folgende Pakete zur Verfügung:

Für einige dieser Bibliotheken bieten wir [Python-Beispiele]({{< relref "help/skripte/python" >}}) mit fertigen Skripten und Beispiel-Bases zum Download an.

| Bibliothek | Beschreibung | Beispiel |
|---|---|---|
| [seatable-api](https://pypi.org/project/seatable-api/) | SeaTable API-Client | alle Beispiele |
| [requests](https://pypi.org/project/requests/) | HTTP-Anfragen | [Aktienkurse abfragen]({{< relref "help/skripte/python/aktienkurs-abfragen" >}}) |
| [pandas](https://pypi.org/project/pandas/) | Datenanalyse und -verarbeitung | |
| [scipy](https://pypi.org/project/scipy/) | Wissenschaftliche Berechnungen | |
| [openai](https://pypi.org/project/openai/) | OpenAI API-Client | |
| [qrcode](https://pypi.org/project/qrcode/) | QR-Code-Erzeugung | [QR-Codes generieren]({{< relref "help/skripte/python/qr-code-generieren" >}}) |
| [python-barcode](https://pypi.org/project/python-barcode/) | Barcode-Erzeugung | [Barcodes generieren]({{< relref "help/skripte/python/barcode-generieren" >}}) |
| [pillow-heif](https://pypi.org/project/pillow-heif/) | HEIC/HEIF-Bildunterstützung | [HEIC zu PNG konvertieren]({{< relref "help/skripte/python/heic-zu-png-konvertieren" >}}) |
| [pdfmerge](https://pypi.org/project/pdfmerge/) | PDF-Zusammenführung | [PDFs zusammenführen]({{< relref "help/skripte/python/pdf-zusammenfuehren" >}}) |
| [rapidfuzz](https://pypi.org/project/rapidfuzz/) | Fuzzy String Matching | |
| [markdown](https://pypi.org/project/Markdown/) | Markdown zu HTML Konvertierung | |
| [ldap3](https://pypi.org/project/ldap3/) | LDAP-Operationen | |
| [dateutils](https://pypi.org/project/dateutils/) | Datums-Hilfsfunktionen | |
| [pyOpenSSL](https://pypi.org/project/pyOpenSSL/) | TLS/SSL-Funktionen | |
| [PyJWT](https://pypi.org/project/PyJWT/) | JSON Web Token Verarbeitung | |

Durch Abhängigkeiten der oben genannten Pakete sind zusätzlich **Pillow** (Bildverarbeitung) und **numpy** (numerische Berechnungen) verfügbar.

{{< warning headline="Diese Liste kann sich ändern" text="Die aktuelle Liste der vorinstallierten Bibliotheken finden Sie in der [requirements.txt des Python Runners](https://github.com/seatable/python-pipeline/blob/main/runner/requirements.txt) auf GitHub." />}}

## Eigene Bibliotheken installieren

In **SeaTable Cloud** sind Sie auf die oben aufgelisteten Bibliotheken beschränkt. Weitere Pakete lassen sich nicht installieren.

Auf einem **selbst gehosteten SeaTable Server** können Sie zusätzliche Bibliotheken hinzufügen, indem Sie einen Custom Python Runner bauen. Eine Anleitung finden Sie im [SeaTable Admin Manual](https://admin.seatable.com/installation/advanced/python-pipeline-custom-python-runner/).
