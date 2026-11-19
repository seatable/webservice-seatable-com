---
title: 'Migration von NocoDB Bases zu SeaTable'
date: 2026-11-19
lastmod: '2026-11-19'
categories:
    - 'import-von-daten'
author: 'bha'
url: '/de/hilfe/migration-von-nocodb-bases-zu-seatable'
seo:
    title: 'NocoDB Bases per Skript nach SeaTable migrieren'
    description: 'Erfahren Sie, wie Sie eine NocoDB Base inklusive Verknüpfungen, Lookups und Formeln per Python-Skript nach SeaTable übertragen und das Ergebnis prüfen.'
---

Sie wollen Ihre NocoDB Bases zu SeaTable umziehen? Mit dem in diesem Artikel vorgestellten Migrationsskript übertragen Sie eine NocoDB Base **inklusive Verknüpfungen** nach SeaTable, und zwar direkt aus dem Skripteditor von SeaTable. Python-Grundkenntnisse sind von Vorteil, aber nicht notwendig.

## So migrieren Sie eine Base per Skript von NocoDB zu SeaTable

Das Migrationsskript liest Ihre NocoDB Base über die NocoDB API aus und legt deren Tabellen, Spalten, Zeilen, Verknüpfungen, Lookups, Rollups und Formeln in einer SeaTable Base neu an. Ein zweites Skript vergleicht anschließend NocoDB und SeaTable, damit Sie prüfen können, dass unterwegs nichts verloren gegangen ist.

Es sind nur wenige **manuelle Angaben** erforderlich, um die Skripte betriebsbereit zu machen. Nach der Migration sind noch ein paar Nacharbeiten notwendig. In diesem Artikel erklären wir, wie Sie das machen.

{{< warning  type="warning" headline="Wichtiger Hinweis"  text="Das Migrationsskript ist funktional, aber noch beta: Es wurde nur mit einer Test-Base getestet, die vermutlich nicht alle Fälle abdeckt. Die Skripte werden ohne jegliche Gewährleistung bereitgestellt, ihre Nutzung erfolgt auf eigenes Risiko. Prüfen Sie Ihre Daten nach der Migration immer. Bei Problemen hinterlassen Sie bitte einen Post im [SeaTable Forum](https://forum.seatable.com/)." />}}

### 1\. Base anlegen

Erstellen Sie in SeaTable eine [neue Base]({{< relref "help/startseite/bases/eine-neue-base-erstellen" >}}). Der Name der SeaTable Base muss nicht dem Namen der zu importierenden NocoDB Base entsprechen. Sie können den Namen frei wählen.

### 2\. Skript einfügen

Öffnen Sie in der neuen Base die [Skript-Seitenleiste]({{< relref "help/skripte/allgemein/anlegen-und-loeschen-eines-skriptes" >}}) durch einen Klick auf das Skript-Icon {{< seatable-icon icon="dtable-icon-script" >}} im Base-Header oben rechts. Wählen Sie dann **Skript hinzufügen**. Das Migrationsskript ist in der Programmiersprache Python geschrieben. Wählen Sie daher **Python** aus.

Markieren Sie nun den folgenden Codeblock, kopieren Sie ihn in den Zwischenspeicher und fügen Sie ihn dann in das linke Fenster des Skripteditors ein:

```python
"""
Migrate a NocoDB base (Cloud, API v2) to the current SeaTable base.

Usage
-----
1. Create a Python script in the target SeaTable base and paste this file into it.
2. Fill in the CONFIGURATION section (NocoDB token and base ID).
3. Run it once with SIMULATION = True to see what would be done, then with SIMULATION = False.
The SeaTable token is provided automatically by the script context.

Running from a local IDE (e.g. if the SeaTable editor stops the script because it runs too
long): pip install seatable-api requests, then set SEATABLE_API_TOKEN (and SEATABLE_SERVER_URL
for a self-hosted server) in the CONFIGURATION section.

Security: a script stored in a base can be read by the collaborators of that base.
Remove the NocoDB token from the script once the migration is done.

Steps
-----
1. Read NocoDB: tables, columns (types, options, formulas, links), records, links.
2. Create the tables and simple columns in SeaTable, then insert the rows.
3. Create the link columns (one per NocoDB relation, both sides) and the links.
4. Create the computed columns: formulas as formula columns, lookups and rollups as link-formula
   columns (formula column as a fallback). Columns that cannot be recreated are imported as
   static values. Everything that needs checking is listed in the final report.
"""

import json
import re
import time

import requests
from seatable_api import Base, context
from seatable_api.constants import ColumnTypes

# ============================== CONFIGURATION ==============================

# SeaTable: filled in automatically when run from the SeaTable script editor.
# To run from a local IDE (no execution time limit), replace '' with the base API token
# and, for a self-hosted server, the server URL.
SEATABLE_SERVER_URL = context.server_url or 'https://cloud.seatable.io'
SEATABLE_API_TOKEN = context.api_token or ''   # API token of the target base (read-write)

NOCODB_URL = 'https://app.nocodb.com'
NOCODB_TOKEN = ''           # NocoDB: Account > API Tokens
NOCODB_BASE_ID = ''         # starts with "p", visible in the NocoDB URL

SIMULATION = True           # True: read NocoDB and log what would be done, without changing SeaTable

ONLY_TABLES = None          # e.g. ['Customers', 'Orders']; None = all tables
TABLE_PREFIX = ''           # prefix added to the names of the tables created in SeaTable
ID_COLUMN = 'NocoDB ID'     # column holding the original record ID (traceability); None = no column
IMPORT_ATTACHMENTS = True   # download attachments and upload them to SeaTable
PERCENT_AS_FRACTION = True  # NocoDB stores 50 for 50 %; SeaTable (percent format) expects 0.5
PREFER_LINK_FORMULA = True  # lookups/rollups as link-formula columns (falls back to formula columns)

NOCODB_MAX_REQUESTS_PER_SECOND = 4  # NocoDB Cloud allows 5 requests/s per user: stay below

# ===========================================================================

REPORT = []


def log(msg):
    print(msg, flush=True)


def warn(msg):
    REPORT.append(msg)
    log('  ! ' + msg)


def plan(msg):
    """Log an action that is only simulated."""
    log('  [simulation] ' + msg)


def chunks(items, size=1000):
    for i in range(0, len(items), size):
        yield items[i:i + size]


def as_dict(value):
    if isinstance(value, str):
        try:
            return json.loads(value)
        except ValueError:
            return {}
    return value or {}


# ------------------------------- NocoDB ------------------------------------

class NocoDB:
    def __init__(self, url, token):
        self.url = url.rstrip('/')
        self.session = requests.Session()
        self.session.headers['xc-token'] = token
        self._last = 0.0

    def get(self, path, **params):
        for attempt in range(6):
            wait = 1 / NOCODB_MAX_REQUESTS_PER_SECOND - (time.time() - self._last)
            if wait > 0:
                time.sleep(wait)
            self._last = time.time()
            r = self.session.get(self.url + path, params=params, timeout=60)
            if r.status_code == 429:
                delay = int(r.headers.get('Retry-After', 30))
                log(f'  (NocoDB rate limit reached, waiting {delay} s)')
                time.sleep(delay)
                continue
            if r.status_code >= 500 and attempt < 5:
                time.sleep(2 ** attempt)
                continue
            r.raise_for_status()
            return r.json()
        raise RuntimeError(f'NocoDB: repeated failure on {path}')

    def paged(self, path, **params):
        rows, offset = [], 0
        while True:
            data = self.get(path, limit=1000, offset=offset, **params)
            page = data.get('list') or []
            rows.extend(page)
            if not page or (data.get('pageInfo') or {}).get('isLastPage', True):
                return rows
            offset += len(page)

    def download(self, url):
        r = self.session.get(url, timeout=120)
        r.raise_for_status()
        return r.content


LINK_UIDTS = ('Links', 'LinkToAnotherRecord')
COMPUTED_UIDTS = ('Formula', 'Lookup', 'Rollup')
SKIPPED_UIDTS = ('ID', 'ForeignKey', 'Button', 'Barcode', 'QrCode', 'Count')

# "Many to one" sides: the record list already contains the linked object,
# which avoids one call to the links API per record.
TO_ONE_TYPES = ('bt', 'mo', 'oo')


def pair_link_columns(tables):
    """Group the two NocoDB columns that represent the same relation.

    Depending on the NocoDB version, relation types are hm/bt/mm/oo or om/mo/mm/oo, and the foreign
    key columns may be swapped from one side to the other: we therefore compare the set of technical
    IDs of the relation and, failing that, pair the remaining columns that point at each other.
    """
    groups = {}
    for t in tables:
        for c in t['columns']:
            if c['uidt'] not in LINK_UIDTS:
                continue
            o = c.get('colOptions') or {}
            ids = frozenset(v for k in ('fk_mm_model_id', 'fk_child_column_id', 'fk_parent_column_id')
                            if (v := o.get(k)))
            key = ids or ('col', c['id'])
            groups.setdefault(key, []).append((t, c))

    paired = [g for g in groups.values() if len(g) > 1]
    single = [g[0] for g in groups.values() if len(g) == 1]
    while single:
        t, c = single.pop(0)
        target = (c.get('colOptions') or {}).get('fk_related_model_id')
        mates = [s for s in single if s[0]['id'] == target
                 and (s[1].get('colOptions') or {}).get('fk_related_model_id') == t['id']
                 and s[1]['id'] != c['id']]
        if len(mates) == 1:
            single.remove(mates[0])
            paired.append([(t, c), mates[0]])
        else:
            if mates:
                warn(f'Link "{t["title"]}.{c["title"]}": ambiguous opposite side, imported on its own')
            paired.append([(t, c)])
    return paired


def extract(noco, base_id):
    """Read the whole NocoDB base and return a self-contained dict."""
    log('== Reading NocoDB')
    tables = []
    for t in noco.get(f'/api/v2/meta/bases/{base_id}/tables').get('list', []):
        if t.get('mm') or (ONLY_TABLES and t['title'] not in ONLY_TABLES):
            continue  # many-to-many junction tables: handled through the links
        meta = noco.get(f'/api/v2/meta/tables/{t["id"]}')
        cols = meta.get('columns', [])
        for c in cols:
            c['meta'] = as_dict(c.get('meta'))
        pk = next((c['title'] for c in cols if c.get('pk')), 'Id')
        user_cols = [c for c in cols if not c.get('system') and not c.get('pk')]
        pv = next((c['title'] for c in user_cols if c.get('pv')), user_cols[0]['title'] if user_cols else pk)
        log(f'  {t["title"]}: {len(user_cols)} columns')
        records = noco.paged(f'/api/v2/tables/{t["id"]}/records')
        log(f'    {len(records)} records')
        tables.append({'id': t['id'], 'title': t['title'], 'pk': pk, 'pv': pv,
                       'columns': user_cols, 'records': records})

    by_id = {t['id']: t for t in tables}

    # Group both sides of each relation; read the links from one side only
    relations = []
    for sides in pair_link_columns(tables):
        sides.sort(key=lambda s: (s[1].get('colOptions') or {}).get('type') not in TO_ONE_TYPES)
        src_t, src_c = sides[0]
        target_id = (src_c.get('colOptions') or {}).get('fk_related_model_id')
        if target_id not in by_id:
            warn(f'Link "{src_t["title"]}.{src_c["title"]}" points to a table that is not imported: skipped')
            continue
        tgt_t = by_id[target_id]
        other = next((s for s in sides[1:]), None)
        log(f'  links {src_t["title"]}.{src_c["title"]} -> {tgt_t["title"]}')
        pairs = {}
        for rec in src_t['records']:
            ids = linked_ids(noco, src_t, src_c, tgt_t, rec)
            if ids:
                pairs[str(rec[src_t['pk']])] = ids
        relations.append({
            'source_table': src_t['id'], 'source_title': src_c['title'],
            'target_table': tgt_t['id'], 'target_title': other[1]['title'] if other else None,
            'type': (src_c.get('colOptions') or {}).get('type'),
            'pairs': pairs,
        })
    return {'tables': tables, 'relations': relations}


def linked_ids(noco, table, col, target, rec):
    value = rec.get(col['title'])
    pk = target['pk']

    def rid(v):
        if isinstance(v, dict):
            return str(v.get(pk, v.get('Id', v.get('id'))))
        return str(v)

    if value is None or value == 0 or value == []:
        return []
    if isinstance(value, dict):
        return [rid(value)]
    if isinstance(value, list):
        return [rid(v) for v in value]
    # A numeric value is the number of links: query the links API
    path = f'/api/v2/tables/{table["id"]}/links/{col["id"]}/records/{rec[table["pk"]]}'
    return [rid(v) for v in noco.paged(path)]


# ------------------------------ SeaTable -----------------------------------

def st(fn, *args, **kwargs):
    """SeaTable call, retried when the rate limit is hit."""
    for attempt in range(5):
        try:
            return fn(*args, **kwargs)
        except Exception as e:
            if ('429' in str(e) or 'too many' in str(e).lower()) and attempt < 4:
                time.sleep(15 * (attempt + 1))
                continue
            raise


FALLBACK_TYPES = {'EMAIL': 'TEXT', 'RATE': 'NUMBER', 'DURATION': 'NUMBER', 'URL': 'TEXT'}
PRIMARY_OK = {'TEXT', 'NUMBER', 'DATE', 'EMAIL', 'URL', 'AUTO_NUMBER'}
CURRENCIES = {'USD': 'dollar', 'EUR': 'euro', 'CNY': 'yuan'}


def number_format(fmt, precision):
    # SeaTable rejects a partial column_data: decimal and thousands separators are mandatory
    return {'format': fmt, 'decimal': 'dot', 'thousands': 'no',
            'enable_precision': bool(precision), 'precision': int(precision or 0)}


def rate_format(meta):
    # SeaTable needs the full rating configuration, otherwise the icons are drawn without color.
    # Defaults observed on a rating column created in the SeaTable UI; the NocoDB color is kept.
    color = meta.get('color')
    return {'rate_max_number': int(meta.get('max') or 5),
            'rate_style_color': color if isinstance(color, str) and color.startswith('#') else '#FF8000',
            'rate_style_type': rate_icon(meta),
            'enable_fill_default_value': False, 'default_value': ''}


# NocoDB rating icons -> SeaTable rate_style_type. NocoDB circles have no SeaTable equivalent: stars.
RATE_ICONS = {'heart': 'dtable-icon-like', 'thumb': 'dtable-icon-praise', 'flag': 'dtable-icon-flag'}
# Order of the icons in the NocoDB picker (meta.iconIdx): star, heart, circle, thumbs up, flag
RATE_ICON_INDEX = {1: 'dtable-icon-like', 3: 'dtable-icon-praise', 4: 'dtable-icon-flag'}


def rate_icon(meta):
    icon = meta.get('icon')
    name = str(icon.get('full', '') if isinstance(icon, dict) else icon or '').lower()
    for word, style in RATE_ICONS.items():
        if word in name:
            return style
    if not name and isinstance(meta.get('iconIdx'), int):
        return RATE_ICON_INDEX.get(meta['iconIdx'], 'dtable-icon-rate')
    return 'dtable-icon-rate'


def column_spec(col):
    """SeaTable type (ColumnTypes member name) and column_data for a simple NocoDB column."""
    u, meta = col['uidt'], col.get('meta') or {}
    if u in ('LongText', 'JSON'):
        return 'LONG_TEXT', None
    if u == 'Email':
        return 'EMAIL', None
    if u == 'URL':
        return 'URL', None
    if u in ('Number', 'Year', 'AutoNumber'):
        return 'NUMBER', number_format('number', 0)
    if u == 'Decimal':
        return 'NUMBER', number_format('number', meta.get('precision', 2))
    if u == 'Currency':
        code = meta.get('currency_code') or 'USD'   # NocoDB displays USD when no currency is set
        fmt = CURRENCIES.get(code, 'number')
        if fmt == 'number':
            warn(f'Currency {code} of "{col["title"]}" not supported: plain number format')
        return 'NUMBER', number_format(fmt, 2)
    if u == 'Percent':
        return 'NUMBER', number_format('percent', meta.get('precision', 0))
    if u == 'Rating':
        return 'RATE', rate_format(meta)
    if u == 'Duration':
        return 'DURATION', {'format': 'duration', 'duration_format': 'h:mm:ss'}
    if u == 'Checkbox':
        return 'CHECKBOX', None
    if u == 'Date':
        return 'DATE', {'format': 'YYYY-MM-DD'}
    if u in ('DateTime', 'CreatedTime', 'LastModifiedTime'):
        return 'DATE', {'format': 'YYYY-MM-DD HH:mm'}
    if u == 'SingleSelect':
        return 'SINGLE_SELECT', None
    if u == 'MultiSelect':
        return 'MULTIPLE_SELECT', None
    if u == 'Attachment':
        return 'FILE', None
    return 'TEXT', None  # SingleLineText, PhoneNumber, GeoData, Time, User, CreatedBy, …


def resolve_type(kind):
    while getattr(ColumnTypes, kind, None) is None:
        kind = FALLBACK_TYPES.get(kind, 'TEXT')
    return kind, getattr(ColumnTypes, kind)


def to_text(value):
    if value is None:
        return None
    if isinstance(value, list):
        return ', '.join(t for t in (to_text(v) for v in value) if t)
    if isinstance(value, dict):
        for k in ('email', 'display_name', 'title', 'name'):
            if value.get(k):
                return str(value[k])
        return json.dumps(value, ensure_ascii=False)
    return str(value)


def split_multi(value):
    if value is None:
        return []
    if isinstance(value, list):
        return [str(v) for v in value]
    return [v.strip() for v in str(value).split(',') if v.strip()]


def to_date(value):
    if not value:
        return None
    s = str(value).replace('T', ' ')
    return s[:10] if len(s) <= 10 else s.replace(' ', 'T', 1)  # ISO 8601 with time zone


# NocoDB rollup function -> SeaTable summary method (same name in link-formula columns and in
# the rollup() formula function), or 'count_links'. countDistinct, sumDistinct and avgDistinct
# have no SeaTable equivalent and are imported as static values.
ROLLUP_FUNCTIONS = {
    'sum': 'sum',
    'avg': 'average',
    'min': 'min',
    'max': 'max',
    'count': 'count_links',
}

# NocoDB functions whose name differs in SeaTable (same arguments)
FUNCTION_NAMES = {'CONCAT': 'concatenate', 'AVG': 'average', 'SUBSTR': 'mid', 'REPLACE': 'substitute'}


def lookup_array_type(target):
    """array_type / array_data of a lookup, from the looked-up SeaTable column.

    Observed in the SeaTable UI: a lookup of a text column gives ('text', None); a lookup of a
    formula column returning a number gives ('number', {}), i.e. the formula's result type.
    """
    ctype, data = target.get('type'), target.get('data') or {}
    if ctype in ('formula', 'link-formula'):
        result = data.get('result_type')
        if result == 'array':  # the target is itself a lookup: reuse its element type
            return data.get('array_type') or 'text', data.get('array_data')
        return result or 'string', {}
    return ctype, target.get('data')


def translate_formula(formula):
    """Rename functions outside of strings and {column} references. Everything else is kept."""
    out, i = [], 0
    while i < len(formula):
        ch = formula[i]
        if ch in '"\'':
            j = formula.find(ch, i + 1)
            j = len(formula) if j < 0 else j + 1
            out.append(formula[i:j]); i = j
        elif ch == '{':
            j = formula.find('}', i)
            j = len(formula) if j < 0 else j + 1
            out.append(formula[i:j]); i = j
        else:
            m = re.match(r'([A-Za-z_][A-Za-z0-9_]*)(\s*\()', formula[i:])
            if m:
                fn = m.group(1)
                out.append(FUNCTION_NAMES.get(fn.upper(), fn.lower()) + m.group(2))
                i += m.end()
            else:
                out.append(ch); i += 1
    return ''.join(out)


class Importer:
    def __init__(self, data, noco):
        self.data = data
        self.noco = noco
        self.base = Base(SEATABLE_API_TOKEN, SEATABLE_SERVER_URL)
        self.base.auth()
        self.tables = data['tables']
        self.tname = {t['id']: TABLE_PREFIX + t['title'] for t in self.tables}
        self.col_by_id = {c['id']: (t, c) for t in self.tables for c in t['columns']}
        self.created = {t['id']: set() for t in self.tables}   # columns that exist in SeaTable
        self.row_map = {t['id']: {} for t in self.tables}      # NocoDB ID -> SeaTable _id
        self.kinds = {}                                        # column id -> chosen SeaTable type

    # --- columns ----------------------------------------------------------

    def add_column(self, table, name, kind, column_data=None, retry_without_data=True):
        kind, ctype = resolve_type(kind)
        tname = self.tname[table['id']]
        if SIMULATION:
            plan(f'add column {tname}.{name} ({ctype.value})')
        else:
            try:
                st(self.base.insert_column, tname, name, ctype, column_data=column_data)
            except Exception as e:
                if not column_data or not retry_without_data:
                    raise
                warn(f'{tname}.{name}: column options rejected ({e}), created without options')
                st(self.base.insert_column, tname, name, ctype)
        self.created[table['id']].add(name)
        return kind

    def add_select_options(self, table, col):
        values = []
        for o in (col.get('colOptions') or {}).get('options', []):
            values.append((o['title'], o.get('color') or '#e9e9e9'))
        known = {v for v, _ in values}
        for rec in table['records']:
            for v in split_multi(rec.get(col['title'])):
                if v not in known:
                    known.add(v)
                    values.append((v, '#e9e9e9'))
        if not values:
            return
        if SIMULATION:
            plan(f'    {len(values)} options: {", ".join(v for v, _ in values)}')
            return
        options = [{'name': v, 'color': c, 'textColor': '#212529'} for v, c in values]
        st(self.base.add_column_options, self.tname[table['id']], col['title'], options)

    def create_tables(self):
        log('== Creating tables')
        existing = {t['name'] for t in st(self.base.list_tables)}
        clash = [n for n in self.tname.values() if n in existing]
        if clash:
            msg = f'Tables already exist in SeaTable: {clash}. Use TABLE_PREFIX or delete them.'
            if not SIMULATION:
                raise SystemExit(msg)
            warn(msg)

        for t in self.tables:
            name = self.tname[t['id']]
            pv = next(c for c in t['columns'] if c['title'] == t['pv']) if t['columns'] else None
            kind, cdata = column_spec(pv) if pv and pv['uidt'] not in COMPUTED_UIDTS + LINK_UIDTS else ('TEXT', None)
            kind, ctype = resolve_type(kind)
            if kind not in PRIMARY_OK:
                kind, ctype, cdata = 'TEXT', ColumnTypes.TEXT, None
            if pv and pv['uidt'] in COMPUTED_UIDTS:
                warn(f'{name}.{pv["title"]} (display column, {pv["uidt"]}) imported as static text')
            primary = {'column_name': t['pv'], 'column_type': ctype.value}
            if cdata:
                primary['column_data'] = cdata
            log(f'  {name}')
            if SIMULATION:
                plan(f'create table {name} (first column {t["pv"]}, {ctype.value})')
            else:
                self._add_table(name, primary)
            self.created[t['id']].add(t['pv'])
            if pv:
                self.kinds[pv['id']] = kind

            if ID_COLUMN:
                self.add_column(t, ID_COLUMN, 'TEXT')
            for c in t['columns']:
                if c['title'] == t['pv'] or c['uidt'] in COMPUTED_UIDTS + LINK_UIDTS:
                    continue
                if c['uidt'] in SKIPPED_UIDTS:
                    warn(f'{name}.{c["title"]} ({c["uidt"]}) not imported')
                    continue
                kind, cdata = column_spec(c)
                self.kinds[c['id']] = self.add_column(t, c['title'], kind, cdata)
                if c['uidt'] in ('User', 'CreatedBy', 'LastModifiedBy'):
                    warn(f'{name}.{c["title"]} ({c["uidt"]}) imported as text (email addresses)')
                if kind in ('SINGLE_SELECT', 'MULTIPLE_SELECT'):
                    self.add_select_options(t, c)

    def _add_table(self, name, primary):
        attempts = [[primary], [{k: v for k, v in primary.items() if k != 'column_data'}]]
        for cols in attempts:
            try:
                return st(self.base.add_table, name, lang='en', columns=cols)
            except Exception:
                if name in {t['name'] for t in st(self.base.list_tables)}:
                    break
        else:
            st(self.base.add_table, name, lang='en')
        first = st(self.base.list_columns, name)[0]
        if first['name'] != primary['column_name']:
            st(self.base.rename_column, name, first['key'], primary['column_name'])

    # --- rows -------------------------------------------------------------

    def convert(self, col, value):
        u, kind = col['uidt'], self.kinds.get(col['id'], 'TEXT')
        if value is None or value == '':
            return None
        if kind == 'TEXT' or kind == 'LONG_TEXT':
            return to_text(value) if not isinstance(value, (dict, list)) or u != 'JSON' \
                else json.dumps(value, ensure_ascii=False)
        if kind == 'NUMBER':
            try:
                n = float(value)
            except (TypeError, ValueError):
                return None
            if u == 'Percent' and PERCENT_AS_FRACTION:
                n /= 100
            return int(n) if n.is_integer() and u not in ('Decimal', 'Currency', 'Percent') else n
        if kind in ('RATE', 'DURATION'):
            return value
        if kind == 'CHECKBOX':
            return bool(value) and value not in ('false', '0')
        if kind == 'DATE':
            return to_date(value)
        if kind == 'SINGLE_SELECT':
            return str(value)
        if kind == 'MULTIPLE_SELECT':
            return split_multi(value)
        if kind == 'FILE':
            return self.upload_files(value) if IMPORT_ATTACHMENTS else None
        return value

    def upload_files(self, attachments):
        attachments = attachments or []
        if SIMULATION:
            self.simulated_files += len(attachments)
            return None
        files = []
        for a in attachments:
            url = a.get('signedUrl') or a.get('url')
            if not url and (a.get('signedPath') or a.get('path')):
                url = NOCODB_URL.rstrip('/') + '/' + (a.get('signedPath') or a['path']).lstrip('/')
            name = a.get('title') or 'file'
            try:
                files.append(st(self.base.upload_bytes_file, name, self.noco.download(url), file_type='file'))
            except Exception as e:
                warn(f'Attachment "{name}" not transferred: {e}')
        return files or None

    def insert_rows(self):
        log('== Inserting rows')
        for t in self.tables:
            name = self.tname[t['id']]
            cols = [c for c in t['columns'] if c['id'] in self.kinds]
            pv_static = next((c for c in t['columns'] if c['title'] == t['pv'] and c['id'] not in self.kinds), None)
            self.simulated_files = 0
            rows, ids = [], []
            for rec in t['records']:
                row = {c['title']: self.convert(c, rec.get(c['title'])) for c in cols}
                if pv_static:
                    row[t['pv']] = to_text(rec.get(t['pv']))
                if ID_COLUMN:
                    row[ID_COLUMN] = str(rec[t['pk']])
                rows.append({k: v for k, v in row.items() if v is not None})
                ids.append(str(rec[t['pk']]))
            if SIMULATION:
                self.row_map[t['id']] = {i: f'sim-{i}' for i in ids}
                files = f', {self.simulated_files} attachment(s) to transfer' if self.simulated_files else ''
                plan(f'insert {len(rows)} rows into {name} in {-(-len(rows) // 1000)} batch(es){files}')
                continue
            for start in range(0, len(rows), 1000):
                res = st(self.base.batch_append_rows, name, rows[start:start + 1000])
                new_ids = [r['_id'] for r in (res or {}).get('row_ids', [])]
                if len(new_ids) != len(rows[start:start + 1000]):
                    raise RuntimeError(f'{name}: SeaTable did not return the IDs of the created rows')
                self.row_map[t['id']].update(zip(ids[start:start + 1000], new_ids))
            log(f'  {name}: {len(rows)} rows')

    # --- links ------------------------------------------------------------

    def create_links(self):
        log('== Links')
        for rel in self.data['relations']:
            src = next(t for t in self.tables if t['id'] == rel['source_table'])
            tgt = next(t for t in self.tables if t['id'] == rel['target_table'])
            s_name, t_name, title = self.tname[src['id']], self.tname[tgt['id']], rel['source_title']
            wanted = rel['target_title'] or src['title']

            src_map, tgt_map = self.row_map[src['id']], self.row_map[tgt['id']]
            links, missing = {}, 0
            for s_id, t_ids in rel['pairs'].items():
                targets = [tgt_map[i] for i in t_ids if i in tgt_map]
                missing += len(t_ids) - len(targets)
                if s_id in src_map and targets:
                    links[src_map[s_id]] = targets
            if missing:
                warn(f'{s_name}.{title}: {missing} link(s) to rows that could not be found')

            self.created[src['id']].add(title)
            if SIMULATION:
                if src['id'] != tgt['id']:
                    self.created[tgt['id']].add(wanted)
                plan(f'link column {s_name}.{title} <-> {t_name}.{wanted} ({rel["type"]}): '
                     f'{len(links)} linked rows')
                continue

            before = {c['key'] for c in st(self.base.list_columns, t_name)}
            st(self.base.insert_column, s_name, title, ColumnTypes.LINK,
               column_data={'table': s_name, 'other_table': t_name})
            link_id = st(self.base.get_column_link_id, s_name, title)

            # Column created automatically on the other side: give it its NocoDB name
            if src['id'] != tgt['id']:
                other = next((c for c in st(self.base.list_columns, t_name)
                              if c['type'] == 'link' and c['key'] not in before), None)
                if other:
                    if other['name'] != wanted and wanted not in self.created[tgt['id']]:
                        st(self.base.rename_column, t_name, other['key'], wanted)
                        other['name'] = wanted
                    self.created[tgt['id']].add(other['name'])

            row_ids = list(links)
            for part in chunks(row_ids):
                st(self.base.batch_update_links, link_id, s_name, t_name, part, {r: links[r] for r in part})
            log(f'  {s_name}.{title} <-> {t_name} ({rel["type"]}): {len(row_ids)} linked rows')

    # --- computed columns -------------------------------------------------

    def computed_spec(self, table, col):
        """Return (spec, dependencies) for a computed column, or (None, reason).

        spec = {'formula': <formula column expression>, 'link_formula': <dict> or None}
        dependencies = [(table id, column name)] that must exist in SeaTable first.
        """
        o = col.get('colOptions') or {}
        u = col['uidt']
        if u == 'Formula':
            raw = o.get('formula_raw') or self.titles_from_ids(o.get('formula', ''))
            deps = [(table['id'], n) for n in re.findall(r'\{([^{}]+)\}', raw)]
            return {'formula': translate_formula(raw), 'link_formula': None}, deps
        rel = self.col_by_id.get(o.get('fk_relation_column_id'))
        target = self.col_by_id.get(o.get('fk_lookup_column_id') or o.get('fk_rollup_column_id'))
        if not rel or not target:
            return None, 'link or target column not found'
        link = rel[1]['title']
        t_table, t_col = target
        deps = [(table['id'], link), (t_table['id'], t_col['title'])]
        if u == 'Lookup':
            return {'formula': '{%s.%s}' % (link, t_col['title']),
                    'link_formula': {'formula': 'lookup', 'link': link,
                                     'target_table': t_table['id'], 'target': t_col['title']}}, deps
        fn = ROLLUP_FUNCTIONS.get(o.get('rollup_function'))
        if not fn:
            return None, f'rollup function "{o.get("rollup_function")}" not supported'
        if fn == 'count_links':
            return {'formula': 'countlinks("%s")' % link,
                    'link_formula': {'formula': 'count_links', 'link': link}}, deps[:1]
        return {'formula': 'rollup("%s", "%s", "%s")' % (link, t_col['title'], fn),
                'link_formula': {'formula': 'rollup', 'link': link, 'target_table': t_table['id'],
                                 'target': t_col['title'], 'method': fn}}, deps

    def titles_from_ids(self, formula):
        def repl(m):
            c = self.col_by_id.get(m.group(1))
            return '{%s}' % c[1]['title'] if c else m.group(0)
        return re.sub(r'\{\{?([^{}]+)\}?\}', repl, formula)

    def link_formula_payload(self, table, lf):
        """column_data of a link-formula column.

        Mirrors the data of link-formula columns created in the SeaTable UI, where column
        references are KEYS. The creation API also requires column NAMES ('link_column',
        'level1_linked_column', 'summary_column'): both forms are sent.
        Rollup summary methods: sum, average, min, max, concatenate.
        """
        link_key = st(self.base.get_column_by_name, self.tname[table['id']], lf['link'])['key']
        common = {'formula': lf['formula'], 'link_column': lf['link'], 'link_column_key': link_key,
                  'operated_columns': [link_key], 'conditions': [], 'include_condition': False,
                  'condition_conjunction': 'And'}
        if lf['formula'] == 'count_links':
            return {**common, 'result_type': 'number'}

        target = st(self.base.get_column_by_name, self.tname[lf['target_table']], lf['target'])
        if lf['formula'] == 'lookup':
            array_type, array_data = lookup_array_type(target)
            return {**common, 'result_type': 'array',
                    'level1_linked_column': lf['target'],
                    'level1_linked_table_column_key': target['key'],
                    'level2_linked_table_column_key': None,
                    'enable_deduplication': False,
                    'array_type': array_type, 'array_data': array_data}

        # rollup
        if lf['method'] in ('sum', 'average'):
            result_type = 'number'
        elif lf['method'] == 'concatenate':
            result_type = 'string'
        elif target.get('type') == 'date':
            result_type = 'date'
        elif target.get('type') in ('number', 'formula', 'link-formula', 'duration', 'rate', 'auto-number'):
            result_type = 'number'
        else:
            result_type = 'string'
        return {**common, 'result_type': result_type,
                'summary_column': lf['target'], 'column_key_in_linked_record': target['key'],
                'summary_method': lf['method']}

    def try_link_formula(self, table, col, lf):
        """Create a link-formula column; returns its column_data, or None if SeaTable rejected it."""
        tname, name = self.tname[table['id']], col['title']
        payload = self.link_formula_payload(table, lf)
        try:
            st(self.base.insert_column, tname, name, ColumnTypes.LINK_FORMULA, column_data=payload)
        except Exception as e:
            log(f'    link-formula rejected for {tname}.{name}: {e}')
            self.drop_if_exists(tname, name)
            return None
        # Check that SeaTable really stored the configuration (and did not silently drop it)
        stored = (st(self.base.get_column_by_name, tname, name) or {}).get('data') or {}
        same_formula = (stored.get('formula') or '').replace('_', '') == payload['formula'].replace('_', '')
        if same_formula and stored.get('link_column_key') == payload['link_column_key']:
            return payload
        log(f'    link-formula configuration not stored for {tname}.{name}: {stored}')
        self.drop_if_exists(tname, name)
        return None

    def drop_if_exists(self, tname, name):
        try:
            column = st(self.base.get_column_by_name, tname, name)
        except Exception:
            return
        if column:
            st(self.base.delete_column, tname, column['key'])

    def create_computed(self):
        log('== Computed columns')
        pending = [(t, c) for t in self.tables for c in t['columns']
                   if c['uidt'] in COMPUTED_UIDTS and c['title'] != t['pv']]
        static = []
        progress = True
        while pending and progress:
            progress, remaining = False, []
            for t, c in pending:
                spec, deps = self.computed_spec(t, c)
                if spec is None:
                    static.append((t, c, deps))
                    progress = True
                    continue
                if not all(n in self.created[tid] for tid, n in deps):
                    remaining.append((t, c))
                    continue
                progress = True
                self.create_computed_column(t, c, spec, static)
            pending = remaining
        static += [(t, c, 'missing dependencies') for t, c in pending]
        for t, c, reason in static:
            self.add_static(t, c, reason)

    def create_computed_column(self, table, col, spec, static):
        tname, name = self.tname[table['id']], col['title']
        lf = spec['link_formula'] if PREFER_LINK_FORMULA else None
        if SIMULATION:
            self.created[table['id']].add(name)
            if lf:
                plan(f'add link-formula column {tname}.{name} ({lf["formula"]}), '
                     f'formula column as fallback → {spec["formula"]}')
            else:
                plan(f'add formula column {tname}.{name} → {spec["formula"]}')
                warn(f'{tname}.{name}: formula to be checked → {spec["formula"]}')
            return
        if lf:
            payload = self.try_link_formula(table, col, lf)
            if payload:
                self.created[table['id']].add(name)
                log(f'  {tname}.{name}: link-formula ({payload["formula"]})')
                return
        try:
            self.add_column(table, name, 'FORMULA', {'formula': spec['formula']}, retry_without_data=False)
        except Exception as e:
            static.append((table, col, f'rejected by SeaTable ({e})'))
            return
        if col['uidt'] == 'Formula':
            warn(f'{tname}.{name}: formula to be checked → {spec["formula"]}')
        else:
            what = 'link-formula rejected, ' if lf else ''
            warn(f'{tname}.{name} ({col["uidt"]}): {what}created as formula column → {spec["formula"]}')

    def add_static(self, table, col, reason):
        name = self.tname[table['id']]
        values = {str(r[table['pk']]): r.get(col['title']) for r in table['records']}
        numeric = all(isinstance(v, (int, float)) for v in values.values() if v is not None)
        self.add_column(table, col['title'], 'NUMBER' if numeric else 'TEXT')
        warn(f'{name}.{col["title"]} ({col["uidt"]}) imported as static values: {reason}')
        updates = [{'row_id': self.row_map[table['id']][k], 'row': {col['title']: v if numeric else to_text(v)}}
                   for k, v in values.items() if v is not None and k in self.row_map[table['id']]]
        if SIMULATION:
            plan(f'    fill {len(updates)} rows of {name}.{col["title"]}')
            return
        for part in chunks(updates):
            st(self.base.batch_update_rows, name, part)

    def run(self):
        self.create_tables()
        self.insert_rows()
        self.create_links()
        self.create_computed()


# --------------------------------- main ------------------------------------

if not (NOCODB_TOKEN and NOCODB_BASE_ID):
    raise SystemExit('Please set NOCODB_TOKEN and NOCODB_BASE_ID in the CONFIGURATION section.')
if not SEATABLE_API_TOKEN:
    raise SystemExit('Please set SEATABLE_API_TOKEN in the CONFIGURATION section (needed outside the SeaTable script editor).')
if SIMULATION:
    log('*** SIMULATION: NocoDB is read, nothing is created or changed in SeaTable ***\n')

nocodb = NocoDB(NOCODB_URL, NOCODB_TOKEN)
Importer(extract(nocodb, NOCODB_BASE_ID), nocodb).run()

log('\n== Report')
log('\n'.join('- ' + r for r in REPORT) if REPORT else 'Nothing to report.')
if SIMULATION:
    log('\nSimulation finished: set SIMULATION = False to run the migration.')
```

Machen Sie sich keine Gedanken, wenn Sie den gerade kopierten Code nicht ganz verstehen. Sie müssen nur den Abschnitt **CONFIGURATION** am Anfang des Skripts anpassen. Die **Kommentare im Code** erläutern jede Einstellung. Kommentare sind alle Zeilen mit führendem Rautezeichen ('#'). Diese Zeilen werden bei der Skriptausführung nicht beachtet, d.h. Sie können Kommentare verändern, löschen oder auch weitere hinzufügen, ohne die Funktionalität des Skripts zu beeinflussen.

Anders als die Kommentare sind die **Einrückungen im Code** bei der Ausführung des Skripts sehr wichtig. Verändern Sie diese bitte nicht.

Sie müssen keinen SeaTable API-Token angeben: Wenn das Skript im Skripteditor ausgeführt wird, verwendet es automatisch die Base, in der es gespeichert ist.

### 3\. NocoDB API-Token und Base ID eintragen

Tragen Sie die folgenden Einstellungen am Anfang des Abschnitts CONFIGURATION ein. Die Werte müssen von einfachen Anführungszeichen umschlossen sein.

- `NOCODB_TOKEN`: ein **API-Token** Ihres NocoDB Kontos. Öffnen Sie in NocoDB das Kontomenü, wählen Sie **Account settings** und dann **Tokens**, um einen Token zu erstellen.
- `NOCODB_BASE_ID`: die **ID der NocoDB Base**, die Sie migrieren möchten. Öffnen Sie die Base in NocoDB: Die ID ist der Teil der URL, der mit einem "p" beginnt, z.B. `https://app.nocodb.com/#/wxxxxxxx/pxxxxxxxxxxxxxx/...`.
- `NOCODB_URL`: Behalten Sie `https://app.nocodb.com` bei, wenn Sie NocoDB Cloud verwenden. Wenn Sie einen anderen NocoDB Server verwenden, dann tragen Sie dessen URL ein.

So sollte es dann aussehen, wobei Ihre Werte natürlich anders sind:

```
NOCODB_URL = 'https://app.nocodb.com'
NOCODB_TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
NOCODB_BASE_ID = 'pxxxxxxxxxxxxxx'
```

### 4\. Optionen anpassen (optional)

Die übrigen Einstellungen des Abschnitts CONFIGURATION sind optional. Ihre Standardwerte eignen sich für die meisten Bases.

| **Einstellung** | **Standardwert** | **Wirkung** |
| --------------- | ---------------- | ----------- |
| `SIMULATION` | `True` | `True`: Das Skript liest NocoDB nur aus und protokolliert, was es tun würde, ohne etwas in SeaTable zu verändern. `False`: Das Skript führt die Migration durch. |
| `ONLY_TABLES` | `None` | Namen der zu migrierenden Tabellen, z.B. `['Customers', 'Orders']`. Mit `None` werden alle Tabellen migriert. Verknüpfungen zu nicht migrierten Tabellen werden übersprungen. |
| `TABLE_PREFIX` | `''` | Präfix, das den Namen der in SeaTable angelegten Tabellen vorangestellt wird, z.B. `'NocoDB - '`. |
| `ID_COLUMN` | `'NocoDB ID'` | Name einer Spalte, welche die ID jedes NocoDB Datensatzes enthält, sodass Sie jede Zeile bis zu NocoDB zurückverfolgen können. Mit `None` wird keine solche Spalte angelegt. |
| `IMPORT_ATTACHMENTS` | `True` | `True`: Die Dateien der Anhangspalten werden aus NocoDB heruntergeladen und in SeaTable hochgeladen. `False`: Die Anhangspalten werden angelegt, bleiben aber leer. |
| `PERCENT_AS_FRACTION` | `True` | NocoDB speichert 50 für 50 %, SeaTable erwartet dagegen 0,5. Mit `True` werden die Werte umgerechnet. |
| `PREFER_LINK_FORMULA` | `True` | `True`: Lookups und Rollups werden als [Spalten vom Typ Formel für Verknüpfungen]({{< relref "help/base-editor/spaltentypen/die-spalte-formel-fuer-verknuepfungen" >}}) angelegt. `False`: Sie werden als [Formel-Spalten]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}}) angelegt. |
| `NOCODB_MAX_REQUESTS_PER_SECOND` | `4` | NocoDB Cloud erlaubt 5 API-Anfragen pro Sekunde: Behalten Sie einen niedrigeren Wert bei. |

Durch den Ausschluss von Anhängen (`IMPORT_ATTACHMENTS = False`) können Sie die Laufzeit des Skripts deutlich reduzieren. Gerade für einen Migrationstest bietet sich das an.

### 5\. Skript im Simulationsmodus ausführen

Führen Sie das Skript zunächst immer mit `SIMULATION = True` aus. In diesem Modus liest das Skript die gesamte NocoDB Base aus, verändert aber nichts in SeaTable.

Führen Sie das Skript jetzt mit einem Klick auf **Skript ausführen** aus. Während der Ausführung sehen Sie auf der rechten Seite im Editor die ausgeführten Schritte: die Tabellen, Spalten, Zeilen und Verknüpfungen, die angelegt würden. Am Ende listet ein **Bericht** alles auf, was Ihre Aufmerksamkeit erfordert, z.B. zu prüfende Formeln oder Spalten, die nicht importiert werden können.

{{< warning  headline="Wichtiger Hinweis"  text="Schließen Sie das Fenster während der Skriptausführung nicht, da der Prozess sonst abgebrochen wird. Dass das Skript beendet ist, erkennen Sie an der Ausgabe im rechten Bereich." />}}

### 6\. Simulation überprüfen

Prüfen Sie nun im Protokoll, ob

- alle Tabellen und alle Spalten importiert werden,
- die Spaltentypen korrekt sind und
- die Verknüpfungen zwischen den Tabellen korrekt sind.

Da die Spaltentypen von NocoDB und SeaTable nicht vollständig kongruent sind, werden manche Spaltentypen in der SeaTable Base von denen in der NocoDB Base abweichen. Die folgende Tabelle stellt dar, wie die Spaltentypen in NocoDB in SeaTable übertragen werden.

| **NocoDB Spaltentyp** | **Import in SeaTable Spaltentyp** |
| --------------------- | --------------------------------- |
| Attachment | Datei |
| AutoNumber | Zahl |
| Barcode | – |
| Button | – |
| Checkbox | Checkbox |
| Count | – |
| CreatedBy | Text (E-Mail-Adresse) |
| CreatedTime | Datum (mit Uhrzeit) |
| Currency | Zahl (Währungsformat) |
| Date | Datum |
| DateTime | Datum (mit Uhrzeit) |
| Decimal | Zahl (gleiche Dezimalstellen) |
| Duration | Dauer |
| Email | E-Mail |
| Formula | Formel (übersetzt) |
| GeoData | Text |
| JSON | Formatierter Text |
| LastModifiedBy | Text (E-Mail-Adresse) |
| LastModifiedTime | Datum (mit Uhrzeit) |
| Links | Verknüpfung zu anderen Einträgen |
| LongText | Formatierter Text |
| Lookup | Formel für Verknüpfungen (Lookup) |
| MultiSelect | Mehrfachauswahl (mit Optionen und Farben) |
| Number | Zahl |
| Percent | Zahl (Prozentformat) |
| PhoneNumber | Text |
| QrCode | – |
| Rating | Rating (gleiches Maximum und gleiche Farbe; NocoDB-Kreise werden zu Sternen) |
| Rollup | Formel für Verknüpfungen (Rollup) |
| SingleLineText | Text |
| SingleSelect | Einfachauswahl (mit Optionen und Farben) |
| Time | Text |
| URL | URL |
| User | Text (E-Mail-Adresse) |
| Year | Zahl |

Eine besondere Rolle spielen Formelspalten sowie die NocoDB Spaltentypen Lookup und Rollup:

- **Formeln** werden automatisch in SeaTable Formeln übersetzt. Einige NocoDB Funktionen haben jedoch keine exakte Entsprechung in SeaTable. Jede Formel wird daher im Bericht aufgeführt, damit Sie sie prüfen können.
- **Lookups und Rollups** werden als Spalten vom Typ Formel für Verknüpfungen angelegt. Lehnt SeaTable eine solche Spalte ab, legt das Skript stattdessen eine Formel-Spalte an und vermerkt dies im Bericht.
- Kann eine berechnete Spalte gar nicht neu angelegt werden, z.B. wegen einer nicht unterstützten Rollup-Funktion, werden ihre **Werte als statische Werte importiert** (Zahlen oder Text). Diese Spalten werden ebenfalls im Bericht aufgeführt.

Wenn etwas nicht richtig ist, dann passen Sie die Einstellungen aus Schritt 4 an und führen Sie die Simulation erneut aus. Sie können die Simulation beliebig häufig ausführen.

### 7\. Base migrieren

Wenn die Überprüfung in Schritt 6 zu Ihrer Zufriedenheit ist, dann kann die Base migriert werden.

Ändern Sie im Skript `SIMULATION = True` zu `SIMULATION = False`:

```
SIMULATION = False
```

Führen Sie das Skript mit einem Klick auf **Skript ausführen** erneut aus. Wieder können Sie auf der rechten Seite die Ausführung des Skripts beobachten und im Hintergrund sehen, wie die Tabellen und Spalten angelegt werden. Das Skript

1. legt die Tabellen und einfachen Spalten an und fügt dann die Zeilen ein,
2. legt die Verknüpfungsspalten an und verknüpft die Zeilen,
3. legt die berechneten Spalten an: Formeln, Lookups und Rollups.

{{< warning  headline="Wichtiger Hinweis"  text="Schließen Sie das Fenster während der Skriptausführung nicht, da der Prozess sonst abgebrochen wird." />}}

Lesen Sie am Ende den Bericht aufmerksam: Er listet die Spalten und Formeln auf, die Sie prüfen sollten. So sieht das Protokoll einer Migration aus (gekürzt):

```
== Reading NocoDB
Customers: 7 columns
4 records
Products: 8 columns
5 records
Orders: 12 columns
5 records
Order Items: 7 columns
9 records
links Orders.Customer -> Customers
links Order Items.Product -> Products
links Order Items.Order -> Orders
== Creating tables
Customers
Products
Orders
Order Items
== Inserting rows
Customers: 4 rows
Products: 5 rows
Orders: 5 rows
Order Items: 9 rows
== Links
Orders.Customer <-> Customers (mo): 5 linked rows
Order Items.Product <-> Products (mo): 9 linked rows
Order Items.Order <-> Orders (mo): 9 linked rows
== Computed columns
Orders.Customer Email: link-formula (lookup)
Order Items.Product SKU: link-formula (lookup)
! Order Items.Line Total: formula to be checked → round({Quantity} * {Unit Price}, 2)
Orders.Order Total: link-formula (rollup)
== Report
- Order Items.Line Total: formula to be checked → round({Quantity} * {Unit Price}, 2)
```

Zeilen, die mit einem Ausrufezeichen (`!`) beginnen, weisen auf Spalten hin, die Ihre Aufmerksamkeit erfordern. Sie werden alle im Bericht am Ende wiederholt.

Wenn das Skript abbricht, weil in der Base bereits Tabellen mit denselben Namen existieren, dann löschen Sie diese Tabellen oder legen Sie ein `TABLE_PREFIX` fest. Wenn Sie mit dem Endergebnis nicht zufrieden sind, dann [löschen Sie die Tabellen]({{< relref "help/base-editor/tabellen/loeschen-einer-tabelle-aus-einer-base" >}}), die das Skript angelegt hat, und starten erneut bei Schritt 4.

### 8\. Ergebnis überprüfen

Um sicherzustellen, dass alle Daten korrekt übertragen wurden, vergleicht ein zweites Skript die NocoDB Base mit der SeaTable Base. Wie das Migrationsskript liest es ausschließlich Daten aus: Es verändert nichts, weder in NocoDB noch in SeaTable.

Für jede importierte Tabelle vergleicht das Prüfskript

- die Anzahl der Zeilen (fehlende und zusätzliche Zeilen),
- jede einfache Spalte, Wert für Wert (Zahlen, Datumsangaben, Auswahlen, Checkboxen, Texte, Anhänge …),
- die Verknüpfungen: die genauen verknüpften Datensätze auf den "many to one"-Seiten, die Anzahl der Verknüpfungen auf den anderen Seiten,
- die berechneten Spalten (Formeln, Lookups, Rollups): den von SeaTable berechneten Wert mit dem von NocoDB berechneten Wert. Diese Prüfung deckt falsch übersetzte Formeln, Zeitzonenverschiebungen und fehlerhafte Prozentumrechnungen auf.

Fügen Sie der Base ein zweites Python-Skript hinzu und fügen Sie den folgenden Codeblock darin ein:

```python
"""
Check a NocoDB -> SeaTable migration made with the migration script.
Meant to be run in the migrated base.

The script is READ-ONLY on both sides. For every imported table it compares NocoDB and SeaTable:
  * row counts (missing and extra rows);
  * every simple column, value by value (numbers, dates, selects, checkboxes, text, attachments…);
  * links: exact linked records on "many to one" sides, number of links on the other sides;
  * computed columns (formulas, lookups, rollups): the value computed by SeaTable against the
    value computed by NocoDB. This is the check that catches badly translated formulas,
    time zone shifts and wrong percentage conversions.

Rows are matched through the ID column created by the migration (ID_COLUMN). If that column was
deleted, they are matched through the display column, provided its values are unique.

Usage: paste into a Python script of the migrated base, fill in the CONFIGURATION section, run.
From a local IDE (e.g. if the SeaTable editor stops the script because it runs too long):
pip install seatable-api requests, then also set SEATABLE_API_TOKEN (and SEATABLE_SERVER_URL).
Use the same ONLY_TABLES, TABLE_PREFIX, ID_COLUMN and PERCENT_AS_FRACTION values as the migration.
"""

import json
import time
from collections import Counter
from datetime import datetime, timezone

import requests
from seatable_api import Base, context

# ============================== CONFIGURATION ==============================

# SeaTable: filled in automatically when run from the SeaTable script editor.
# To run from a local IDE (no execution time limit), replace '' with the base API token
# and, for a self-hosted server, the server URL.
SEATABLE_SERVER_URL = context.server_url or 'https://cloud.seatable.io'
SEATABLE_API_TOKEN = context.api_token or ''   # API token of the target base (read-write)

NOCODB_URL = 'https://app.nocodb.com'
NOCODB_TOKEN = ''           # NocoDB: Account > API Tokens
NOCODB_BASE_ID = ''         # starts with "p", visible in the NocoDB URL

ONLY_TABLES = None          # same value as for the migration
TABLE_PREFIX = ''           # same value as for the migration
ID_COLUMN = 'NocoDB ID'     # same value as for the migration; None if it was not created/was deleted
PERCENT_AS_FRACTION = True  # same value as for the migration

MAX_EXAMPLES = 5            # differences shown per column
NUMBER_TOLERANCE = 1e-6     # absolute tolerance when comparing numbers

NOCODB_MAX_REQUESTS_PER_SECOND = 4  # NocoDB Cloud allows 5 requests/s per user: stay below

# ===========================================================================

LINK_UIDTS = ('Links', 'LinkToAnotherRecord')
COMPUTED_UIDTS = ('Formula', 'Lookup', 'Rollup')
NOT_IMPORTED_UIDTS = ('ID', 'ForeignKey', 'Button', 'Barcode', 'QrCode', 'Count')
NUMBER_UIDTS = ('Number', 'Decimal', 'Currency', 'Year', 'AutoNumber', 'Rating', 'Duration')
DATETIME_UIDTS = ('DateTime', 'CreatedTime', 'LastModifiedTime')
TEXT_UIDTS = ('User', 'CreatedBy', 'LastModifiedBy', 'Time', 'GeoData', 'PhoneNumber')
ERROR_VALUES = ('#ERROR', '#VALUE!', '#NAME?', '#DIV/0!', '#N/A', '#REF!', '#NUM!', '#NULL!')


def log(msg=''):
    print(msg, flush=True)


# ------------------------------- NocoDB ------------------------------------

class NocoDB:
    def __init__(self, url, token):
        self.url = url.rstrip('/')
        self.session = requests.Session()
        self.session.headers['xc-token'] = token
        self._last = 0.0

    def get(self, path, **params):
        for attempt in range(6):
            wait = 1 / NOCODB_MAX_REQUESTS_PER_SECOND - (time.time() - self._last)
            if wait > 0:
                time.sleep(wait)
            self._last = time.time()
            r = self.session.get(self.url + path, params=params, timeout=60)
            if r.status_code == 429:
                time.sleep(int(r.headers.get('Retry-After', 30)))
                continue
            if r.status_code >= 500 and attempt < 5:
                time.sleep(2 ** attempt)
                continue
            r.raise_for_status()
            return r.json()
        raise RuntimeError(f'NocoDB: repeated failure on {path}')

    def paged(self, path):
        rows, offset = [], 0
        while True:
            data = self.get(path, limit=1000, offset=offset)
            page = data.get('list') or []
            rows.extend(page)
            if not page or (data.get('pageInfo') or {}).get('isLastPage', True):
                return rows
            offset += len(page)


def read_nocodb(noco):
    tables = []
    for t in noco.get(f'/api/v2/meta/bases/{NOCODB_BASE_ID}/tables').get('list', []):
        if t.get('mm') or (ONLY_TABLES and t['title'] not in ONLY_TABLES):
            continue
        cols = noco.get(f'/api/v2/meta/tables/{t["id"]}').get('columns', [])
        for c in cols:
            if isinstance(c.get('meta'), str):
                try:
                    c['meta'] = json.loads(c['meta'])
                except ValueError:
                    c['meta'] = {}
        pk = next((c['title'] for c in cols if c.get('pk')), 'Id')
        user_cols = [c for c in cols if not c.get('system') and not c.get('pk')]
        pv = next((c['title'] for c in user_cols if c.get('pv')), user_cols[0]['title'] if user_cols else pk)
        tables.append({'id': t['id'], 'title': t['title'], 'pk': pk, 'pv': pv, 'columns': user_cols,
                       'records': noco.paged(f'/api/v2/tables/{t["id"]}/records')})
    return tables


# ------------------------------ SeaTable -----------------------------------

def read_seatable_rows(base, table_name):
    rows, start = [], 0
    while True:
        page = base.list_rows(table_name, start=start, limit=1000)
        rows.extend(page)
        if len(page) < 1000:
            return rows
        start += len(page)


# ----------------------------- comparison ----------------------------------

def is_empty(v):
    return v is None or v == '' or v == [] or v == {}


def as_number(v):
    if isinstance(v, bool):
        return None
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def as_datetime(v):
    try:
        d = datetime.fromisoformat(str(v).strip().replace('Z', '+00:00'))
    except ValueError:
        return None
    return d if d.tzinfo else d.replace(tzinfo=timezone.utc)


def text_of(v):
    if v is None:
        return ''
    if isinstance(v, dict):
        for k in ('text', 'display_value', 'email', 'display_name', 'name', 'title'):
            if v.get(k) is not None:
                return str(v[k]).strip()
        return json.dumps(v, sort_keys=True, ensure_ascii=False)
    if isinstance(v, list):
        return ', '.join(text_of(x) for x in v)
    if isinstance(v, float) and v.is_integer():
        return str(int(v))
    return str(v).strip()


def as_list(v):
    if is_empty(v):
        return []
    return v if isinstance(v, list) else [v]


def split_multi(v):
    if isinstance(v, list):
        return [str(x) for x in v]
    return [x.strip() for x in str(v or '').split(',') if x.strip()]


def same_value(a, b):
    """Generic comparison, used for formulas, lookups and rollups."""
    if is_empty(a) and is_empty(b):
        return True, None
    if isinstance(a, list) or isinstance(b, list):
        la, lb = as_list(a), as_list(b)
        if len(la) == len(lb) and all(same_value(x, y)[0] for x, y in zip(sorted(la, key=text_of), sorted(lb, key=text_of))):
            return True, None
        if Counter(map(text_of, la)) == Counter(map(text_of, lb)):
            return True, None
        return False, None
    na, nb = as_number(a), as_number(b)
    if na is not None and nb is not None:
        return abs(na - nb) <= NUMBER_TOLERANCE, None
    if isinstance(a, str) and isinstance(b, str) and len(a) >= 10 and len(b) >= 10:
        da, db = as_datetime(a), as_datetime(b)
        if da and db:
            return compare_datetimes(da, db)
    return text_of(a) == text_of(b), None


def compare_datetimes(da, db):
    if da == db:
        return True, None
    hours = (db - da).total_seconds() / 3600
    if hours.is_integer() and abs(hours) <= 14:
        return False, f'shifted by {hours:+.0f} h (time zone?)'
    return False, None


def compare(col, nv, sv):
    """Compare a NocoDB value with the SeaTable value of the same column.
    Returns (ok, note)."""
    u = col['uidt']
    if isinstance(sv, str) and sv.strip().upper() in ERROR_VALUES:
        return False, 'SeaTable error value'
    if u in COMPUTED_UIDTS:
        return same_value(nv, sv)
    if u == 'Checkbox':
        return (bool(nv) and nv not in ('false', '0')) == bool(sv), None
    if is_empty(nv) and is_empty(sv):
        return True, None
    if u in NUMBER_UIDTS or u == 'Percent':
        na, nb = as_number(nv), as_number(sv)
        if na is not None and u == 'Percent' and PERCENT_AS_FRACTION:
            na /= 100
        return na is not None and nb is not None and abs(na - nb) <= NUMBER_TOLERANCE, None
    if u == 'Date':
        return text_of(nv)[:10] == text_of(sv)[:10], None
    if u in DATETIME_UIDTS:
        da, db = as_datetime(nv), as_datetime(sv)
        if da and db:
            return compare_datetimes(da, db)
        return False, 'unreadable date'
    if u == 'MultiSelect':
        return sorted(split_multi(nv)) == sorted(split_multi(sv)), None
    if u == 'Attachment':
        n, s = len(as_list(nv)), len(as_list(sv))
        return n == s, None if n == s else f'{n} file(s) in NocoDB, {s} in SeaTable'
    if u == 'JSON':
        try:
            a = json.loads(nv) if isinstance(nv, str) else nv
            b = json.loads(sv) if isinstance(sv, str) else sv
            return a == b, None
        except (TypeError, ValueError):
            pass
    if u in TEXT_UIDTS:
        return text_of(nv) == text_of(sv), None
    return text_of(nv) == text_of(sv), None


def short(v, size=60):
    s = text_of(v) if not isinstance(v, str) else v
    s = s.replace('\n', ' ')
    return s if len(s) <= size else s[:size - 1] + '…'


# -------------------------------- checks -----------------------------------

class Checker:
    def __init__(self, tables, base):
        self.tables = tables
        self.by_id = {t['id']: t for t in tables}
        self.base = base
        self.problems = []          # (table, column, message) for the final summary
        self.checked_columns = 0
        self.st_rows = {}           # table id -> {NocoDB id: SeaTable row}
        self.st_to_nid = {}         # table id -> {SeaTable _id: NocoDB id}

    def problem(self, table, column, message):
        self.problems.append((table, column, message))

    def match_rows(self, t, rows):
        name = TABLE_PREFIX + t['title']
        if ID_COLUMN and rows and ID_COLUMN in rows[0]:
            key = lambda row: text_of(row.get(ID_COLUMN))
            nkey = lambda rec: str(rec[t['pk']])
        else:
            values = [text_of(r.get(t['pv'])) for r in t['records']]
            if len(set(values)) != len(values):
                self.problem(name, None, f'no "{ID_COLUMN}" column and duplicate display values: '
                                         'rows cannot be matched, table not checked')
                return None
            key = lambda row: text_of(row.get(t['pv']))
            nkey = lambda rec: text_of(rec.get(t['pv']))
            log(f'  rows matched on the display column "{t["pv"]}"')
        st_by_key = {}
        for row in rows:
            st_by_key.setdefault(key(row), []).append(row)
        matched = {}
        for rec in t['records']:
            candidates = st_by_key.pop(nkey(rec), [])
            if candidates:
                matched[str(rec[t['pk']])] = candidates[0]
                if len(candidates) > 1:
                    self.problem(name, None, f'record {nkey(rec)} imported {len(candidates)} times')
        missing = len(t['records']) - len(matched)
        extra = sum(len(v) for v in st_by_key.values())
        log(f'  rows: NocoDB {len(t["records"])}, SeaTable {len(rows)}, matched {len(matched)}')
        if missing:
            self.problem(name, None, f'{missing} NocoDB record(s) not found in SeaTable')
        if extra:
            self.problem(name, None, f'{extra} SeaTable row(s) without NocoDB counterpart')
        return matched

    def load(self):
        existing = {t['name'] for t in self.base.list_tables()}
        for t in self.tables:
            name = TABLE_PREFIX + t['title']
            log(f'\n== {name}')
            if name not in existing:
                self.problem(name, None, 'table missing in SeaTable')
                log('  ! table missing in SeaTable')
                continue
            rows = read_seatable_rows(self.base, name)
            matched = self.match_rows(t, rows)
            if matched is None:
                log('  ! rows cannot be matched')
                continue
            self.st_rows[t['id']] = matched
            self.st_to_nid[t['id']] = {row['_id']: nid for nid, row in matched.items()}
            t['st_columns'] = {c['name']: c for c in self.base.list_columns(name)}

    def check_table(self, t):
        name = TABLE_PREFIX + t['title']
        matched = self.st_rows.get(t['id'])
        if matched is None:
            return
        log(f'\n== {name}: columns')
        records = {str(r[t['pk']]): r for r in t['records']}
        for col in t['columns']:
            title, u = col['title'], col['uidt']
            if u in NOT_IMPORTED_UIDTS:
                continue
            if title not in t['st_columns']:
                self.problem(name, title, 'column missing in SeaTable')
                log(f'  ! {title}: column missing in SeaTable')
                continue
            self.checked_columns += 1
            if u in LINK_UIDTS:
                diffs = self.check_link(t, col, records, matched)
            else:
                diffs = []
                for nid, row in matched.items():
                    ok, note = compare(col, records[nid].get(title), row.get(title))
                    if not ok:
                        diffs.append((nid, records[nid].get(title), row.get(title), note))
            st_type = t['st_columns'][title]['type']
            if not diffs:
                log(f'  ok  {title} ({u} -> {st_type})')
                continue
            log(f'  !!  {title} ({u} -> {st_type}): {len(diffs)} difference(s) out of {len(matched)} rows')
            notes = Counter(d[3] for d in diffs if d[3])
            for note, n in notes.items():
                log(f'        {n} × {note}')
            for nid, nv, sv, note in diffs[:MAX_EXAMPLES]:
                log(f'        record {nid}: NocoDB «{short(nv)}»  SeaTable «{short(sv)}»')
            summary = f'{len(diffs)} difference(s)'
            if notes:
                summary += ' (' + ', '.join(notes) + ')'
            self.problem(name, title, summary)

    def check_link(self, t, col, records, matched):
        """Exact IDs when NocoDB returns the linked record(s), link counts otherwise."""
        target_id = (col.get('colOptions') or {}).get('fk_related_model_id')
        target = self.by_id.get(target_id)
        back = self.st_to_nid.get(target_id, {})
        diffs = []
        for nid, row in matched.items():
            nv, sv = records[nid].get(col['title']), as_list(row.get(col['title']))
            st_ids = sorted(back.get(x.get('row_id') if isinstance(x, dict) else x, '?') for x in sv)
            if isinstance(nv, (dict, list)) and target:
                pk = target['pk']
                noco_ids = sorted(str(x.get(pk, x.get('Id', x.get('id')))) if isinstance(x, dict) else str(x)
                                  for x in as_list(nv))
                if noco_ids != st_ids:
                    diffs.append((nid, ', '.join(noco_ids), ', '.join(st_ids), None))
            else:
                count = int(nv or 0)
                if count != len(sv):
                    diffs.append((nid, f'{count} link(s)', f'{len(sv)} link(s)', 'different number of links'))
        return diffs

    def run(self):
        self.load()
        for t in self.tables:
            self.check_table(t)


# --------------------------------- main ------------------------------------

if not (NOCODB_TOKEN and NOCODB_BASE_ID):
    raise SystemExit('Please set NOCODB_TOKEN and NOCODB_BASE_ID in the CONFIGURATION section.')
if not SEATABLE_API_TOKEN:
    raise SystemExit('Please set SEATABLE_API_TOKEN in the CONFIGURATION section (needed outside the SeaTable script editor).')

log('== Reading NocoDB')
nocodb_tables = read_nocodb(NocoDB(NOCODB_URL, NOCODB_TOKEN))
log(f'  {len(nocodb_tables)} table(s), {sum(len(t["records"]) for t in nocodb_tables)} record(s)')

seatable = Base(SEATABLE_API_TOKEN, SEATABLE_SERVER_URL)
seatable.auth()
checker = Checker(nocodb_tables, seatable)
checker.run()

log('\n== Summary')
log(f'{len(nocodb_tables)} table(s), {checker.checked_columns} column(s) checked')
if not checker.problems:
    log('No difference found.')
else:
    log(f'{len(checker.problems)} problem(s):')
    for table, column, message in checker.problems:
        log(f'- {table}' + (f'.{column}' if column else '') + f': {message}')
log('\nNot checked: display formats (currency, percent, date format), views, column order.')
```

Tragen Sie `NOCODB_URL`, `NOCODB_TOKEN` und `NOCODB_BASE_ID` wie in Schritt 3 ein. Wenn Sie `ONLY_TABLES`, `TABLE_PREFIX`, `ID_COLUMN` oder `PERCENT_AS_FRACTION` im Migrationsskript geändert haben, verwenden Sie hier **dieselben Werte**. Klicken Sie dann auf **Skript ausführen**.

Für jede Tabelle zeigt das Protokoll `ok` für jede Spalte ohne Abweichung und `!!` für jede Spalte mit Abweichungen, jeweils mit einigen Beispielen. Eine Zusammenfassung am Ende listet alle gefundenen Probleme auf. Anzeigeformate (Währung, Prozent, Datumsformat) werden nicht geprüft.

So sieht das Protokoll einer erfolgreichen Prüfung aus (gekürzt):

```
== Reading NocoDB
4 table(s), 23 record(s)
== Customers
rows: NocoDB 4, SeaTable 4, matched 4
== Products
rows: NocoDB 5, SeaTable 5, matched 5
== Orders
rows: NocoDB 5, SeaTable 5, matched 5
== Order Items
rows: NocoDB 9, SeaTable 9, matched 9
== Customers: columns
ok Customer Name (SingleLineText -> text)
ok Email (Email -> email)
ok Joined On (Date -> date)
ok Orders (LinkToAnotherRecord -> link)
== Products: columns
ok Product Name (SingleLineText -> text)
ok Unit Price (Currency -> number)
ok Product Image (Attachment -> file)
ok Order Items (LinkToAnotherRecord -> link)
== Orders: columns
ok Order Number (SingleLineText -> text)
ok Ordered At (DateTime -> date)
ok Customer (LinkToAnotherRecord -> link)
ok Order Items (LinkToAnotherRecord -> link)
ok Customer Email (Lookup -> link-formula)
ok Order Total (Rollup -> link-formula)
== Order Items: columns
ok Quantity (Number -> number)
ok Unit Price (Currency -> number)
ok Order (LinkToAnotherRecord -> link)
ok Product (LinkToAnotherRecord -> link)
ok Product SKU (Lookup -> link-formula)
ok Line Total (Formula -> formula)
== Summary
4 table(s), 34 column(s) checked
No difference found.
Not checked: display formats (currency, percent, date format), views, column order.
```

### 9\. Migration abschließen

Das Migrationsskript hat die Daten übertragen. Einige manuelle Nacharbeiten sind nun ggf. noch notwendig.

Zum einen sollten Sie die im Bericht des Migrationsskripts aufgeführten Formeln und Spalten sowie die vom Prüfskript gefundenen Abweichungen überprüfen.

Zum anderen müssen Sie die folgenden Elemente selbst neu anlegen, da diese nicht aus der NocoDB Base übertragen werden:

- Ansichten mit ihren Filtern, Sortierungen und ausgeblendeten Spalten,
- Formulare,
- Automationen, Webhooks, Skripte und Erweiterungen,
- Mitarbeiter und Berechtigungen,
- Kommentare und Änderungsverlauf der Datensätze,
- Standardwerte und Validierungsregeln,
- die Reihenfolge der Spalten.

Die Zeilen erhalten in SeaTable ein neues Erstellungsdatum. Wenn Ihre NocoDB Tabellen Spalten vom Typ CreatedTime oder LastModifiedTime enthalten, werden deren Werte als normale Datumsspalten importiert.

Entfernen Sie abschließend **den NocoDB API-Token aus beiden Skripten**: Die Mitarbeiter der Base können die darin gespeicherten Skripte lesen. Wenn Sie die Spalte `NocoDB ID` nicht mehr benötigen, können Sie sie löschen.

## FAQ-Bereich

{{< faq "Ändert das Skript Daten in meiner NocoDB Base?" >}}Nein. Beide Skripte lesen Ihre NocoDB Base ausschließlich aus. Die Daten in der NocoDB Base werden nicht verändert.
{{< /faq >}}

{{< faq "Wie verhalte ich mich bei Fehlermeldungen?" >}}Eine Fehlermeldung bei der ersten Ausführung ist gar nicht unwahrscheinlich. Gründe dafür gibt es genug, z.B. ein falscher Token, eine falsche Base ID, ein fehlendes Anführungszeichen oder eine nicht korrekte Einrückung. Ein einzelner Fehler kann zu einem Abbruch der Skriptausführung führen.  
Wenn Sie eine Fehlermeldung erhalten, dann ist dies grundsätzlich kein Problem. In NocoDB können keine Daten verloren gehen. Gehen Sie wie folgt vor, um die Ursache des Fehlers zu finden:

- Die Fehlermeldung gibt Ihnen in den meisten Fällen einen Hinweis, wo der Fehler zu finden ist. Folgen Sie diesem, korrigieren Sie die eingegebenen Parameter und führen Sie das Skript erneut aus.
- Wenn die Migration abgebrochen wurde, dann löschen Sie die bereits vom Skript angelegten Tabellen (oder legen Sie ein anderes `TABLE_PREFIX` fest), bevor Sie das Skript erneut ausführen.
- Ist die Fehlermeldung unverständlich, prüfen Sie alle Eingaben auf Korrektheit und versuchen Sie es nochmals.
- Wenn keiner der Tipps hilft, holen Sie sich Hilfe im [SeaTable Forum](https://forum.seatable.com/).

> **Wichtiger Hinweis**: Bitte entfernen Sie den NocoDB API-Token und die Base ID, bevor Sie Screenshots oder Skripte im Forum posten.

{{< /faq >}}

{{< faq "Können NocoDB Bases beliebiger Größe migriert werden?" >}}Grundsätzlich ja. Die in diesem Artikel vorgestellte Vorgehensweise mit dem integrierten Python Editor unterliegt jedoch einer maximalen Laufzeitbeschränkung von 15 Minuten, d.h. Skripte, die länger als 15 Minuten laufen, werden abgebrochen. Bei Bases mit vielen Datensätzen oder vielen Dateianhängen kann dieses Limit eine Rolle spielen. In dem Fall können Sie durch das Ausschließen der Anhänge (`IMPORT_ATTACHMENTS = False`) die Laufzeit verringern. Andernfalls müssen Sie das Python Skript lokal auf einem Rechner ausführen, bei dem es keine Laufzeitbeschränkung gibt: In diesem Fall müssen Sie zusätzlich einen [API-Token]({{< relref "help/integrationen/seatable-api/erzeugen-eines-api-tokens" >}}) der SeaTable Base mit Lese- und Schreibrechten in `SEATABLE_API_TOKEN` eintragen.
{{< /faq >}}

{{< faq "Kann man Tabellen in eine bestehende Base importieren?" >}}Ja. Das Skript erfordert nicht, dass eine Base leer ist, bricht aber ab, wenn bereits eine Tabelle mit demselben Namen wie eine NocoDB Tabelle existiert. Verwenden Sie in diesem Fall die Einstellung `TABLE_PREFIX`. Eine neue, leere Base bleibt dennoch die sicherste Wahl.
{{< /faq >}}

{{< faq "Kann ich eine Base von einem selbst gehosteten NocoDB Server migrieren?" >}}Ja. Tragen Sie die URL Ihres NocoDB Servers in `NOCODB_URL` ein. Das Skript verwendet die Version 2 der NocoDB API.
{{< /faq >}}
