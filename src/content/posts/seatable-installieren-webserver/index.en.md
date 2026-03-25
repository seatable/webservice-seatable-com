---
title: 'Install SeaTable Enterprise on your own server behind a web server - SeaTable'
description: 'Need to install SeaTable but ports are in use by another web server? This guide walks you through custom ports, nginx/Apache proxy configs, database tweaks, and SSL certificates for secure, seamless deployment of SeaTable Enterprise on your own infrastructure.'
date: 2021-05-15
lastmod: '2023-07-11'
categories: 
    - 'product-features'
url: '//seatable-enterprise-installation-server-webserver'
aliases:
    - /seatable-enterprise-auf-dem-eigenen-server-hinter-einem-webserver-installieren
seo:
    title: 'Install SeaTable Behind a Web Server: Step-by-Step Guide'
    description: 'Learn to securely deploy SeaTable Enterprise behind an existing web server—ports, proxies & SSL setup made easy.'
color: '#265697'
---

In the article [Installing SeaTable Enterprise Edition under Ubuntu Server 20.04 LTS]({{< relref "posts/seatable-installieren-ubuntu-20-04" >}}) we explained the standard installation of SeaTable Enterprise on a server with Ubuntu Linux. In the standard installation, SeaTable is installed on a server on which no other web applications are running. But what if ports 80 and 443 are already occupied by another service such as an nginx or Apache web server? We will answer this question in this article. As you will see, the answer is delightfully simple.

{{< warning headline="This manual is outdated" text="Kindly be aware that this manual is outdated. Refer to the updated installation instructions available at [https://admin.seatable.com/](https://admin.seatable.com/)" />}}

## Requirements

The requirements for installing SeaTable behind an existing web server are identical to those for the standard installation:

- VServer / Dedicated Server with at least 4 cores, 8GB RAM and 10GB memory
- Root access to the server (via SSH or console)
- Subdomain that refers to the IP address of the server via A-record (IPv4) or AAAA-record (IPv6).
- Server accessible on port 80 and 443 via the subdomain

## Preparation and download

Not only the prerequisites, but also the first steps are identical to those of the standard installation: First the installation of docker-compose, then the pull of the SeaTable image from Docker Hub and finally the saving of the docker-compose file in YAML format in the directory /opt/seatable.

With these commands you perform these actions:  
`apt update   apt upgrade -y   apt install docker-compose -y   docker pull seatable/seatable-ee:latest   mkdir /opt/seatable   cd /opt/seatable   wget -O "docker-compose.yml" "https://manual.seatable.io/docker/Enterprise-Edition/docker-compose.yml"`

SeaTable can also be created in a location other than the /opt/seatable directory. If you want to do this, however, you should also store all other SeaTable files in this other location for reasons of consistency. Since this can easily lead to errors, we advise against it.

## Customization of the docker-compose.yml

The instructions for the standard installation explain the structure and function of the docker-compose file. This should not be repeated here. [This link]({{< relref "posts/seatable-installieren-ubuntu-20-04" >}}) will take you directly to the relevant part of the article on the standard installation.

In the YAML file, it is now necessary to make a few adjustments, on the one hand to take into account your own requirements, and on the other hand to enable operation behind a web server.

The necessary adjustments include in particular the database password, which must be changed in the container db (MYSQL_ROOT_PASSWORD) and in the container seatable (DB_ROOT_PASSWD). The URL under which SeaTable is to be accessible must also be changed. The value SEATABLE_SERVER_HOSTNAME is used for this purpose. Enter the domain without http:// or https://.

In addition to these modifications, which must also be made for the standard installation, the HTTP and HTTPS port must also be adapted. The configuration of the ports of the seatable container can be found in the section with the same name. The default values in SeaTables docker-compose.yml are:  
 `- "80:80" #HTTP port   - "443:443" #HTTPS port`  
The value before the colon is the container port on the Docker host, i.e. the port to which the Docker proxy listens and which is forwarded to the container. The second value after the colon is the port within the Docker container to which the requests are forwarded. These two ports do not have to be identical and we make use of this property.

Since ports 80 and 443 are already occupied on the server, the ports on the Docker host must be changed. The ports in the container, however, can and should remain unchanged. This avoids unnecessary changes to the SeaTable configuration files. An alternative configuration of the ports could look like this:

 `- "880:80" #HTTP port   - "4443:443" #HTTPS port`

The ports 880 and 4443 chosen here are popular alternative ports for port 80 and 443. Other port numbers can also be used in their place. These must then be taken into account instead when configuring the web server on the host (see below).

Leave the value SEATABLE_SERVER_LETSENCRYPT set to False. This function can only be used with the standard installation.

## Initialisation of the database

With the adapted docker-compose.yml the database of SeaTable can now be initialised. The steps - how could it be otherwise - are those of the standard installation:

`cd /opt/seatable   docker-compose up`

On the screen, you can now watch live how Docker processes the instructions in the YAML file. After a while, the activities come to a halt. The last message is "This is an idle script (infinite loop) to keep container running." Stop the process at this point by pressing CTRL + C.

## Setting up HTTP access

To ensure that calls to the SeaTable URL also end up in the SeaTable container, the configuration file of the web server on the host must be adapted. Specifically, the requests that come in via the SeaTable URL and port 80 must be forwarded to the Docker proxy. This listens - as defined in the docker-compose - on port 880.

For example, a directive that does this for nginx looks like this:

`server {   listen 80;   listen [::]:80;   server_name seatable.example.com;`

location / {  
proxy_pass http://127.0.0.1:880;  
}  
}

(We will provide a code block for Apache in due course).

After adjusting the web server configuration, restart the web server to make the change effective.

Since the communication within the Docker container seatable is unchanged, no adjustments have to be made to the various configuration files in the folder /opt/seatable/seatable-data/seatable/conf.

## Launch of SeaTable

Now SeaTable is ready to go live. First, start all Docker containers again by executing docker-compose.yml, this time in the so-called "detached" mode, then call the SH script to start SeaTable in the seatable container and finally create the first admin user.

`docker-compose up -d   docker exec -d seatable /shared/seatable/scripts/seatable.sh start   docker exec -it seatable /shared/seatable/scripts/seatable.sh superuser`

Now you can already reach Seatable via port 80. By calling the SeaTable domain (here in the example seatable.example.com) you will get to the login page of your SeaTable server.

Calling up https://seatable.example.com does not work yet. Encrypted access must now be set up as a final step.

## Setting up HTTPS access

The procedure for setting up HTTPS access depends on the SSL/TLS certificate used. If you already have a corresponding certificate, please follow the instructions of the Certificate Authority from which you purchased the SSL certificate.

If you are part of the majority and want to manage your HTTPS certificate using Let's Encrypt, just follow the instructions on the [Certbot website of the Electronic Frontier Foundation](https://certbot.eff.org/).

![certbot instructions generator](certbot_instructions_generator.png)

In the case of nginx on Ubuntu 20.04, only four commands are necessary to request and include a Let's Encrypt SSL certificate:  
`sudo snap install core; sudo snap refresh core   sudo snap install --classic certbot   sudo ln -s /snap/bin/certbot /usr/bin/certbot   sudo certbot --nginx`

After calling up the last command, the interactive Certbot menu is called up. Follow the instructions and make the necessary decisions. If the requirements for Let's Encrypt are met, the certificate is requested and integrated. The next time the URL of SeaTable is called up, the connection is established via port 443 and HTTPS.

If you instruct Certbot to automatically change the web server configuration to include the requested SSL certificate, it will look like this (or similar) afterwards in the case of nginx:

`server {   listen 443 ssl; # managed by Certbot   listen [::]:443 ssl; # managed by Certbot   server_name seatable.example.com;`

ssl_certificate /etc/letsencrypt/live/seatable.example.com/fullchain.pem; # managed by Certbot  
ssl_certificate_key /etc/letsencrypt/live/seatable.example.com/privkey.pem; # managed by Certbot  
include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot  
ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

location / {  
proxy_pass http://127.0.0.1:880;  
}  
}

In case you have decided not to change the web server configuration by Let's Encrypt, you have to do this modification manually. Important: Do not forget the obligatory web server restart afterwards.

Finally, the conversion to HTTPS must also be taken into account in two configuration files of SeaTable. Specifically, these two configuration files are located in the folder /opt/seatable/seatable-data/seatable/conf:

- ccnet.conf
- dtable_web_settings.py

In ccnet.conf the SERVICE_URL must be changed from "http://" to "https://".

In the dtable_web_settings.py all URLs must be adapted. For DTABLE_SERVER_URL, DTABLE_SOCKET_URL, DTABLE_WEB_SERVICE_URL and FILE_SERVER_ROOT, add an "s" after the "http" so that all URLs start with "https".

Restart SeaTable now and have fun with SeaTable!
