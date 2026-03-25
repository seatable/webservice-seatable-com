---
title: 'SeaTable prices: Transparent rates for every team size'
description: ''
date: '2025-03-30'
url: '/prices'
aliases:
    - '/en/preise/'
    - '/en/pricing/'
    - '/preise/'
seo:
    title: 'SeaTable Pricing: Transparent Plans for Every Team'
    description: 'Discover flexible plans for all team sizes. Compare features & pricing – find your ideal data management solution.'

sections:
    - name: hero-price
      weight: 1
      title: SeaTable Cloud. Tailored to you.
      subtitle: What we offer
      text: Start for free and get more features and higher limits from €7 per user per month when you need them
      title2: SeaTable Server. Full control for your organization.
      subtitle2: What you get
      text2: Install SeaTable on your own server and benefit from maximum data sovereignty, individual customization, and all enterprise features.

    - name: 'price-1'
      weight: 2
      xshow: 'showCloud'

    - name: price-table
      weight: 3
      xshow: 'showCloud'
      classes:
        - curved
        - bg-gray-100
      title: Compare all details
      table:
        head: ['Free', 'Plus', 'Enterprise', 'Dedicated']
        rows:
          - type: section
            label: 'Price (per user, excl. VAT)'
          - key: 'Annual billing'
            values: ['0€', '7€', '14€', '*']
          - key: 'Monthly billing'
            values: ['0€', '9€', '18€', '*']
          - type: section
            label: 'Usage (total per team)'
          - key: 'Bases'
            values: ['∞', '∞', '∞', '∞']  
          - key: 'Tables'
            values: ['∞', '∞', '∞', '∞']
          - key: 'Rows'
            values: ['10,000', '50,000', '∞', '∞']
          - key: 'Max. rows per base'
            values: ['10.000', '50.000', '100.000', '200.000']
          - key: 'Storage space'
            values: ['2 GB', '50 GB', '100 GB', '∞']
          - key: 'Snapshot retention period'
            values: ['1 month', '6 months', '12 months', '24 months']
          - key: 'JavaScript script runs (per month)'
            values: ['∞', '∞', '∞', '∞']
          - key: 'Python script runs (per month)'
            values: ['100', '5,000', '∞', '∞']
          - key: 'API calls (per month and user)'
            values: ['3,000 (fixed)', '10.000', '50.000', '∞']
          - key: 'Maximum team size'
            values: ['25', '∞', '∞', '∞']
          - type: section
            label: 'Features'
          - key: '25 column types'
            values: ['+', '+', '+', '+']
          - key: 'Filter, grouping and sorting'
            values: ['+', '+', '+', '+']
          - key: 'Views'
            values: ['+', '+', '+', '+']
          - key: 'Private views'
            values: ['-', '+', '+', '+']
          - key: 'Sharing views'
            values: ['-', '+', '+', '+']
          - key: 'Web forms'
            values: ['+', '+', '+', '+']
          - key: 'Shared datasets'
            values: ['+', '+', '+', '+']
          - key: 'Import / Export (CSV, XLSX and DTABLE)'
            values: ['+', '+', '+', '+']
          - key: 'Notifications'
            values: ['+', '+', '+', '+']
          - key: 'Plugins'
            values: ['+', '+', '+', '+']
          - key: 'JavaScript and Python support'
            values: ['+', '+', '+', '+']
          - key: 'App Builder'
            values: ['+', '+', '+', '+']
          - key: 'Individual sharing permissions (Base)'
            values: ['-', '+', '+', '+']
          - key: 'Table, view and column permissions (Base)'
            values: ['-', '+', '+', '+']
          - key: 'Row locking'
            values: ['-', '+', '+', '+']
          - key: 'Page permissions (App)'
            values: ['-', '-', '+', '+']
          - key: 'Web form customization (logo, header image)'
            values: ['-', '-', '+', '+']
          - key: 'Automations (per month and user)'
            values: ['100 (fixed)', '500', '5,000', '∞']
          - key: 'AI Credits (per month and user)'
            values: ['12.5 (fixed)', '50', '500', '∞']
          - key: 'Big data storage'
            values: ['-', '-', '+', '+']
          - type: section
            label: 'Support'
          - key: 'Help center'
            values: ['+', '+', '+', '+']
          - key: 'SeaTable forum'
            values: ['+', '+', '+', '+']
          - key: 'Email support'
            values: ['-', '-', '+', '+']
          - key: 'Professional services (paid)'
            values: ['-', '-', '+', '+']
          - type: section
            label: 'Admin & Security'
          - key: '2-factor authentication'
            values: ['+', '+', '+', '+']
          - key: 'Enterprise admin panel'
            values: ['-', '-', '-', '+']
          - key: 'Authentication via AD/LDAP, SAML or OAuth'
            values: ['-', '-', '-', '+']
          - type: section
            label: 'Billing'
          - key: 'Payment by credit card'
            values: ['+', '+', '+', '+']
          - key: 'Payment by bank transfer (min. 10 users, annual payment)'
            values: ['-', '-', '+', '+']


    # details on-premise
    - name: 'content-9'
      weight: 3
      classes:
          - bg-gray-100
          - curved
      xshow: '!showCloud'
      title: Advantages of your own server
      subtitle: Reasons for on-premises
      items:
          - headline: Enterprise Features
            text: With your own server, there are no different versions. You always get the full range of features from SeaTable Enterprise.
            icon: robot
          - headline: Enterprise Support
            text: The price of the SeaTable Enterprise license always includes our Enterprise Support.
            icon: award
          - headline: Customization
            text: With your SeaTable Enterprise system, you can use your own URL, custom templates, individual color codes, as well as roles and permissions.
            icon: paint-roller
          - headline: Maximum Data Protection
            text: SeaTable is one of the few cloud solutions that you can also get as an on-premises solution.<br><br>You license a SeaTable Enterprise Server and can install and operate the server software wherever you want.
            icon: file-shield
          - headline: Authentication
            text: SeaTable supports all common authentication methods such as SAML, OAuth, Shibboleth, Active Directory, and LDAP. It enables two-factor authentication and single sign-on.
            icon: fingerprint
          - headline: Custom Limits
            text: In your system, you decide which API limits should apply or whether any should apply at all.
            icon: compass

    - name: 'customer-1'
      weight: 9
      title: 'Companies and teams of all sizes worldwide trust SeaTable'
      subtitle: 'You are in good company'
      show_numbers: 'no'
      buttons: []

    - name: content-11
      weight: 10
      title: Discounts for non-profit organizations
      subtitle: Affordable for everyone
      items:
          - text: We are pleased to support people in great projects. Non-profit organizations and educational institutions generally receive a 50% discount. Local associations may even receive up to a 75% discount on SeaTable Plus and SeaTable Enterprise subscriptions in exceptional cases. Send us [your discount request via team management]({{< relref "help/teamverwaltung/abonnement/rabatte" >}}).
      image: /images/image-341.png
      image_alt: 'SeaTable graphic about discounts for non-profit organizations, educational institutions and public bodies'

    - name: platform-selector
      weight: 18

    - name: faq
      weight: 19
      xshow: '!showCloud'
      title: Frequently Asked Questions
      items:
          - q: What is a user?
            a: 'A user means an (active) user account on a SeaTable Server instance. An (active) user account allows authentication and login to the system.<br><br>
            A login and thus a user account is required for the following actions:<br>
            – Creating, editing and deleting bases, apps and web forms<br>
            – Entering, editing and deleting data in bases and apps<br><br>
            No login and therefore no user account is required for these actions:<br>
            – Use of public apps<br>
            – Accessing bases/views via external links<br>
            – Submission of public web forms'
          - q: What is an inactive user?
            a: An inactive user means a user account that has been set to inactive and that does not allow logging in to the system. Inactive users do not count against the license and the license does not limit the number of inactive users. The activity status of a user can be changed by a system administrator at any time.
          - q: Which payment methods can I use?
            a: You can always pay by credit card as well as with Apple Pay and Google Pay. You can also pay for licenses for 50 users and more by bank transfer.
          - q: Can I purchase a license for SeaTable Server without automatic renewal?
            a: If you want to purchase a SeaTable Server license without automatic renewal of the license, please purchase a license with automatic renewal and deactivate the automatic renewal in the [SeaTable Server Subscription Management Portal](https://licenses.seatable.com/p/login/5kA4j61uU641eqY000) immediately after purchase.
          - q: How can I cancel the automatic renewal of the SeaTable Server license?
            a: You can deactivate automatic renewal at any time in the [SeaTable Server Subscription Management Portal](https://licenses.seatable.com/p/login/5kA4j61uU641eqY000).
          - q: How can I change the billing address?
            a: You can change the billing address at any time in the [SeaTable Server Subscription Management Portal](https://licenses.seatable.com/p/login/5kA4j61uU641eqY000).<br><br>It is not possible to change an invoice retrospectively.
          - q: Can I change the size of a running SeaTable Server license?
            a: You can extend a SeaTable Server license for 50 users or more at any time. Please contact sales@seatable.com and state the license key and the desired number of users. The license price for the additional users is calculated pro rata temporis.<br><br>A SeaTable Server license for 10 and 25 users cannot be extended during the term. If you need more users, you must purchase a new license.<br><br>It is not possible to combine multiple licenses. A SeaTable Server instance can only be connected to one license.
          - q: Can I combine multiple SeaTable Server licenses?
            a: It is not possible to combine multiple SeaTable Server licenses. Only one license is activated on a SeaTable Server instance at a time.
          - q: How does automatic renewal work?
            a: About 30 days before your SeaTable Server license expires, you will receive an email notifying you of the upcoming renewal. The e-mail will explain when the renewal will take place and which payment method will be used. The email will also contain a link to the [SeaTable Server Subscription Management Portal](https://licenses.seatable.com/p/login/5kA4j61uU641eqY000). There you can change the billing address and payment method. After the renewal, you will receive the invoice and the license documents by e-mail. To activate the renewed license, upload the license file to your SeaTable Server instance.
          - q: Can I specify an order number or cost center when purchasing a license?
            a: 'If you require a reference on the invoice, please contact sales@seatable.com. Please include the following information in your request: Number of users, billing address, VAT ID, contact e-mail and invoice e-mail if applicable. You will then receive an offer by e-mail. Please provide us with the reference when confirming the offer. The reference will then be mentioned on the invoice.'
          - q: Do I get a discount as a public body or as a non-profit organization?
            a: Public institutions and non-profit organizations receive a discount on SeaTable Server licenses. Please contact [our sales department]({{< relref "pages/contact" >}}).<br><br>SeaTable Server licenses for 10 and 25 users are generally not discounted.
          - q: For which license periods can I purchase a license for SeaTable Server?
            a: The minimum term of a software license for SeaTable Server is 1 year. You can also purchase licenses with terms of 2 and 3 years. You save 5% or 10% on licenses with 2 or 3-year terms.<br><br>The license fee is generally invoiced and due at the beginning of the license period for the entire term.<br><br>For licenses with a longer term, please contact [our sales department]({{< relref "pages/contact" >}}) and state the desired term and number of users. You will then receive an offer by e-mail.
          - q: How do I activate the license for SeaTable Server?
            a: You must take action to activate the license! Log in to your SeaTable Server instance as a user with administrator rights and call up the system administration. To do this, click on your avatar in the top right-hand corner of the start page. You can upload the license file in the info area of the system administration. The license period of the license is then immediately displayed in the info area.<br><br>If the web interface of your SeaTable Server instance is no longer accessible, you must save the license file in the file system of the host. You can find more information in the [SeaTable Admin Manual](https://admin.seatable.com).
          - q: What rights does the software license for SeaTable Server give me?
            a: A software license for SeaTable is the authorization for the licensee to use SeaTable Server. The rights of use granted by the license and other rights can be found in the [SeaTable Server Enterprise Edition EULA]({{< relref "pages/legal/eula" >}}).
          - q: Is a license transferable?
            a: The [SeaTable Server Enterprise Edition EULA]({{< relref "pages/legal/eula" >}}) excludes the transfer of rights of use. You may not sell or assign a license.
          - q: Can I also purchase a license for SeaTable Server from a dealer?
            a: You can only purchase SeaTable Server licenses directly from SeaTable GmbH.
          - q: What are the minimum requirements for operating SeaTable Server?
            a: Consult the [SeaTable Admin Manual](https://admin.seatable.com) for all technical questions.

    - name: faq
      weight: 20
      xshow: 'showCloud'
      title: Frequently Asked Questions
      items:
          - q: Can I use SeaTable Cloud for free?
            a: 'With our Free subscription, you can use SeaTable Cloud permanently with up to 25 users at no cost. By registering, you conclude such a subscription.<br><br>If the limits or features of the Free subscription are insufficient, you can upgrade at any time to the paid Plus or Enterprise subscription with higher limits and extended features.'
          - q: Can I test the Enterprise features?
            a: We can upgrade your Free or Plus subscription to an Enterprise subscription for a limited time at no cost. [Please send us a corresponding request via team management](https://account.seatable.com/).
          - q: What is a team and what is a user?
            a: In SeaTable Cloud, you collaborate in teams. Each team member has a user account and is thus a user. (A team can also have just one member.)<br><br>When registering for SeaTable Cloud, a team is created. The first user is the team administrator. The team administrator can add more users to the team and manage existing team members. The administrator can also appoint one or more additional team members as team administrators.<br><br>A user is identified by their email address. A user can only be assigned to one team.
          - q: Can I change the number of users in my team?
            a: 'You can adjust the number of users in your team at any time.<br><br>With SeaTable Cloud Free, Plus and Enterprise, you can do this yourself by adjusting your subscription in [team management](https://account.seatable.com/). For SeaTable Dedicated, please contact your personal contact person.<br><br>In the Free subscription, the team size is limited to 25. With SeaTable Cloud Plus and Enterprise as well as SeaTable Dedicated, the number of users is unlimited.'
          - q: Can I combine different subscriptions in my team?
            a: 'Combining different subscriptions in one team is not possible. A team with all its members is either on the Free, Plus or Enterprise subscription.<br><br>You can distribute your users across two or more teams. These teams can have different subscriptions.'
          - q: Can I combine different billing periods?
            a: 'Combining different billing periods in a Plus and Enterprise subscription is not possible. A team with all its members is billed either monthly or annually.<br><br>With annual payment, you pay about 20% less than with monthly billing.'
          - q: How can I cancel a Plus or Enterprise subscription?
            a: 'You can cancel your Plus and Enterprise subscription at any time in [team management](https://account.seatable.com/) at the end of the current subscription period. Until then, you can continue to use all features of the canceled subscription.<br><br>When the cancellation takes effect, your paid subscription will be converted to a Free subscription. So you can still access your data in SeaTable Cloud even after the paid subscription ends. Due to the lower limits of the Free subscription, you may only have read access to your bases after the downgrade.'
          - q: 'What happens when I reach my subscription limit?'
            a: 'When you reach your row or storage limit, we will inform you. You can still access your bases and tables; but you cannot create additional rows or upload files.'
          - q: 'Which payment methods can I use?'
            a: 'You can generally pay by credit card as well as with Apple Pay and Google Pay. Enterprise subscribers with annual payment and 10 or more users can also pay by bank transfer.'
          - q: 'How can I adjust the billing address?'
            a: 'You can adjust the billing address at any time in [team management](https://account.seatable.com/).<br><br>Subsequent changes to an invoice are not possible.'
          - q: 'What about data protection and security?'
            a: 'Data protection and security are our top priorities. Your data stored in SeaTable is processed exclusively in German data centers, permanently monitored and regularly backed up. Further details can be found on the [Data Protection]({{< relref "pages/legal/data-privacy" >}}) and [Security]({{< relref "pages/legal/security" >}}) pages.'
          - q: 'How can I delete my account?'
            a: 'The team administrator can delete individual team users or the entire team at any time via [team management](https://account.seatable.com). If you are the only user in the team, you are also the team administrator. If you don''t have access to team management, contact your team administrator.<br><br>We''re sorry if you no longer wish to use SeaTable. [Please share with us the reasons for your departure]({{< relref "pages/contact" >}}).<br><br>The [SeaTable Cloud Terms of Service]({{< relref "pages/legal/terms-of-service" >}}) explain what happens to your data following account deletion.'
---
