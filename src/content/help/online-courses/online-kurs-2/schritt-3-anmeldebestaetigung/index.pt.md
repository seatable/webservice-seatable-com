---
title: 'Passo 3: Confirmação do registo'
date: 2024-09-19
lastmod: '2024-09-24'
categories:
    - 'online-kurs-2'
author: 'cdb'
url: '/pt/ajuda/etapa-3-confirmacao-de-inscricao'
aliases:
    - '/pt/ajuda/schritt-3-anmeldebestaetigung'
seo:
    title: 'Etapa 3: Confirmação de inscrição por email'
    description: 'Saiba como enviar confirmações de inscrição e cobranças por email aos participantes do curso usando SeaTable.'
---

Agora, acrescentamos a função de os participantes que se inscreveram num curso receberem uma confirmação de inscrição e um pedido de pagamento por correio eletrónico.

## Enviar mensagens de correio eletrónico com o SeaTable

Para enviar mensagens de correio eletrónico com o SeaTable, é necessário criar primeiro uma conta de correio eletrónico na base. Como a configuração varia consoante o fornecedor, recomendamos a utilização do [mailtrap](https://mailtrap.io). _O Mailtrap_ permite-lhe enviar mensagens de correio eletrónico para uma caixa de correio virtual, o que tem a vantagem de não serem enviadas mensagens de correio eletrónico para clientes reais ou fictícios - mas pode simular o envio de mensagens de correio eletrónico de forma realista.

{{< warning  headline="Qual o fornecedor de correio eletrónico mais adequado para mim"  text="Não existe um fornecedor de correio eletrónico _certo_ ou _errado_. Se enviar apenas algumas mensagens de correio eletrónico por dia, a sua conta de correio eletrónico atual será provavelmente suficiente. No entanto, à medida que o seu volume de correio eletrónico aumenta, deve considerar um fornecedor profissional como o [Brevo.com](https://brevo.com), que lhe permite controlar melhor a entrega de correio eletrónico." />}}

### Criar uma conta Mailtrap

Para começar, visite a [página de registo do Mailtrap](https://mailtrap.io/register/signup) e crie uma conta gratuita.

![Página de registo do Mailtrap com formulário de criação de conta](images/lvl2-mailtrap.png)

Confirme o seu endereço de correio eletrónico e inicie sessão. Depois de responder a algumas perguntas sobre os seus interesses - que não são relevantes para o resto do processo - será encaminhado para a página inicial do _Mailtrap_.

![Ecrã inicial do Mailtrap com caixa de entrada predefinida «My Inbox»](images/lvl2-mailtrap-inbox.png)

No menu do lado esquerdo, clique em `E-Mail Testing > Inboxes`. Aí já encontrará uma caixa de entrada pré-configurada com o nome `My Inbox`. São necessários os dados de acesso SMTP correspondentes para a configuração no SeaTable.

![Credenciais SMTP da caixa «My Inbox» para utilização no SeaTable](images/lvl2-mailtrap-smtp-credentials.png)

### Configurar o envio de correio eletrónico no SeaTable

Com os dados de acesso SMTP do Mailtrap, pode agora configurar [o envio de correio eletrónico no SeaTable]({{< relref "help/base-editor/weitere-optionen/einrichtung-eines-e-mail-kontos-in-einer-base" >}}).

![Janela do SeaTable com dados SMTP do Mailtrap preenchidos para envio de e-mails](images/lvl2-mailtrap-in-seatable.png)

As mensagens de correio eletrónico não são realmente enviadas, mas aparecem na sua caixa de correio Mailtrap. Teste isto enviando uma mensagem de correio eletrónico para qualquer destinatário - só aparecerá na sua caixa de correio virtual.

![E-mail de teste na caixa do Mailtrap para verificar o envio a partir do SeaTable](images/lvl2-mailtest.gif)

## Enviar uma mensagem de correio eletrónico ao cliente

Agora podemos ver no quadro `Registrations` para criar uma nova coluna para enviar mensagens de correio eletrónico. Utilize as seguintes definições:

> Nome: qualquer
>
> Tipo de coluna: `{{< seatable-icon icon="dtable-icon-button" >}} Botão`
>
> Rótulo: `Send`
>
> Ação: `{{< seatable-icon icon="dtable-icon-email" >}} Enviar email`
>
> Assunto: `Confirmation: Course {Registered for}`
>
> Recebedora: `customer@example.com`

![Tabela do SeaTable com coluna de botão «Send» para enviar e-mails a participantes](images/lvl2-create-button.png)

Pode utilizar o seguinte modelo de texto para o texto da mensagem:

> Hey,  
> Thank you for registering for the course {Registered for} on {Date}.
>
> To complete your registration, please transfer the course fee using the details below:
>
> Amount: {Price}  
> Bank: Example Bank LTD  
> IBAN: XYZ
>
> We appreciate your prompt payment!
>
> Best regards

No editor de texto simples, os marcadores de posição entre parênteses rectos são substituídos automaticamente. Se estiver a utilizar o editor de rich text, tem de substituir os marcadores de posição manualmente utilizando a opção `{{< seatable-icon icon="dtable-icon-choose-column" >}} Insira a coluna`.`

![Editor de texto formatado do SeaTable com placeholders para curso e data](images/lvl2-rich-text-editor.png)

Em seguida, clique no botão e verifique se a mensagem aparece na sua caixa de correio Mailtrap.

Parabéns! Acabou de enviar a sua primeira mensagem de correio eletrónico através do SeaTable - mesmo que tenha ido apenas para a caixa de correio virtual do Mailtrap.

{{< warning  headline="Enviar e-mails automaticamente"  text="Por agora, o envio dos e-mails é acionado com um clique num botão. Uma automação também pode tratar disso: as automações são abordadas no curso 4." />}}

## Artigo de ajuda com mais informações

- [Criação de uma conta de e-mail numa Base]({{< relref "help/base-editor/weitere-optionen/einrichtung-eines-e-mail-kontos-in-einer-base" >}})
- [Configurar o Gmail para enviar emails via SMTP]({{< relref "help/integrationen/integrationen-innerhalb-von-seatable/gmail-fuer-den-versand-von-e-mails-per-smtp-einrichten" >}})
- [O botão]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}})
- [Envio de um e-mail por botão]({{< relref "help/base-editor/schaltflaechen/eine-e-mail-per-schaltflaeche-verschicken" >}})
- [Envio de e-mails via automatização]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}})
