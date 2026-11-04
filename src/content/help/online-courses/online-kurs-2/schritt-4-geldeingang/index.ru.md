---
title: 'Шаг 4: Кассовый чек'
date: 2024-09-19
lastmod: '2024-09-24'
categories:
    - 'online-kurs-2'
author: 'cdb'
url: '/ru/pomoshch/shag4-postuplenie-oplaty-seatable'
aliases:
    - '/ru/pomoshch/schritt-4-geldeingang'
seo:
    title: 'Шаг 4 курса SeaTable 2: поступление оплаты – автоматизация'
    description: 'На четвертом шаге вы создадите кнопку в SeaTable, чтобы фиксировать оплату и сразу отправлять письма с подтверждением участникам курса.'
---

После того как участники курса получат запрос на оплату по электронной почте, они переведут оплату за курс на ваш банковский счет. На этом этапе мы не будем дополнительно автоматизировать проверку входящих платежей. Тем не менее, имеет смысл интегрировать в вашу базу дополнительную кнопку, выполняющую две задачи:

1. Подтверждение получения оплаты и, таким образом, полной регистрации участника на курс.
2. Документирование процесса оплаты в базе.

## Несколько действий одной кнопкой

Это легко реализовать в SeaTable. В таблице добавьте `Registrations` добавляет новую кнопку, которая выполняет два действия:

- Отправьте участнику электронное письмо с подтверждением оплаты.
- Сайт `Payment Status` на `Paid` набор.

С вашими недавно приобретенными знаниями это не должно быть проблемой. Вы можете использовать следующий текст для своего письма:

> Subject: Payment Confirmation and Online Meeting Details
>
> Hey,
>
> Thank you for your payment! We’re excited to confirm that we’ve successfully received it.
>
> You can join the online meeting using the link below:  
> – https://meet.jit.si/{Course-ID}
>
> We look forward to seeing you there!  
> Best regards

## Справочная статья с дополнительной информацией

- [Настройка учетной записи электронной почты в базе]({{< relref "help/base-editor/weitere-optionen/einrichtung-eines-e-mail-kontos-in-einer-base" >}})
- [Настройка Gmail для отправки электронной почты через SMTP]({{< relref "help/integrationen/integrationen-innerhalb-von-seatable/gmail-fuer-den-versand-von-e-mails-per-smtp-einrichten" >}})
- [Кнопка]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}})
- [Отправка сообщения электронной почты с помощью кнопки]({{< relref "help/base-editor/schaltflaechen/eine-e-mail-per-schaltflaeche-verschicken" >}})
- [Отправка электронных писем с помощью автоматизации]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}})
