---
title: 'Comparação entre as edições SeaTable Developer e Enterprise'
description: 'SeaTable está disponível em duas edições diferentes: A Enterprise Edition oferece toda a gama de funcionalidades. Também SeaTable Cloud se baseia na Enterprise Edition. A SeaTable Developer Edition tem funcionalidade limitada, mas destaca-se como base de dados flexível para projetos web. A Enterprise Edition requer uma licença paga, enquanto a Developer Edition pode ser utilizada gratuitamente e sem restrições.'
color: '#069214'
categories:
    - 'product-features'
date: 2022-02-03
lastmod: '2025-07-22'
author: 'cdb'
url: '/pt/comparacao-edicoes'
aliases:
    - /pt/editionsvergleich
seo:
    title: "Comparação entre as edições SeaTable Developer e Enterprise"
    description: "SeaTable oferece duas edições No-Code: Enterprise e Developer. Conheça os detalhes sobre funcionalidades e casos de uso da plataforma."
---

[SeaTable Server]({{< relref "pages/product/seatable-server" >}}) é SeaTable para o seu próprio servidor. Ao instalar SeaTable na sua própria infraestrutura, tem total controlo sobre a localização dos seus dados e sobre quem tem acesso aos mesmos. SeaTable é também recomendado para casos de utilização em que não queira retirar os seus dados das suas instalações. Pode também operar SeaTable Server exclusivamente na rede local, sem acesso através da Internet.

## Comparação rápida: SeaTable Developer Edition vs Enterprise Edition

### SeaTable Enterprise Edition

A SeaTable Enterprise Edition (SeaTable EE) é a solução [No-Code]({{< relref "posts/20250307-low-code" >}}) perfeita para equipas e organizações de qualquer dimensão que procuram uma base de dados No-Code poderosa e que não querem abdicar da plena [soberania dos dados]({{< relref "posts/digitale-souveraenitaet" >}}). Com permissões de partilha avançadas, automatizações, App Builder integrado e backend Big Data, os utilizadores podem implementar também casos de uso exigentes. Funcionalidades empresariais como autenticação externa (AD/LDAP, SAML), gestão de permissões baseada em funções, verificação de malware e log de auditoria irão agradar aos administradores.

Obtém gratuitamente uma licença SeaTable EE para até três utilizadores. Para mais utilizadores é necessária uma [licença paga]({{< relref "pages/prices" >}}). Graças ao [Docker Compose](https://admin.seatable.com), a instalação fica concluída em poucos minutos.

### SeaTable Developer Edition

A SeaTable Developer Edition (SeaTable DE) destina-se a programadores que queiram utilizar SeaTable como uma base de dados flexível e para quem as funcionalidades do frontend são de importância secundária. Nestes casos de uso, a SeaTable DE destaca-se pelo suporte de inúmeros tipos de dados, uma poderosa [REST API](https://api.seatable.com/) e aplicações para plataformas de automação conhecidas como Zapier, Make e n8n.

A SeaTable DE não requer qualquer licença paga. Pode encontrar as instruções de instalação [aqui](https://admin.seatable.com/installation/basic-setup/).

## Comparação funcional

|                                              | Developer Edition                                                                                          | Enterprise Edition                                                  |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **Plataforma e ambiente**                    |                                                                                                            |                                                                     |
| Sistema operativo do servidor                | Linux                                                                                                      | Linux                                                               |
| Método de instalação                         | Docker                                                                                                     | Docker                                                              |
| Imagens Docker                               | [Docker Hub](https://hub.docker.com/r/seatable/seatable-developer)                                         | [Docker Hub](https://hub.docker.com/r/seatable/seatable-enterprise) |
| **Licença**                                  |                                                                                                            |                                                                     |
| Tipo de licença                              | [híbrida (open source e proprietária)](https://admin.seatable.com/introduction/dtable-server-license/)     | [proprietária]({{< relref "pages/legal/terms-of-service" >}})       |
| Modelo de preço da licença                   | gratuito                                                                                                   | baseado no utilizador                                               |
| **Limites**                                  |                                                                                                            |                                                                     |
| Bases ilimitadas                             | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Tabelas ilimitadas                           | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Linhas ilimitadas                            | {{< icon icon="circle-check" class="text-seatable-orange" >}} (mas sem backend de arquivo)                 | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Armazenamento ilimitado                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Utilizadores ilimitados                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}} (licença necessária) |
| Versionamento (snapshots)                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| **Captura e edição de dados**                |                                                                                                            |                                                                     |
| 26 tipos de colunas                          | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| 6 tipos de vistas                            | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Vistas privadas                              | {{< icon "circle-xmark" >}}                                                                                | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Filtro                                       | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Agrupamento                                  | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Ordenação                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Formatação condicional                       | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Formulários web                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Registos partilhados                         | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Processamento de dados                       | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Estatísticas                                 | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Importação de CSV e XLSX                     | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Exportação para CSV e XLSX                   | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Notificações                                 | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Automatizações                               | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Backend Big Data                             | {{< icon "circle-xmark" >}}                                                                                | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Suporte JavaScript                           | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Suporte Python (instalação separada)         | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| **Colaboração**                              |                                                                                                            |                                                                     |
| Colaboração em tempo real                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Ligações externas                            | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Ligações de convite                          | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Partilha de bases                            | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Partilha de vistas                           | {{< icon "circle-xmark" >}}                                                                                | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Permissões de partilha individuais           | {{< icon "circle-xmark" >}}                                                                                | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Permissões de tabela                         | {{< icon "circle-xmark" >}}                                                                                | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Permissões de coluna                         | {{< icon "circle-xmark" >}}                                                                                | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Bloqueio de linhas                           | {{< icon "circle-xmark" >}}                                                                                | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| **Construção de aplicações**                 |                                                                                                            |                                                                     |
| App Builder universal                        | {{< icon "circle-xmark" >}}                                                                                | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| App Builder de consulta de dados             | {{< icon "circle-xmark" >}}                                                                                | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| **Plugins e extensões**                      |                                                                                                            |                                                                     |
| Mapas                                        | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Design de página                             | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Design de relatórios                         | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Consulta SQL                                 | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}}       |
| Integração Google Calendar                   | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}} (instalação separada necessária) |
| Integração ONLYOFFICE                        | {{< icon "circle-xmark" >}}                                                                                | {{< icon icon="circle-check" class="text-seatable-orange" >}} (instalação separada necessária) |


|                                               | Developer Edition                                             | Enterprise Edition                                            |
| --------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| **API e opções de integração**                |                                                               |                                                               |
| REST API                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Zapier                                        | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Make                                          | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| n8n                                           | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Integrately                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| **Branding e personalização**                 |                                                               |                                                               |
| Modelos próprios                              | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| URL próprio                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Logótipo próprio                              | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Logótipo no formulário web                    | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Imagem de capa no formulário web              | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Ocultar “Powered by”                          | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| **Gestão de utilizadores e permissões**       |                                                               |                                                               |
| Base de dados local de utilizadores           | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Autenticação de dois fatores                  | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Autenticação via AD/LDAP                      | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Single sign-on via SAML/OAuth2                | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Funções de utilizador                         | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| **Backend e escalabilidade**                  |                                                               |                                                               |
| Suporte S3                                    | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Suporte de clusters                           | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |

## Diferenças entre as versões

Tanto a SeaTable Enterprise Edition como a SeaTable Developer Edition podem ser facilmente descarregadas do Docker Hub:

- https://hub.docker.com/r/seatable/seatable-enterprise
- https://hub.docker.com/r/seatable/seatable-developer

**As edições diferem sobretudo na sua gestão de versões:**

A SeaTable Developer Edition disponibiliza apenas uma versão base, por exemplo **5.3.0**, baseada na primeira versão Enterprise correspondente. A Enterprise Edition é continuamente desenvolvida e mantida. Aí encontrará sempre a versão mais recente, como por exemplo **5.3.12**.

Os problemas identificados na SeaTable Developer Edition só são corrigidos com a versão principal seguinte (por exemplo, de 5.3.0 para 5.4.0).

## Diferenças de testes e suporte

A **SeaTable Enterprise Edition** é amplamente testada para garantir o máximo de estabilidade e ausência de erros. Em contrapartida, **não são realizados testes sistemáticos** para a **SeaTable Developer Edition**.

O **suporte pago** está disponível apenas para a Enterprise Edition; **não há suporte oficial** para a SeaTable Developer Edition.

Se tiver dúvidas sobre a SeaTable Developer Edition, recomendamos o uso do [Fórum da Comunidade SeaTable](https://forum.seatable.com). No entanto, esteja ciente de que a maioria das discussões refere-se à Enterprise Edition, que é mais usada e oficialmente suportada.
