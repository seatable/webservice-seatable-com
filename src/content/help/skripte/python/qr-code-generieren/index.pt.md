---
title: 'Exemplo Python: Gerar códigos QR'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/pt/ajuda/python-gerar-qr'
seo:
    title: 'Python: Gerar códigos QR no SeaTable'
    description: 'Gere códigos QR a partir de texto ou URLs e guarde-os como imagens diretamente no SeaTable com este script Python.'
---


Este script lê conteúdo de texto (por ex. URLs, IDs de produto) de uma coluna, gera imagens de códigos QR e guarda-as numa coluna de imagem. O script percorre todas as linhas da tabela e é portanto adequado para execução manual ou como automação — não como script de botão.

![QR Code Generator in SeaTable](qr-code-generator.png)

{{< dtable-download name="QR Code Generator" file="/downloads/python-examples/qr-code.dtable" text="Base com dados de exemplo e script pronto para experimentar diretamente." />}}

## Pré-requisitos

A tabela necessita de pelo menos duas colunas:

- Uma **coluna de texto** ou **URL** com o conteúdo a codificar como código QR.
- Uma **coluna de imagem** onde o código QR gerado será guardado.

## O script

Adapte as quatro variáveis no início à estrutura da sua tabela. O script ignora as linhas que não têm valor de texto ou que já contêm um código QR. Defina `OVERWRITE = True` para regenerar os códigos QR existentes.

```python
from seatable_api import Base, context
import qrcode
from io import BytesIO

base = Base(context.api_token, context.server_url)
base.auth()

TABLE_NAME = "Table1"
TEXT_COLUMN = "URL"
IMAGE_COLUMN = "QR Code"
OVERWRITE = False

rows = base.list_rows(TABLE_NAME)
for row in rows:
    text = row.get(TEXT_COLUMN)
    existing = row.get(IMAGE_COLUMN)
    if not text or (existing and not OVERWRITE):
        continue

    qr = qrcode.QRCode(version=2, error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=10, border=4)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    buf = BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)

    info = base.upload_bytes_file(str(text) + '.png', buf.read(), file_type='image')
    base.update_row(TABLE_NAME, row['_id'], {IMAGE_COLUMN: [info.get('url')]})

print("QR codes generated.")
```

## Execução

O script pode ser iniciado de três formas:

- **Manualmente** no editor Python da base
- **Por automação** (por ex. agendada ou ao criar novas linhas)
- **Por botão** — para isso o script teria de ser adaptado para processar apenas a linha atual

Saiba mais [aqui]({{< relref "help/skripte/allgemein/skript-manuell-per-schaltflaeche-oder-automation-ausfuehren" >}}).

Para a referência completa das funções, visite o [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
