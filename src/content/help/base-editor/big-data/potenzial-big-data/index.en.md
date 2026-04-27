---
title: 'Introduction to the possibilities of Big Data'
date: 2023-05-12
lastmod: '2024-05-13'
categories:
    - 'big-data'
author: 'cdb'
url: '/help/big-data-capabilities'
aliases:
    - '/help/potenzial-big-data'
seo:
    title: 'SeaTable Big Data: store millions of rows per base'
    description: 'Learn how SeaTable’s big data feature lets you manage and analyze millions of rows per base flexibly and securely.'

---

{{< required-version "Enterprise" >}}

SeaTable offers you two different storage options for the data records in a base: **By default**, a base can hold **a maximum of 100,000 rows**, which is sufficient for most use cases. If you need even more capacity, you can activate the **Big Data storage** with an [Enterprise subscription]({{< relref "help/teamverwaltung/abonnement/plus-oder-enterprise-abonnement-buchen" >}}), which can hold an almost unlimited number of rows . The fact that millions of rows are possible in one base makes SeaTable an alternative for classic SQL databases.

This article gives you an initial overview of the Big Data function in SeaTable, while you will find separate help articles for the various details.

![Big data backend in action](images/SeaTable-3.1-Base-Stats-with-Big-Data.png)

## A solution for every need

By using two storage solutions, you gain additional flexibility as a user. The standard SeaTable solution is ideal for **collaborative work** on projects, while the big data storage is ideal for data-intensive applications with automatic data collection (e.g. log files or static measured values).

Once you [have activated]({{< relref "help/base-editor/big-data/aktivieren-des-big-data-backends-in-einer-base" >}}), both solutions are available to you and you can move your data records back and forth between the standard solution and the big data storage. However, the advantage of unlimited storage of rows has the disadvantage [of limited collaborative capabilities]({{< relref "help/base-editor/big-data/einschraenkungen-in-der-nutzung-von-big-data" >}}).

## Separate views for the two memories

As already mentioned, the big data storage must be activated in a base. You can then create a new view with which you can access the entries in the big data storage. Further details on this big **data view** can be found [in this help article]({{< relref "help/base-editor/big-data/so-erstellen-sie-eine-big-data-ansicht" >}}).

## Infinite possibilities

The big data storage is a unique feature that you won't find in other no-code or low-code solutions. While other platforms and providers have hard caps and limits for the maximum number of rows , SeaTable does not restrict you in your work.

The big data function makes it possible to implement processes and applications that would not be possible with [Airtable]({{< relref "pages/landing-pages/alternatives/airtable-alternative" >}}), for example. Try it out for yourself. You will be amazed by the potential and the possibilities that big data storage offers you.
