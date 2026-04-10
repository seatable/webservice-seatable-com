---
title: 'Разрешения страниц в приложении'
date: 2023-05-03
lastmod: '2023-11-30'
categories:
    - 'universelle-apps'
author: 'nsc2'
url: '/ru/pomoshch/prava-stranic-v-universalnom-prilozhenii'
aliases:
    - '/ru/pomoshch/seitenberechtigungen-in-einer-universellen-app'
seo:
    title: 'Права страниц в приложении – инструкция'
    description: 'Узнайте, как управлять правами страниц в приложениях SeaTable: роли, доступ, редактирование и просмотр данных.'
---

{{< required-version "Enterprise" >}}

Для точного контроля **доступа к данным** можно установить **индивидуальные разрешения** для каждой **страницы**, созданной в приложении. Редактирование разрешений осуществляется через настройки страницы.

{{< warning  type="warning" headline="Авторизация страницы по умолчанию" text="Когда Вы создаете **новые страницы** в своем приложении, они изначально предоставляют все доступные права всем пользователям. Однако, если Вы хотите ограничить права использования, Вам необходимо настроить авторизацию страниц." />}}

## Установка и редактирование прав доступа к страницам

1. Откройте **базу**, в которую вы уже добавили приложение.
2. Нажмите **Приложения** в заголовке База.
![Нажмите Приложения в заголовке База](images/click-apps-in-the-base-header.jpg)
3. Наведите курсор на приложение и нажмите на **значок карандаша** {{< seatable-icon icon="dtable-icon-rename" >}}.
![Нажмите на значок редактирования](images/add-page-to-universal-app-1.png)
4. Выберите нужную **страницу** из навигации в левой части страницы и нажмите на **символ шестеренки** {{< seatable-icon icon="dtable-icon-set-up" >}}.
![Нажмите на значок редактирования](images/page-permissions-universal-app.png)
5. Установите необходимые **разрешения** в **настройках страницы**, которые отображаются в правой части страницы.
![Определение прав доступа к странице](images/page-permissions.png)
6. Определенные разрешения страниц **автоматически** сохраняются и **немедленно** применяются.

## Какие полномочия для страниц доступны

Вы можете установить следующие разрешения страниц:

- Кто может добавлять строки?
- Кому разрешено редактировать строки?
- Кому разрешено удалять строки?
- Кто может видеть страницу?

Не все полномочия доступны для всех [типов страниц]({{< relref "help/app-builder/seitentypen-in-universellen-apps/ueberblick" >}}). Взгляните на этот обзор:

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

## Какие группы пользователей вы можете авторизовать

Для каждого разрешения можно выбрать один из следующих вариантов, чтобы ограничить группу людей: **Никто**, **Администраторы**, **Определенные роли** и **Все**.

![Доступные параметры разрешения страницы Кто может видеть страницу?](images/page-permission-who-can-add-records.png)

Выберите опцию **Конкретные роли**, чтобы определить собственные роли. Для этого предварительно создайте новые **роли** для отдельных групп пользователей в [администрировании пользователей и ролей]({{< relref "help/app-builder/einstellungen/benutzer-und-rollenverwaltung-einer-universellen-app" >}}), которым вы сможете назначать разрешения индивидуально на каждой странице приложения.

![Определение конкретных ролей, имеющих соответствующие полномочия](images/define-roles.png)
