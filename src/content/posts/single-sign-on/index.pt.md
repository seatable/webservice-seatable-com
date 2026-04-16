---
title: 'Single Sign-On – Significado, vantagens e configuração'
description: 'Dezenas de palavras-passe, solicitações constantes de login, funcionários frustrados e equipas de TI que lidam diariamente com redefinições de palavras-passe. O Single Sign-On (SSO) elimina esse caos. Mas como funciona? Quais protocolos existem? E quão segura é realmente uma autenticação centralizada? Descubra por que o SSO é indispensável para as empresas modernas.'
seo:
    title: 'Autenticação de início de sessão único para maior segurança de TI'
    description: 'Single Sign-On explicado: como o SSO elimina a confusão de palavras-passe, maximiza a segurança de TI e economiza tempo valioso no login.'
date: 2026-02-02
url: '/pt/single-sign-on/'
categories:
    - 'best-practice'
tags:
    - 'Segurança informática e privacidade dos dados'
    - 'Transformação digital'
color: '#3962d2'
register:
   show: true 
--- 

## O que significa SSO? 

Os funcionários das empresas precisam alternar diariamente entre diferentes aplicações. Cada uma delas requer uma palavra-passe segura e única, que deve ser alterada regularmente – e o que isso significa exatamente varia de ferramenta para ferramenta. Os gestores de palavras-passe são uma forma comprovada de evitar que os seus funcionários se esqueçam constantemente das suas palavras-passe; no entanto, também exigem uma palavra-passe. Isso resulta em tickets desnecessários para o suporte técnico, perda de produtividade e também problemas de segurança. O Single Sign-On resolve esse problema, permitindo que os utilizadores **acessem várias aplicações ou sistemas através de um login centralizado**.

### Principais conclusões

* O Single Sign-On (SSO) **aumenta a segurança de TI** no seu [ITSM]({{< relref "pages/landing-pages/industry-solutions/software-development" >}}) através de uma autenticação centralizada de utilizadores e uma monitorização simplificada do acesso. 
* A utilização de procedimentos de Single Sign-On **aumenta a produtividade** através da redução dos registos de palavras-passe.
* Protocolos comuns, como SAML, OAuth e LDAP, permitem uma **integração flexível** em ambientes de nuvem e híbridos, como o SeaTable. 
* As soluções SSO baseadas na UE ou no local cumprem os requisitos do RGPD e evitam transferências de dados para países terceiros.

## Como funciona a autenticação SSO?

O processo SSO baseia-se essencialmente numa comunicação baseada em tokens entre a aplicação web e um **provedor de identidade central** (IdP).

![O Single Sign-On simplifica o login do utilizador.](single-sign-on.png)


* Os utilizadores são autenticados uma única vez num IdP – por exemplo, Okta ou [Authentik](https://goauthentik.io/). O administrador do sistema responsável concede então acesso a todos os serviços autorizados, sem que seja necessário introduzir novamente palavras-passe. 
* Após a autenticação SSO bem-sucedida, o IdP gera um token SSO – um tipo de certificado de segurança, por exemplo, como uma asserção SAML (baseada em XML) ou como um JWT (JSON Web Token) – e o armazena no sistema SSO ou no navegador da web. Os tokens SSO contêm informações sobre o utilizador em questão, por exemplo, o nome de utilizador e um endereço de e-mail. 
* Se o utilizador desejar iniciar sessão numa aplicação web, como o SeaTable, através do procedimento SSO, a aplicação envia um token para o IdP, que é comparado com o token SSO existente. Se o utilizador puder ser identificado e estiver autorizado para a aplicação, a solução SSO valida o token de autenticação e o utilizador obtém acesso à aplicação.

Todo o processo de login demora apenas alguns segundos, sem que o utilizador perceba o processo de autenticação em segundo plano. Se o seu colaborador iniciar sessão posteriormente noutra aplicação integrada, esta verificará primeiro se já existe um token válido do IdP. Se sim, **o utilizador é automaticamente registado**, sem precisar de fazer login novamente. Isso é o "único" no Single Sign-On. E também existe um Single Logout: quando o utilizador sai de uma aplicação web, o token é invalidado e todas as outras aplicações vinculadas também são desligadas.

## Por que razão as empresas devem implementar o SSO? As vantagens concretas

* **Uma gestão centralizada em vez de silos de palavras-passe**: em vez de gerir direitos de acesso em diferentes ferramentas, os seus responsáveis de TI gerem funções e autorizações num local central. Isto não é apenas uma vantagem para os seus colaboradores de TI, mas também reduz a superfície de ataque e os erros manuais.   
* **Maior aceitação dos processos de transformação digital**: quando a transição para novas ferramentas ocorre sem problemas, sem complicações com senhas, sem frustrações com logins e sem preocupações com segurança, os seus funcionários aceitam as mudanças mais rapidamente – e economizam, segundo estimativas, cerca de 30 minutos de trabalho por dia, nos quais não precisam introduzir ou redefinir senhas. Após apenas duas semanas com o login SSO, isso representa um dia inteiro de trabalho ganho para tarefas produtivas. 
    
* **Maior segurança de TI e conformidade**: muitas soluções SSO exigem autenticação multifatorial e os registos de auditoria mostram de forma completa quem acedeu a quais sistemas e quando.

* **Evitar a TI paralela**: ao permitir que os funcionários acessem aplicações aprovadas de forma fácil e conveniente, a TI reduz o uso de ferramentas não autorizadas e potencialmente inseguras. Assim, o SSO pode ajudar a impedir o surgimento de [estruturas de TI paralelas]({{< relref "posts/schatten-it" >}}). 

![O Single Sign-On aumenta a segurança de TI.](single-sign-on-it-security.png)    

## Quais são os protocolos de autenticação única mais comuns?

A segurança dos sistemas SSO baseia-se em vários protocolos que regulam a troca de informações entre a aplicação e o provedor de identidade. O protocolo mais adequado para uma empresa depende muito do ambiente de TI e dos requisitos. Apresentamos aqui os protocolos mais importantes para uma melhor compreensão.

### SAML 2.0: O Padrão Empresarial

A SAML (Security Assertion Markup Language) domina há anos os ambientes empresariais e é o padrão **de facto para SSO em toda a empresa** – sendo também suportada pela [gestão de equipas no SeaTable]({{< relref "help/teamverwaltung/abonnement" >}}). Neste caso, o token SSO é uma asserção baseada em XML – uma espécie de carta de certificação digital – assinada com um certificado. As vantagens do Single Sign On com SAML são consideráveis:

* O SAML é baseado em navegador e funciona perfeitamente com aplicações empresariais clássicas.
    
* O SAML também suporta o Single Logout – quando um utilizador se desconecta, o IdP pode encerrar todas as sessões simultaneamente.
    
* Para setores regulamentados, como a administração pública, o SAML é uma grande vantagem devido aos seus registos fáceis de auditar.  

No entanto, o SAML também apresenta desvantagens.:

* O formato XML é mais difícil de depurar do que o JSON. 
    
* O SAML não é compatível com dispositivos móveis.
    
### OAuth 2.0: Moderno e nativo para dispositivos móveis

O OAuth 2.0 foi projetado especificamente **como SSO para a nuvem** e é adequado para ambientes com microsserviços ou ligações API. Conhecido pelo lema «Sign in with Google» ou «Login with Facebook», o OAuth concede direitos de acesso delegados sem revelar a palavra-passe real. É nativo para dispositivos móveis: as aplicações em smartphones e tablets funcionam perfeitamente com o OAuth. Semelhante ao SAML, este protocolo também permite definir direitos de acesso granulares.

O ponto fraco: originalmente, o OAuth foi concebido apenas para autorização, não para autenticação. Para resolver isso, foi criado o OpenID Connect (OIDC), que amplia o OAuth e oferece autenticação real. Outra desvantagem é **a gestão de tokens de atualização, que é um pouco mais complexa**, para evitar que os utilizadores tenham de se registar novamente quando um token expira.

![O Single Sign-On permite um login conveniente.](single-sign-on-protokolle.png)

### LDAP: O clássico

O LDAP (Lightweight Directory Access Protocol) é mais antigo que o SAML e o OAuth e já está em uso desde a década de 1990. O LDAP armazena diretórios de utilizadores numa estrutura em árvore e é tradicionalmente utilizado pelo Microsoft Active Directory (AD) em ambientes Windows. Portanto, se utiliza um ambiente exclusivamente Windows com servidores locais, esta solução é ideal.

Uma desvantagem significativa: **o LDAP foi desenvolvido antes da era da nuvem** e não está otimizado para SSO na web.

### JWT: O token descentralizado

Os JSON Web Tokens (JWT) são mais uma tecnologia do que um protocolo SSO, mas estão a tornar-se cada vez mais essenciais para as autenticações modernas. Um JWT é um token assinado, baseado em texto, que contém informações sobre o utilizador, como ID do utilizador, funções e tempo de expiração. Como cada token contém todas as informações e os JSON Web Tokens são compatíveis com dispositivos móveis, **esta solução é adequada para sistemas escaláveis**, descentralizados e microsserviços, também porque as APIs podem validar facilmente uma autenticação JWT.

É evidente que existe também uma desvantagem: os JSON Web Tokens não podem ser eliminados e permanecem válidos até ao seu prazo de validade. Retirar imediatamente os direitos de acesso a um utilizador, por exemplo, após um incidente de segurança ou uma rescisão sem aviso prévio, não é tão simples.

### Kerberos: O clássico da rede Windows

O Kerberos foi a resposta da Microsoft para a autenticação segura de rede em domínios Windows. Baseia-se num sistema de bilhetes: o cliente obtém um bilhete do servidor Kerberos que lhe permite aceder a um serviço específico sem partilhar a palavra-passe. Num domínio Windows puro, pode utilizar o Kerberos sem problemas para o login SSO.

No entanto, o foco estrito no Windows local também é uma desvantagem significativa. A utilização como SSO na nuvem ou em ambientes híbridos só funciona com soluções complementares. E as aplicações móveis modernas? O Kerberos não foi concebido para isso. 

## Quais são os provedores de identidade disponíveis para o procedimento de autenticação única?

Se pretende utilizar o procedimento de autenticação única (Single Sign-On) na sua empresa, necessita de uma ferramenta de gestão de identidades e acessos, ou, resumidamente, de um provedor de identidades. Nessa ferramenta, define as aplicações às quais cada utilizador autenticado tem acesso. Entretanto, o mercado de ferramentas correspondentes consolidou-se e reduziu-se a poucos fornecedores, dos quais apresentamos aqui os mais importantes:  

* **Okta**: Líder de mercado nativo da nuvem com mais de 7.000 integrações de aplicações pré-configuradas. A Okta destaca-se por suas **funcionalidades abrangentes** (MFA adaptável, políticas baseadas em risco, análises) e suporte robusto; no entanto, está sediada nos EUA e, portanto, **sua recomendação em termos de proteção de dados é limitada**.  
    
* **Microsoft Entra ID** (anteriormente Azure AD): a Entra cresceu significativamente e é atualmente **o principal concorrente da Okta**. O sistema é gratuito para utilizadores do Microsoft 365 e está profundamente integrado na Microsoft. No entanto, como solução norte-americana, existem **preocupações relacionadas com a proteção de dados**, tal como no caso da Okta. Além disso, a integração de aplicações fora do ecossistema Microsoft é complexa.
    
* **Authentik**: Esta **solução de código aberto** é excelente em todos os aspetos (e é utilizada pela SeaTable como IdP). O Authentik **pode ser auto-hospedado, é gratuito** e suporta autenticação SAML, OAuth e LDAP. A desvantagem: a configuração requer conhecimentos técnicos, e o suporte é fornecido apenas pela comunidade.
      
![Os provedores de identidade permitem o login único.](single-sign-on-identity-provider.png)
    
* OneLogin: O OneLogin oferece funcionalidades sólidas e possui uma **infraestrutura global com servidores na Alemanha**. A desvantagem: o OneLogin suporta apenas cerca de metade das aplicações que o Okta e não oferece suporte gratuito.
    
* **Authelia**: A solução mais leve entre as soluções de código aberto para processos SSO. A Authelia **baseia-se em proxies** e é ideal se necessitar apenas de uma solução rápida e simples para autenticação SSO. A grande desvantagem: a Authelia não é, estritamente falando, **um IdP completo**, mas utiliza autenticação direta através de proxies reversos, em vez de protocolos independentes.    

## O Single Sign-On é realmente seguro?

Se um sistema SSO for invadido, os invasores podem ter acesso a todas as informações de acesso. Isso não representa um risco de segurança desproporcionalmente elevado? A objeção é totalmente válida, mas não pode ser respondida com um sim ou um não definitivo.

Não há dúvida: com as soluções de Single Sign-On, concentra-se o risco – portanto, um IdP invadido é um assunto extremamente sério. No entanto, os procedimentos SSO também oferecem vantagens que compensam esse risco: 

1\. **Com o SSO, há menos palavras-passe em circulação**. Cada palavra-passe armazenada de forma descentralizada aumenta o risco de invasões por hackers.

2\. O IdP pode exigir que cada utilizador utilize um segundo fator de autenticação. **A autenticação multifatorial (MFA) bloqueia 99% de todos os ataques de phishing**.

3\. **Os tokens SSO têm uma validade curta.** Por exemplo, um token SAML ou JWT roubado é válido apenas por uma hora e, em seguida, expira. Uma palavra-passe roubada pode continuar a funcionar por meses. 

Portanto, sim, o uso do Single Sign-On não oferece 100% de segurança, especialmente quando não é exigida a MFA. No entanto, quando implementado corretamente, o SSO oferece **um nível de proteção que dificilmente seria alcançado com senhas gerenciadas de forma descentralizada**.

![O Single Sign-On frequentemente requer MFA.](single-sign-on-mfa.png)

## SSO e proteção de dados – o que os utilizadores devem considerar?

As soluções de autenticação única (SSO) também podem ser utilizadas localmente. No entanto, a autenticação SSO é mais frequentemente utilizada em ambientes de nuvem. Por isso, os gestores de TI responsáveis devem sempre **considerar a proteção de dados e a conformidade legal** ao selecionar uma solução adequada. Os seguintes pontos são particularmente importantes:

1\. Que dados são transferidos? Ao utilizar o SSO na nuvem, as informações do utilizador fluem do IdP para a aplicação. Esses dados são pessoais e, portanto, relevantes em termos de proteção de dados. No que diz respeito ao RGPD europeu, torna-se particularmente crítico quando o IdP está localizado nos EUA e os dados são transferidos para lá. Recomendamos, portanto, a utilização de um provedor de identidade europeu ou uma solução local, como o Authentik. 
    
2\. Preste atenção ao consentimento e à economia de dados. O RGPD exige que os utilizadores concordem conscientemente com a transferência dos seus dados a terceiros. Um bom IdP torna, portanto, transparente quais os dados que são partilhados com as diferentes aplicações.
    
3\. Trabalhe com registos de auditoria bem mantidos. O Artigo 5.º do RGPD obriga as empresas que recolhem dados pessoais a prestar contas sobre o tratamento legal e seguro desses dados. Concretamente, isso significa, neste caso, que os responsáveis devem rastrear de forma comprovável quem se registou, quando e onde. A boa notícia: normalmente, os provedores de identidade registam isso automaticamente de forma pseudonimizada. 
    
4\. É necessário poder eliminar utilizadores. O artigo 17.º do RGPD regula o direito à eliminação. Independentemente disso, no entanto, deve ser do interesse de todas as empresas conceder aos funcionários apenas os acessos de que realmente necessitam e bloquear os acessos dos ex-funcionários. Um sistema SSO deve, portanto, facilitar a eliminação de um utilizador – se necessário, imediatamente. 

{{< youtube HUIJ8k2zlgY >}}

## SSO no SeaTable 

O SeaTable é mais do que apenas **uma solução de IA no-code, hospedada na Alemanha e em conformidade com o RGPD**, para bases de dados flexíveis, automatizações assistidas por IA e criação de aplicações. Como ferramenta para a transformação digital de processos empresariais, integra-se perfeitamente em ambientes de TI existentes graças à **API SeaTable**. 

Os assinantes empresariais do [SeaTable Cloud]({{< relref "pages/product/seatable-cloud" >}}) e os utilizadores da oferta local [SeaTable Server]({{< relref "pages/product/seatable-server" >}}) podem configurar o login através do Single-Sign On, garantindo assim ainda mais segurança. A integração é simples e leva apenas alguns minutos. Para isso, os utilizadores da nuvem devem se registrar em um provedor de identidade que suporte SAML 2.0, que é usado pelo SeaTable como protocolo de autenticação. No nosso [artigo de ajuda]({{< relref "help/teamverwaltung/sso/konfiguration" >}}) sobre o Single Sign-On, encontrará todas as etapas descritas. Os clientes do servidor também podem utilizar LDAP ou JWT e encontrar informações detalhadas no [manual do administrador](https://admin.seatable.com/configuration/authentication/ldap/).

{{< newsletter title="Mantenha-se informado" subtitle="" submit="Inscreva-se agora" >}}

Receba a nossa newsletter e mantenha-se atualizado sobre segurança de TI e proteção de dados.

{{< /newsletter >}}

## Perguntas frequentes – Autenticação única

{{< faq "O que é necessário para utilizar o SSO?" >}}
É necessário apenas um domínio de e-mail empresarial e um provedor de identidade de login único, como Okta ou Authentik.
{{< /faq >}}

{{< faq "É possível revogar facilmente os direitos de acesso concedidos através do Single Sign-On?" >}}
Em princípio, é possível invalidar tokens SSO e eliminar utilizadores, para que, por exemplo, ex-funcionários não tenham mais acesso. No entanto, em caso de autenticação via JWT, o token não pode ser eliminado imediatamente, permanecendo ativo até ao prazo de validade definido.
{{< /faq >}}

{{< faq "É possível utilizar o procedimento de autenticação única com vários provedores de identidade?" >}}
Não, isso não é possível. Todos os utilizadores dos domínios que criou devem ser geridos no mesmo provedor de identidade.
{{< /faq >}}

{{< faq "O que é um token SSO?" >}}
Um token SSO é um conjunto de dados ou informações que é transmitido de um sistema para outro durante o processo SSO. Os tokens são assinados digitalmente pelos provedores de identidade, de modo que o destinatário do token possa verificar se ele provém de uma fonte confiável. Um certificado de segurança necessário para essa assinatura digital é fornecido durante a configuração inicial do IdP.
{{< /faq >}}

{{< faq "Quais provedores de identidade podem se comunicar com o SeaTable Cloud?" >}}
Recomendamos que utilize o Okta, o Authentik ou o Microsoft Entra ID.
{{< /faq >}}