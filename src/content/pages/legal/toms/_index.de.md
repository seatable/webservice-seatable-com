---
title: 'Technische & organisatorische Maßnahmen <br />gemäß Art. 32 DSGVO'
description: ''
seo:
    title: 'TOMs'
    description: '...'
date: 2025-10-16
version: '1.1.5'
type: 'legal'
url: '/de/technisch-organisatorische-massnahmen'
---

## Präambel

Unter Berücksichtigung des Stands der Technik, der Implementierungskosten und der Art, des Umfangs, der Umstände und der Zwecke der Verarbeitung sowie der unterschiedlichen Eintrittswahrscheinlichkeit und Schwere des Risikos für die Rechte und Freiheiten natürlicher Personen, hat die SeaTable GmbH geeignete technische und organisatorische Maßnahmen (TOM) getroffen, um ein dem Risiko angemessenes Schutzniveau der persönlichen Daten zu gewährleisten.

Diese Dokumentation enthält die ergriffenen TOMs. Die Darstellung der TOMs folgt den in Art. 32 Abs. 1 DSGVO namentlich genannten Maßnahmen. Diese gelten allgemein bzw. für die bei der Akenes SA (Exoscale) angemieteten Datenverarbeitungssysteme, auf denen der angebotene Online-Dienst betrieben wird, wenn es explizit erwähnt wird.

---

## 1. Pseudonymisierung und Verschlüsselung (Art. 32 Abs. 1 lit. a DSGVO)

| Technische Maßnahmen                  | Organisatorische Maßnahmen                                                                 |
| ------------------------------------- | ------------------------------------------------------------------------------------------ |
| Verschlüsselung von Datenbank-Backups | Zeitnahe Löschung personenbezogener Daten, insoweit andere Normen dem nicht entgegenstehen |

_Hinweis:_ Pseudonymisierung und die Verschlüsselung von Daten des Auftraggebers sind grundsätzlich nicht Gegenstand der zu erbringenden Leistung und wäre technisch auch nur mit massiver Funktionseinschränkung möglich.

---

## 2. Fähigkeiten zur Sicherstellung der Vertraulichkeit (Art. 32 Abs. 1 lit. b DSGVO)

### 2.1 Zutrittskontrolle

| Technische Maßnahmen                                         | Organisatorische Maßnahmen               |
| ------------------------------------------------------------ | ---------------------------------------- |
| Biometrische Zugangssperren und Protokollierung der Zutritte | Schlüsselregelung / Liste                |
| Türen mit Knauf Außenseite                                   | Besucher in Begleitung durch Mitarbeiter |
|                                                              | Sorgfalt bei Auswahl Reinigungsdienste   |

### 2.2 Zugangskontrolle

| Technische Maßnahmen                   | Organisatorische Maßnahmen                                                |
| -------------------------------------- | ------------------------------------------------------------------------- |
| Firewall in Router und Server          | Dedizierte Verwaltung von Nutzerberechtigungen                            |
| Verwendung von IP-Blocker              | Prozess-Dokumentation für Zugangsdeaktivierung bei Mitarbeiterausscheiden |
| Linux Betriebssystemen auf Servern     | Allgemeine Richtlinie Datenschutz                                         |
| Einsatz VPN bei Remote-Zugriffen       |                                                                           |
| Zentrale Benutzerverwaltung            |                                                                           |
| 2-Faktor Authentifizierung (2FA)       |                                                                           |
| Mindestkomplexität von Passwörtern     |                                                                           |
| Aktuelle Betriebssysteme               |                                                                           |
| Antivirenprogramm auf Windows Systemen |                                                                           |
| Lokale Firewall                        |                                                                           |

**Technische Maßnahmen (Exoscale) und organisatorische Maßnahmen (Exoscale)**

| Technische Maßnahmen (Exoscale)                                        | Organisatorische Maßnahmen (Exoscale) |
| ---------------------------------------------------------------------- | ------------------------------------- |
| Absicherung des Webzugriffs mit Captcha, IP-Blocker und optionaler 2FA | Dedizierte Administratoren            |
| Absicherung des API-Zugriffs mit IP-Blocker und optionaler 2FA         |                                       |
| Remote-Zugriff via SSH mit Zertifikat                                  |                                       |
| SSH-Hardening (z.B. no root-login)                                     |                                       |
| Überwachung SSH-Zugang mit IP-Blocker                                  |                                       |
| Software-Firewall auf Server                                           |                                       |
| Protokollierung der User-Logins                                        |                                       |
| Regelmäßige Software-Updates                                           |                                       |
| Verschlüsselung von Backups                                            |                                       |

### 2.3 Zugriffskontrolle

| Technische Maßnahmen                                                       | Organisatorische Maßnahmen                           |
| -------------------------------------------------------------------------- | ---------------------------------------------------- |
| Zentrale Berechtigungsverwaltung                                           | Einsatz Berechtigungskonzepte                        |
| Protokollierung von Zugriffen auf die Serverinfrastruktur                  | Minimale Anzahl an Administratoren                   |
| Passwortsafe mit dedizierter Berechtigungsverwaltung und Zugriffskontrolle | Verwaltung von Benutzerrechten durch Administratoren |

## 3. Fähigkeiten zur Sicherstellung der Integrität

_Art. 32 Abs. 1 lit. b DSGVO_

| Technische Maßnahmen                                                        | Organisatorische Maßnahmen                                                                        |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| Trennung von Produktiv- & Testumgebung                                      | Berechtigungskonzept                                                                              |
| Informationsaustausch über SSL-verschlüsselte Datenverbindung               | Nachvollziehbarkeit von Eingabe, Änderung und Löschung von Daten durch individuelle Benutzernamen |
| Einsatz von SSH, VPN sowie zertifizierter Fernwartungssoftware (TeamViewer) |                                                                                                   |
| Protokollierung der Zugriffe und Abrufe                                     |                                                                                                   |
| Manuelle oder automatisierte Kontrolle von Protokollen                      |                                                                                                   |

## 4. Fähigkeiten zur Sicherstellung der Verfügbarkeit und Belastbarkeit

_(Art. 32 Abs. 1 lit. b DSGVO)_

| Technische Maßnahmen                                             | Organisatorische Maßnahmen                                                      |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| Regelmäßige Systemwartungen                                      | Protokollierung der Systemwartungen                                             |
| Regelmäßige Datensicherungen                                     | Kontrolle des Datensicherungsvorgangs                                           |
| Firewalls                                                        | Regelmäßige Tests zur Datenwiederherstellung und Protokollierung der Ergebnisse |
| Redundante Datenspeicherung                                      | Datensicherung an sicheren Drittorten                                           |
| Unterbrechungsfreie Stromversorgung                              | Keine sanitären Anschlüsse im oder oberhalb des Serverraums                     |
| Penetrationstests durch professionelle IT-Sicherheitsunternehmen |                                                                                 |

## 5. Zeitnahe Datenwiederherstellung

_Art. 32 Abs. 1 lit. c DSGVO_

| Technische Maßnahmen         | Organisatorische Maßnahmen                      |
| ---------------------------- | ----------------------------------------------- |
| Regelmäßige Datensicherungen | Geeignete mündliche Instruktion der Mitarbeiter |
| Ersatzhardware vorrätig      | Handynummer des/der Admins bekannt              |
| LTE-Modem vorrätig           |                                                 |

## 6. Verfahren zur regelmäßigen Überprüfung, Bewertung und Evaluierung

_Art. 32 Abs. 1 lit. d DSGVO; Art. 25 Abs. 1 DSGVO_

| Technische Maßnahmen                                                                                      | Organisatorische Maßnahmen                                                                                           |
| --------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Zentrale Dokumentation aller Verfahrensweisen und Regelungen zum Datenschutz                              | Mitarbeiter geschult und auf Vertraulichkeit/Datengeheimnis verpflichtet                                             |
| Regelmäßige Überprüfung der Zugangsberechtigungen                                                         | Jährliche Sensibilisierung der Mitarbeiter                                                                           |
| Regelmäßige Überprüfung der Datenschutzbestimmungen und Bewertung der Angemessenheit der techn. Maßnahmen | Regelmäßige Überprüfung der Datenschutzbestimmungen und Bewertung der Angemessenheit der organisatorischen Maßnahmen |
|                                                                                                           | Disziplinarmaßnahmen im Falle einer Datenschutzverletzung                                                            |
