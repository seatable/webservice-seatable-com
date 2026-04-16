---
title: 'Exemplo Python: Gerar códigos de barras'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/pt/ajuda/python-gerar-codigos-barras'
seo:
    title: 'Python: Gerar códigos de barras no SeaTable'
    description: 'Converta texto em imagens de código de barras (Code 128) e guarde-as no SeaTable com este script Python.'
---


Este script converte valores de texto (por ex. IDs de produto, números de série) em imagens de código de barras no formato Code 128 e guarda-as como imagens no SeaTable. O script percorre todas as linhas e ignora as que já têm um código de barras. É adequado para execução manual ou como automação.

![Barcode Generator in SeaTable](barcode-generator.png)

{{< dtable-download name="Barcode Generator" file="/downloads/python-examples/barcode-generator.dtable" text="Base com dados de exemplo e script pronto para experimentar diretamente." />}}

## Pré-requisitos

A tabela necessita de pelo menos duas colunas:

- Uma **coluna de texto** com o valor a codificar como código de barras (por ex. «Product ID»)
- Uma **coluna de imagem** onde o código de barras gerado será guardado (por ex. «Barcode»)

## O script

Adapte as três variáveis no início à estrutura da sua tabela. Pode personalizar a aparência do código de barras através das `options` (largura, altura, tamanho da fonte, etc.).

```python
from seatable_api import Base, context
import barcode
from barcode.writer import ImageWriter
from io import BytesIO

base = Base(context.api_token, context.server_url)
base.auth()

TABLE_NAME = "Table1"
TEXT_COLUMN = "Product ID"
IMAGE_COLUMN = "Barcode"

rows = base.list_rows(TABLE_NAME)
for row in rows:
    text = row.get(TEXT_COLUMN)
    existing = row.get(IMAGE_COLUMN)
    if not text or existing:
        continue

    code128 = barcode.get_barcode_class('code128')
    rv = code128(str(text), writer=ImageWriter())

    buf = BytesIO()
    rv.write(buf, options={"module_width": 0.4, "module_height": 10, "quiet_zone": 1, "font_size": 10, "text_distance": 2})
    buf.seek(0)

    info = base.upload_bytes_file(str(text) + '.png', buf.read(), file_type='image')
    base.update_row(TABLE_NAME, row['_id'], {IMAGE_COLUMN: [info.get('url')]})

print("Barcodes generated.")
```

## Execução

O script pode ser iniciado de três formas:

- **Manualmente** no editor Python da base
- **Por automação** (por ex. agendada ou ao criar novas linhas)
- **Por botão** — para isso o script teria de ser adaptado para processar apenas a linha atual

Saiba mais [aqui]({{< relref "help/skripte/allgemein/skript-manuell-per-schaltflaeche-oder-automation-ausfuehren" >}}).

Para a referência completa das funções, visite o [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
