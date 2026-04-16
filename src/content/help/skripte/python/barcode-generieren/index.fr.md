---
title: 'Exemple Python : Générer des codes-barres'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/fr/aide/python-generer-codes-barres'
seo:
    title: 'Python : Générer des codes-barres dans SeaTable'
    description: 'Convertissez du texte en images de codes-barres (Code 128) et enregistrez-les dans SeaTable avec ce script Python.'
---


Ce script convertit des valeurs textuelles (par ex. identifiants de produit, numéros de série) en images de codes-barres au format Code 128 et les enregistre comme images dans SeaTable. Le script parcourt toutes les lignes et ignore celles qui ont déjà un code-barres. Il convient à une exécution manuelle ou comme automation.

![Barcode Generator in SeaTable](barcode-generator.png)

{{< dtable-download name="Barcode Generator" file="/downloads/python-examples/barcode-generator.dtable" text="Base avec données d'exemple et script prêt à l'emploi pour essayer directement." />}}

## Prérequis

La table nécessite au moins deux colonnes :

- Une **colonne texte** avec la valeur à encoder en code-barres (par ex. « Product ID »)
- Une **colonne image** où le code-barres généré sera enregistré (par ex. « Barcode »)

## Le script

Adaptez les trois variables au début à la structure de votre table. Vous pouvez personnaliser l'apparence du code-barres via les `options` (largeur, hauteur, taille de police, etc.).

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

## Exécution

Le script peut être lancé de trois manières :

- **Manuellement** dans l'éditeur Python de la base
- **Par automation** (par ex. planifiée ou lors de nouvelles lignes)
- **Par bouton** — pour cela, le script devrait être adapté pour ne traiter que la ligne actuelle

En savoir plus [ici]({{< relref "help/skripte/allgemein/skript-manuell-per-schaltflaeche-oder-automation-ausfuehren" >}}).

Pour la référence complète des fonctions, consultez le [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
