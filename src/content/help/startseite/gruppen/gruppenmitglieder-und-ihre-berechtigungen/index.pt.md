---
title: 'Membros do grupo e suas permissões'
date: 2022-09-07
lastmod: '2023-08-14'
categories:
    - 'arbeiten-mit-gruppen'
author: 'nsc2'
url: '/pt/ajuda/membros-grupo-permissoes-seatable'
aliases:
    - '/pt/ajuda/gruppenmitglieder-und-ihre-berechtigungen'
seo:
    title: 'Membros de grupo SeaTable: permissões, funções e controle de acesso'
    description: 'Saiba quais direitos têm proprietários, administradores e membros em grupos SeaTable – com tabela de permissões e dicas de gestão.'
---

Dentro de um grupo SeaTable existem três funções diferentes: **Proprietário**, **Administrador** e **Membro**. Dependendo da sua função, que pode ser diferente de grupo para grupo, os utilizadores estão autorizados a realizar diferentes acções. A **tabela** seguinte dá-lhe uma visão geral das permissões que cada função tem.

![Gerir os membros do grupo](images/manage-group-members.png)

## Todas as permissões num relance

|                                                                                 | Proprietário                                                  | Admin                                                         | Membro                                                        |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| Criar novo grupo                                                                | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Trabalhar numa base                                                             | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| **Gestão de grupo**                                                             |                                                               |                                                               |                                                               |
| Renomear grupo                                                                  | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}                                   | {{< icon "circle-xmark" >}}                                   |
| Gerir membros                                                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}                                   |
| Grupo de transferência                                                          | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}                                   | {{< icon "circle-xmark" >}}                                   |
| Deixar o grupo                                                                  | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Eliminar grupo                                                                  | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}                                   | {{< icon "circle-xmark" >}}                                   |
| **Gestão de base num grupo**                                                    |                                                               |                                                               |                                                               |
| Adicionar uma base ou pasta                                                     | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}                                   |
| Editar base                                                                     | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}                                   |
| Gestão de Bases de um Grupo no Lixo                                             | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}                                   |
| Bases de lançamento                                                             | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}                                   |
| Adicionar Bases aos Favoritos                                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Eliminar bases                                                                  | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}                                   |
| Mover bases para uma pasta                                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}                                   |
| Copiar bases                                                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Bases de exportação                                                             | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Definir uma palavra-passe para uma base                                         | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}                                   |
| Acesso e restauro de snapshots de uma base                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Funções avançadas (fichas API, webhooks, gestão de anexos e ligação Seafile) | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}                                   |

{{< warning  headline="Atribuir autorizações" >}}

Se quiser atribuir uma permissão, as nossas instruções sobre a [atribuição de permissões num grupo]({{< relref "help/startseite/gruppen/berechtigungen-in-einer-gruppe-vergeben" >}}) ajudá-lo-ão certamente.

{{< /warning >}}

## Que grupos e bases vê?

Cada utilizador só pode ver os grupos dos quais é membro. Os grupos e bases aos quais não pertence não são, naturalmente, exibidos.
