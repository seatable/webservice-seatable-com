---
title: 'Changelog'
seo:
    title: 'Changelog do SeaTable: Atualizações & Novidades'
    description: 'Veja todas as atualizações e melhorias do SeaTable Server, com acesso rápido aos changelogs e notas de versão.'
url: '/pt/changelog'

sections:
    - name: 'hero-2'
      weight: 1
      title: Registro de alterações do SeaTable Server
      subtitle: Novidades
      text: Todas as mudanças, atualizações e melhorias podem ser encontradas neste registro de alterações. Mais informações sobre as principais mudanças estão disponíveis nas notas de lançamento.

    - name: 'content-27'
      weight: 2
      title: 'Vá diretamente para a versão mais recente:'
      subtitle: 'Versões disponíveis'
      text: "Recomendamos que você assine nossa newsletter para sempre receber informações sobre a versão mais recente e segura do SeaTable Server."
      items:
          - icon: fingerprint
            headline: 'SeaTable 6'
            link: '#release-6'
          - icon: bullseye
            headline: 'SeaTable 5'
            link: '#release-5'
          - icon: code
            headline: 'Versões anteriores'
            link: '#release-4'

    - name: 'content-11'
      weight: 3
      title: Escolha a nuvem europeia ou execute seu próprio servidor
      subtitle: Privacidade precisa de segurança
      description: 'Privacidade e segurança são inseparáveis — a verdadeira privacidade não pode existir sem medidas de segurança robustas. Proteger seus dados contra acessos não autorizados, violações e uso indevido é essencial para manter a confidencialidade e a confiança. Manter-se atualizado com os mais recentes padrões e melhores práticas de segurança é crucial para garantir que suas informações pessoais e empresariais permaneçam privadas e protegidas.<br><br>
      Com o SeaTable, você tem a flexibilidade de escolher a solução que melhor se adapta às suas necessidades de privacidade e conformidade. Você pode optar pela nossa oferta SaaS hospedada na Europa, que é totalmente compatível com o GDPR e se beneficia de rigorosas leis europeias de proteção de dados e data centers seguros. Alternativamente, você pode executar seu próprio servidor SeaTable, tendo controle total sobre seus dados e infraestrutura de segurança. Ambas as opções são projetadas para lhe proporcionar transparência, conformidade e tranquilidade.'
      image: ''

    - name: "content-26"
      weight: 10
      title: Lançamento do SeaTable 6
      subtitle: Detalhes da versão
      anchor: release-6
      items:
        - text: 'Versão **6.0.10** em 4 de novembro de 2025: [Notas da versão 6.0]({{< relref "posts/seatable-releases/seatable-release-6-0" >}})'
        - text: 'Versão **6.1.8** em 20 de março de 2026: [Notas da versão 6.1]({{< relref "posts/seatable-releases/seatable-release-6-1" >}})'
      template: "c9124bcd934b47bc8f30"

    - name: "content-26"
      weight: 11
      title: Lançamento do SeaTable 5
      subtitle: Detalhes da versão
      anchor: release-5
      items:
        - text: 'Versão **5.3.10** em 16 de junho de 2025: [Notas da versão 5.3]({{< relref "posts/seatable-releases/seatable-release-5-3" >}})'
        - text: 'Versão **5.2.7** em 25 de fevereiro de 2025: [Notas da versão 5.2]({{< relref "posts/seatable-releases/seatable-release-5-2" >}})'
        - text: 'Versão **5.1.9** em 8 de novembro de 2024: [Notas da versão 5.1]({{< relref "posts/seatable-releases/seatable-release-5-1" >}})'
        - text: 'Versão **5.0.7** em 15 de julho de 2024: [Notas da versão 5.0]({{< relref "posts/seatable-releases/seatable-release-5-0" >}})'
      template: "5964c9e4b6534372b1d8"

    - name: "content-26"
      weight: 12
      title: Lançamento do SeaTable 4
      subtitle: Detalhes da versão
      anchor: release-4
      items:
        - text: 'Versão **4.4.9** em 15 de maio de 2024: [Notas da versão 4.4]({{< relref "posts/seatable-releases/seatable-release-4-4" >}})'
        - text: 'Versão **4.3.8** em 8 de fevereiro de 2024: [Notas da versão 4.3]({{< relref "posts/seatable-releases/seatable-release-4-3" >}})'
        - text: 'Versão **4.2.11** em 22 de novembro de 2023: [Notas da versão 4.2]({{< relref "posts/seatable-releases/seatable-release-4-2" >}})'
        - text: 'Versão **4.1.9** em 23 de agosto de 2023: [Notas da versão 4.1]({{< relref "posts/seatable-releases/seatable-release-4-1" >}})'
        - text: 'Versão **4.0.7** em 27 de junho de 2023: [Notas da versão 4.0]({{< relref "posts/seatable-releases/seatable-release-4-0" >}})'
      template: "d2ccee45fb3b4301836a"

    - name: "content-26"
      weight: 13
      title: Lançamento do SeaTable 3
      subtitle: Detalhes da versão
      anchor: release-3
      items:
        - text: 'Versão **3.5.10** em 12 de abril de 2023: [Notas da versão 3.5]({{< relref "posts/seatable-releases/seatable-release-3-5" >}})'
      template: "3d65a8f8c8ad4482abea"

    - name: "faq"
      weight: 14
      title: Perguntas frequentes sobre o registro de alterações
      subtitle: Tudo o que você precisa saber
      items:
        - q: Qual é o ciclo de lançamentos do SeaTable?
          a: O SeaTable Server é atualizado regularmente. Lançamos uma nova versão principal (X.0) todo verão e uma nova versão secundária (5.X) a cada dois ou três meses.
        - q: Como se manter informado sobre novas versões ou mudanças?
          a: Recomendamos que você assine nossa newsletter para sempre receber informações sobre a versão mais recente e segura do SeaTable Server que se adapta às suas necessidades.
        - q: Existem versões diferentes para o SeaTable Cloud ou SeaTable Server?
          a: Não, existe apenas uma versão do SeaTable. Utilizamos a mesma imagem Docker para o SeaTable Cloud, que você pode baixar para executar em seu próprio servidor.
        - q: Onde posso baixar o SeaTable?
          a: 'O SeaTable é publicado como um contêiner Docker. Você pode obter a imagem mais recente no [Docker Hub](https://hub.docker.com/r/seatable/seatable-enterprise)'
        - q: 'Quero executar meu próprio SeaTable Server. Onde posso obter mais informações?'
          a: 'Por favor, consulte o [Manual de Administração do SeaTable](https://admin.seatable.com) para instruções sobre como instalar seu próprio servidor. Você pode comprar um arquivo de licença diretamente em nossa [página de preços]({{< relref "pages/prices" >}}).'
---
