---
title: 'Passo 4: Recibo de caixa'
date: 2024-09-19
lastmod: '2024-09-24'
categories:
    - 'online-kurs-2'
author: 'cdb'
url: '/pt/ajuda/passo4-recebimento-pagamento-seatable'
aliases:
    - '/pt/ajuda/schritt-4-geldeingang'
seo:
    title: 'Passo 4 do Curso SeaTable 2: recebimento – botão e e-mail'
    description: 'No quarto passo, configure um botão no SeaTable para documentar pagamentos recebidos e enviar confirmação automática por e-mail no fluxo do curso.'
---

Depois de os participantes no curso receberem o pedido de pagamento por correio eletrónico, transferirão a taxa do curso para a sua conta bancária. Nesta altura, não automatizamos a verificação dos pagamentos recebidos. No entanto, faria sentido integrar um botão adicional na sua base que executasse duas tarefas:

1. Confirmação da receção do pagamento e, por conseguinte, da inscrição completa do participante no curso.
2. Documentação do processo de pagamento na base.

## Várias acções num só botão

Isto é fácil de implementar no SeaTable. Na tabela, adicione `Registrations` adiciona um novo botão que executa duas acções:

- Enviar uma mensagem eletrónica com uma confirmação de pagamento ao participante.
- O `Payment Status` sobre `Paid` definir.

Com os conhecimentos recentemente adquiridos, isso não deverá ser um problema. Pode utilizar o seguinte texto para a sua mensagem de correio eletrónico:

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

## Artigo de ajuda com mais informações

- [Criação de uma conta de e-mail numa Base]({{< relref "help/base-editor/weitere-optionen/einrichtung-eines-e-mail-kontos-in-einer-base" >}})
- [Configurar o Gmail para enviar emails via SMTP]({{< relref "help/integrationen/integrationen-innerhalb-von-seatable/gmail-fuer-den-versand-von-e-mails-per-smtp-einrichten" >}})
- [O botão]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}})
- [Envio de um e-mail por botão]({{< relref "help/base-editor/schaltflaechen/eine-e-mail-per-schaltflaeche-verschicken" >}})
- [Envio de e-mails via automatização]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}})
