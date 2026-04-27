---
title: 'Scripts Python : Questions fréquentes'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/fr/aide/python-questions-frequentes'
seo:
    title: 'Scripts Python dans SeaTable : Questions fréquentes'
    description: 'Réponses aux questions fréquentes sur les scripts Python dans SeaTable : bibliothèques supportées, opérations par lot, exécution locale et conseils de débogage.'
weight: 2
star: true
---

## Comment exécuter un script à la fois localement et dans SeaTable ?

Vous pouvez écrire votre script de manière à ce qu'il fonctionne dans les deux environnements sans modification. L'astuce consiste à vérifier si l'objet `context` est disponible :

```python
from seatable_api import Base

try:
    from seatable_api import context
    base = Base(context.api_token, context.server_url)
except:
    base = Base('your-api-token', 'https://cloud.seatable.io')

base.auth()
```

## Quelles bibliothèques sont disponibles ?

Une liste complète de toutes les bibliothèques préinstallées se trouve dans l'article [Bibliothèques Python supportées]({{< relref "help/skripte/python/unterstuetzte-python-bibliotheken" >}}). Vous y apprendrez également comment ajouter des bibliothèques personnalisées sur un serveur auto-hébergé.

## Comment traiter plus de 1 000 lignes ?

La méthode `base.list_rows()` renvoie par défaut un maximum de 1 000 lignes. Pour traiter plus de lignes, utilisez l'une de ces approches :

**Option 1 : Boucle avec offset**
```python
all_rows = []
offset = 0
while True:
    rows = base.list_rows(TABLE_NAME, start=offset, limit=1000)
    if not rows:
        break
    all_rows.extend(rows)
    offset += 1000
```

**Option 2 : Requête SQL**
```python
rows = base.query("SELECT * FROM `Table1` LIMIT 10000")
```

Les requêtes SQL supportent jusqu'à 10 000 lignes par requête.

## Comment déboguer des structures de données complexes ?

Utilisez `json.dumps()` avec indentation pour afficher les dictionnaires et listes de manière formatée :

```python
import json
metadata = base.get_metadata()
print(json.dumps(metadata, indent=2))
```

Pour la référence complète des fonctions, consultez le [SeaTable Developer Manual](https://developer.seatable.com/python/).
