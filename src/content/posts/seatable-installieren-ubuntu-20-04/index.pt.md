---
title: 'Instalar SeaTable Enterprise Edition sob Ubuntu Server 20.04 LTS - SeaTable'
description: 'Com Docker, a instalação do SeaTable Enterprise no Ubuntu 20.04 torna-se simples. Aprenda a preparar o ambiente, configurar o YAML e iniciar o serviço para obter uma nuvem colaborativa própria, ideal para dados sensíveis e privacidade.'
date: 2021-01-23
lastmod: '2024-01-19'
categories: 
    - 'product-features'
url: '/pt/instalacao-seatable-enterprise-ubuntu-20-04'
aliases:
    - /pt/seatable-enterprise-edition-unter-ubuntu-20-04-lts-installieren
seo:
    title: 'Instale SeaTable Enterprise no Ubuntu 20.04'
    description: 'Saiba como instalar o SeaTable Enterprise Edition no Ubuntu 20.04 em poucos minutos usando Docker e docker-compose.'
color: '#3b6bb1'
---

Graças a Docker , a instalação da SeaTable Enterprise Edition é muito simples e pode ser feita em apenas alguns momentos. Ubuntu Server como um sistema operativo Linux amplamente utilizado e bem documentado é uma excelente base para o SeaTable. Se já tem um servidor Ubuntu, pode aprender aqui como instalar o SeaTable nele em 10 minutos.

{{< warning headline="Este manual está desatualizado" text="Tenha em atenção que este manual está desatualizado. Consulte as instruções de instalação actualizadas disponíveis em [https://admin.seatable.com/](https://admin.seatable.com/)" />}}

## Requisitos

Para que o SeaTable seja criado de forma tão suave como aqui descrito, alguns pré-requisitos devem ser satisfeitos. Estes são:

- VServer / Servidor Dedicado com 4 núcleos, 8GB RAM e cerca de 10GB de memória para o sistema operativo Ubuntu, SeaTable e outros requisitos.
- Acesso de raiz ao servidor (via SSH ou consola)
- Subdomínio que se refere ao endereço IP do servidor através do registo A (IPv4) ou do registo AAAA (IPv6).
- Servidor acessível na porta 80 e 443 através do subdomínio
- Nenhum outro serviço ouve nos portos 80 e 443

É claro que deve planear mais do que o espaço do disco rígido acima mencionado, a fim de poder armazenar os seus próprios dados no suporte de dados, para além do sistema operativo e SeaTable. Em particular, se pretende organizar ficheiros em SeaTable, deve planear muito generosamente para espaço de armazenamento adicional.

Não é um pré-requisito, mas útil, se o servidor puder ser alcançado através de um endereço IPv4 estático. Isto maximiza a acessibilidade do servidor enquanto em movimento. Na Europa, existem ainda [redes móveis que ainda não suportam IPv6](https://www.datamate.org/status-der-ipv6-implementierung-in-mobilfunknetzen-in-dach/). O seu servidor SeaTable não pode ser alcançado através de tal rede se não tiver um endereço IPv4.

No caso da porta 80 e/ou 443 já estarem ocupadas no seu servidor, encontrará tudo o que precisa de saber para a instalação na sua situação no artigo [Instalando o SeaTable Enterprise no seu próprio servidor, atrás de um servidor web]({{< relref "posts/seatable-installieren-webserver" >}}).

Está pronto? Vamos lá! Assumimos que tem uma casca de raiz aberta no seu servidor.

## Preparação

Primeiro actualizamos o sistema para ter todos os pacotes actualizados:

`apt update   apt upgrade -y`

É claro que estes e todos os comandos seguintes devem ser executados com direitos de raiz, salvo especificação em contrário.

SeaTable utiliza docker-compor e precisa de instalar este pacote. Uma vez que está disponível através das fontes do pacote Ubuntu, o comando é suficiente:

`apt install docker-compose -y`

Os pacotes docker.io e containerd assim como numerosas bibliotecas Python3 fazem parte das dependências de docker-comporta. Estes são, portanto, instalados ao mesmo tempo. O sistema está pronto para o SeaTable!

## Descarregar SeaTable Enterprise

A imagem Docker da SeaTable Enterprise Edition está localizada num repositório em Docker Hub. Use o seguinte comando para iniciar o descarregamento da imagem SeaTable:

`docker pull seatable/seatable-ee:latest`

Passemos ao único tópico um pouco mais difícil na criação da SeaTable. Com as explicações alargadas, contudo, este passo também se torna facilmente realizável.

## Individualização de docker-compose.yml

Para introduzir esta secção, um pequeno conhecimento básico sobre a instalação da SeaTable: SeaTable fornece os seus serviços através de vários [Docker](https://www.docker.com/resources/what-container) contentores. Para além do próprio contentor SeaTable, no qual o servidor SeaTable funciona, há três outros contentores envolvidos. Especificamente, estes são a base de dados MariaDB, o serviço de cache Memcached e o servidor de dicionário redis.

O ficheiro docker-compose.yml, que será discutido dentro de momentos, é a receita utilizada por Docker para a instalação e configuração da SeaTable e dos outros recipientes. Contém definições centrais de segurança (por exemplo, a palavra-passe da base de dados) e permite-lhe adaptar a instalação aos seus próprios desejos e necessidades (por exemplo, configuração SSL/TLS).

Primeiro crie o directório com assento em /opt. Desde a instalação do contentord, o directório /opt já contém o directório com o mesmo nome. Depois descarregue o docker-compose.yml para este directório e abra o ficheiro com um editor de texto. O exemplo de código abaixo descreve o procedimento em pormenor. Utilizamos o editor de texto nano para editar o docker-compose.yml. Logicamente, porém, vim ou qualquer outro editor de texto também funcionará.

`mkdir /opt/seatable   cd /opt/seatable   wget -O "docker-compose.yml" "https://manual.seatable.io/docker/Enterprise-Edition/docker-compose.yml"   nano docker-compose.yml`

Este é o aspecto do ficheiro YAML após o download:  
![docker-compose.yml ficheiro](SeaTable_dockercompose.png)

![docker-compose.yml ficheiro](SeaTable_dockercompose.png)

À primeira vista, pode ver os quatro contentores que Docker configura quando a receita é executada: db, memcached, redis e seatable. Para cada contentor, a imagem a ser utilizada ("image") e o nome do contentor ("container_name") são declarados. O nome do contentor é o nome que pode ser utilizado mais tarde para gerir o contentor através da Consola Docker .

Além disso, cada contentor tem algumas configurações individuais, algumas das quais precisam agora da sua atenção.

No **contentor db**, é necessário alterar a palavra-passe da base de dados. Substitua "YOUR_PASSWORD" por uma palavra-passe alfanumérica de vários dígitos. Além disso, pode ajustar o caminho sob o qual o diretório /opt/seatable/mysql-data/ é disponibilizado no contentor seatable-mysql. Por defeito, este é o caminho /var/lib/mysql. Isto não é necessário.

O **contentor memcached** e o **contentor redis** não requerem quaisquer ajustes. Se já estiver a executar memcached ou redis, pode remover estes dois recipientes do ficheiro Compose. No entanto, para que o SeaTable funcione, terá de fazer ajustes manuais nos ficheiros de configuração mais tarde.

Os ajustes mais extensos devem ser efectuados no **contentor seatable**: Em primeiro lugar, a MYSQL_ROOT_PASSWORD deve ser introduzida aí. Caso contrário, o SeaTable não consegue comunicar com a base de dados. Por isso, introduza a palavra-passe especificada acima para o contentor db em "DB_ROOT_PASSWD".

Depois, é uma questão de decidir se a Let's Encrypt deve solicitar um certificado SSL para si e incluí-lo na configuração do servidor Web. Se quiser fazer isto - o que é provavelmente a recomendação para a maioria dos utilizadores - então altere o valor da chave SEATABLE_SERVER_LETSENCRYPT para "True" e introduza o subdomínio que está a utilizar para SEATABLE_SERVER_HOSTNAME. O Certbot do Let's Encrypt solicitará então um certificado SSL como parte da configuração e tê-lo-á em conta na configuração do servidor Web.

Pode deixar o fuso horário definido para Etc/UTC para a Europa Central. Se estiver fora da Europa Central, utilize os códigos de fuso horário habituais.

## Inicialização da base de dados

Depois do ficheiro YAML ter sido adaptado às suas necessidades, o passo seguinte é rubricar a base de dados. Para o fazer, introduza os seguintes comandos:

`cd /opt/seatable   docker-compose up`

O comando docker-compose executa a receita contida no ficheiro YAML: Várias imagens Docker são descarregadas do Docker Hub e extraídas. Primeiro MariaDB, depois Memcached, depois redis e finalmente o próprio SeaTable - na ordem prescrita no docker-compose.yml. Após o download, o contêiner de banco de dados seatable-mysql é iniciado. Você pode acompanhar as atividades na tela (veja abaixo). Quando o contentor seatable finalmente assume o controlo e a mensagem "This is an idle script (infinite loop) to keep container running." aparece no ecrã, pode cancelar o processo com a combinação de teclas CTRL + C.

Será que isto funcionou até agora? Então está muito próximo da sua própria instância de SeaTable! Caso contrário, consulte as dicas de resolução de problemas no final deste artigo.

## Lançamento do SeaTable

Execute docker-compose.yml novamente. Ao contrário da etapa anterior, docker-compose agora é executado em segundo plano ou "desanexado". Depois disso, o servidor SeaTable também pode ser iniciado de forma sentada no contêiner Docker . Por fim, só é necessário criar um utilizador administrador. Seu servidor SeaTable está pronto para suas tarefas!

`docker-compose up -d   docker exec -d seatable /shared/seatable/scripts/seatable.sh start   docker exec -it seatable /shared/seatable/scripts/seatable.sh superuser`

Após o último comando, ser-lhe-á pedido que introduza um endereço de correio electrónico e uma palavra-passe. Bravo, criou o primeiro utilizador no seu sistema SeaTable on-premises.

## Comissionamento

Chame agora o URL que especificou no docker-compose.yml em SEATABLE_SERVER_HOSTNAME. Irá aterrar na página de login do seu servidor SeaTable. Instalação bem sucedida!

Se votou para utilizar Let's Encrypt no site docker-compose.yml, então o seu pedido deve ser redireccionado directamente para https e assim a comunicação com o seu servidor deve ser encriptada. Se não, então deverá agora inserir o seu próprio certificado SSL. Copiar o certificado para a pasta /opt/seatable/ssl/ e ajustar a configuração do nginx do servidor web. Também tem de alterar os endereços de http para https nos ficheiros de configuração ccnet.conf, dtable_web_seetings.py e dtable_server_config.json. Depois disso, nginx, SeaTable e Memcached têm de ser reiniciados. Faz-se isto com estes três comandos:

`docker exec -it seatable /shared/seatable/scripts/seatable.sh restart   docker restart seatable-memcached   docker exec -it seatable /usr/sbin/nginx -s reload`

Pode saber mais sobre a integração do seu próprio certificado SSL no [manual SeaTable](https://manual.seatable.io/docker/Enterprise-Edition/Deploy%20SeaTable-EE%20with%20Docker/#ssltls).

![Menu de utilizadores na administração do sistema SeaTable](SeaTableEE_SystemAdministration_Users.png)

## Activação da licença SeaTable

Pode utilizar SeaTable Enterprise Edition com todas as funções sem uma licença paga com um máximo de três utilizadores - tanto privados como comerciais e também permanentes. Por esta razão, não é necessária uma licença para começar.

No entanto, se quiser criar mais de três utilizadores no SeaTable, o SeaTable recusar-se-á a fazê-lo. Pode obter uma licença do [nosso departamento de vendas]({{< relref "pages/contact" >}}). Pode encontrar mais informações sobre os preços da SeaTable Enterprise na nossa [página de preços]({{< relref "pages/prices" >}}).

Para activar a licença, guardar o ficheiro da licença, um ficheiro TXT, na pasta /opt/seatable/seatable-data/seatable e reiniciar o SeaTable:

`docker exec -d seatable /shared/seatable/scripts/seatable.sh restart`

Os utilizadores adicionais ficam então imediatamente disponíveis e afixados no painel de controlo.

## Resolução de problemas

Se algo correu mal durante a instalação, basta apagar o directório /opt/seatable e recomeçar. Mas tenha cuidado: os dados armazenados no SeaTable perder-se-ão.

Se se esqueceu da senha do seu administrador, execute o comando

`docker exec -it seatable /shared/seatable/scripts/seatable.sh superuser`

novamente. O comando cria outro utilizador com direitos de administrador. Se o comando produzir um erro, então a sua licença SeaTable não permite a criação de mais utilizadores. (Isto também se aplica ao modo de teste com um máximo de três utilizadores.) Neste caso, é necessário definir um utilizador para inactivo na base de dados MySQL e depois executar novamente o comando.
