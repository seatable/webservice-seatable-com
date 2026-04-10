---
title: 'Permissões de página numa aplicação'
date: 2023-05-03
lastmod: '2023-11-30'
categories:
    - 'universelle-apps'
author: 'nsc2'
url: '/pt/ajuda/permissoes-de-pagina-em-uma-app-universal'
aliases:
    - '/pt/ajuda/seitenberechtigungen-in-einer-universellen-app'
seo:
    title: 'Permissões de página em aplicação – guia SeaTable'
    description: 'Veja como definir e ajustar permissões nas aplicações do SeaTable, controlando acesso, edição e funções de cada usuário.'
---

{{< required-version "Enterprise" >}}

Para controlar com precisão **o acesso aos seus dados**, pode definir **permissões de página individuais** para cada página que criou numa aplicação. Pode editar as permissões através das definições da página.

{{< warning  type="warning" headline="Autorização de página predefinida" text="Quando cria **novas páginas** na sua aplicação, estas concedem inicialmente todos os direitos disponíveis a todos os utilizadores. No entanto, se quiser restringir os direitos de utilização, terá de ajustar as autorizações de página." />}}

## Definir e editar permissões de página

1. Abra uma **Base** à qual já tenha adicionado uma aplicação.
2. Clique em **Apps** no cabeçalho Base.
![Clique em Apps no cabeçalho Base](images/click-apps-in-the-base-header.jpg)
3. Coloque o cursor do rato sobre a aplicação e clique no **ícone de lápis** {{< seatable-icon icon="dtable-icon-rename" >}}.
![Clique no ícone de edição](images/add-page-to-universal-app-1.png)
4. Seleccione a **página** pretendida na navegação do lado esquerdo da página e clique no **símbolo da roda dentada** {{< seatable-icon icon="dtable-icon-set-up" >}}.
![Clique no ícone de edição](images/page-permissions-universal-app.png)
5. Defina as **permissões** pretendidas nas **definições da página** que aparecem no lado direito da página.
![Determinar as permissões da página](images/page-permissions.png)
6. As permissões de página definidas são **automaticamente** guardadas e **imediatamente** aplicadas.

## Que autorizações de página estão disponíveis

Pode definir as seguintes permissões de página:

- Quem pode acrescentar linhas?
- Quem está autorizado a editar linhas?
- Quem está autorizado a apagar linhas?
- Quem pode ver a página?

Nem todas as autorizações de página estão disponíveis para todos os [tipos de página]({{< relref "help/app-builder/seitentypen-in-universellen-apps/ueberblick" >}}). Veja esta visão geral:

| Page type                             | Add records                                                     | Modify records                                                  | Delete records                                                  | View page                                                       |
| ------------------------------------- | --------------------------------------------------------------- | ----------------------------------------------------------------| --------------------------------------------------------------- | --------------------------------------------------------------- |
| Table page                            | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Form page                             | {{< icon "circle-xmark" >}}                                     | {{< icon "circle-xmark" >}}                                     | {{< icon "circle-xmark" >}}                                     | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Gallery page                          | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Calendar page                         | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}                                     | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Custom page                           | {{< icon "circle-xmark" >}}                                     | {{< icon "circle-xmark" >}}                                     | {{< icon "circle-xmark" >}}                                     | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Kanban page                           | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Timeline page                         | {{< icon "circle-xmark" >}}                                     | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}                                     | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Query page                            | {{< icon "circle-xmark" >}}                                     | {{< icon "circle-xmark" >}}                                     | {{< icon "circle-xmark" >}}                                     | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Single record page                    | {{< icon "circle-xmark" >}}                                     | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}                                     | {{< icon icon="circle-check" class="text-seatable-orange" >}} |

## Que grupos de utilizadores pode autorizar

Para cada permissão, pode escolher entre as seguintes opções para limitar o grupo de pessoas: **Ninguém**, **Administradores**, **Funções específicas** e **Todos**.

![Opções de permissão de página disponíveis Quem pode ver a página?](images/page-permission-who-can-add-records.png)

Seleccione a opção **Funções específicas** para definir as suas próprias funções. Para tal, crie previamente novas **funções** para grupos de utilizadores individuais na [administração de utilizadores e funções]({{< relref "help/app-builder/einstellungen/benutzer-und-rollenverwaltung-einer-universellen-app" >}}), às quais pode atribuir permissões individualmente em cada página da aplicação.

![Definição de funções específicas que têm uma autorização correspondente](images/define-roles.png)
