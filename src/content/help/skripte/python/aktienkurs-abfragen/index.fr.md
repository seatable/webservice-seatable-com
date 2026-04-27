---
title: 'Exemple Python : Consulter les cours boursiers'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/fr/aide/python-cours-boursiers'
seo:
    title: 'Python : Récupérer les cours boursiers dans SeaTable'
    description: 'Récupérez les cours boursiers actuels depuis une API externe et mettez à jour votre table SeaTable avec ce script Python.'
---


Ce script récupère les cours boursiers actuels depuis l'API Twelve Data et inscrit les prix dans une table SeaTable. Il montre comment appeler des API externes depuis un script Python SeaTable. Le script parcourt toutes les lignes et convient à une exécution manuelle ou comme automation planifiée.

![Stock Prices in SeaTable](stock-prices.png)

{{< dtable-download name="Stock Prices" file="/downloads/python-examples/stock-prices.dtable" text="Base avec données d'exemple et script prêt à l'emploi pour essayer directement." />}}

## Prérequis

- Une clé API gratuite de [Twelve Data](https://twelvedata.com/)
- Une table avec les colonnes `Symbol` (texte) et `Price` (nombre)

## Le script

Saisissez votre clé API dans `API_KEY`. Le script vérifie si une clé valide est définie et s'arrête immédiatement en cas d'erreur API.

```python
from seatable_api import Base, context
import requests

base = Base(context.api_token, context.server_url)
base.auth()

TABLE_NAME = "Stocks"
API_KEY = "your-api-key"

if API_KEY == "your-api-key":
    print("ERROR: Please set your Twelve Data API key first.")
    print("Get a free key at https://twelvedata.com/")
else:
    rows = base.list_rows(TABLE_NAME)
    for row in rows:
        symbol = row.get('Symbol')
        if not symbol:
            continue

        url = f"https://api.twelvedata.com/price?symbol={symbol}&apikey={API_KEY}"
        response = requests.get(url)
        data = response.json()

        if 'price' in data:
            base.update_row(TABLE_NAME, row['_id'], {
                'Price': float(data['price'])
            })
            print(f"{symbol}: {data['price']}")
        else:
            print(f"API error: {data.get('message', 'unknown error')}")
            break

    print("---")
    print("Stock prices updated.")
```

Vous pouvez remplacer l'API Twelve Data par un autre fournisseur de données financières. Adaptez l'URL et le traitement de la réponse en conséquence.

Pour la référence complète des fonctions, consultez le [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
