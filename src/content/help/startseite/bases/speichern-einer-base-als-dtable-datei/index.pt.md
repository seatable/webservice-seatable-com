---
title: 'Exportar uma base como um ficheiro DTABLE'
date: 2023-01-11
lastmod: '2024-03-11'
categories:
    - 'import-von-daten'
author: 'kgr'
url: '/pt/ajuda/exportar-base-arquivo-dtable'
aliases:
    - '/pt/ajuda/speichern-einer-base-als-dtable-datei'
seo:
    title: 'Exportar Base SeaTable em arquivo DTABLE: passo a passo e pontos importantes'
    description: 'Exporte sua base SeaTable como arquivo DTABLE para backups ou transferências: conteúdo completo, sem histórico, observe o limite de tamanho.'
---

Pode exportar uma base como um ficheiro DTABLE em qualquer altura e, assim, guardar uma cópia de segurança completa no seu dispositivo. Pode descobrir como isto funciona e o que deve ter em conta no artigo seguinte.

## Para exportar uma base

![Base de exportação](images/Base-exportieren.png)

1. Ir para a **página inicial do** SeaTable.
2. Mova o ponteiro do rato para o nome da **base** que pretende exportar e clique no **ícone de três pontos** que aparece na extrema direita.
3. Seleccionar o item do menu **Exportar**.

[Exportação da base](images/export-base.png)

4. Decida se pretende incluir os **Assets** (por exemplo, imagens e ficheiros) e o último **backup de Big Data** no ficheiro de exportação, activando ou desactivando os controlos deslizantes.
5. Confirme com **Exportar**.

Dependendo das configurações do seu navegador, o **descarregamento** começará automaticamente ou ser-lhe-á perguntado onde pretende guardar o ficheiro de exportação. Se necessário, seleccionar um **local de armazenamento** adequado e confirmar a selecção.

Assim que o seu ficheiro com a extensão **.dtable** aparecer no local de armazenamento especificado, a exportação da base é concluída.

{{< warning  headline="Nota" >}}

Tenha em atenção que o **ficheiro DTABLE** pode tornar-se muito **grande** se tiver feito uso extensivo de colunas de ficheiros e imagens na base exportada. As bases com um **tamanho máximo de até 100 MB** podem ser exportadas no SeaTable Cloud. Pode utilizar o [gestor de ficheiros]({{< relref "help/base-editor/dateien/das-dateimanagement-einer-base" >}}) para **eliminar os anexos de ficheiros** em bases que excedam este limite de tamanho para permitir a exportação.

{{< /warning >}}

## O que é que um ficheiro DTABLE armazena?

O ficheiro DTABLE exportado contém o estado actual da sua base, incluindo todos os

- Quadros e vistas,
- Linhas, colunas e valores,
- Imagens e ficheiros,
- Formulários Web,
- Estatísticas,
- Guiões,
- Plugins e
- Aplicações.

{{< warning  headline="Atenção"  text="No entanto, um ficheiro DTABLE **não** guarda o histórico da base. Os instantâneos, os comentários, o conteúdo eliminado na reciclagem e o registo não são incluídos no ficheiro de exportação. Os dados no backend de Big Data também não são exportados para o ficheiro DTABLE." />}}

## Restaurar uma Base a partir de um ficheiro DTABLE

Pode **importar** um ficheiro DTABLE para o SeaTable como uma nova base em qualquer altura. Pode ler mais sobre isto no artigo [Criar uma Base a partir de um ficheiro DTABLE]({{< relref "help/startseite/import-von-daten/erstellen-einer-base-aus-einer-dtable-datei" >}}).
