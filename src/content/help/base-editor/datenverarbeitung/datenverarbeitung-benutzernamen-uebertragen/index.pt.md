---
title: 'Processamento de dados: Transferência de nomes de utilizador'
date: 2023-03-17
lastmod: '2023-03-17'
categories:
    - 'datenverarbeitung'
author: 'nsc2'
url: '/pt/ajuda/transferir-nomes-usuario-seatable'
aliases:
    - '/pt/ajuda/datenverarbeitung-benutzernamen-uebertragen'
seo:
    title: 'Transfira nomes de usuário rapidamente no SeaTable'
    description: 'Transfira nomes de usuário entre colunas SeaTable usando processamento de dados – para listas, filtros e fluxos automatizados.'
---

Usando a função de processamento de dados, é possível realizar várias operações através de uma coluna. A **transferência de nomes de utilizador** é uma operação que pode copiar dados de colunas do tipo [Colaborador]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}}), [Criador]({{< relref "help/base-editor/spaltentypen/die-spalten-ersteller-und-erstelldatum" >}}) ou [Último modificador]({{< relref "help/base-editor/spaltentypen/die-spalten-letzter-bearbeiter-und-bearbeitungsdatum" >}}) para uma [coluna de texto]({{< relref "help/base-editor/spaltentypen/die-text-spalte" >}}).

## Pôr em prática a operação

![Criar uma acção de tratamento de dados](images/create-an-data-processing-action-1.jpg)

1. Abrir qualquer **tabela** e clicar nos **três pontos** das opções de visualização.
2. Clique em **Data Processing** e depois em **Add Data Processing Operation**.
3. Dar um **nome** à operação e seleccionar **Transferir** nome de **utilizador**.

![Nomear a acção de tratamento de dados e seleccionar o tipo de operação](images/select-operation-and-name-example-name.jpg)

5. Definir **tabela**, **vista**, **coluna de origem** e **coluna de resultados**.

![Definição de tabela, vista, coluna de origem e coluna de resultados da operação](images/define-table-view-and-columns-example-name.png)

7. Clique em **Guardar para** guardar a acção e executá-la mais tarde, ou em **Executar** para executar a acção directamente.

A primeira vez que é executado com sucesso, um pequeno **carrapato verde**.  
![Se a acção de processamento de dados for executada com sucesso pela primeira vez, aparece uma marca verde](images/gruener-haken-zur-bestaetigung-der-ersten-ausfuehrung.jpg)

## Execução da operação

Se, por exemplo, mantiver uma tabela com tarefas a realizar na qual **os membros da** sua **equipa** são registados como pessoas de contacto responsáveis numa [coluna de pessoal]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}}), pode simplesmente copiar os nomes de utilizador para uma [coluna de texto]({{< relref "help/base-editor/spaltentypen/die-text-spalte" >}}), por exemplo para os utilizar para uma lista de pessoal.

Para tal, seguir os passos descritos acima e seleccionar a coluna do pessoal como coluna de **origem** e a coluna de texto como coluna de **resultado**.

![Definição da acção de tratamento de dados](images/name-operation-and-define-columns-example-name-1.png)

Se a operação for executada com sucesso, os **nomes de utilizador seleccionados** são extraídos da coluna de pessoal e transferidos para a coluna de texto separados por uma vírgula.

![Nomes de utilizador transferidos para uma coluna de texto ou resultado](images/table-after-operation-example-user-name.png)

{{< warning  headline="Nota importante"  text="Note-se que a cada nova execução desta operação, as entradas existentes na coluna de resultados são **sobrescritas**, desde que os nomes dos utilizadores na coluna de origem tenham sido alterados." />}}
