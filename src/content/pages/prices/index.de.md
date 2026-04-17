---
title: 'SeaTable Preise: Transparente Tarife für jede Teamgröße'
description: ''
date: '2025-03-30'
url: '/de/preise'
seo:
    title: 'SeaTable Preise: Transparente Tarife für jedes Team'
    description: 'Entdecken Sie alle Funktionen zu fairen Preisen. Vergleichen Sie Tarife und wählen Sie Ihre perfekte Datenlösung.'

sections:
    - name: hero-price
      weight: 1
      title: SeaTable Cloud. Maßgeschneidert für Sie.
      subtitle: Was wir bieten
      text: Starten Sie kostenlos und holen Sie sich bei Bedarf mehr Funktionen und mehr Limits ab 7 € pro Nutzer und Monat
      title2: SeaTable Server. Volle Kontrolle für Ihr Unternehmen.
      subtitle2: Was Sie bekommen
      text2: Installieren Sie SeaTable auf Ihrem eigenen Server und profitieren Sie von maximaler Datensouveränität, individueller Anpassbarkeit und allen Enterprise-Funktionen.

    - name: 'price-1'
      weight: 2
      xshow: 'showCloud'

    - name: price-table
      weight: 3
      xshow: 'showCloud'
      classes:
        - curved
        - bg-gray-100
      title: Alle Details vergleichen
      table:
          head: ['Free', 'Plus', 'Enterprise', 'Dedicated']
          rows:
              - type: section
                label: 'Preis (pro Nutzer, zzgl. MwSt.)'
              - key: 'Jährliche Abrechnung'
                values: ['0€', '7€', '14€', '*']
              - key: 'Monatliche Abrechnung'
                values: ['0€', '9€', '18€', '*']
              - type: section
                label: 'Nutzung (Gesamt pro Team)'
              - key: 'Bases'
                values: ['∞', '∞', '∞', '∞']  
              - key: 'Tabellen'
                values: ['∞', '∞', '∞', '∞']
              - key: 'Zeilen'
                values: ['10.000', '50.000', '∞', '∞']
              - key: 'Maximale Zeilen in einer Base'
                values: ['10.000', '50.000', '100.000', '200.000']
              - key: 'Speicherplatz'
                values: ['2 GB', '50 GB', ' 100 GB', '∞']
              - key: 'Aufbewahrungszeit Snapshots'
                values: ['1 Monat', '6 Monate', ' 12 Monate', '24 Monate']
              - key: 'JavaScript Läufe (pro Monat)'
                values: ['∞', '∞', '∞', '∞']
              - key: 'Python Läufe (pro Monat)'
                values: ['100', '5.000', '∞', '∞']
              - key: 'API-Aufrufe (pro Monat und Benutzer)'
                values: ['3.000 (fix)', '10.000', '50.000', '∞']
              - key: 'Maximale Teamgröße'
                values: ['25', '∞', '∞', '∞']
              - type: section
                label: 'Funktionen'
              - key: '26 Spaltentypen'
                values: ['+', '+', '+', '+']
              - key: 'Filter, Gruppierung und Sortierung'
                values: ['+', '+', '+', '+']
              - key: 'Ansichten'
                values: ['+', '+', '+', '+']
              - key: 'Private Ansichten'
                values: ['-', '+', '+', '+']
              - key: 'Freigabe von Ansichten'
                values: ['-', '+', '+', '+']
              - key: 'Webformulare'
                values: ['+', '+', '+', '+']
              - key: 'Gemeinsame Datensätze'
                values: ['+', '+', '+', '+']
              - key: 'Import / Export (CSV, XLSX und DTABLE)'
                values: ['+', '+', '+', '+']
              - key: 'Benachrichtigungen'
                values: ['+', '+', '+', '+']
              - key: 'Plugins'
                values: ['+', '+', '+', '+']
              - key: 'Javascript und Python Support'
                values: ['+', '+', '+', '+']
              - key: 'App Builder'
                values: ['+', '+', '+', '+']
              - key: 'Individuelle Freigabeberechtigungen (Base)'
                values: ['-', '+', '+', '+']
              - key: 'Tabellen-, Ansichts- und Spaltenberechtigungen (Base)'
                values: ['-', '+', '+', '+']
              - key: 'Zeilensperrung'
                values: ['-', '+', '+', '+']
              - key: 'Seitenberechtigungen (App)'
                values: ['-', '-', '+', '+']
              - key: 'Anpassungen des Webformulars (Logo, Header-Bild)'
                values: ['-', '-', '+', '+']
              - key: 'Automationen (pro Monat und Benutzer)'
                values: ['100 (fix)', '500', '5.000', '∞']
              - key: 'KI-Credits (pro Monat und Benutzer)'
                values: ['12,5 (fix)', '50', '500', '∞']
              - key: 'Big-Data-Speicher'
                values: ['-', '-', '+', '+']
              - type: section
                label: 'Support'
              - key: 'Hilfebereich'
                values: ['+', '+', '+', '+']
              - key: 'SeaTable Forum'
                values: ['+', '+', '+', '+']
              - key: 'E-Mail-Support'
                values: ['-', '-', '+', '+']
              - key: 'Professional Services (kostenpflichtig)'
                values: ['-', '-', '+', '+']
              - type: section
                label: 'Admin & Sicherheit'
              - key: '2 Faktor-Authentifizierung'
                values: ['+', '+', '+', '+']
              - key: 'Enterprise Admin Panel'
                values: ['-', '-', '-', '+']
              - key: 'Authentifizierung per AD/LDAP, SAML oder OAuth'
                values: ['-', '-', '-', '+']
              - type: section
                label: 'Abrechnung'
              - key: 'Zahlung per Kreditkarte'
                values: ['+', '+', '+', '+']
              - key: 'Zahlung per Überweisung (mind. 10 Benutzer, jährliche Zahlung)'
                values: ['-', '-', '+', '+']


    # details on-premise
    - name: 'content-9'
      weight: 3
      classes:
          - bg-gray-100
          - curved
      xshow: '!showCloud'
      title: Vorteile eines eigenen Servers
      subtitle: Gründe für on-premises
      items:
          - headline: Enterprise-Funktionen
            text: Bei Ihrem eigenen Server, gibt es keine unterschiedlichen Versionen. Sie erhalten immer den vollen Funktionsumfang von SeaTable Enterprise.
            icon: robot
          - headline: Enterprise Support
            text: Im Preis der SeaTable Enterprise Lizenz ist immer unser Enterprise Support inklusive.
            icon: award
          - headline: Customizing
            text: Bei Ihrem SeaTable Enterprise System können Sie eine eigene URL, eigene Templates, individuelle Farbcodes sowie Rollen und Berechtigungen verwenden.
            icon: paint-roller
          - headline: Maximaler Datenschutz
            text: SeaTable ist eine der wenigen Cloud-Lösungen, die Sie auch als On-Premises-Lösung bekommen können.<br><br>Sie lizenzieren einen SeaTable Enterprise Server und können die Server-Software dort installieren und betreiben, wo Sie wollen.
            icon: file-shield
          - headline: Authentifizierung
            text: SeaTable unterstützt alle gängigen Authentifizierungstechniken wie SAML, OAuth, Shibboleth, Active Directory und LDAP. Es ermöglicht Zwei-Faktor-Authentifizierung und Single Sign-on.
            icon: fingerprint
          - headline: Eigene Limits
            text: In Ihrem System bestimmen Sie, welche API-Limits gelten sollen bzw. ob überhaupt welche gelten sollen.
            icon: compass

    - name: 'customer-1'
      weight: 9
      title: 'Weltweit vertrauen Unternehmen und Teams jeder Größe auf SeaTable'
      subtitle: 'Sie sind in guter Gesellschaft'
      show_numbers: 'no'
      buttons: []

    - name: content-11
      weight: 10
      title: Rabatte für gemeinnützige Organisationen
      subtitle: Für jeden bezahlbar
      items:
          - text: Wir freuen uns, Menschen bei großartigen Projekten zu unterstützen. Gemeinnützige Non-Profit Organisationen und Bildungseinrichtungen erhalten grundsätzlich 50% Rabatt. Lokale Vereine erhalten in Ausnahmefällen sogar bis zu 75% Rabatt auf das SeaTable Plus- und SeaTable Enterprise-Abonnement. Senden Sie uns [Ihre Rabattanfrage über die Teamverwaltung]({{< relref "help/teamverwaltung/abonnement/rabatte" >}}).
      image: /images/image-341.png
      image_alt: 'SeaTable Grafik zu Rabatten für gemeinnützige Organisationen, Bildungseinrichtungen und öffentliche Institutionen'

    - name: platform-selector
      weight: 18

    - name: faq
      weight: 19
      xshow: '!showCloud'
      title: Häufig gestellte Fragen
      items:
          - q: Was ist ein Benutzer?
            a: 'Ein Benutzer meint ein (aktives) Benutzerkonto auf einer SeaTable Server Instanz. Ein (aktives) Benutzerkonto erlaubt die Authentifizierung und Anmeldung am System.<br><br>
            Eine Anmeldung und damit ein Benutzerkonto ist für folgende Aktionen notwendig:<br>
            – Erstellung, Bearbeitung und Löschung von Bases, Apps und Webformularen<br>
            – Erfassung, Bearbeitung und Löschung von Daten in Bases und Apps<br><br>
            Keine Anmeldung und damit kein Benutzerkonto ist für diese Aktionen notwendig:<br>
            – Nutzung von öffentlichen Apps<br>
            – Zugriff auf Bases/Ansichten über externe Links<br>
            – Einreichung von öffentlichen Webformularen'
          - q: Was ist ein inaktiver Benutzer?
            a: Ein inaktiver Benutzer meint ein Benutzerkonto, das auf inaktiv gesetzt wurde und das keine Anmeldung am System erlaubt. Inaktive Benutzer zählen nicht gegen die Lizenz und die Lizenz limitiert auch nicht die Anzahl inaktiver Benutzer. Der Aktivitätsstatus eines Benutzers kann durch einen Systemadministrator jederzeit geändert werden.
          - q: Welche Zahlungsmethoden kann ich nutzen?
            a: Sie können grundsätzlich mit Kreditkarte sowie mit Apple Pay und Google Pay bezahlen. Eine Lizenz für 50 Benutzer und mehr können Sie auch per Banküberweisung bezahlen.
          - q: Kann ich eine Lizenz für SeaTable Server ohne automatische Verlängerung erwerben?
            a: Wenn Sie eine SeaTable Server Lizenz ohne automatische Verlängerung der Lizenz erwerben wollen, dann erwerben Sie bitte eine Lizenz mit automatischer Verlängerung und deaktivieren unmittelbar nach dem Kauf die automatische Verlängerung im [SeaTable Server Subscription Management Portal](https://licenses.seatable.com/p/login/5kA4j61uU641eqY000).
          - q: Wie kann ich die automatische Verlängerung der Lizenz für SeaTable Server kündigen?
            a: Sie können die automatische Verlängerung jederzeit im [SeaTable Server Subscription Management Portal](https://licenses.seatable.com/p/login/5kA4j61uU641eqY000) deaktivieren.
          - q: Wie kann ich die Rechnungsadresse anpassen?
            a: Sie können die Rechnungsadresse jederzeit im [SeaTable Server Subscription Management Portal](https://licenses.seatable.com/p/login/5kA4j61uU641eqY000) anpassen.<br><br>Die nachträgliche Änderung einer Rechnung ist nicht möglich.
          - q: Kann ich die Größe einer laufenden SeaTable Server Lizenz ändern?
            a: Eine SeaTable Server Lizenz für 50 Benutzer und mehr können Sie jederzeit vergrößern. Kontaktieren Sie bitte sales@seatable.com und nennen Sie den Lizenzkey und die gewünschte Benutzeranzahl. Der Lizenzpreis für die zusätzlichen Benutzer wird zeitanteilig berechnet.<br><br>Eine SeaTable Server Lizenz für 10 und 25 Benutzer können Sie während der Laufzeit nicht vergrößern. Wenn Sie mehr Benutzer benötigen, dann müssen Sie eine neue Lizenz erwerben.<br><br>Die Kombination mehrerer Lizenzen ist nicht möglich. Eine SeaTable Server Instanz kann nur mit einer Lizenz verbunden werden.
          - q: Kann ich mehrere SeaTable Server Lizenzen kombinieren?
            a: Die Kombination mehrerer SeaTable Server Lizenzen ist nicht möglich. Auf einer SeaTable Server Instanz ist immer nur eine Lizenz aktiviert.
          - q: Wie erfolgt die automatische Verlängerung?
            a: Sie erhalten rund 30 Tage vor Ablauf Ihrer SeaTable Server Lizenz per E-Mail einen Hinweis über die anstehende Verlängerung. Die E-Mail erläutert, wann die Verlängerung erfolgt und welche Zahlungsmethode verwendet wird. Die E-Mail enthält auch einen Link zum [SeaTable Server Subscription Management Portal](https://licenses.seatable.com/p/login/5kA4j61uU641eqY000). Dort können Sie die Rechnungsadresse und die Zahlungsmethode ändern. Nach der Verlängerung erhalten Sie die Rechnung sowie die Lizenzunterlagen per E-Mail. Um die verlängerte Lizenz zu aktivieren, **laden Sie die Lizenzdatei auf Ihre SeaTable Server Instanz hoch.**
          - q: Kann ich beim Kauf einer Lizenz eine Bestellnummer bzw. eine Kostenstelle angeben?
            a: "Wenn Sie auf der Rechnung eine Referenz benötigen, dann kontaktieren Sie bitte [unseren Verkauf]({{< relref \"pages/contact\" >}}). Geben Sie in Ihrer Anfrage folgende Informationen an: Benutzeranzahl, Rechnungsadresse, Umsatzsteuer ID,Kontakt-E-Mail sowie ggf. Rechnungs-E-Mail. Sie erhalten dann ein Angebot per E-Mail. Teilen Sie uns bitte bei der Angebotsbestätigung die Referenz mit. Die Referenz wird dann auf der Rechnung erwähnt sein."
          - q: Erhalte ich als öffentliche Stelle oder als nicht-gewinnorientierte Organisation Rabatt?
            a: Öffentliche Einrichtungen und nicht-gewinnorientierte Organisationen erhalten Rabatt auf SeaTable Server Lizenzen. Kontaktieren Sie bitte [unseren Verkauf]({{< relref "pages/contact" >}}).<br><br>Auf SeaTable Server Lizenzen für 10 und 25 Benutzer wird grundsätzlich kein Rabatt gewährt.
          - q: Für welche Lizenzperioden kann ich eine Lizenz für SeaTable Server erwerben?
            a: Die Mindestlaufzeit einer Software-Lizenz für SeaTable Server ist 1 Jahr. Sie können auch Lizenzen mit Laufzeiten von 2 und 3 Jahren erwerben. Sie sparen 5% bzw. 10% bei Lizenzen mit 2 bzw. 3-jähriger Laufzeit.<br><br>Die Lizenzgebühr wird grundsätzlich zu Beginn der Lizenzperiode für die gesamte Laufzeit in Rechnung gestellt und fällig.<br><br>Für Lizenzen mit längerer Laufzeit kontaktieren Sie bitte [unseren Verkauf]({{< relref "pages/contact" >}}) und nennen Sie die gewünschte Laufzeit sowie Benutzeranzahl. Sie erhalten dann ein Angebot per E-Mail.
          - q: Wie aktiviere ich die Lizenz für SeaTable Server?
            a: Sie müssen aktiv werden, um die Lizenz zu aktivieren! Melden Sie sich als Benutzer mit Administratorrechten an Ihrer SeaTable Server Instanz an und rufen die System-Administration auf. Klicken Sie dazu auf der Startseite auf Ihren Avatar in der rechten oberen Ecke. Im Info-Bereich der System-Administration können Sie die Lizenzdatei hochladen. Die Lizenzperiode der Lizenz wird dann unmittelbar im Info-Bereich angezeigt.<br><br>Ist das Webinterface Ihrer SeaTable Server Instanz nicht mehr erreichbar, dann müssen Sie die Lizenzdatei im Dateisystem des Hosts abspeichern. Mehr Informationen finden Sie im [SeaTable Admin Manual](https://admin.seatable.com).
          - q: Welche Rechte gibt mir die Software-Lizenz für SeaTable Server?
            a: Eine Software-Lizenz für SeaTable ist die Berechtigung an den Lizenznehmer, SeaTable Server zu nutzen. Die durch die Lizenz eingeräumten Nutzungsrechte und weitere Rechte finden Sie in der [EULA von SeaTable Server Enterprise Edition]({{< relref "pages/legal/eula" >}}).
          - q: Ist eine Lizenz übertragbar?
            a: Die [EULA von SeaTable Server Enterprise Edition]({{< relref "pages/legal/eula" >}}) schließt die Übertragung der Nutzungsrechte aus. Sie dürfen eine Lizenz nicht veräußern oder abtreten.
          - q: Kann ich eine Lizenz für SeaTable Server auch bei einem Händler erwerben?
            a: Sie können SeaTable Server Lizenzen nur direkt über die SeaTable GmbH erwerben.
          - q: Was sind die Mindestanforderungen für den Betrieb von SeaTable Server?
            a: Konsultieren Sie das [SeaTable Admin Manual](https://admin.seatable.com) für alle technischen Fragen.

    - name: faq
      weight: 20
      xshow: 'showCloud'
      title: Häufig gestellte Fragen
      items:
          - q: Kann ich SeaTable Cloud kostenlos nutzen?
            a: 'Mit unserem Free Abonnement können Sie SeaTable Cloud dauerhaft mit bis zu 25 Benutzern kostenfrei benutzen. Mit der Registrierung schließen Sie ein solches Abonnement ab.<br><br>Wenn Ihnen die Limite oder Funktionen des Free Abonnements nicht ausreichen, dann können Sie jederzeit ein Upgrade auf das kostenpflichtige Plus oder Enterprise Abonnement mit höheren Limits und erweiterten Funktionen durchführen.'
          - q: Kann ich die Enterprise Funktionen testen?
            a: Wir können Ihr Free oder Plus Abonnement für eine beschränkte Zeit kostenfrei auf ein Enterprise Abonnement upgraden. [Senden Sie uns bitte über die Teamverwaltung eine entsprechende Anfrage](https://account.seatable.com/).
          - q: Was ist ein Team und was ist ein Benutzer?
            a: In SeaTable Cloud arbeiten Sie in Teams zusammen. Jedes Teammitglied hat ein Benutzerkonto und ist damit ein Benutzer. (Ein Team kann aber auch nur ein Mitglied haben.)<br><br>Mit der Registrierung an SeaTable Cloud wird ein Team erstellt. Der erste Benutzer ist der Administrator des Teams. Der Teamadministrator kann dem Team weitere Benutzer hinzufügen und bestehende Teammitglieder verwalten. Der Administrator kann auch einen oder mehrere weitere Teammitglieder zu Teamadministratoren machen.<br><br>Ein Benutzer wird über seine E-Mail-Adresse identifiziert. Ein Benutzer kann immer nur einem Team zugeordnet sein.
          - q: Kann ich die Anzahl der Benutzer in meinem Team ändern?
            a: 'Sie können die Benutzeranzahl in Ihrem Team jederzeit anpassen.<br><br>Bei SeaTable Cloud Free, Plus und Enterprise können Sie dies selbst über die Anpassung Ihres Abonnements in der [Teamverwaltung](https://account.seatable.com/) machen. Bei SeaTable Dedicated sprechen Sie bitte Ihren persönlichen Ansprechpartner an.<br><br>Im Free Abonnement ist die Teamgröße auf 25 begrenzt. Bei SeaTable Cloud Plus und Enterprise sowie bei SeaTable Dedicated ist die Benutzeranzahl unbegrenzt.'
          - q: Kann ich verschiedene Abonnements in meinem Team kombinieren?
            a: 'Die Kombination verschiedener Abonnements in einem Team ist nicht möglich. Ein Team ist mit allen Mitgliedern entweder im Free oder im Plus oder im Enterprise Abonnement.<br><br>Sie können Ihre Benutzer auf zwei oder mehr Teams aufteilen. Diese Teams können verschiedene Abonnements haben.'
          - q: Kann ich verschiedene Abrechnungsperioden kombinieren?
            a: 'Die Kombination verschiedener Abrechnungsperioden in einem Plus und Enterprise Abonnement ist nicht möglich. Ein Team wird mit allen Mitgliedern entweder monatlich oder jährlich abgerechnet.<br><br>Bei jährlicher Zahlung zahlen Sie rund 20% weniger als bei monatlicher Abrechnung.'
          - q: Wie kann ich ein Plus oder Enterprise Abonnement kündigen?
            a: 'Sie können Ihr Plus und Enterprise Abonnement jederzeit in der [Teamverwaltung](https://account.seatable.com/) zum Ende der aktuellen Aboperiode kündigen. Bis dahin können Sie alle Funktionen des gekündigten Abonnements weiter nutzen.<br><br>Mit Wirksamwerden der Kündigung wird Ihr kostenpflichtiges Abonnement in ein Free Abonnement umgewandelt. Sie können also auch über das Ende des kostenpflichtigen Abonnements hinaus auf Ihre Daten in SeaTable Cloud zugreifen. Aufgrund der geringeren Limite des Free Abonnements können Sie nach dem Downgrade ggf. aber nur noch lesend auf Ihre Bases zugreifen.'
          - q: 'Was passiert, wenn ich das Limit meines Abonnements erreiche?'
            a: 'Wenn Sie Ihr Zeilen- oder Speicherlimit erreichen, dann informieren wir Sie darüber. Sie können weiterhin auf Ihre Bases und Tabellen zugreifen; Sie können aber keine weiteren Zeilen erstellen oder Dateien hochladen.'
          - q: 'Welche Zahlungsmethoden kann ich nutzen?'
            a: 'Sie können grundsätzlich mit Kreditkarte sowie mit Apple Pay und Google Pay bezahlen. Enterprise Abonnenten mit jährlicher Zahlungsweise sowie 10 Benutzern und mehr können auch per Banküberweisung bezahlen.'
          - q: 'Wie kann ich die Rechnungsadresse anpassen?'
            a: 'Sie können die Rechnungsadresse jederzeit in der [Teamverwaltung](https://account.seatable.com/) anpassen.<br><br>Die nachträgliche Änderung einer Rechnung ist nicht möglich.'
          - q: 'Wie steht es um den Datenschutz und Sicherheit?'
            a: 'Datenschutz und Sicherheit haben bei uns oberste Priorität. Ihre in SeaTable gespeicherten Daten werden ausschließlich in deutschen Rechenzentren verarbeitet, permanent überwacht und regelmäßig gesichert. Weitere Details finden Sie auf den Seiten [Datenschutz]({{< relref "pages/legal/data-privacy" >}}) und [Sicherheit]({{< relref "pages/legal/security" >}}).'
          - q: 'Wie kann ich mein Konto löschen?'
            a: 'Der Teamadministrator kann jederzeit über die [Teamverwaltung](https://account.seatable.com) einzelne Benutzer des Teams und auch das gesamte Team löschen. Wenn Sie der einzige Benutzer im Team sind, dann sind Sie auch Teamadministrator. Wenn Sie keinen Zugriff auf die Teamverwaltung haben, dann kontaktieren Sie den Administrator Ihres Teams.<br><br>Wir bedauern es, wenn Sie SeaTable nicht mehr nutzen wollen. [Bitte teilen Sie uns die Gründe für Ihren Abschied mit]({{< relref "pages/contact" >}}).<br><br>In den [Nutzungsbedingungen von SeaTable Cloud]({{< relref "pages/legal/terms-of-service" >}}) finden Sie Erläuterungen, was mit Ihren Daten in Folge der Kontolöschung passiert.'
---
