---
title: 'Preços SeaTable: Tarifas transparentes para cada tamanho de equipa'
description: ''
date: '2025-03-30'
url: '/pt/preco'
aliases:
    - '/pt/preise/'
    - '/pt/prices/'
seo:
    title: 'Preços SeaTable: Planos para todos os times'
    description: 'Explore todos os recursos, compare planos SeaTable e encontre a melhor solução para sua equipe.'

sections:
    - name: hero-price
      weight: 1
      title: SeaTable Cloud. Feito sob medida para você.
      subtitle: O que oferecemos
      text: Comece gratuitamente e obtenha mais recursos e limites maiores a partir de € 7 por usuário/mês quando precisar
      title2: SeaTable Server. Controle total para a sua organização.
      subtitle2: O que você recebe
      text2: Instale o SeaTable no seu próprio servidor e beneficie-se da máxima soberania de dados, personalização individual e de todas as funcionalidades empresariais.

    - name: 'price-1'
      weight: 2
      xshow: 'showCloud'

    - name: price-table
      weight: 3
      xshow: 'showCloud'
      classes:
          - curved
          - bg-gray-100
      title: Compare todos os detalhes
      table:
          head: ['Grátis', 'Plus', 'Enterprise', 'Dedicado']
          rows:
              - type: section
                label: 'Preço (por usuário, sem IVA)'
              - key: 'Faturamento anual'
                values: ['0€', '7€', '14€', '*']
              - key: 'Faturamento mensal'
                values: ['0€', '9€', '18€', '*']
              - type: section
                label: 'Uso (total por equipe)'
              - key: 'Bases'
                values: ['∞', '∞', '∞', '∞']
              - key: 'Tabelas'
                values: ['∞', '∞', '∞', '∞']
              - key: 'Linhas'
                values: ['10.000', '50.000', '∞', '∞']
              - key: 'Máximo de linhas numa base'
                values: ['10.000', '50.000', '∞', '∞']
              - key: 'Espaço de armazenamento'
                values: ['2 GB', '50 GB', '100 GB', '∞']
              - key: 'Período de retenção de snapshots'
                values: ['1 mês', '6 meses', '12 meses', '24 meses']
              - key: 'Execuções de JavaScript (por mês)'
                values: ['∞', '∞', '∞', '∞']
              - key: 'Execuções de Python (por mês)'
                values: ['100', '5.000', '∞', '∞']
              - key: 'Tamanho máximo da equipe'
                values: ['25', '∞', '∞', '∞']
              - type: section
                label: 'Funcionalidades'
              - key: '25 tipos de colunas'
                values: ['+', '+', '+', '+']
              - key: 'Filtrar, agrupar e ordenar'
                values: ['+', '+', '+', '+']
              - key: 'Visualizações'
                values: ['+', '+', '+', '+']
              - key: 'Visualizações privadas'
                values: ['-', '+', '+', '+']
              - key: 'Compartilhamento de visualizações'
                values: ['-', '+', '+', '+']
              - key: 'Formulários web'
                values: ['+', '+', '+', '+']
              - key: 'Conjuntos de dados compartilhados'
                values: ['+', '+', '+', '+']
              - key: 'Importação / Exportação (CSV, XLSX e DTABLE)'
                values: ['+', '+', '+', '+']
              - key: 'Notificações'
                values: ['+', '+', '+', '+']
              - key: 'Plugins'
                values: ['+', '+', '+', '+']
              - key: 'Suporte a Javascript e Python'
                values: ['+', '+', '+', '+']
              - key: 'App Builder'
                values: ['+', '+', '+', '+']
              - key: 'Permissões de compartilhamento individual (Base)'
                values: ['-', '+', '+', '+']
              - key: 'Permissões de tabela, visualização e coluna (Base)'
                values: ['-', '+', '+', '+']
              - key: 'Bloqueio de linhas'
                values: ['-', '+', '+', '+']
              - key: 'Permissões de página (App)'
                values: ['-', '-', '+', '+']
              - key: 'Personalização de formulários web (logo, imagem de cabeçalho)'
                values: ['-', '-', '+', '+']
              - key: 'Automatizações (por mês e usuário)'
                values: ['100 (fixo)', '500', '5.000', '∞']
              - key: 'Créditos de IA (por mês e usuário)'
                values: ['12,5 (fixo)', '50', '500', '∞']
              - key: 'Armazenamento de Big Data'
                values: ['-', '-', '+', '+']
              - type: section
                label: 'Suporte'
              - key: 'Central de ajuda'
                values: ['+', '+', '+', '+']
              - key: 'Fórum SeaTable'
                values: ['+', '+', '+', '+']
              - key: 'Suporte por e-mail'
                values: ['-', '-', '+', '+']
              - key: 'Serviços profissionais (pagos)'
                values: ['-', '-', '+', '+']
              - type: section
                label: 'Administração & Segurança'
              - key: 'Autenticação em dois fatores'
                values: ['+', '+', '+', '+']
              - key: 'Painel de administração Enterprise'
                values: ['-', '-', '-', '+']
              - key: 'Autenticação via AD/LDAP, SAML ou OAuth'
                values: ['-', '-', '-', '+']
              - type: section
                label: 'Faturamento'
              - key: 'Pagamento com cartão de crédito'
                values: ['+', '+', '+', '+']
              - key: 'Pagamento por transferência bancária (mín. 10 usuários, pagamento anual)'
                values: ['-', '-', '+', '+']

    # details on-premise
    - name: 'content-9'
      weight: 3
      classes:
          - bg-gray-100
          - curved
      xshow: '!showCloud'
      title: Vantagens de ter seu próprio servidor
      subtitle: Razões para on-premises
      items:
          - headline: Funcionalidades Enterprise
            text: Com seu próprio servidor, não há diferentes versões. Você sempre obtém o conjunto completo de funcionalidades do SeaTable Enterprise.
            icon: robot
          - headline: Suporte Enterprise
            text: O preço da licença do SeaTable Enterprise sempre inclui nosso Suporte Enterprise.
            icon: award
          - headline: Personalização
            text: Com seu sistema SeaTable Enterprise, você pode usar seu próprio URL, modelos personalizados, códigos de cores individuais, além de funções e permissões.
            icon: paint-roller
          - headline: Máxima Proteção de Dados
            text: O SeaTable é uma das poucas soluções em nuvem que você também pode obter como solução on-premises.<br><br>Você licencia um SeaTable Enterprise Server e pode instalar e operar o software do servidor onde quiser.
            icon: file-shield
          - headline: Autenticação
            text: O SeaTable suporta todos os métodos de autenticação comuns, como SAML, OAuth, Shibboleth, Active Directory e LDAP. Ele permite autenticação de dois fatores e Single Sign-On.
            icon: fingerprint
          - headline: Limites Personalizados
            text: No seu sistema, você decide quais limites de API devem ser aplicados ou se algum limite deve ser aplicado.
            icon: compass

    - name: 'customer-1'
      weight: 9
      title: 'Empresas e equipes de todos os tamanhos confiam no SeaTable em todo o mundo'
      subtitle: 'Você está em boa companhia'
      show_numbers: 'no'
      buttons: []

    - name: content-11
      weight: 10
      title: Descontos para organizações sem fins lucrativos
      subtitle: Acessível para todos
      items:
          - text: Temos prazer em apoiar pessoas em projetos extraordinários. Organizações sem fins lucrativos e instituições de ensino recebem 50% de desconto. Em casos excepcionais, associações locais podem obter até 75% de desconto nas assinaturas do SeaTable Plus e SeaTable Enterprise. Envie-nos [sua solicitação de desconto via gerenciamento de equipe]({{< relref "help/teamverwaltung/abonnement/rabatte" >}}).
      image: /images/image-341.png
      image_alt: 'Gráfico do SeaTable sobre descontos para organizações sem fins lucrativos, instituições de ensino e entidades públicas'

    - name: platform-selector
      weight: 18

    - name: faq
      weight: 19
      xshow: '!showCloud'
      title: Perguntas Frequentes
      items:
          - q: O que é um usuário?
            a: "Um usuário refere-se a uma conta de usuário (ativa) em uma instância do SeaTable Server. Uma conta de usuário (ativa) permite a autenticação e o login no sistema.
            Um login e, portanto, uma conta de usuário, é necessário para as seguintes ações:<br>
            – Criação, edição e exclusão de bases, aplicativos e formulários web<br>
            – Inserção, edição e exclusão de dados em bases e aplicativos<br><br>
            Nenhum login e, portanto, nenhuma conta de usuário é necessário para estas ações:<br>
            – Uso de aplicativos públicos<br>
            – Acesso a bases/visualizações através de links externos<br>
            – Envio de formulários web públicos"
          - q: O que é um usuário inativo?
            a: Um usuário inativo refere-se a uma conta de usuário que foi definida como inativa e que não permite login no sistema. Usuários inativos não contam para a licença e a licença também não limita o número de usuários inativos. O status de atividade de um usuário pode ser alterado a qualquer momento por um administrador do sistema.
          - q:
            a:
          - q:
            a:
          - q:
            a:
          - q:
            a:
          - q:
            a:
          - q:
            a:
          - q:
            a:
          - q:
            a:
          - q:
            a:
          - q:
            a:
          - q:
            a:
          - q:
            a:
          - q:
            a:
          - q:
            a:
          - q:
            a:
          - q:
            a:

    - name: faq
      weight: 20
      xshow: 'showCloud'
      title: Perguntas Frequentes
      items:
          - q: Posso usar o SeaTable Cloud gratuitamente?
            a: 'Com nossa assinatura Free, você pode usar o SeaTable Cloud permanentemente com até 25 usuários sem custo. Ao se registrar, você ativa essa assinatura.<br><br>Se os limites ou recursos da assinatura Free forem insuficientes, você pode atualizar a qualquer momento para os planos pagos Plus ou Enterprise com limites maiores e funcionalidades estendidas.'

          - q: Posso testar os recursos do Enterprise?
            a: Podemos atualizar sua assinatura Free ou Plus para Enterprise por tempo limitado sem custo. [Envie uma solicitação via gerenciamento de equipe](https://account.seatable.com/).

          - q: O que é um time e o que é um usuário?
            a: No SeaTable Cloud, você colabora em times. Cada membro tem uma conta de usuário (um time pode ter apenas um membro).<br><br>Ao se registrar, um time é criado onde você é o administrador. Você pode adicionar mais usuários e designar outros administradores.<br><br>Usuários são identificados por e-mail e só podem estar em um time.

          - q: Posso alterar o número de usuários no meu time?
            a: 'Você pode ajustar o número de usuários a qualquer momento.<br><br>Nos planos Free, Plus e Enterprise, faça isso no [gerenciamento de time](https://account.seatable.com/). Para SeaTable Dedicated, contate seu representante.<br><br>O plano Free limita a 25 usuários. Plus, Enterprise e Dedicated não têm limite.'

          - q: Posso combinar diferentes assinaturas no meu time?
            a: 'Não é possível combinar assinaturas em um mesmo time.<br><br>Mas você pode distribuir usuários em vários times com assinaturas diferentes.'

          - q: Posso combinar diferentes períodos de cobrança?
            a: 'Não é possível combinar períodos de cobrança. Um time é cobrado totalmente mensal ou anualmente.<br><br>O pagamento anual oferece cerca de 20% de desconto.'

          - q: Como cancelo uma assinatura Plus ou Enterprise?
            a: 'Cancele pelo [gerenciamento de time](https://account.seatable.com/). Você poderá usar os recursos até o fim do período.<br><br>Depois, voltará ao plano Free, que pode limitar seu acesso a somente leitura.'

          - q: 'O que acontece se eu atingir os limites da minha assinatura?'
            a: 'Te avisaremos. Você ainda poderá acessar suas bases mas não adicionar linhas ou arquivos.'

          - q: 'Quais métodos de pagamento são aceitos?'
            a: 'Cartões, Apple Pay e Google Pay. Clientes Enterprise com pagamento anual e 10+ usuários podem pagar por transferência.'

          - q: 'Como altero o endereço de cobrança?'
            a: 'Atualize a qualquer momento no [gerenciamento de time](https://account.seatable.com/).<br><br>Faturas emitidas não podem ser alteradas.'

          - q: 'E sobre privacidade e segurança?'
            a: 'São nossa prioridade máxima. Seus dados são processados exclusivamente em data centers alemães com monitoramento contínuo. Mais detalhes em [Privacidade]({{< relref "pages/legal/data-privacy" >}}) e [Segurança]({{< relref "pages/legal/security" >}}).'

          - q: 'Como excluo minha conta?'
            a: 'O administrador pode excluir usuários ou times inteiros pelo [gerenciamento](https://account.seatable.com). Se for o único usuário, você é o administrador.<br><br>Lamentamos sua saída. [Compartilhe seus motivos]({{< relref "pages/contact" >}}).<br><br>Os [Termos de Serviço]({{< relref "pages/legal/terms-of-service" >}}) detalham o tratamento de dados após exclusão.'
---
