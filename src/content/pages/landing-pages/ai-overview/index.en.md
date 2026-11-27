---
title: 'AI in SeaTable: All AI Features at a Glance'
description: ''
seo:
    title: 'AI in SeaTable: All AI Features at a Glance | SeaTable'
    description: 'AI in SeaTable: automations, AI Chat, apps by prompt and MCP for ChatGPT, Claude and Cursor – GDPR-compliant in German data centers.'
date: '2026-11-24'
lastmod: '2026-11-24'
url: '/ai'

sections:
    - name: hero-2
      weight: 1
      classes:
          - bg-[#ece5e2]
      title: 'AI features for your data – no code and GDPR-compliant'
      subtitle: 'AI in SeaTable'
      text: 'With SeaTable, you use artificial intelligence right where your data lives: AI automations analyze documents and texts automatically, the AI Chat answers questions about your database, the AI App Builder creates apps from a description, and with MCP you connect AI agents such as ChatGPT or Claude to your bases. All without programming skills and GDPR-compliant – with an AI model in German data centers and no data transfer to US providers.'

    - name: content-4
      weight: 2
      title: 'AI in SeaTable at a glance'
      subtitle: 'The key facts'
      text: 'SeaTable is an [AI no-code platform]({{< relref "/" >}}) for relational databases, automations and apps with built-in artificial intelligence. You can use AI in four ways: in **AI automations**, in the **AI Chat**, in the **AI App Builder** and via **MCP** with AI agents such as ChatGPT, Claude or Cursor. The default model is SeaTable AI: the open-weights model Qwen 3.8 27B, which runs in German data centers operated by our infrastructure partner Exoscale. *Status: SeaTable 7.0, November 2026.*'
      items:
          - headline: AI automations
            text: 'Summarize, classify, extract and recognize text (OCR) – automatically in the background.'
            link: pages/landing-pages/use-cases/ai-automations
          - headline: AI Chat
            text: 'Ask your own base questions in natural language – the chat reads and writes data.'
            link: help/ai/ai-chat/introduction
          - headline: AI App Builder
            text: 'Create HTML pages for your SeaTable app in a conversation with the AI – by describing them instead of coding.'
            link: pages/landing-pages/use-cases/no-code-app-builder
          - headline: MCP and AI agents
            text: 'Connect ChatGPT, Claude, Claude Code or Cursor to your bases via the SeaTable MCP Server.'
            link: posts/mcp-server
          - headline: Data protection and security
            text: 'AI model in German data centers, no model training with your data, full control over permissions.'
            link: pages/legal/security
          - headline: AI credits and pricing
            text: 'Every subscription includes a monthly allowance of AI credits per user.'
            link: pages/prices

    - name: content-22
      weight: 3
      title: 'Try AI in SeaTable for free'
      subtitle: 'Get started now'
      text: 'Sign up for free and try AI automations, the AI Chat and the AI App Builder directly in SeaTable Cloud. Every subscription includes a monthly allowance of AI credits.'
      buttons:
          - label: Sign up now
            link: 'pages/registration'
            style: primary
            id: en-ki-overview-registration-content-22
          - label: Watch the video
            link: 'https://www.youtube.com/watch?v=kk5FtrG56Jo'
            style: secondary

    - name: content-1
      weight: 4
      title: 'Handle recurring tasks automatically'
      subtitle: 'AI automations'
      description: 'AI actions are available right in the automation editor. An incoming invoice is uploaded, and the AI writes the invoice number, date and amount into the matching columns – for every new entry, without code.'
      classes:
          - bg-gray-100
          - curved
      items:
          - headline: Four ready-made AI actions
            text: 'Summarize, classify, extract and recognize text (OCR) – plus your own prompts for individual tasks.'
          - headline: Structured results
            text: 'The AI writes its results into defined columns of your base, so you can filter, analyze and process them right away.'
          - headline: Traceable
            text: 'Every run is recorded in the automation''s execution log. You can see the credit usage in the team administration.'
      image: '/images/landing-page-ki-01.png'
      image_alt: 'AI actions in the SeaTable automation editor'
      buttons:
          - label: More about AI automation
            link: 'pages/landing-pages/use-cases/ai-automations'

    - name: content-12
      weight: 5
      title: 'Ask your own database questions'
      subtitle: 'AI Chat'
      description: 'Open the AI Chat in your base and ask, for example: "How many open deals over €10,000 have had no contact for 30 days?" The AI knows the structure of your base and queries exactly the relevant data.'
      classes:
          - bg-white
          - curved
      items:
          - text: Query and analyze data in natural language
          - text: Create records, change values and link rows
          - text: Confirmation before data is changed or deleted
          - text: In English, German, French and other languages
          - text: Uses SeaTable AI by default, no API key of your own required
          - text: Optionally with models from Anthropic, OpenAI or Mistral via your own API key
          - text: Available in SeaTable Cloud and SeaTable Dedicated
      image: '/images/landing-page-ki-02.png'
      image_alt: 'AI Chat in a SeaTable base'
      buttons:
          - label: More about the AI Chat
            link: 'help/ai/ai-chat/introduction'

    - name: content-12
      weight: 6
      classes:
          - bg-gray-100
          - curved
      title: 'Create apps by describing them'
      subtitle: 'AI App Builder'
      description: 'In the App Builder, you create HTML pages in a conversation with the AI. You describe what the page should do and how it should look – the AI builds a first version that you refine in the conversation and publish with a single click.'
      items:
          - text: Assistant for name, UI style, data sources and permissions
          - text: Preview of every version right in the chat
          - text: Full history saved, earlier versions can be restored
          - text: Insight into every step of the AI through its reasoning process
          - text: Base data never reaches the AI model, only prompts and schemas
      image: '/images/landing-page-ki-03.png'
      image_position: 'left'
      image_alt: 'Creating an HTML page with AI in the SeaTable App Builder'
      buttons:
          - label: More about the no-code App Builder
            link: 'pages/landing-pages/use-cases/no-code-app-builder'

    - name: content-1
      weight: 7
      title: 'Connect AI agents directly to your data'
      subtitle: 'MCP and AI agents'
      description: 'With the Model Context Protocol (MCP), AI agents access your bases directly – no CSV export, no copy and paste. The agent reads, analyzes and writes to your base, just as if you were asking a colleague.'
      classes:
          - bg-white
          - curved
      items:
          - headline: Official SeaTable MCP Server
            text: 'Connect ChatGPT, Claude Desktop, Claude Code or Cursor to SeaTable. You''ll find step-by-step guides in the Help Center.'
          - headline: Permissions via API token
            text: 'You decide which bases the agent can access and whether it has read-only access.'
          - headline: Work in the tools you know
            text: 'Use your SeaTable data in the AI tool your team already works with.'
      image: '/images/landing-page-ki-04.png'
      image_alt: 'Data flow between AI agent, SeaTable MCP Server and SeaTable'
      buttons:
          - label: More about SeaTable and MCP
            link: 'posts/mcp-server'

    - name: content-2
      weight: 8
      title: AI in practice
      subtitle: Examples from teams and industries
      description: 'This is how teams use SeaTable''s AI features in their daily work. You''ll find more examples in the solutions for your team.'
      items:
          - headline: Classify support tickets
            text: 'Incoming requests are analyzed, categorized and prioritized by an AI automation before they reach the responsible team. More about [IT service management]({{< relref "pages/landing-pages/industry-solutions/software-development" >}}).'
            icon: terminal
          - headline: Summarize job applications
            text: 'The AI summarizes cover letters and CVs so your HR team can review applications faster. More about [applicant management]({{< relref "pages/landing-pages/use-cases/bewerbermanagement" >}}).'
            icon: people-group
          - headline: Check project status
            text: 'In the AI Chat, ask for projects with a deadline in the next 7 days or have reports created from meeting notes. More about [project management]({{< relref "pages/landing-pages/industry-solutions/project-management" >}}).'
            icon: bullseye
          - headline: Read receipts with OCR
            text: 'The AI reads the invoice number, date, amount and supplier from invoices and triggers the approval workflow.'
            icon: chart-simple

    - name: banner-4
      weight: 10
      title: Currently using Airtable?
      subtitle: 'The Airtable alternative with data sovereignty'
      text: 'SeaTable combines database, automations, App Builder and AI in one system – with an AI model in German data centers and full control over your data.'
      buttons:
          - label: Explore the Airtable alternative
            link: 'pages/landing-pages/alternatives/airtable-alternative'
            style: primary

    - name: content-9
      weight: 9
      title: Data protection and control when using AI
      subtitle: AI without losing control
      description: 'SeaTable Cloud is hosted by the Swiss provider Exoscale in ISO 27001-certified data centers in Germany. The AI model runs there as well. More about [security and data protection]({{< relref "pages/legal/security" >}}).'
      items:
          - headline: AI model in Germany
            text: 'SeaTable AI (Qwen 3.8 27B) runs in Exoscale''s German data centers. No transfer to OpenAI, Google or other US providers.'
            icon: shield-halved
          - headline: No model training
            text: 'Data that SeaTable processes with its own AI model is not used to train AI models.'
            icon: fingerprint
          - headline: Confirmation before changes
            text: 'The AI Chat asks before it changes or deletes data – once, for the session or not at all.'
            icon: toggle-off
          - headline: Permissions via API token
            text: 'For AI agents, the API token determines which bases are visible and whether access is read-only.'
            icon: leaf
          - headline: Transparent costs
            text: 'Every subscription includes a monthly allowance of AI credits per user. You can see the usage in the team administration.'
            icon: medal
          - headline: Traceable
            text: 'Every AI automation is recorded in the execution log, so it is always clear which data was processed.'
            icon: signature

    - name: youtube
      weight: 12
      title: AI automations explained in a few minutes
      subtitle: Video
      videoId: kk5FtrG56Jo

    - name: content-21
      weight: 13
      title: Resources on AI in SeaTable
      text: 'Guides, background information and news about SeaTable''s AI features.'
      items:
          - headline: AI Help Center
            text: 'Step-by-step guides to AI automations, the AI Chat and AI agents in the [Help Center]({{< relref "help/ai" >}}).'
          - headline: Connect AI agents
            text: 'Guides for ChatGPT, Claude Desktop, Claude Code and Cursor under [What are AI agents?]({{< relref "help/ai/ai-agents/what-are-ai-agents" >}})'
          - headline: What's new in SeaTable 7.0?
            text: 'AI App Builder, AI Chat out of beta and the new AI model: all the details in the [SeaTable 7.0 release notes]({{< relref "posts/seatable-releases/seatable-release-7-0" >}}).'
          - headline: Background on AI and data protection
            text: 'Why AI and data sovereignty belong together: read the article [AI in SeaTable: Automate Processing or Ask Directly]({{< relref "posts/ai-in-seatable" >}}).'

    - name: faq
      weight: 99
      title: Frequently asked questions about AI in SeaTable
      items:
          - q: What is an AI no-code platform?
            a: 'An AI no-code platform like SeaTable is software that lets business users or [citizen developers]({{< relref "posts/20250317-citizen-developer" >}}) build databases, automations and apps and use artificial intelligence without programming. Typical features are visual editors, predefined AI actions such as summarizing, classifying or text recognition, and operation in natural language, for example via an AI chat.'
          - q: What AI features does SeaTable offer?
            a: SeaTable offers four ways to use AI. AI automations summarize, classify, extract and recognize text via OCR. The AI Chat answers questions about your base and edits data. The AI App Builder creates HTML pages from a description. Via MCP, you connect AI agents such as ChatGPT, Claude or Cursor to your data.
          - q: When should I use AI automations, the AI Chat, the AI App Builder or MCP?
            a: AI automations are suited to recurring, clearly defined tasks that should run in the background. The AI Chat is ideal for open questions and analyses directly in SeaTable. With the AI App Builder, you create your own interfaces such as dashboards or data entry forms. Use MCP if your team already works with ChatGPT, Claude or Cursor.
          - q: How does SeaTable's AI differ from Airtable AI?
            a: 'With Omni and Field Agents, Airtable offers extensive AI features, for example to create apps from a description or to fill fields automatically. SeaTable focuses on data sovereignty: the default model SeaTable AI runs in German data centers, and data is neither transferred to US providers nor used for model training. How the two platforms compare overall is shown in our [comparison of the best Airtable alternatives]({{< relref "posts/airtable-alternativen" >}}).'
          - q: Which AI model does SeaTable use?
            a: SeaTable Cloud uses SeaTable AI by default. It is powered by the open-weights model Qwen 3.8 27B with 27 billion parameters, developed by Alibaba. It runs in German data centers operated by our infrastructure partner Exoscale, which also runs the servers for SeaTable Cloud.
          - q: Does my data leave the EU when I use AI?
            a: No. With AI automations, the AI App Builder and the AI Chat with the default model, your data stays in German data centers. Only if you deliberately choose an external model from Anthropic, OpenAI or Mistral in the AI Chat, or connect an external AI agent via MCP, is the queried data transferred to that provider.
          - q: How much does AI usage cost and what are AI credits?
            a: 'AI features are billed via AI credits. Every subscription includes a monthly allowance of AI credits per user; the figures are listed on the pricing page. In the AI Chat, 1 million input tokens correspond to 500 AI credits and 1 million output tokens to 1,500 AI credits.'
          - q: Which AI agents can be connected via MCP?
            a: 'The SeaTable MCP Server works with AI agents such as ChatGPT, Claude Desktop, Claude Code and Cursor. You''ll find step-by-step guides in the Help Center.'
          - q: Do I need programming skills?
            a: 'No. You set up AI automations in the visual editor, and you use the AI Chat and the AI App Builder in natural language. SeaTable is an AI no-code platform for business users without programming skills.'
---
