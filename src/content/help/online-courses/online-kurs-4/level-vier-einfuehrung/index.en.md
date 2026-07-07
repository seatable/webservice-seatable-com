---
title: 'Level Four: Introduction'
date: 2026-07-02
lastmod: '2026-07-02'
categories:
    - 'online-kurs-4'
author: 'bha'
url: '/help/level-four-introduction'
aliases:
    - '/help/level-vier-einfuehrung'
seo:
    title: 'SeaTable Online Course Level 4: Automation and Integration'
    description: 'Automate your SeaTable processes and connect them to your tools: no-code automations, Python scripts, API, webhooks, n8n and AI document extraction, around a warehouse scenario.'
weight: 1
---

Welcome to the SeaTable Online Course Level 4!

In the previous courses you learned the basics (Level 1), built a complete business process (Level 2), and worked as a team on shared data (Level 3). So far, every action went through your own hands: you typed, you clicked, you updated. This course shifts register: you will learn to make SeaTable work for you, then to connect it to the rest of your tools. That is what this level is all about — automation and integration.

To make it concrete, you run a warehouse that receives deliveries from its suppliers. With every delivery, you have to check what arrives, compare it against what was announced, update the stock and alert the right person. An ideal sequence to discover, one building block at a time, everything SeaTable can automate and connect.

## Is this the right course for me?

This course is ideal for you if you:

- have completed the [Level 1]({{< relref "help/online-courses/online-kurs-1/level-eins-einfuehrung" >}}), [Level 2]({{< relref "help/online-courses/online-kurs-2/level-zwei-einfuehrung" >}}) and [Level 3]({{< relref "help/online-courses/online-kurs-3/level-drei-einfuehrung" >}}) online courses and want to go further.
- spend too much time on repetitive tasks that SeaTable could take care of on its own.
- want to connect SeaTable to your other tools — a management system, a notification service, a storage space.
- are not afraid of a little code: a few Python scripts turn up along the way, but they are always provided for you.

## What will I learn in this online course?

The through-line is a warehouse operation: receive a supplier delivery, validate it, update the stock and get notified. You start from a base that already holds your products and a delivery to process, and you equip it step by step.

Throughout the course, you will learn to:

- automate an action without writing a single line of code — a trigger, a condition, an action.
- write a short Python script for what automation alone cannot do.
- call SeaTable's API, and let an outside tool write to it in turn.
- send a notification to the outside world with a webhook.
- orchestrate a small workflow with n8n to archive a document.
- let artificial intelligence read a delivery note and extract its lines on its own.

By the end, you will have a complete toolkit to automate your processes and connect them to the outside world.

## An interactive course

Like the previous courses, you follow this one here, on the site. What is new is a companion: a plugin you add to your base and switch to at certain moments — to discover a feature, or to have what you just built checked. You set up an automation or a script by following the course, you open the plugin, you click `Verify`, and it checks whether the expected effect is really there in your data.

![The online-courses plugin open on the warehouse base, showing the current exercise and the verify button](images/lvl4-course-plugin.png)

Some steps, on the other hand, take you out of SeaTable for real — sending an actual notification to your phone, archiving an actual file in another service. For those, the plugin scores nothing: it simply tells you to trigger the action, then to go and see the result on the other side. That manual check is part of the lesson.

## What are the requirements?

To follow this course successfully, you will need:

1. **SeaTable**: any SeaTable system works. The easiest is a [free SeaTable Cloud account]({{< relref "pages/registration" >}}). Everything the course uses is available on the free plan, both on the cloud and self-hosted.
2. **The course plugin**: the online-courses plugin, to add to your base. We explain how to install it just before the first step. <!-- TODO: plugin install procedure / link -->
3. **A forum**: an [account on our community forum](https://forum.seatable.com/) if you would like a badge at the end of the course.
4. **Optional, for the webhook step**: you will send an external notification using [ntfy](https://ntfy.sh/). No account is needed and you can confirm receipt in your browser, but to receive it on your phone you will need to install the ntfy app from your app store.
5. **Optional, for the n8n step**: this step follows very well as a simple demonstration, with nothing to install. But if you want to carry it out yourself, you will need an [n8n](https://n8n.io/) account and a [Seafile](https://www.seafile.com/en/home/) account — two services offering a free trial with no credit card (Seafile is from the same family as SeaTable). Nothing to set up in advance: you will open them only if, once there, you decide to get your hands dirty.
6. **Browser**: we recommend Google Chrome.
7. **Language**: the course is available in several languages, but the quiz, screenshots and sample data are in English.

## How long does the course last?

The course takes **about an hour and a half**, but you go at your own pace. Breaks are possible at any time, and you decide how far to push the "going further" sections scattered along the way.

## How do I complete the course?

At the end of this course, you can test your knowledge with a quiz:

- The quiz is in English and mixes multiple-choice questions with tasks about the base you will have equipped throughout the course. <!-- TODO: quiz URL -->
- If you pass, you receive a badge for your forum profile, which makes your skills visible. <!-- TODO: forum badge URL -->

What are we waiting for? Let's go!
