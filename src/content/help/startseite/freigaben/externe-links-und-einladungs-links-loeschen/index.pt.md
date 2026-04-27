---
title: 'Eliminar ligações externas e ligações de convite'
date: 2023-03-02
lastmod: '2023-03-02'
categories:
    - 'freigaben'
author: 'nsc2'
url: '/pt/ajuda/apagar-links-externos-convite'
aliases:
    - '/pt/ajuda/externe-links-und-einladungs-links-loeschen'
seo:
    title: 'Apagar links externos e de convite no SeaTable'
    description: 'Saiba como remover links externos e de convite compartilhados no SeaTable com segurança, direitos de acesso e efeitos da exclusão.'

---

Pode **apagar** tanto as **ligações externas** como as **ligações de convite** em qualquer altura de duas formas diferentes. Por favor, tenha em atenção as consequências que a eliminação tem para o acesso aos seus dados.

## Formas de eliminar ligações externas e ligações de convite

- Eliminação através do ícone de partilha {{< seatable-icon icon="dtable-icon-share" >}} para bases ou vistas
- Eliminação através da [administração da equipa]({{< relref "help/teamverwaltung/abonnement/die-funktionen-der-teamverwaltung-in-der-uebersicht" >}})

{{< warning  headline="Nota"  text="Estão disponíveis links externos para bases e vistas, links de convite apenas para bases." />}}

## Eliminação através do ícone de acção

![Clique no ícone de partilha na sua tabela](images/share-single-tablesheets-from-the-base-options.png)

1. Abrir uma **base** ou **vista para** a qual deseja apagar um link.
2. Clique no **ícone de partilha** {{< seatable-icon icon="dtable-icon-share" >}} para bases ou vistas.
3. Dependendo do tipo de link que pretende eliminar, clique em **Convite** ou **Link Externo**.
4. Mova o rato sobre o link e clique no **símbolo x**.

![Eliminar ligações externas e ligações de convite](images/delete-invitation-and-external-links.jpg)

## Eliminação através da administração da equipa

{{< warning  headline="Apenas para a equipa Admins"  text="Para aceder à administração da equipa, é necessário ser **administrador da equipa**." />}}

1. Ir para a **página inicial do** SeaTable e clicar na sua **imagem de avatar**.

![Acesso à gestão da equipa](images/Zugriff-auf-die-Teamverwaltung.png)

3. Abra a **gestão de equipa da** sua conta.
4. Clique em **Bases** na navegação.
5. Dependendo do tipo de link que pretende eliminar, clique em **Links de Convite** ou **Links Externos**.
6. Seleccione o **link** que pretende eliminar.
7. Confirmar a eliminação activando o **Controlador** e clique em **Eliminar link do convite** (para ligações de convite) ou **Apagar liberação** (para ligações externas).  
   ![Confirmar a eliminação](images/confirm-delete-invitation-and-external-links-way2.jpg)

{{< warning  headline="Só funciona com ligações de base" >}}

Não se pode eliminar uma [ligação externa para uma visualização]({{< relref "help/startseite/freigaben/externen-link-fuer-eine-ansicht-erstellen" >}}) através da administração da equipa, mas apenas através do ícone de partilha de visualizações.

{{< /warning >}}

## Consequências da eliminação

### Eliminação de um link de convite

A eliminação de um **link de convite** tem as seguintes **consequências**:

Se os utilizadores tentarem abrir um link de convite **eliminado**, aparece a seguinte **mensagem de erro**.

![Mensagem de erro ao abrir ligações de convite eliminadas](images/fehlermeldung-geloeschter-einladungs-link.jpg)

Depois de eliminar o link do convite, **nenhum outro utilizador** pode aceder à base partilhada.

{{< warning  headline="Os utilizadores convidados retêm o acesso" >}}

Os utilizadores que aceitaram o seu convite antes do link ter sido eliminado podem ainda aceder à base partilhada e estão listados nas [partilhas de utilizadores]({{< relref "help/startseite/freigaben/anlegen-einer-benutzerfreigabe" >}}). No entanto, é claro que pode apagar a partilha aí.

{{< /warning >}}

### Eliminação de uma ligação externa

A eliminação de uma **ligação externa** tem as seguintes **consequências**:

Se os utilizadores tentarem abrir uma ligação externa **eliminada**, aparece a seguinte **mensagem de erro**.

![Mensagem de erro ao apagar uma ligação externa](images/Fehlermeldung-bei-Loeschung-eines-externen-Links.png)

Após a eliminação de uma ligação externa, todos os utilizadores **perdem** consequentemente o acesso aos dados. Mesmo os sítios web nos quais tenha incorporado uma visualização através de uma ligação externa já não podem exibir os dados.
