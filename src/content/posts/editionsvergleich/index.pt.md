---
title: 'Comparação entre as edições Developer e Enterprise do SeaTable'
description: 'O SeaTable está disponível em duas edições diferentes. Enquanto a Enterprise Edition oferece toda a gama de funções e é, portanto, utilizada para o SeaTable Cloud e sistemas dedicados, a Developer Edition pode ser utilizada gratuitamente e é ideal para programadores como base de dados flexível.'
color: '#069214'
categories:
    - 'product-features'
lastmod: '2025-07-22'
url: '/pt/comparacao-edicoes'
aliases:
    - /pt/editionsvergleich
seo:
    title: "SeaTable Developer e Enterprise Edition em comparação"
    description: "SeaTable oferece duas edições No-Code auto-hospedadas: Enterprise e Developer. Conheça recursos e casos de uso de cada edição."
---

O SeaTable Server é SeaTable para o seu próprio servidor. Ao instalar o SeaTable na sua própria infra-estrutura, tem total controlo sobre a localização dos seus dados e sobre quem tem acesso aos mesmos. SeaTable também é recomendado para casos de utilização em que não queira retirar os seus dados do local. Também pode operar o SeaTable Server exclusivamente na rede local sem acesso através da Internet.

## O SeaTable Server está disponível em duas edições diferentes

### SeaTable Server Enterprise Edition

O SeaTable Server Enterprise Edition é a solução perfeita [sem código]({{< relref "posts/20250307-low-code" >}}) para equipas e organizações de todos os tamanhos que querem funcionalidade e controlo total de dados. Apenas a Edição Enterprise oferece a possibilidade de utilizar autenticação externa via LDAP ou SAML. Além disso, as permissões avançadas de partilha e as automatizações só se encontram nesta edição.  
Pode obter uma licença SeaTable Enterprise para um máximo de três utilizadores em qualquer altura. Encontrará o formulário de registo correspondente [nesta ligação]({{< relref "pages/product/seatable-server" >}}). A instalação é realizada de acordo com o [manual de administração](https://admin.seatable.com) utilizando Docker.

### SeaTable Server Developer Edition

O SeaTable Server Developer Edition destina-se principalmente a programadores que queiram utilizar o SeaTable como uma base de dados flexível e que não possam utilizar o frontend de forma alguma. Aqui, a Developer Edition pontua com a poderosa [API SeaTable](https://api.seatable.com/), as aplicações para as várias plataformas de automação e o apoio total de todos os tipos de colunas. A Edição Developer pode ser utilizada gratuitamente. As instruções de instalação podem ser encontradas [aqui](https://admin.seatable.com).

## Diferenças na comparação

|                                       | Edição Developer                                                                                 | Edição Empresarial                                                                               |
| ------------------------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| Plataforma e ambiente                 |                                                                                                  |                                                                                                  |
| Sistema operativo do servidor         | Linux                                                                                            | Linux                                                                                            |
| Método de instalação                  | Docker                                                                                           | Docker                                                                                           |
| Docker Imagens                        | [Docker Hub](https://hub.docker.com/r/seatable/seatable-developer)                               | [Docker Hub](https://hub.docker.com/r/seatable/seatable-enterprise)                               |
| Licença                               |                                                                                                  |                                                                                                  |
| Tipo de licença                       | [híbrido (fonte aberta e proprietário)](https://admin.seatable.com/introduction/requirements/#license)                | [propriedade]({{< relref "pages/legal/terms-of-service" >}})                                     |
| Modelo de preço da licença            | Sem custos                                                                                       | Baseado no utilizador                                                                            |
| Limites                               |                                                                                                  |                                                                                                  |
| Bases ilimitadas                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Tabelas ilimitadas                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Linhas ilimitadas                     | {{< icon icon="circle-check" class="text-seatable-orange" >}} **(mas sem backend de arquivo)**   | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Memória ilimitada                     | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Utilizadores ilimitados               | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}} **(licença necessária)**           |
| Versionamento (instantâneos)          | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Aquisição e processamento de dados    |                                                                                                  |                                                                                                  |
| 24 tipos de colunas                   | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Vistas                                | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Opiniões privadas                     |                                                                                                  | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Filtro                                | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Agrupamento                           | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Ordenação                             | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Formatação condicional                | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Formulários Web                       | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Conjuntos de dados partilhados        | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Processamento de dados                | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Estatísticas                          | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Importação de CSV e XLSX              | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Exportação para CSV e XLSX            | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Notificações                          | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Automatizações                        | {{< icon "circle-xmark" >}}                                                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Função de arquivo                     | {{< icon "circle-xmark" >}}                                                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Suporte JavaScript                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Apoio Python                          | {{< icon icon="circle-check" class="text-seatable-orange" >}} _(instalação separada necessária)_ | {{< icon icon="circle-check" class="text-seatable-orange" >}} _(instalação separada necessária)_ |
| Colaboração                           |                                                                                                  |                                                                                                  |
| Colaboração em tempo real             | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Ligações externas                     | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Ligações para convites                | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Lançamento da base                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Ver lançamento                        | {{< icon "circle-xmark" >}}                                                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Autorizações de libertação individual | {{< icon "circle-xmark" >}}                                                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Autorizações de tabelas               | {{< icon "circle-xmark" >}}                                                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Permissões de coluna                  | {{< icon "circle-xmark" >}}                                                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Bloqueio de linha                     | {{< icon "circle-xmark" >}}                                                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Plugins e extensões                   |                                                                                                  |                                                                                                  |
| Calendário                            | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Linha do tempo                        | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Galeria                               | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Kanban                                | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Mapas                                 | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Desenho da página                     | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Estatísticas avançadas                | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Consulta SQL                          | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Integração de ONLYOFFICE              | {{< icon "circle-xmark" >}}                                                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}} _(instalação separada necessária)_ |

---

|                                                        | Edição Developer                                              | Edição Empresarial                                            |
| ------------------------------------------------------ | ------------------------------------------------------------- | ------------------------------------------------------------- |
| API e opções de integração                             |                                                               |                                                               |
| REST API                                               | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Zapier                                                 | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Integromat                                             | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| n8n                                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Locoia                                                 | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Branding e personalização                              |                                                               |                                                               |
| Modelos próprios                                       | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| URL próprio                                            | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Logótipo próprio                                       | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Logótipo no formulário da web                          | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Imagem da capa no formulário da web                    | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| "Esconder "Powered by                                  | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Administração de utilizadores e gestão de autorizações |                                                               |                                                               |
| Base de dados de utilizadores locais                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Autenticação de 2 factores                             | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Autenticação via AD/LDAP                               | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Single sign-on via SAML                                | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Funções do utilizador                                  | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Backend e escalabilidade                               |                                                               |                                                               |
| Apoio S3                                               | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Apoio a clusters                                       | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |

## Diferenças entre as versões

Tanto a **SeaTable Enterprise Edition** quanto a **Developer Edition** podem ser facilmente baixadas do Docker Hub:

- https://hub.docker.com/r/seatable/seatable-enterprise
- https://hub.docker.com/r/seatable/seatable-developer

**A principal diferença entre as edições está nas versões disponibilizadas:**

A Developer Edition fornece apenas uma versão base, como por exemplo **5.3.0**, baseada na primeira versão correspondente da Enterprise Edition. Já a Enterprise Edition é continuamente desenvolvida e mantida. Assim, a versão mais recente, como **5.3.12**, está sempre disponível no Docker Hub.

Problemas identificados na Developer Edition só são corrigidos na próxima versão principal (por exemplo, da 5.3.x para a 5.4.0).

## Diferenças de testes e suporte

A **SeaTable Enterprise Edition** é amplamente testada para garantir o máximo de estabilidade e ausência de erros. Em contrapartida, **nenhum teste sistemático** é realizado para a **Developer Edition**.

O **suporte pago** está disponível apenas para a Enterprise Edition; **não há suporte oficial** para a Developer Edition.

Se tiver dúvidas sobre a Developer Edition, recomendamos o uso do [Fórum da Comunidade SeaTable](https://forum.seatable.com). No entanto, esteja ciente de que a maioria das discussões refere-se à Enterprise Edition, que é mais usada e oficialmente suportada.
