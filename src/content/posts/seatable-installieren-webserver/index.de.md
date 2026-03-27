---
title: SeaTable Server auf dem eigenen Server installieren
description: SeaTable lässt sich dank Docker in wenigen Minuten auf jedem Linux-Server installieren. Erfahren Sie, welche Voraussetzungen Sie brauchen, wie die Installation abläuft und warum Self-Hosting mit SeaTable so einfach ist.
date: 2021-05-15
lastmod: 2025-03-27
categories:
    - product-features
url: /de/seatable-enterprise-installation-server-webserver
aliases:
    - /de/seatable-enterprise-auf-dem-eigenen-server-hinter-einem-webserver-installieren
    - /de/seatable-enterprise-installation-ubuntu-20-04
    - /de/seatable-enterprise-edition-unter-ubuntu-20-04-lts-installieren
seo:
    title: "SeaTable Server installieren: Self-Hosting leicht gemacht"
    description: "SeaTable Server in wenigen Minuten auf dem eigenen Linux-Server installieren – dank Docker und Caddy. Alle Infos zu Voraussetzungen und Ablauf."
color: '#265697'
---

Wer seine Daten lieber auf dem eigenen Server behalten möchte, für den ist SeaTable Server die ideale Lösung. Dank Docker ist die Installation unkompliziert und in wenigen Minuten erledigt – unabhängig davon, welche Linux-Distribution Sie verwenden.

Die vollständige Schritt-für-Schritt-Anleitung zur Installation finden Sie im SeaTable Admin Manual: **[Zur Installationsanleitung auf admin.seatable.com](https://admin.seatable.com/installation/basic-setup/)**

Im Folgenden erfahren Sie, was Sie für die Installation benötigen, wie der Ablauf aussieht und was SeaTable als Plattform alles möglich macht.

## Warum SeaTable selbst hosten?

SeaTable ist als Cloud-Lösung unter [cloud.seatable.io](https://cloud.seatable.io) verfügbar. Viele Unternehmen und Organisationen möchten ihre Daten jedoch auf eigener Infrastruktur betreiben – sei es aus Datenschutzgründen, wegen interner Compliance-Vorgaben oder einfach, um die volle Kontrolle zu behalten. SeaTable Enterprise Edition macht genau das möglich: Sie installieren SeaTable auf Ihrem eigenen Server und können es dort nach Ihren Vorstellungen konfigurieren und betreiben.

## Was Sie brauchen

Die Voraussetzungen für eine SeaTable-Installation sind überschaubar:

- **Ein Linux-Server** mit mindestens 4 CPU-Kernen, 8 GB RAM und 10 GB freiem Speicherplatz (zzgl. Speicher für Ihre Daten)
- **Root-Zugriff** auf den Server, per SSH oder Konsole
- **Eine (Sub-)Domain**, die per DNS auf die IP-Adresse Ihres Servers zeigt
- **Erreichbarkeit auf Port 80 und 443** über diese Domain

Welche Linux-Distribution Sie verwenden, spielt keine Rolle – ob Ubuntu, Debian, Rocky Linux oder eine andere Variante: Solange Docker darauf läuft, funktioniert SeaTable. Hilfreich, aber nicht zwingend, ist eine statische IPv4-Adresse. Sie maximiert die Erreichbarkeit Ihres Servers, da einige Mobilfunknetze nach wie vor kein IPv6 unterstützen.

## Was unter der Haube steckt

SeaTable nutzt Docker, um seine Dienste über mehrere Container bereitzustellen. Neben dem eigentlichen SeaTable Server laufen eine MariaDB-Datenbank zur Speicherung der Daten, Redis für schnelles Caching und ein Reverse Proxy, der eingehende Anfragen entgegennimmt und an SeaTable weiterleitet. All diese Komponenten werden über Docker Compose gemeinsam verwaltet – Sie müssen sich nicht um jede einzeln kümmern.

Als Reverse Proxy liefert SeaTable standardmäßig Caddy mit. Caddy hat den großen Vorteil, dass es HTTPS-Zertifikate über Let’s Encrypt vollautomatisch beantragt und erneuert. Wer seine Domain auf den Server zeigen lässt und Port 80 und 443 freigibt, bekommt verschlüsselte Verbindungen ohne jede manuelle Konfiguration.

## So läuft die Installation ab

Die komplette Installation ist in fünf Schritte gegliedert:

1. **Docker installieren** – Falls noch nicht vorhanden, wird Docker auf dem Server eingerichtet.
2. **Compose-Dateien herunterladen** – SeaTable stellt fertige YAML-Konfigurationsdateien bereit, die alle benötigten Komponenten definieren.
3. **Konfiguration anpassen** – In einer zentralen `.env`-Datei tragen Sie Ihre Domain, Passwörter und Grundeinstellungen ein.
4. **Lizenz anfordern** – SeaTable Enterprise ist mit bis zu drei Benutzern kostenlos nutzbar. Eine Lizenzdatei erhalten Sie unkompliziert per E-Mail.
5. **Server starten** – Ein einzelner `docker compose up` Befehl startet alle Container und SeaTable ist einsatzbereit.

Der gesamte Vorgang dauert in der Regel nicht mehr als 10 Minuten.

## SeaTable hinter einem eigenen Webserver

Caddy ist die empfohlene und einfachste Lösung, aber nicht die einzige. Falls auf Ihrem Server bereits ein Webserver wie nginx, Apache oder Traefik läuft, können Sie SeaTable auch dahinter betreiben. In diesem Fall deaktivieren Sie den mitgelieferten Caddy-Proxy und konfigurieren Ihren bestehenden Webserver als Reverse Proxy für SeaTable. Dabei leitet der Webserver eingehende Anfragen auf der SeaTable-Domain an den SeaTable-Container weiter – ein gängiges Verfahren, das die meisten Administratoren bereits kennen.

Um HTTPS-Zertifikate kümmern Sie sich in diesem Szenario selbst, z.B. über Let’s Encrypt und Certbot oder ein vorhandenes SSL-Zertifikat Ihrer Organisation. Die offizielle Dokumentation beschreibt auch dieses Szenario im Detail.

## Updates leicht gemacht

Auch nach der Installation profitieren Sie von der Docker-Architektur: Updates auf eine neue SeaTable-Version sind mit wenigen Befehlen erledigt. Sie laden das aktuelle Docker Image herunter, starten die Container neu – fertig. Ihre Daten und Konfigurationen bleiben dabei erhalten.

## Was Sie mit SeaTable alles umsetzen können

SeaTable ist weit mehr als eine Datenbank. Es ist eine Plattform, mit der auch Anwender ohne IT-Erfahrung in kürzester Zeit eigene Lösungen bauen können.

Ein Beispiel aus der Praxis: Eine Universitätsverwaltung möchte eingehende Förderanträge digital verwalten. Mit SeaTable legt ein Mitarbeiter eine Base an, erstellt daraus ein Webformular für die Antragstellung und richtet eine KI-Automation ein, die relevante Informationen aus eingereichten Dokumenten automatisch ausliest. Benachrichtigungen informieren das Team bei Statusänderungen, und über eine individuelle App können Antragsteller jederzeit den Stand ihres Antrags einsehen. Das alles ist ohne Programmierkenntnisse möglich und innerhalb weniger Stunden aufgesetzt.

Ob Projektmanagement, Inventarverwaltung, CRM oder Eventplanung – die Einsatzmöglichkeiten sind so vielfältig wie die Anforderungen Ihrer Organisation.

![CRM und Vertrieb in SeaTable: Opportunities nach Owner gruppiert mit Status, Kunden und geschätztem Wert](seatable-crm-example.png)

## Kostenlos starten

SeaTable Enterprise Edition können Sie mit bis zu drei Benutzern dauerhaft kostenlos nutzen – sowohl privat als auch gewerblich. Die kostenlose Lizenz erhalten Sie unkompliziert per E-Mail.

Wenn Sie mehr Benutzer benötigen, können Sie Lizenzen für 10, 25 oder 50 Benutzer direkt auf der [SeaTable Preisseite]({{< relref "pages/prices" >}}) bestellen. Für größere Installationen nehmen Sie bitte über das [Kontaktformular]({{< relref "pages/contact" >}}) Kontakt mit uns auf.
