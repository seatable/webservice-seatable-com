---
title: 'SeaTable Developer und Enterprise Edition im Vergleich'
description: 'SeaTable gibt es in zwei verschiedenen Editionen. Während die Enterprise Edition den vollen Funktionsumfang liefert und deshalb für die SeaTable Cloud und Dedicated Systeme zum Einsatz kommt, ist die Developer Edition kostenlos nutzbar und bietet sich geradezu für Entwickler als flexible Datenbank an.'
color: '#069214'
categories:
    - 'product-features'
date: 2022-02-03
lastmod: '2025-07-22'
author: 'cdb'
url: '/de/editionsvergleich'
seo:
    title: 'SeaTable Developer vs Enterprise Edition im Vergleich'
    description: 'SeaTable bietet zwei No-Code Editionen: Enterprise und Developer. Erfahren Sie Details zu Features und Einsatzmöglichkeiten der Plattform.'
---

SeaTable Server ist SeaTable für den eigenen Server. Durch die Installation von SeaTable in der eigenen Infratruktur haben Sie volle Kontrolle darüber, wo Ihre Daten liegen und wer darauf zugreift. Samit empfiehlt sich SeaTable auch für Anwendungsfälle, in denen Sie Ihre Daten nicht außer Haus geben wollen. Sie können SeaTable Server auch ausschließlich im lokalen Netzwerk ohne Zugriffsmöglichkeit über das Internet betreiben.

## SeaTable Server gibt es in zwei verschiedenen Editionen

### SeaTable Enterprise Edition

Die SeaTable Server Enterprise Edition ist die perfekte [No-Code]({{< relref "posts/20250307-low-code" >}}) Lösung für Teams und Organisationen jeder Größe, die den vollen Funktionsumfang und volle Datenkontrolle erhalten möchten. Nur die Enterprise Edition bietet die Möglichkeit eine externe Authentifizierung per LDAP oder SAML zu verwenden. Auch die *erweiterten* Freigabeberechtigungen und Automationen finden Sie nur in dieser Edition.  
Sie können jederzeit eine SeaTable Enterprise Lizenz für bis zu drei Anwender erhalten. Sie finden das entsprechende Registrierungsformular [unter diesem Link](/on-premises/). Die Installation erfolgt gemäß dem [Administrationshandbuch](https://admin.seatable.com) mithilfe von Docker.

### SeaTable Developer Edition

Die SeaTable Server Developer Edition richtet sich primär an Entwickler, die SeaTable als flexible Datenbank verwenden möchten und eventuell gar nicht auf das Frontend zurückgreifen werden. Hier punktet die Developer Edition mit der leistungsfähigen [SeaTable API](https://api.seatable.com/), den Apps für die verschiedenen Automatisierungsplattform und der vollen Unterstützung sämtlicher Spaltentypen. Für die Developer Edition kann kostenfrei genutzt werden. Die Installationsanleitung finden Sie [hier](https://admin.seatable.com).

## Unterschiede in der Gegenüberstellung

|                                     | Developer Edition                                                               | Enterprise Edition                                                  |
| ----------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **Plattform und Umgebung**          |                                                                                 |                                                                     |
| Server-Betriebssystem               | Linux                                                                           | Linux                                                               |
| Installationsmethode                | Docker                                                                          | Docker                                                              |
| Docker Images                       | [Docker Hub](https://hub.docker.com/r/seatable/seatable-developer)              | [Docker Hub](https://hub.docker.com/r/seatable/seatable-enterprise)  |
| **Lizenz**                          |                                                                                 |                                                                     |
| Lizenztyp                           | [hybrid (Open Source und proprietär)](https://admin.seatable.com/introduction/requirements/#license) | [proprietär]({{< relref "pages/legal/terms-of-service" >}})         |
| Lizenzpreismodell                   | kostenlos                                                                       | Benutzerbasiert                                                     |
| **Limits**                          |                                                                                 |                                                                     |
| Unlimitierte Bases                  | {{< icon icon="circle-check" class="text-seatable-orange" >}}                   | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Unlimitierte Tabellen               | {{< icon icon="circle-check" class="text-seatable-orange" >}}                   | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Unlimitierte Zeilen                 | {{< icon icon="circle-check" class="text-seatable-orange" >}}\*\*               | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Unlimitierter Speicher              | {{< icon icon="circle-check" class="text-seatable-orange" >}}                   | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Unlimitierte Benutzer               | {{< icon icon="circle-check" class="text-seatable-orange" >}}                   | {{< icon icon="circle-check" class="text-seatable-orange" >}}\*\*\* |
| Versionierung (Snapshots)           | {{< icon icon="circle-check" class="text-seatable-orange" >}}                   | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| **Datenerfassung und -bearbeitung** |                                                                                 |                                                                     |
| 24 Spaltentypen                     | {{< icon icon="circle-check" class="text-seatable-orange" >}}                   | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Ansichten                           | {{< icon icon="circle-check" class="text-seatable-orange" >}}                   | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Private Ansichten                   |                                                                                 | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Filter                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}                   | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Gruppierung                         | {{< icon icon="circle-check" class="text-seatable-orange" >}}                   | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Sortierung                          | {{< icon icon="circle-check" class="text-seatable-orange" >}}                   | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Bedingte Formatierung               | {{< icon icon="circle-check" class="text-seatable-orange" >}}                   | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Webformulare                        | {{< icon icon="circle-check" class="text-seatable-orange" >}}                   | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Geteilte Datensätze                 | {{< icon icon="circle-check" class="text-seatable-orange" >}}                   | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Datenverarbeitungen                 | {{< icon icon="circle-check" class="text-seatable-orange" >}}                   | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Statistik                           | {{< icon icon="circle-check" class="text-seatable-orange" >}}                   | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Import aus CSV und XLSX             | {{< icon icon="circle-check" class="text-seatable-orange" >}}                   | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Export in CSV und XLSX              | {{< icon icon="circle-check" class="text-seatable-orange" >}}                   | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Benachrichtigungen                  | {{< icon icon="circle-check" class="text-seatable-orange" >}}                   | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Automationen                        | {{< icon "circle-xmark" >}}                                                     | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Archivfunktion                      | {{< icon "circle-xmark" >}}                                                     | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| JavaScript Unterstützung            | {{< icon icon="circle-check" class="text-seatable-orange" >}}                   | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Python Unterstützung                | {{< icon icon="circle-check" class="text-seatable-orange" >}}                   | {{< icon icon="circle-check" class="text-seatable-orange" >}}\*     |
| **Kollaboration**                   |                                                                                 |                                                                     |
| Echtzeit-Zusammenarbeit             | {{< icon icon="circle-check" class="text-seatable-orange" >}}                   | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Extene Links                        | {{< icon icon="circle-check" class="text-seatable-orange" >}}                   | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Einladungs-Links                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                   | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Freigabe von Bases                  | {{< icon icon="circle-check" class="text-seatable-orange" >}}                   | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Freigabe von Ansichten              | {{< icon "circle-xmark" >}}                                                     | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Individuelle Freigabeberechtigungen | {{< icon "circle-xmark" >}}                                                     | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Tabellenberechtigungen              | {{< icon "circle-xmark" >}}                                                     | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Spaltenberechtigungen               | {{< icon "circle-xmark" >}}                                                     | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Zeilensperrung                      | {{< icon "circle-xmark" >}}                                                     | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| **Plugins und Erweiterungen**       |                                                                                 |                                                                     |
| Kalender                            | {{< icon icon="circle-check" class="text-seatable-orange" >}}                   | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Zeitleiste                          | {{< icon icon="circle-check" class="text-seatable-orange" >}}                   | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Galerie                             | {{< icon icon="circle-check" class="text-seatable-orange" >}}                   | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Kanban                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}                   | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Karten                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}                   | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Seitendesign                        | {{< icon icon="circle-check" class="text-seatable-orange" >}}                   | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Erweiterte Statistiken              | {{< icon icon="circle-check" class="text-seatable-orange" >}}                   | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| SQL-Abfrage                         | {{< icon icon="circle-check" class="text-seatable-orange" >}}                   | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| ONLYOFFICE Integration              | {{< icon "circle-xmark" >}}                                                     | {{< icon icon="circle-check" class="text-seatable-orange" >}}\*     |

- \*: separate Installation erforderlich
- \*\*: aber kein Archiv-Backend
- \*\*\*: Lizenz erforderlich

|                                                    | Developer Edition                                             | Enterprise Edition                                            |
| -------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| **API und Integrationsoptionen**                   |                                                               |                                                               |
| REST API                                           | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Zapier                                             | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Integromat                                         | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| n8n                                                | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| **Branding und Customizing**                       |                                                               |                                                               |
| Eigene Vorlagen                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Eigene URL                                         | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Eigenes Logo                                       | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Logo im Webformular                                | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Titelbild im Webformular                           | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| “Powered by” ausblenden                            | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| **Benutzerverwaltung und Berechtigungsverwaltung** |                                                               |                                                               |
| Lokale Benutzerdatenbank                           | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| 2-Faktor Authentifizierung                         | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Authentifizierung via AD/LDAP                      | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Single Sign-on via SAML                            | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Benutzerrollen                                     | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| **Backend und Skalierbarkeit**                     |                                                               |                                                               |
| S3-Support                                         | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Cluster-Support                                    | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |

## Unterschiede in den Versionen

Sowohl die SeaTable Enterprise Edition als auch die Developer Edition laden Sie bequem von Docker Hub herunter:

- https://hub.docker.com/r/seatable/seatable-enterprise
- https://hub.docker.com/r/seatable/seatable-developer

**Die Editionen unterscheiden sich vor allem bei den Versionen:**

Die Developer Edition stellt jeweils nur eine Grundversion bereit, zum Beispiel **5.3.0**, die auf der ersten Enterprise-Version basiert. Die Enterprise Edition entwickelt sich stetig weiter. Dort finden Sie stets die aktuellste Version, etwa **5.3.12**.

Entdeckte Probleme in der Developer Edition beheben wir erst mit der nächsten Hauptversion (z.B. von 5.3.x zu 5.4.0).

## Unterschiede bei Testing und Support

Die **SeaTable Enterprise Edition** wird von uns umfassend getestet, um eine möglichst fehlerfreie und stabile Nutzung sicherzustellen. Für die **Developer Edition** führen wir hingegen **keine systematischen Tests** durch.

**Kostenpflichtiger Support** wird ausschließlich für die Enterprise Edition angeboten; für die Developer Edition steht **kein offizieller Support** zur Verfügung.

Bei Fragen zur Developer Edition empfehlen wir das [SeaTable Community-Forum](https://forum.seatable.com). Beachten Sie jedoch, dass dort überwiegend Themen zur Enterprise Edition behandelt werden, da diese intensiver genutzt und offiziell unterstützt wird.
