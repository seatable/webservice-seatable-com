---
title: 'Члены группы и их полномочия'
date: 2022-09-07
lastmod: '2023-08-14'
categories:
    - 'arbeiten-mit-gruppen'
author: 'nsc2'
url: '/ru/pomoshch/chleny-gruppy-razresheniya-seatable'
aliases:
    - '/ru/pomoshch/gruppenmitglieder-und-ihre-berechtigungen'
seo:
    title: 'Члены группы в SeaTable: роли, разрешения и контроль доступа'
    description: 'Узнайте, какие права имеют владелец, админы и участники в группах SeaTable — с таблицей разрешений и советами по управлению.'
---

В группе SeaTable существует три различные роли: **Владелец**, **Администратор** и **Член**. В зависимости от роли, которая может быть различной в разных группах, пользователи имеют право выполнять различные действия. В следующей **таблице** приведен обзор разрешений, которыми обладает каждая роль.

![Управление членами группы](images/manage-group-members.png)

## Все разрешения с первого взгляда

|                                                                                        | Владелец                                                      | Администратор                                                 | Член                                                          |
| -------------------------------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| Создать новую группу                                                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Работа на базе                                                                         | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| **Управление группой**                                                                 |                                                               |                                                               |                                                               |
| Переименовать группу                                                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}                                   | {{< icon "circle-xmark" >}}                                   |
| Управление членами                                                                     | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}                                   |
| Трансферная группа                                                                     | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}                                   | {{< icon "circle-xmark" >}}                                   |
| Оставить группу                                                                        | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Удалить группу                                                                         | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}                                   | {{< icon "circle-xmark" >}}                                   |
| **Управление базой в группе**                                                          |                                                               |                                                               |                                                               |
| Добавить базу или папку                                                                | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}                                   |
| Редактировать базу                                                                     | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}                                   |
| Управление базами группы в корзине                                                     | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}                                   |
| Основания для выпуска                                                                  | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}                                   |
| Добавить базы в избранное                                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Удалить основания                                                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}                                   |
| Переместить базы в папку                                                               | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}                                   |
| Копировальные базы                                                                     | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Экспортные базы                                                                        | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Установка пароля для базы                                                              | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}                                   |
| Доступ к моментальным снимкам базы и их восстановление                                 | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Расширенные функции (API-токены, webhooks, управление вложениями и подключение Seafile) | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}                                   |

{{< warning  headline="Назначение полномочий" >}}

Если вы хотите назначить разрешение, вам наверняка помогут наши инструкции по [назначению разрешений в группе]({{< relref "help/startseite/gruppen/berechtigungen-in-einer-gruppe-vergeben" >}}).

{{< /warning >}}

## Какие группы и основания вы видите?

Каждый пользователь может видеть только те группы, членом которых он является. Группы и базы, к которым вы не принадлежите, конечно же, не отображаются для вас.
