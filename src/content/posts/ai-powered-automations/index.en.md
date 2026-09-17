---
title: 'AI powered automations: The highlight of SeaTable 6.0'
description: 'With SeaTable 6.0, AI powered automations make their way into the cloud. Benefit from intelligent process automation, full GDPR compliance, and maximum data sovereignty thanks to our own AI server in Germany.'
date: '2025-09-30'
lastmod: '2025-10-31'
url: '/ai-automations-data-privacy'
seo:
    title: 'AI made in Europe: SeaTable brings secure AI powered automations to the cloud'
    description: 'Experience AI-powered automation with SeaTable 6.0 – secure cloud solutions combining innovation and German data privacy.'
categories:
    - 'product-features'
tags:
    - 'IT Security & Data Privacy'
    - 'IT Processes'
    - 'Digital Transformation'
    - 'Artificial Intelligence'
color: '#f2d1e3'
register:
   show: true
---

October 1, 2025 marks a special moment for us at SeaTable: the release of version 6.0. And this version is a big step forward. With the new **AI powered automations**, we are opening a whole new chapter – one that will noticeably change everyday work in companies.

Automations have always been a core part of SeaTable. They help standardize recurring processes and simplify workflows. But now we're taking the decisive next step: we're combining our automations with artificial intelligence (AI). Suddenly, processes can be not only _automated_ but also _intelligently_ controlled. Invoices that are automatically entered into tables, emails that are sorted and forwarded based on content, or long texts that are condensed to the essentials in seconds – all of this is now reality with SeaTable.

## Why we operate our own AI server

Of course, you could simply rely on the services of well-known AI providers. Many software solutions do exactly that: they integrate an American model, send their customers’ data there – often without disclosing that this data is not only processed but potentially used to train the next generation of models. At first, this sounds convenient, but from a data protection perspective, it is a nightmare: sensitive company data ends up somewhere where control is lost.

How real these risks are was recently demonstrated by a much-discussed incident at Samsung in 2023: employees had entered confidential source code and internal notes into ChatGPT to get support with their work. Since OpenAI stores these inputs according to its own terms of use and may use them for training, sensitive trade secrets suddenly resided with an external US provider – a loss of control with incalculable consequences. Samsung then stopped the use of ChatGPT in the company and is now exploring its own solutions. ([Source: HÄRTING Rechtsanwälte](https://haerting.de/wissen/samsungs-chatgpt-leak-ki-risiken-im-berufsalltag/))

{{< warning headline="This case highlights" text="Anyone who carelessly feeds company data into external AI services risks massive security and legal problems." />}}

At SeaTable, we wanted to take a different path. A path that gives companies the confidence to rely on modern AI without having to give up their data sovereignty. That’s why we operate our own AI server – in the highly secure data center of Hetzner in Germany. This guarantees: all data stays in Europe, all processes are fully GDPR-compliant.

For us, this means responsibility. For you, it means increased transparency, data protection, and trust.

## Technical foundation of our AI server "made in Europe" for SeaTable Cloud

To meet this claim, we rely on a carefully designed infrastructure. The heart of it is a GPU server at Hetzner (GEX44, starting at €220 per month), running the model Gemma 4 E4B. We deliberately chose this model:

- Smaller models did not deliver the required quality in our tests – they were simply too inaccurate, especially in multilingual scenarios or tasks like OCR.
- Larger models may have more potential but require significantly more powerful (and thus more expensive) hardware.

With Gemma 4 E4B, we achieve the perfect middle ground: a powerful, established model that reliably understands text as well as visual inputs.

And the performance is impressive:

| Parameter         | Expected value on Hetzner GEX44 with vLLM & Gemma 4 E4B |
| ----------------- | ------------------------------------------------------- |
| Token throughput  | 1,200–2,000 tokens per second                           |
| Parallel requests | 5–10 simultaneously                                     |
| Response times    | ~5 seconds                                              |

Fast, efficient, and stable enough to provide real added value in daily operations.

If it turns out that this GPU server does not provide the required performance, we will adjust the hardware as needed.

## AI automations in practice

Especially exciting are the concrete applications this makes possible – and the results always end up where they belong: in your **SeaTable Base**.

- **Invoice processing:** Incoming invoices by email are automatically recognized, contents such as invoice number, date, or amount are extracted and saved directly.
- **Smart support management:** Support requests are analyzed, categorized, and passed on to the right employees. This accelerates ticket processing.
- **Text and document summarization:** Long reports or memos are condensed into compact overview texts within seconds.
- **Multilingual recognition:** Content in different languages can be processed easily – a real advantage for internationally operating teams.

All features are designed to be easily usable even for AI beginners.

![Automation wizard with AI automations in SeaTable 6.0](ai-automations-in-seatable.png 'The new Automation Wizard with AI automations in SeaTable 6.0')

## Availability and outlook

With **version 6.0**, the _AI powered automations_ are available free of charge to all **Enterprise customers** – with sufficient quotas to test the new possibilities intensively.

With **version 6.1**, we will open the features to Free and Plus plans in a limited scope. Additionally, we will expand the **logging** and create the option to purchase additional **AI credits** through us to cover more demanding scenarios.

## LLM Freedom in SeaTable: From Hetzner Hosting to OpenAI and Beyond

Another key feature we are planning for upcoming versions is to give users the option to use not only our self-hosted LLM (Large Language Model) at Hetzner but also other models from the cloud. For automations that access publicly available data—or where there are no data protection concerns—you will be able to choose freely whether to use Gemma, DeepSeek, Mistral, OpenAI, or similar providers. Our goal is to give users the freedom to decide which AI model best fits their use case.

## Conclusion: Innovation meets responsibility

With SeaTable 6.0, we are not just launching a new version, but offering companies the chance to elevate their work to a new level. Intelligent automation saves time, makes processes more efficient, and creates freedom – and with our European approach, the highest good remains untouched: the sovereignty over your data.

_AI powered automations – a promise of innovation, data protection, and future security. Made in Europe, made for you._

{{< newsletter title="Interested in AI, automations, and data protection?" submit="Sign up now" >}}

Subscribe to our **newsletter** and receive the latest trends, tips, and updates on AI, smart automations, and data protection – presented in a practical and understandable way.

{{< /newsletter >}}
