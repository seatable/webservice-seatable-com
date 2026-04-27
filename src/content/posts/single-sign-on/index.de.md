---
title: 'Single Sign-On – Bedeutung, Vorteile und Konfiguration'
description: 'Dutzende Passwörter, ständige Login-Aufforderungen, frustrierte Mitarbeiter – und IT-Teams, die täglich Passwort-Resets bearbeiten. Single Sign-On beendet dieses Chaos. Doch wie funktioniert es? Welche Protokolle gibt es? Und wie sicher ist eine zentrale Authentifizierung tatsächlich? Erfahren Sie, warum SSO für moderne Unternehmen unverzichtbar ist.'
seo:
    title: 'Single Sign-On Authentifizierung für mehr IT-Sicherheit'
    description: 'Single Sign-On erklärt: Wie SSO Ihr Passwort-Chaos beendet, die IT-Sicherheit maximiert und wertvolle Zeit beim Login einspart.'
date: 2026-02-04
url: '/de/single-sign-on/'
categories:
    - 'best-practice'
tags:
    - 'IT Sicherheit & Datenschutz'
    - 'Digitale Transformation'
color: '#3962d2'
register:
   show: true 
--- 

## Was bedeutet SSO?

Mitarbeiter in Unternehmen müssen täglich zwischen verschiedenen Anwendungen wechseln. Jede erfordert ein sicheres und einmaliges Passwort, das regelmäßig geändert werden sollte – und was das genau bedeutet, variiert von Tool zu Tool. Passwortmanager sind eine bewährte Methode, um zu verhindern, dass Ihre Mitarbeiter ihre Passwörter ständig vergessen; sie erfordern jedoch ebenfalls wieder ein Passwort. Unnötige Helpdesk-Tickets, Produktivitätsverluste und auch Sicherheitsprobleme sind die Folge. Single Sign-On löst dieses Problem auf, indem es Nutzern erlaubt, **über eine zentrale Anmeldung auf mehrere Anwendungen oder Systeme zuzugreifen**.

### Key Take-aways

* Single Sign-On (SSO) **erhöht die IT-Sicherheit** in Ihrem [ITSM]({{< relref "pages/landing-pages/industry-solutions/software-development" >}}) durch eine zentrale Nutzer-Authentifizierung und eine vereinfachte Zugriffsüberwachung. 
* Die Nutzung von Single Sign-On Verfahren **steigert die Produktivität** durch reduzierte Passwort-Anmeldungen.
* Gängige Protokolle wie SAML, OAuth und LDAP ermöglichen eine **flexible Integration** in Cloud- und hybride Umgebungen wie SeaTable. 
* EU-basierte oder on-premises SSO-Lösungen erfüllen DSGVO-Anforderungen und vermeiden Datentransfers in Drittländer.

## Wie funktioniert die SSO Authentifizierung?

Das SSO Verfahren beruht im Grunde auf einer tokenbasierten Kommunikation zwischen Webanwendung und einem **zentralen Identity Provider** (IdP).

![Single Sign-On vereinfacht die Benutzeranmeldung.](single-sign-on.png)


* Nutzer werden einmalig bei einem IdP – z. B. Okta oder [Authentik](https://goauthentik.io/) – authentifiziert. Der verantwortliche Systemadministrator gewährt dann Zugriff auf alle autorisierten Services, ohne dass erneut Passwörter eingegeben werden müssen. 
* Nach erfolgreicher SSO Authentifizierung wird durch den IdP ein SSO Token generiert – eine Art Sicherheitszertifikat z. B. als SAML-Assertion (XML-basiert) oder als JWT (JSON Web Token) – und entweder im SSO-System oder im Webbrowser gespeichert. SSO Tokens enthalten Informationen über den jeweiligen Nutzer, z. B. den Benutzernamen und eine E-Mail-Adresse. 
* Wenn sich der Nutzer bei einer Webanwendung wie z. B. SeaTable per SSO Verfahren anmelden möchte, sendet die Anwendung ihrerseits ein Token an den IdP, das mit dem bestehenden SSO Token abgeglichen wird. Kann der Nutzer identifiziert werden und ist er für die Anwendung freigegeben, validiert die SSO-Lösung das Authentifizierungstoken und der Nutzer erhält Zugriff auf die Anwendung.

Der ganze Login-Vorgang dauert nur wenige Sekunden, ohne dass der Nutzer etwas vom Authentifizierungprozess im Hintergrund mitbekommt. Loggt sich Ihr Mitarbeiter später bei einer anderen integrierten Anwendung ein, prüft diese zunächst, ob bereits ein gültiges Token vom IdP existiert. Wenn ja, **wird der Nutzer automatisch angemeldet**, ohne sich erneut einloggen zu müssen. Das ist das „Single" in Single Sign-On. Und ebenso gibt es auch einen Single Logout: Wenn sich der Nutzer von einer Webanwendung abmeldet, wird das Token invalidiert und auch alle anderen verknüpften Anwendungen abgemeldet.

## Warum sollten Unternehmen SSO implementieren? Die konkreten Vorteile

* **Eine zentrale Verwaltung statt Passwortsilos**: Statt Zugriffsrechte in verschiedenen Tools zu verwalten, managen Ihre IT-Verantwortlichen Rollen und Berechtigungen an einer zentralen Stelle. Das ist nicht nur ein Segen für Ihre IT-Mitarbeiter, sondern reduziert auch die Angriffsfläche und manuelle Fehler.
    
* **Größere Akzeptanz digitaler Transformationsprozesse**: Wenn der Umstieg auf neue Tools reibungslos funktioniert, ohne Passwort-Hickhack, ohne Login-Frust und Sicherheitsbedenken, akzeptieren Ihre Mitarbeiter Veränderungen schneller – und sparen nach Schätzungen etwa  30 Minuten Arbeitszeit pro Tag, in denen sie keine Passwörter eingeben oder zurücksetzen müssen. Schon nach zwei Wochen mit SSO-Anmeldung ist das ein ganzer Arbeitstag, der für produktive Aufgaben gewonnen ist. 
    
* **Größere IT-Sicherheit und Compliance**: Viele SSO-Lösungen erfordern Multi-Faktor-Authentifizierung und Audit-Logs zeigen lückenlos, wer wann auf welche Systeme zugegriffen hat.

* **Vermeiden von Schatten-IT**: Indem Mitarbeiter einfach und komfortabel auf genehmigte Anwendungen zugreifen können, verringert die IT die Nutzung nicht autorisierter und potenziell unsicherer  Tools. Dadurch kann SSO helfen, die Entstehung von [Schatten-IT-Strukturen]({{< relref "posts/schatten-it" >}}) zu verhindern. 

![Single Sign-On erhöht die IT-Sicherheit.](single-sign-on-it-security.png)    

## Was sind die gängigsten Single Sign-On Protokolle?

Die Sicherheit von SSO-Systemen basiert auf verschiedenen Protokollen, die den Austausch von Informationen zwischen Anwendung und Identity Provider regeln. Welches Protokoll für ein Unternehmen am geeignetsten ist, hängt stark von der IT-Umgebung und den Anforderungen ab. Die wichtigsten Protokolle stellen wir an dieser Stelle zum besseren Verständnis vor.

### SAML 2.0: Der Enterprise-Standard

SAML (Security Assertion Markup Language) dominiert seit Jahren Enterprise-Umgebungen und ist **der De-facto-Standard für unternehmensweites SSO** – und wird auch von der [Teamverwaltung in SeaTable]({{< relref "help/teamverwaltung/abonnement" >}}) unterstützt. Das SSO Token ist in diesem Fall eine XML-basierte Assertion – sozusagen ein digitaler Beglaubigungsbrief – die mit einem Zertifikat signiert wird. Die Vorteile von Single Sign On mit SAML sind erheblich:

* SAML ist browserbasiert und funktioniert nahtlos mit klassischen Unternehmensanwendungen.
    
* SAML unterstützt auch Single Logout – wenn sich ein Nutzer abmeldet, kann der IdP alle Sessions gleichzeitig beenden.
    
* Für regulierte Branchen wie öffentliche Verwaltung ist SAML wegen seiner audit-freundlichen Logs ein großer Pluspunkt.    

Aber SAML hat auch Nachteile:

* Das XML-Format ist gegenüber JSON schwer zu debuggen. 
    
* SAML ist nicht mobil-freundlich.
    
### OAuth 2.0: Modern und mobil-nativ

OAuth 2.0 wurde speziell als **SSO für die Cloud** designt und eignet sich für Umgebungen mit Microservices oder API-Verbindungen. Bekannt unter dem Motto „Sign in with Google" oder „Login with Facebook", gewährt OAuth delegierte Zugriffsrechte, ohne das eigentliche Passwort preiszugeben. Es ist mobil-nativ: Apps auf Smartphone und Tablet arbeiten reibungslos mit OAuth. Ähnlich wie mit SAML lassen sich auch mit diesem Protokoll granulare Zugriffsrechte festlegen.

Der Schwachpunkt: OAuth war ursprünglich nur für Authorization gedacht, nicht für Authentifizierung. Um das zu beheben, wurde OpenID Connect (OIDC) erfunden, das OAuth erweitert und echte Authentifizierung bietet. Ein weiteres Manko ist das **etwas aufwendigere Refresh-Token-Management**, um zu verhindern, dass User sich neu anmelden müssen, wenn ein Token abläuft.

![Single Sign-On erlaubt komfortable Anmeldungen.](single-sign-on-protokolle.png)

### LDAP: Der Oldie

LDAP (Lightweight Directory Access Protocol) ist älter als SAML und OAuth und bereits seit den 1990ern im Einsatz. LDAP speichert User-Verzeichnisse in einer Baumstruktur und wird klassisch von Microsoft Active Directory (AD) in Windows-Umgebungen genutzt. Wenn Sie also eine reine Windows-Umgebung mit On-Premises-Servern nutzen, ist diese Lösung ideal.

Ein echter Malus: **LDAP wurde vor der Cloud-Ära entwickelt** und ist nicht für Web-SSO optimiert.

### JWT: Der dezentralisierte Token

JSON Web Tokens (JWT) sind eher eine Technologie, nicht primär ein SSO-Protokoll, aber zunehmend zentral für moderne Authentifizierungen. Ein JWT ist ein signiertes, textbasiertes Token, das Aussagen über den Nutzer enthält – etwa User-ID, Rollen, Ablaufzeit. Da jedes Token alle Informationen enthält und JSON Web Tokens mobilfreundlich sind, **eignet sich diese Lösung gut für skalierbare, dezentrale Systeme und Microservices** – auch weil APIs eine JWT Authentication sehr leicht validieren können.

Natürlich gibt es auch hier einen Nachteil: JSON Web Tokens können nicht gelöscht werden und sind immer bis zum Ablauf gültig. Einem User z. B. nach einem Sicherheitsvorfall oder einer fristlosen Kündigung sofort Zugriffsrechte zu entziehen, ist nicht so einfach möglich.

### Kerberos: Der Windows-Netzwerk-Klassiker

Kerberos war Microsofts Antwort auf sichere Netzwerk-Authentifizierung in Windows-Domains. Es basiert auf einem Ticket-System: Der Client besorgt sich vom Kerberos-Server ein Ticket, das ihm Zugriff auf einen spezifischen Service ermöglicht, ohne das Passwort zu teilen. In einer reinen Windows-Domain können Sie Kerberos problemlos für die SSO Anmeldung nutzen.

Die strikte Ausrichtung auf On-Premises-Windows ist jedoch auch ein entscheidender Nachteil. Die Nutzung als Cloud SSO oder in hybriden Umgebungen funktioniert nur mit ergänzenden Lösungen. Und moderne Mobile-Apps? Dafür ist Kerberos nicht gemacht.  

## Welche Identity Provider für Single Sign-On Verfahren gibt es?

Wenn Sie das Single Sign-On Verfahren für Ihr Unternehmen nutzen möchten, brauchen Sie ein Identity & Access Management Tool, oder kurz einen Identity Provider. Dort legen Sie dann für jeden authentifizierten User die Anwendungen fest, auf die Zugriff gewährt wird. Inzwischen hat sich der Markt an entsprechenden Tools konsolidiert und auf wenige Anbieter reduziert, von denen wir hier die wichtigsten vorstellen:  

* **Okta**: Der cloud-native Marktführer mit über 7.000 vorkonfigurierten App-Integrationen. Okta glänzt durch **umfassende Features** (Adaptive MFA, Risk-basierte Policies, Analytics) und starken Support, sitzt jedoch in den USA und ist daher **datenschutzrechtlich nur eingeschränkt zu empfehlen**.  
    
* **Microsoft Entra ID** (ehemals Azure AD): Entra ist stark gewachsen und inzwischen **der größte Rivale von Okta**. Das System ist gratis für Microsoft 365-Nutzer und tief in Microsoft integriert. Als US-Lösung bestehen indes wie bei Okta **datenschutzrechtliche Bedenken**. Zudem ist die Integration von Apps außerhalb der Microsoft-Welt kompliziert.
    
* **Authentik**: Diese **Open-Source-Lösung** punktet auf ganzer Linie (und wird von uns bei SeaTable als IdP genutzt). Authentik **kann selbst gehostet werden, ist kostenlos nutzbar**, und unterstützt SAML, OAuth und LDAP Authentication. Der Nachteil: Das Setup braucht technisches Know-how, Support kommt nur aus der Community.
   
![Identity Provider ermöglichen Single Sign-On.](single-sign-on-identity-provider.png)
    
* **OneLogin**: OneLogin bietet solide Features und verfügt über eine **globale Infrastruktur mit Servern in Deutschland**. Der Nachteil: OneLogin unterstützt nur etwa halb so viele Apps wie Okta und bietet keinen kostenfreien Support.
    
* **Authelia**: Das Leichtgewicht unter den Open-Source-Lösungen für SSO Verfahren. Authelia **basiert auf Proxys** und ist ideal, wenn Sie nur eine schnelle, simple Lösung zur SSO Authentifizierung brauchen. Der große Nachteil: Authelia ist streng genommen **kein vollwertiger IdP**, sondern nutzt Forward-Auth via Reverse Proxys, statt eigenständiger Protokolle.    

## Ist Single Sign-On wirklich sicher?

Wenn ein SSO-System gehackt wird, haben Angreifer unter Umständen Zugriff auf alle Zugangsinformationen. Entsteht dadurch nicht ein unverhältnismäßig hohes Sicherheitsrisiko? Der Einwand ist durchaus berechtigt, lässt sich jedoch nicht eindeutig mit Ja oder Nein beantworten.

Keine Frage: Mit Single-Sign-On-Lösungen konzentrieren Sie das Risiko – ein gehackter IdP ist also verdammt ernst. SSO Verfahren bieten jedoch auch Vorteile, die dieses Risiko aufwiegen: 

1\. **Mit SSO sind weniger Passwörter im Umlauf**. Jedes dezentral gespeicherte Passwort erhöht das Risiko von Hacker-Einbrüchen.

2\. Der IdP kann verlangen, dass jeder Nutzer einen zweiten Authentifizierungs-Faktor nutzt. **Multi-Faktor-Authentifizierung (MFA) blockiert 99 % aller Phishing-Angriffe**.

3\. **SSO Token sind kurzlebig**. Ein gestohlenes SAML-Token oder JWT ist z. B. nur eine Stunde gültig und verfällt dann. Ein gestohlenes Passwort funktioniert unter Umständen noch monatelang. 

Also ja, die Nutzung von Single Sign-On schafft keine hundertprozentige Sicherheit, insbesondere, wenn kein MFA gefordert wird. Richtig umgesetzt bietet SSO jedoch **ein Schutzniveau, das mit dezentral verwalteten Passwörtern kaum flächendeckend erreicht wird**.

![Single Sign-On erfordert häufig MFA.](single-sign-on-mfa.png)

## SSO und Datenschutz – was müssen Nutzer beachten?

Single-Sign-On-Lösungen können zwar auch on-premises genutzt werden. Am häufigsten genutzt wird die SSO Authentifizierung indes in Cloud-Umgebungen. Verantwortliche IT Manager müssen daher bei der Auswahl einer entsprechenden Lösung immer **Datenschutz und Legal Compliance berücksichtigen**. Insbesondere die folgenden Punkte sind von Bedeutung:

1\. Welche Daten werden übertragen? Bei der Nutzung von SSO in der Cloud fließen Nutzer-Informationen vom IdP zur Anwendung. Diese Daten sind personenbezogen und daher datenschutzrechtlich relevant. Im Hinblick auf die europäische DSGVO wird es besonders kritisch, wenn der IdP in den USA sitzt und Daten dorthin transferiert. Wir empfehlen daher einen europäischen Identity Provider oder eine on-premises Lösung wie Authentik zu nutzen. 
    
2\. Achten Sie auf Consent und Datensparsamkeit. Die DSGVO verlangt, dass Nutzer einem Transfer Ihrer Daten an Dritte bewusst zustimmen müssen. Ein guter IdP macht daher transparent, welche Daten mit den verschiedenen Anwendungen geteilt werden.
    
3\. Arbeiten Sie mit sauber gepflegten Audit-Logs. DSGVO Art. 5 verpflichtet Unternehmen, die personenbezogene Daten erheben, zur Rechenschaft über die rechtmäßige und sichere Verarbeitung. Konkret bedeutet es in diesem Fall, dass Verantwortliche nachweislich tracken müssen, wer sich wann wo eingeloggt hat. Die gute Nachricht: In der Regel protokollieren Identity Provider dies automatisch pseudonymisiert. 
    
4\. Sie müssen Nutzer löschen können. DSGVO Art. 17 regelt das Recht auf Löschung. Unabhängig davon sollte es jedoch im Eigeninteresse jedes Unternehmen sein, Mitarbeitern nur Zugänge zu gewähren, die sie tatsächlich brauchen und die Zugänge ehemaliger Mitarbeiter zu sperren. Ein SSO-System sollte es Ihnen daher einfach machen, einen Nutzer zu löschen – wenn es sein muss auch unverzüglich. 

{{< youtube HUIJ8k2zlgY >}}

## SSO bei SeaTable

SeaTable ist mehr als nur eine **in Deutschland gehostete, DSGVO-konforme KI No-Code-Lösung** für flexible Datenbanken, KI-unterstützte Automatisierungen und App-Erstellung. Als Werkzeug zur digitalen Transformation von Geschäftsprozessen fügt es sich dank der **SeaTable API** bereits jetzt nahtlos in bestehende IT-Landschaften ein. 

Enterprise-Abonnenten von [SeaTable Cloud]({{< relref "pages/product/seatable-cloud" >}}) und Nutzer des on-premises Angebots [SeaTable Server]({{< relref "pages/product/seatable-server" >}}) können Login über Single-Sign On einrichten und somit für noch mehr Sicherheit sorgen. Die Integration ist unkompliziert und dauert nur wenige Minuten. Cloud-Nutzer müssen sich dafür bei einem Identity Provider anmelden, der SAML 2.0 unterstützt, das von SeaTable als Authentifizierungsprotokoll genutzt wird. In unserem [Hilfe-Artikel über Single Sign-On]({{< relref "help/teamverwaltung/sso/konfiguration" >}}) finden Sie alle Schritte beschrieben. Server-Kunden können auch LDAP oder JWT nutzen und finden ausführliche Informationen im [Admin-Handbuch](https://admin.seatable.com/configuration/authentication/ldap/).

{{< newsletter title="Bleiben Sie informiert" subtitle="" submit="Jetzt abonnieren" >}}

Erhalten Sie unseren **Newsletter** und bleiben Sie auf dem Laufenden, was IT-Sicherheit und Datenschutz angeht!

{{< /newsletter >}}

## FAQ – Single Sign-On

{{< faq "Was brauche ich, um SSO zu nutzen?" >}}
Sie benötigen lediglich eine geschäftliche E-Mail-Domain und einen Single Sign-On-Identity Provider wie Okta oder Authentik.
{{< /faq >}}

{{< faq "Lassen sich gewährte Single-Sign-On-Zugriffsrechte einfach widerrufen?" >}}
Grundsätzlich können Sie SSO-Tokens invalidieren und Nutzer löschen, sodass z. B. ehemalige Mitarbeiter keinen Zugriff mehr haben. Bei einer Authentifizierung über JWT kann das Token jedoch nicht sofort gelöscht werden, sondern bleibt bis zum festgelegten Ablauf aktiv.
{{< /faq >}}

{{< faq "Kann ich das Single Sign-On Verfahren auch mit mehreren Identity Providern nutzen?" >}}
Nein, das ist nicht möglich. Alle User für die von dir eingerichteten Domains müssen in demselben Identity Provider verwaltet werden.
{{< /faq >}}

{{< faq "Was ist ein SSO Token?" >}}
Ein SSO-Token ist eine Sammlung von Daten oder Informationen, die während des SSO-Verfahrens von einem System zu einem anderen weitergegeben wird. Die Tokens werden durch die Identity Provider digital signiert, so dass ein Token-Empfänger prüfen kann, ob es von einer vertrauenswürdigen Quelle stammt. Ein für diese digitale Signatur notwendiges Sicherheitszertifikat wird bei der initialen Konfiguration des IdP bereitgestellt.
{{< /faq >}}

{{< faq "Welche Identity Provider können mit SeaTable Cloud kommunizieren?" >}}
Wir empfehlen Ihnen Okta, Authentik oder Microsoft Entra ID zu nutzen.
{{< /faq >}}