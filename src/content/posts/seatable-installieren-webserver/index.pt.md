---
title: Instalar o SeaTable Server no seu próprio servidor
description: Graças ao Docker, o SeaTable pode ser instalado em qualquer servidor Linux em poucos minutos. Saiba o que precisa, como funciona a instalação e por que o auto-hospedagem com o SeaTable é tão simples.
date: 2021-05-15
lastmod: 2025-03-27
categories:
    - product-features
url: /pt/instalacao-seatable-enterprise-servidor-web
aliases:
    - /pt/seatable-enterprise-auf-dem-eigenen-server-hinter-einem-webserver-installieren
    - /pt/instalacao-seatable-enterprise-ubuntu-20-04
    - /pt/seatable-enterprise-edition-unter-ubuntu-20-04-lts-installieren
color: '#265697'
seo:
    title: "Instalar o SeaTable Server: auto-hospedagem simplificada"
    description: "Instale o SeaTable Server no seu próprio servidor Linux em minutos com Docker e Caddy. Tudo sobre requisitos e processo de instalação."
---

Se prefere manter os seus dados no seu próprio servidor, o SeaTable Server é a solução ideal. Graças ao Docker, a instalação é simples e conclui-se em poucos minutos, independentemente da distribuição Linux que utilize.

O guia de instalação completo passo a passo encontra-se no SeaTable Admin Manual: **[Ir para o guia de instalação em admin.seatable.com](https://admin.seatable.com/installation/basic-setup/)**

De seguida, descubra o que precisa para a instalação, como funciona o processo e tudo o que o SeaTable como plataforma lhe pode oferecer.

## Porquê alojar o SeaTable no seu próprio servidor?

O SeaTable está disponível como solução cloud em [cloud.seatable.io](https://cloud.seatable.io). No entanto, muitas empresas e organizações preferem operar os seus dados na sua própria infraestrutura, seja por razões de proteção de dados, requisitos internos de conformidade ou simplesmente para manter o controlo total. O SeaTable Enterprise Edition torna isso possível: instala o SeaTable no seu próprio servidor e configura-o e opera-o de acordo com as suas necessidades.

## O que precisa

Os requisitos para uma instalação do SeaTable são simples:

- **Um servidor Linux** com pelo menos 4 núcleos de CPU, 8 GB de RAM e 10 GB de armazenamento livre (mais espaço para os seus dados)
- **Acesso root** ao servidor, por SSH ou consola
- **Um (sub)domínio** com DNS apontando para o endereço IP do seu servidor
- **Acessibilidade nas portas 80 e 443** através deste domínio

Não importa qual distribuição Linux utiliza: Ubuntu, Debian, Rocky Linux ou outra variante. Desde que o Docker funcione nela, o SeaTable funcionará. Um endereço IPv4 estático é útil mas não obrigatório. Maximiza a acessibilidade do seu servidor, já que algumas redes móveis ainda não suportam IPv6.

## O que está por baixo do capô

O SeaTable utiliza o Docker para executar os seus serviços através de múltiplos contentores. Para além do próprio SeaTable Server, existe uma base de dados MariaDB para armazenamento de dados, Redis para cache rápida e um proxy reverso que recebe os pedidos e os encaminha para o SeaTable. Todos estes componentes são geridos conjuntamente via Docker Compose: não precisa de se preocupar com cada um individualmente.

Por defeito, o SeaTable inclui o Caddy como proxy reverso. A grande vantagem do Caddy é que solicita e renova automaticamente os certificados HTTPS via Let's Encrypt. Se apontar o seu domínio para o servidor e abrir as portas 80 e 443, obtém conexões encriptadas sem qualquer configuração manual.

## Como funciona a instalação

A instalação completa divide-se em cinco passos:

1. **Instalar o Docker** – Se ainda não estiver presente, o Docker é configurado no servidor.
2. **Descarregar ficheiros Compose** – O SeaTable fornece ficheiros de configuração YAML prontos que definem todos os componentes necessários.
3. **Ajustar a configuração** – Num ficheiro central `.env`, introduz o seu domínio, palavras-passe e configurações básicas.
4. **Solicitar uma licença** – O SeaTable Enterprise é gratuito para até três utilizadores. Receberá um ficheiro de licença comodamente por e-mail.
5. **Iniciar o servidor** – Um único comando `docker compose up` inicia todos os contentores e o SeaTable está pronto a usar.

Todo o processo demora normalmente não mais do que 10 minutos.

## SeaTable atrás do seu próprio servidor web

O Caddy é a solução recomendada e mais simples, mas não a única. Se já tem um servidor web como nginx, Apache ou Traefik no seu servidor, também pode executar o SeaTable atrás dele. Nesse caso, desativa o proxy Caddy incluído e configura o seu servidor web existente como proxy reverso para o SeaTable. O servidor web encaminha os pedidos no domínio do SeaTable para o contentor do SeaTable, um procedimento comum que a maioria dos administradores já conhece.

Neste cenário, os certificados HTTPS ficam por sua conta, por exemplo via Let's Encrypt e Certbot ou um certificado SSL existente da sua organização. A documentação oficial descreve este cenário em detalhe.

## Atualizações fáceis

A arquitetura Docker também compensa após a instalação: as atualizações para uma nova versão do SeaTable fazem-se com poucos comandos. Descarrega a imagem Docker mais recente, reinicia os contentores e pronto. Os seus dados e configurações mantêm-se intactos.

## O que pode construir com o SeaTable

O SeaTable é muito mais do que uma base de dados. É uma plataforma que permite até a utilizadores sem experiência em TI criar soluções personalizadas em muito pouco tempo.

Um exemplo prático: uma administração universitária precisa de gerir candidaturas a bolsas de forma digital. Com o SeaTable, um colaborador cria uma base, gera um formulário web para a submissão de candidaturas e configura uma automatização com IA que extrai automaticamente informações relevantes dos documentos submetidos. As notificações mantêm a equipa informada sobre alterações de estado, e através de uma aplicação personalizada, os candidatos podem consultar o estado da sua candidatura a qualquer momento. Tudo isto é possível sem conhecimentos de programação e configura-se em poucas horas.

Seja gestão de projetos, inventário, CRM ou planeamento de eventos: as possibilidades são tão diversas quanto as necessidades da sua organização.

![CRM e vendas no SeaTable: oportunidades agrupadas por proprietário com estado, clientes e valor estimado](seatable-crm-example.png)

## Comece gratuitamente

Pode utilizar o SeaTable Enterprise Edition com até três utilizadores de forma permanente e gratuita, tanto para uso pessoal como comercial. A licença gratuita é enviada comodamente por e-mail.

Se precisar de mais utilizadores, pode adquirir licenças para 10, 25 ou 50 utilizadores diretamente na [página de preços do SeaTable]({{< relref "pages/prices" >}}). Para instalações maiores, contacte-nos através do [formulário de contacto]({{< relref "pages/contact" >}}).
