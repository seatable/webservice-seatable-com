---
title: 'SeaTable Enterprise Edition unter Ubuntu Server 20.04 LTS installieren'
description: 'Dank Docker gelingt die Installation von SeaTable Enterprise unter Ubuntu 20.04 schnell und unkompliziert. Diese Anleitung beschreibt Schritt für Schritt, wie Sie Ihren eigenen SeaTable-Server optimal vorbereiten, aufsetzen und zur Nutzung aktivieren. Jetzt loslegen und alle Vorteile der On-Premises-Lösung nutzen!'
date: 2021-01-23
lastmod: '2024-01-19'
categories: 
    - 'product-features'
url: '/de/seatable-enterprise-installation-ubuntu-20-04'
aliases:
    - /de/seatable-enterprise-edition-unter-ubuntu-20-04-lts-installieren
seo:
    title: 'SeaTable Enterprise auf Ubuntu 20.04 einfach installieren'
    description: 'So installieren Sie SeaTable Enterprise Edition in wenigen Minuten auf Ubuntu 20.04 – Schritt-für-Schritt-Anleitung für Ihre On-Premises-Cloud.'
color: '#3b6bb1'
---

Dank Docker ist die Installation von SeaTable Enterprise Edition ganz einfach und in wenigen Augenblicken gemacht. Ubuntu Server als weitverbreitetes und gut dokumentiertes Linux Betriebssystem bietet sich als Basis für SeaTable hervorragend an. Wenn Sie bereits einen Ubuntu Server haben, dann erfahren Sie hier, wie Sie in 10 Minuten auf diesem SeaTable installieren.

{{< warning headline="Diese Anleitung ist veraltet" text="Bitte beachten Sie, dass dieses Handbuch veraltet ist. Die aktualisierten Installationsanweisungen finden Sie unter [https://admin.seatable.com](https://admin.seatable.com)" />}}

## Voraussetzungen

Damit die Einrichtung von SeaTable so problemlos durchläuft wie hier beschrieben, müssen einige Voraussetzungen erfüllt sein. Dies sind:

- VServer / Dedicated Server mit 4 Kernen, 8GB RAM und rund 10GB Speicher für das Ubuntu Betriebssystem, SeaTable und weitere Voraussetzungen
- Root Zugriff auf den Server (per SSH oder Konsole)
- Subdomain, die per A-Record (IPv4) oder AAAA-Record (IPv6) auf die IP-Adresse des Servers verweist
- Server auf Port 80 und 443 über die Subdomain erreichbar
- Kein anderer Dienst hört auf Port 80 und 443

Natürlich sollten Sie mehr als den oben angegebenen Festplattenspeicher einplanen, um auf dem Datenträger neben Betriebssystem und SeaTable auch noch Ihre eigenen Daten ablegen zu können. Insbesondere wenn Sie beabsichtigen, in SeaTable auch Dateien zu organisieren, dann sollten Sie sehr großzügig weiteren Speicherplatz einplanen.

Keine Voraussetzung, aber hilfreich, ist es, wenn der Server über eine statische IPv4-Adresse erreichbar ist. Damit maximieren Sie die Erreichbarkeit des Servers von unterwegs. In Europa gibt es noch [Mobilfunknetze, die noch kein IPv6 beherrschen.](https://www.datamate.org/status-der-ipv6-implementierung-in-mobilfunknetzen-in-dach/) Über ein solches Netz ist Ihr SeaTable Server nicht erreichbar, wenn er keine IPv4-Adresse hat.

Für den Fall, dass auf Ihrem Server bereits Port 80 und/oder 443 belegt sind, finden Sie im Beitrag [SeaTable Enterprise auf dem eigenen Server hinter einem Webserver installieren]({{< relref "posts/seatable-installieren-webserver" >}}) alles was Sie für die Installation in Ihrer Situation wissen müssen.

Sie sind bereit? Los geht’s! Wir gehen davon aus, dass Sie eine Root Shell auf Ihrem Server offen haben.

## Vorbereitung

Zunächst aktualisieren wir das System, um alle Pakete auf dem neusten Stand zu haben:

```
apt update
apt upgrade -y
```

Natürlich müssen diese und alle folgenden Befehle mit Root-Rechten ausgeführt werden, wenn nicht anders angegeben.

SeaTable verwendet docker-compose und dieses Paket müssen Sie installieren. Da es über die Ubuntu-Paketquellen verfügbar ist, reicht der Befehl:

```
apt install docker-compose -y
```

Die Pakete docker.io und containerd sowie zahlreiche Python3 Bibliotheken gehören zu den Abhängigkeiten von docker-compose. Diese werden daher gleich mitinstalliert. Das System ist bereit für SeaTable!

## Download von SeaTable Enterprise

Das Docker Image von SeaTable Enterprise Edition befindet sich in einem Repository auf Docker Hub. Mit dem folgenden Befehl starten Sie den Download des SeaTable Images:

```
docker pull seatable/seatable-ee:latest
```

Kommen wir zum einzigen etwas schwierigeren Thema bei der Einrichtung von SeaTable. Mit den erweiterten Erläuterungen wird aber auch dieser Schritt gut machbar.

## Individualisierung der docker-compose.yml

Zur Einleitung dieses Abschnitts ein bisschen Grundlagenwissen zur Installation von SeaTable: SeaTable stellt seine Dienste über mehrere [Docker Container](https://www.docker.com/resources/what-container) bereit. Neben dem SeaTable Container selbst, in dem der SeaTable Server läuft, sind noch drei weitere Container im Spiel. Konkret sind das die Datenbank MariaDB, der Caching Dienst Memcached und der Dictionary Server redis.

Die Datei docker-compose.yml, um die es gleich gehen wird, ist das Rezept, das Docker für die Installation und Konfiguration des SeaTable und der anderen Container verwendet. Es beinhaltet zentrale Sicherheitseinstellungen (z.B. das Datenbankpasswort) und erlaubt die Anpassung der Installation an eigene Wünsche und Bedürfnisse (z.B. SSL/TLS-Konfiguration).

Legen Sie zunächst in /opt das Verzeichnis seatable an. Im Verzeichnis /opt befindet sich seit der Installation von containerd bereits das gleichnamige Verzeichnis. Dann laden Sie die docker-compose.yml in dieses Verzeichnis runter und öffnen die Datei mit einem Texteditor. Das Code-Beispiel unten beschreibt das Vorgehen im Detail. Wir verwenden für die Bearbeitung der docker-compose.yml den Texteditor nano. Logischerweise geht aber auch vim oder jeder anderer Texteditor.

```
mkdir /opt/seatable
cd /opt/seatable
wget -O "docker-compose.yml" "https://manual.seatable.io/docker/Enterprise-Edition/docker-compose.yml"
nano docker-compose.yml
```

So sieht die YAML-Datei nach dem Download aus:

![docker-compose.yml file](SeaTable_dockercompose.png)

Auf den ersten Blick sieht man die vier Container, die Docker bei Ausführung des Rezepts einrichtet: db, memcached, redis und seatable. Für jeden Container wird das zu verwendende Image (“image”) und die Bezeichnung des Containers (“container_name”) deklariert. Die Container-Bezeichnung ist der Name, über den sich später der Container per Docker Console verwalten lässt.

Darüber hinaus hat jeder Container ein paar individuelle Einstellungen, von denen manche nun Ihre Aufmerksamkeit brauchen.

Im **Container db** müssen Sie das Datenbank Passwort verändern. Ersetzen Sie “YOUR_PASSWORD” durch ein mehrstelliges, alphanumerisches Passwort. Darüber hinaus können Sie den Pfad, unter dem das Verzeichnis /opt/seatable/mysql-data/ im Container seatable-mysql verfügbar gemacht wird, anpassen. Im Standard ist dies der Pfad /var/lib/mysql. Notwendig ist dies nicht.

Der **Container memcached** und der **Container redis** benötigen keine Anpassungen. Wenn Sie memcached oder redis bereits betreiben, dann können Sie diese beiden Container aus der Compose-Datei entfernen. Damit SeaTable lauffähig ist, müssen Sie aber später in den Konfigurationsdateien manuelle Anpassungen vornehmen.

Im **Container seatable** sind die umfangreichsten Anpassungen vorzunehmen: Dort muss zunächst einmal das MYSQL_ROOT_PASSWORD eingetragen werden. Ansonsten kann SeaTable nicht mit der Datenbank kommunizieren. Tragen Sie also bei “DB_ROOT_PASSWD” das oben für den Container db spezifizierte Passwort ein.

Dann heißt es, die Entscheidung zu treffen, ob Let’s Encrypt für Sie ein SSL-Zertifikat beantragen und in die Konfiguration des Webservers einbinden soll. Wenn Sie dies wollen – was vermutlich für die meisten Benutzer die Empfehlung ist -, dann ändern Sie den Wert des Schlüssels SEATABLE_SERVER_LETSENCRYPT auf “True” und geben Sie bei SEATABLE_SERVER_HOSTNAME die von Ihnen verwendete Subdomain ein. Der Certbot von Let’s Encrypt wird dann im Rahmen der Einrichtung ein SSL-Zertifikat beantragen und in der Konfiguration des Webservers berücksichtigen.

Die Zeitzone können Sie auf Etc/UTC für Zentraleuropa belassen. Wenn Sie außerhalb Zentraleuropas sind, dann nutzen Sie die gewöhnlichen Zeitzonencodes.

## Initialisierung der Datenbank

Nachdem die YAML-Datei auf Ihre Bedürfnisse angepasst wurde, wird nun im nächsten Schritt die Datenbank initialisiert. Dazu geben Sie folgende Befehle ein:

```
cd /opt/seatable
docker-compose up
```

Durch den docker-compose Befehl wird das in der YAML-Datei enthaltene Rezept ausgeführt: Es werden mehrere Docker Images von Docker Hub heruntergeladen und extrahiert. Zunächst MariaDB, dann Memcached, darauf redis und abschließend SeaTable selbst – also in der in der docker-compose.yml vorgeschriebenen Reihenfolge. Nach dem Download startet der Datenbank-Container seatable-mysql. Sie können die Aktivitäten auf dem Bildschirm verfolgen (siehe unten). Wenn schließlich der seatable Container übernimmt und die Meldung “This is an idle script (infinite loop) to keep container running.” auf dem Bildschirm erscheint, dann können Sie mit der Tastenkombination CTRL + C den Prozess abbrechen.

Hat dies soweit geklappt? Dann sind Sie Ihrer eigenen, selbstgehosteten SeaTable Instanz ganz nah! Wenn nicht, sehen Sie bitte am Endes Artikels in den Troubleshooting Hinweisen nach.

## Start von SeaTable

Führen Sie die docker-compose.yml nochmals aus. Anders als im Schritt davor wird docker-compose nun aber im Hintergrund bzw. “detached” ausgeführt. Im Anschluss daran lässt sich auch der SeaTable Server im Docker Container seatable starten. Zum Abschluss muss nur noch ein Adminbenutzer angelegt werden. Ihr SeaTable Server ist dann für seine Aufgaben bereit!

```
docker-compose up -d
docker exec -d seatable /shared/seatable/scripts/seatable.sh start
docker exec -it seatable /shared/seatable/scripts/seatable.sh superuser
```

Nach dem letzten Befehl werden Sie aufgefordert, eine E-Mail-Adresse und ein Passwort zu vergeben. Bravo, Sie haben in Ihrem SeaTable on-premises System den ersten Benutzer angelegt.

## Inbetriebnahme

Rufen Sie nun die URL auf, die Sie in der docker-compose.yml unter SEATABLE_SERVER_HOSTNAME angegeben haben. Sie landen auf der Login-Seite Ihres SeaTable Servers. Installation erfolgreich!

Wenn Sie in der docker-compose.yml für die Nutzung von Let’s Encrypt votiert haben, dann sollte Ihre Anfrage direkt auf https umgeleitet werden und somit die Kommunikation mit Ihrem Server verschlüsselt erfolgen. Wenn nicht, dann sollten Sie nun Ihr eigenes SSL-Zertifikat einfügen. Kopieren Sie das Zertifikat in den Ordner /opt/seatable/ssl/ und passen Sie die Konfiguration des Webservers nginx an. Ebenfalls müssen Sie in den Konfigurationsdateien ccnet.conf, dtable_web_seetings.py und der dtable_server_config.json die Adressen von http auf https umstellen. Danach müssen nginx, SeaTable und Memcached neu gestartet werden. Mit diesen drei Befehlen tun Sie dies:

```
docker exec -it seatable /shared/seatable/scripts/seatable.sh restart
docker restart seatable-memcached
docker exec -it seatable /usr/sbin/nginx -s reload
```

Mehr zur Integration eines eigenen SSL-Zertifikats finden Sie im [SeaTable Admin Manual](https://manual.seatable.io/docker/Enterprise-Edition/Deploy%20SeaTable-EE%20with%20Docker/#ssltls).

![Users menu in SeaTable's System Administration](SeaTableEE_SystemAdministration_Users.png)

## Aktivierung der SeaTable Lizenz

Sie können SeaTable Enterprise Edition mit allen Funktionen ohne kostenpflichtige Lizenz mit bis zu drei Benutzern benutzen – privat wie gewerblich und auch dauerhaft. Aus diesem Grund benötigen Sie für die Inbetriebnahme keine Lizenz.

Wenn Sie jedoch mehr als drei Benutzer in SeaTable anlegen wollen, dann wird sich SeaTable dem verweigern. Eine Lizenz erhalten Sie über [unseren Vertrieb]({{< relref "pages/contact" >}}). Mehr Informationen zu den Preisen von SeaTable Enterprise finden Sie auf unserer [Preisseite]({{< relref "pages/prices" >}}).

Um die Lizenz zu aktivieren, speichern Sie die Lizenzdatei, eine TXT-Datei, im Ordner /opt/seatable/seatable-data/seatable und starten Sie SeaTable neu:

```
docker exec -d seatable /shared/seatable/scripts/seatable.sh restart
```

Die zusätzlichen Benutzer stehen dann sofort zur Verfügung und werden in der Systemsteuerung angezeigt.

## Troubleshooting

Falls bei der Installation irgendetwas schief gegangen ist, dann löschen Sie einfach das Verzeichnis /opt/seatable und fangen Sie von vorne an. Aber Vorsicht: Die in SeaTable gespeicherten Daten gehen dabei verloren.

Wenn Sie das Passwort Ihres Administrators vergessen haben, dann führen Sie den Befehl

```
docker exec -it seatable /shared/seatable/scripts/seatable.sh superuser
```

einfach erneut aus. Der Befehl legt einen weiteren Benutzer mit Admin-Rechten an. Wenn der Befehl einen Fehler produziert, dann erlaubt Ihre SeaTable Lizenz die Anlage weiterer Benutzer nicht. (Dies gilt auch für den Testbetrieb mit maximal drei Nutzern.) In diesem Fall müssen Sie in der MySQL Datenbank einen Benutzer auf inaktiv setzen und dann den Befehl erneut ausführen.
