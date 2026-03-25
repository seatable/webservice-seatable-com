---
title: 'Instale o SeaTable Enterprise no seu próprio servidor por detrás de um servidor web - SeaTable'
description: 'Veja como instalar o SeaTable Enterprise mesmo com portas ocupadas: mude configurações de porta, ajuste o proxy nginx/Apache e ative SSL facilmente. Simplifique a implantação e garanta máxima segurança nos seus projetos.'
date: 2021-05-15
lastmod: '2023-07-11'
categories: 
    - 'product-features'
url: '/pt/instalacao-seatable-enterprise-servidor-web'
aliases:
    - /pt/seatable-enterprise-auf-dem-eigenen-server-hinter-einem-webserver-installieren
color: '#265697'
seo:
    title: 'Instalar SeaTable atrás de um webserver: passo a passo'
    description: 'Guia para instalar o SeaTable Enterprise atrás de outro servidor web usando proxy e SSL.'
---

No artigo [Instalando SeaTable Enterprise Edition sob Ubuntu Server 20.04 LTS]({{< relref "posts/seatable-installieren-ubuntu-20-04" >}}) explicamos a instalação padrão de SeaTable Enterprise num servidor com Ubuntu Linux. Na instalação padrão, o SeaTable é instalado num servidor em que nenhuma outra aplicação web está em execução. Mas e se as portas 80 e 443 já estiverem ocupadas por outro serviço como um servidor web nginx ou Apache? Respondemos a esta pergunta neste artigo. Como verá, a resposta é encantadoramente simples.

{{< warning headline="Este manual está desatualizado" text="Tenha em atenção que este manual está desatualizado. Consulte as instruções de instalação actualizadas disponíveis em [https://admin.seatable.com/](https://admin.seatable.com/)" />}}

## Requisitos

Os requisitos para a instalação de SeaTable atrás de um servidor web existente são idênticos aos da instalação padrão:

- VServer / Servidor Dedicado com pelo menos 4 núcleos, 8GB de RAM e 10GB de memória
- Acesso de raiz ao servidor (via SSH ou consola)
- Subdomínio que se refere ao endereço IP do servidor através do registo A (IPv4) ou do registo AAAA (IPv6).
- Servidor acessível na porta 80 e 443 através do subdomínio

## Preparação e download

Não só os pré-requisitos, mas também os primeiros passos são idênticos aos da instalação padrão: Primeiro a instalação de docker-compose, depois a extracção da imagem SeaTable de Docker Hub e finalmente a gravação do ficheiro docker-compose em formato YAML no directório /opt/seatable.

Utilize estes comandos para realizar estas acções:  
`apt update   apt upgrade -y   apt install docker-compose -y   docker pull seatable/seatable-ee:latest   mkdir /opt/seatable   cd /opt/seatable   wget -O "docker-compose.yml" "https://manual.seatable.io/docker/Enterprise-Edition/docker-compose.yml"`

SeaTable também pode ser criado num local diferente do directório /opt/seatable. No entanto, se quiser fazer isto, deve também guardar todos os outros ficheiros SeaTable neste outro local por razões de consistência. Uma vez que isto pode facilmente conduzir a erros, desaconselhamos a sua utilização.

## Individualização de docker-compose.yml

As instruções para a instalação padrão explicam a estrutura e função do ficheiro docker-compose. Isto não deve ser repetido aqui. Utilize [este link]({{< relref "posts/seatable-installieren-ubuntu-20-04" >}}) para saltar directamente para a parte relevante do artigo sobre a instalação padrão.

No ficheiro YAML, é agora necessário fazer alguns ajustes, por um lado para ter em conta as suas próprias exigências, e por outro lado para permitir o funcionamento por detrás de um servidor web.

Os ajustamentos necessários incluem em particular a palavra-chave da base de dados, que deve ser alterada no contentor db (MYSQL_ROOT_PASSWORD) e no contentor seatable (DB_ROOT_PASSWD). O URL sob o qual o SeaTable deve ser acessível deve também ser alterado. O valor SEATABLE_SERVER_HOSTNAME é utilizado para este fim. Entrar no domínio sem http:// ou https://.

Para além destas modificações, que também devem ser feitas para a instalação padrão, a porta HTTP e HTTPS também deve ser adaptada. A configuração dos portos do contentor com assento pode ser encontrada na secção com o mesmo nome. Os valores por defeito em SeaTables docker-compose.yml são:  
 `- "80:80" #HTTP port   - "443:443" #HTTPS port`  
O valor antes do cólon é o porto de contentores no anfitrião Docker , ou seja, o porto para o qual o procurador Docker ouve e que é encaminhado para o contentor. O segundo valor após os dois pontos é o porto dentro do contentor Docker para o qual os pedidos são encaminhados. Estes dois portos não têm de ser idênticos e nós fazemos uso desta propriedade.

Uma vez que os portos 80 e 443 já estão ocupados no servidor, os portos do servidor Docker devem ser alterados. Os portos no contentor, no entanto, podem e devem permanecer inalterados. Isto evita alterações desnecessárias aos ficheiros de configuração da SeaTable. Uma configuração alternativa dos portos poderia ter este aspecto:

 `- "880:80" #HTTP port   - "4443:443" #HTTPS port`

Os portos 880 e 4443 aqui escolhidos são portos alternativos populares para os portos 80 e 443. Outros números de portos também podem ser utilizados no seu lugar. Estes devem então ser tidos em conta na configuração do servidor web no anfitrião (ver abaixo).

Deixe o valor SEATABLE_SERVER_LETSENCRYPT definido para Falso. Esta função só pode ser utilizada com a instalação padrão.

## Inicialização da base de dados

Com o adaptado docker-compose.yml a base de dados de SeaTable pode agora ser rubricada. Os passos - como poderia ser de outra forma - são os da instalação padrão:

`cd /opt/seatable   docker-compose up`

Pode agora seguir em direto no ecrã como Docker processa as instruções no ficheiro YAML. Após algum tempo, as actividades param. A última mensagem é "Este é um script inativo (loop infinito) para manter o contentor a funcionar". Pare o processo neste ponto com a combinação de teclas CTRL + C.

## Configuração do acesso HTTP

Para que as chamadas para o SeaTable URL possam também aterrar no contentor SeaTable, o ficheiro de configuração do servidor web no anfitrião deve ser adaptado. Especificamente, os pedidos que chegam através do SeaTable URL e porto 80 devem ser encaminhados para o procurador Docker . Isto ouve - tal como definido no docker-compose - no porto 880.

Por exemplo, uma directiva que faz isto para nginx parece-se com isto:

`server {   listen 80;   listen [::]:80;   server_name seatable.example.com;`

location / {  
proxy_pass http://127.0.0.1:880;  
}  
}

(Forneceremos em devido tempo um bloco de código para Apache).

Após ajustar a configuração do servidor web, reinicie o servidor web para que a alteração seja efectiva.

Uma vez que a comunicação no interior do contentor de Docker não foi alterada, não é necessário fazer quaisquer ajustamentos aos vários ficheiros de configuração na pasta /opt/seatable/seatable-data/seatable/conf.

## Lançamento do SeaTable

Agora o SeaTable está pronto para entrar em funcionamento. Primeiro, inicie todos os contentores Docker novamente executando docker-compose.yml, desta vez no chamado modo "detached", depois chame o script SH para iniciar o SeaTable no contentor seatable e, finalmente, crie o primeiro utilizador administrador.

`docker-compose up -d   docker exec -d seatable /shared/seatable/scripts/seatable.sh start   docker exec -it seatable /shared/seatable/scripts/seatable.sh superuser`

Agora já pode chegar a Seatable via porto 80. Ao chamar o domínio SeaTable (aqui no exemplo seatable.example.com) chegará à página de login do seu servidor SeaTable.

A chamada para https://seatable.example.com ainda não funciona. O acesso encriptado deve agora ser estabelecido como passo final.

## Criação de acesso HTTPS

O procedimento para o estabelecimento do acesso HTTPS depende do certificado SSL/TLS utilizado. Se já tiver um certificado correspondente, por favor siga as instruções da Autoridade Certificadora à qual adquiriu o certificado SSL.

Se fizer parte da maioria e quiser gerir o seu certificado HTTPS utilizando Let's Encrypt, basta seguir as instruções no [site Certbot da Fundação Fronteira Electrónica](https://certbot.eff.org/).

![gerador de instruções certbot](certbot_instructions_generator.png)

No caso do nginx no Ubuntu 20.04, apenas quatro comandos são necessários para solicitar e incluir um certificado Let's Encrypt SSL:  
`sudo snap install core; sudo snap refresh core   sudo snap install --classic certbot   sudo ln -s /snap/bin/certbot /usr/bin/certbot   sudo certbot --nginx`

Depois de chamar o último comando, o menu interactivo Certbot é chamado. Seguir as instruções e tomar as decisões necessárias. Se os requisitos de Let's Encrypt forem cumpridos, o certificado é solicitado e integrado. Da próxima vez que o URL do SeaTable for chamado, a ligação é estabelecida através da porta 443 e HTTPS.

Se instruir a Certbot a alterar automaticamente a configuração do servidor web para incluir o certificado SSL solicitado, este (ou semelhante) terá este aspecto (ou semelhante) posteriormente, no caso do nginx:

`server {   listen 443 ssl; # managed by Certbot   listen [::]:443 ssl; # managed by Certbot   server_name seatable.example.com;`

ssl_certificate /etc/letsencrypt/live/seatable.example.com/fullchain.pem; # gerido por Certbot  
ssl_certificate_key /etc/letsencrypt/live/seatable.example.com/privkey.pem; # gerido por Certbot  
incluir /etc/letsencrypt/options-ssl-nginx.conf; # gerido por Certbot  
ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # gerido por Certbot

location / {  
proxy_pass http://127.0.0.1:880;  
}  
}

Caso tenha decidido não alterar a configuração do servidor web através do Let's Encrypt, então deve fazer esta modificação manualmente. Importante: Não esquecer o reinício obrigatório do servidor web depois.

Finalmente, a conversão para HTTPS deve também ser tida em conta em dois ficheiros de configuração da SeaTable. Especificamente, estes dois ficheiros de configuração estão localizados na pasta /opt/seatable/seatable-data/seatable-conf:

- ccnet.conf
- dtable_web_settings.py

Em ccnet.conf, o SERVICE_URL deve ser alterado de "http://" para "https://".

Em dtable_web_settings.py, todos os URL devem ser adaptados. Acrescentar um "s" depois de "http" em DTABLE_SERVER_URL, DTABLE_SOCKET_URL, DTABLE_WEB_SERVICE_URL e FILE_SERVER_ROOT para que todos os URL comecem por "https".

Agora reinicie o SeaTable e divirta-se com o SeaTable!
