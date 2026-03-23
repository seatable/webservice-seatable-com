---
title: 'Changelog'
seo:
    title: 'SeaTable Changelog: Alle Neuerungen & Updates'
    description: 'Alle Änderungen und Updates auf einen Blick. Finden Sie detaillierte Changelogs und Release Notes zu jeder Server-Version von SeaTable.'
url: '/de/changelog'

sections:
    - name: 'hero-2'
      weight: 1
      title: SeaTable Server Changelog
      subtitle: Was gibt es neues?
      text: Alle Änderungen, Aktualisierungen und Verbesserungen sind in diesem Changelog zu finden. Weitere Informationen zu den wichtigsten Änderungen finden Sie in den Versionshinweisen.

    - name: 'content-27'
      weight: 2
      title: 'Gehen Sie direkt zur letzten Version:'
      subtitle: 'Verfügbare Versionen'
      text: "Wir empfehlen Ihnen, unseren Newsletter zu abonnieren, um immer über die neueste und sicherste SeaTable-Server-Version informiert zu werden"
      items:
          - icon: fingerprint
            headline: 'SeaTable 6'
            link: '#release-6'
          - icon: bullseye
            headline: 'SeaTable 5'
            link: '#release-5'
          - icon: code
            headline: 'Older versions'
            link: '#release-4'
          
    - name: 'content-11'
      weight: 3
      title: Wählen Sie die europäische Cloud oder betreiben Sie Ihren eigenen Server
      subtitle: Privatsphäre braucht Sicherheit
      description: 'Datenschutz und Sicherheit sind untrennbar miteinander verbunden - echter Datenschutz ist ohne solide Sicherheitsmaßnahmen nicht möglich. Protecting your data against unauthorized access, breaches, and misuse is essential for maintaining confidentiality and trust. Um sicherzustellen, dass Ihre persönlichen und geschäftlichen Daten vertraulich und geschützt bleiben, ist es wichtig, dass Sie sich über die neuesten Sicherheitsstandards und bewährten Verfahren auf dem Laufenden halten.<br><br>
      Mit SeaTable haben Sie die Flexibilität, die Lösung zu wählen, die Ihren Anforderungen an Datenschutz und Compliance am besten entspricht. Sie können sich für unser in Europa gehostetes SaaS-Angebot entscheiden, das vollständig GDPR-konform ist und von den strengen europäischen Datenschutzgesetzen und sicheren Rechenzentren profitiert. <br><br>Alternativ können Sie auch Ihren eigenen SeaTable-Server betreiben, der Ihnen die volle Kontrolle über Ihre Daten und Ihre Sicherheitsinfrastruktur gibt. Beide Optionen sind so konzipiert, dass sie Ihnen Transparenz, Compliance und Sicherheit bieten.'
      image: ''

    - name: "content-26"
      weight: 10
      title: SeaTable Release 6
      subtitle: Version details
      anchor: release-6
      items:
        - text: 'Version **6.0.10** am 4. November 2025: [Release Notes Version 6.0]({{< relref "posts/seatable-releases/seatable-release-6-0" >}})'
        - text: 'Version **6.1.8** am 20. März 2026: [Release Notes Version 6.1]({{< relref "posts/seatable-releases/seatable-release-6-1" >}})'

      template: "c9124bcd934b47bc8f30"

    - name: "content-26"
      weight: 11
      title: SeaTable Release 5
      subtitle: Version details
      anchor: release-5
      items:
        - text: 'Version **5.3.10** am 16. Juni 2025: [Release Notes Version 5.3]({{< relref "posts/seatable-releases/seatable-release-5-3" >}})'
        - text: 'Version **5.2.7** am 25. Februar 2025: [Release Notes Version 5.2]({{< relref "posts/seatable-releases/seatable-release-5-2" >}})'
        - text: 'Version **5.1.9** am 8. November 2024: [Release Notes Version 5.1]({{< relref "posts/seatable-releases/seatable-release-5-1" >}})'
        - text: 'Version **5.0.7** am 15. Juli 2024: [Release Notes Version 5.0]({{< relref "posts/seatable-releases/seatable-release-5-0" >}})'
      template: "5964c9e4b6534372b1d8"

    - name: "content-26"
      weight: 12
      title: SeaTable Release 4
      subtitle: Version details
      anchor: release-4
      items:
        - text: 'Version **4.4.9** am 15. Mai 2024: [Release Notes Version 4.4]({{< relref "posts/seatable-releases/seatable-release-4-4" >}})'
        - text: 'Version **4.3.8** am 8. Februar 2024: [Release Notes Version 4.3]({{< relref "posts/seatable-releases/seatable-release-4-3" >}})'
        - text: 'Version **4.2.11** am 22. November 2023: [Release Notes Version 4.2]({{< relref "posts/seatable-releases/seatable-release-4-2" >}})'
        - text: 'Version **4.1.9** am 23. August 2023: [Release Notes Version 4.1]({{< relref "posts/seatable-releases/seatable-release-4-1" >}})'
        - text: 'Version **4.0.7** am 27. Juni 2023: [Release Notes Version 4.0]({{< relref "posts/seatable-releases/seatable-release-4-0" >}})'
      template: "d2ccee45fb3b4301836a"

    - name: "content-26"
      weight: 13
      title: SeaTable Release 3
      subtitle: Version details
      anchor: release-3
      items:
        - text: 'Version **3.5.10** am 12. April 2023: [Release Notes Version 3.5]({{< relref "posts/seatable-releases/seatable-release-3-5" >}})'
      template: "3d65a8f8c8ad4482abea"

    - name: "faq"
      weight: 14
      title: FHäufig gestellte Fragen zum Changelog
      subtitle: Alles was Sie wissen müssen
      items:
        - q: Wie ist der Release Zyklus von SeaTable?
          a: SeaTable Server wird regelmäßig aktualisiert. Wir veröffentlichen jeden Sommer eine neue Hauptversion (X.0) und alle zwei bis drei Monate eine neue Nebenversion (5.X).
        - q: Wie kann ich über neue Versionen oder Änderungen auf dem Laufenden bleiben?
          a: Wir empfehlen Ihnen, unseren Newsletter zu abonnieren, damit Sie immer über die neueste und sicherste SeaTable Server-Version informiert sind, die Ihren Anforderungen entspricht.
        - q: Kommen bei SeaTable Cloud und SeaTable Server unterschiedlichen Versionen zum Einsatz?
          a: Nein, es gibt nur eine Version von SeaTable. Wir verwenden für SeaTable Cloud das gleiche Docker-Image, das Sie auch herunterladen können, um Ihren eigenen Server zu betreiben.
        - q: Wo kann ich SeaTable herunterladen?
          a: 'SeaTable wird als Docker-Container veröffentlicht. Das aktuellste Image erhalten Sie auf dem [Docker Hub](https://hub.docker.com/r/seatable/seatable-enterprise).'
        - q: 'Ich will meinen eigenen SeaTable Server betreiben. Wo finde ich weitere Informationen?'
          a: 'Bitte schauen Sie in das [SeaTable Admin Manual](https://admin.seatable.com) für Anleitungen zur Installation Ihres eigenen Servers. Eine Lizenzdatei können Sie direkt auf unserer [Preisseite]({{< relref "pages/prices" >}}) erwerben.'

---
