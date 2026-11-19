---
title: 'Migration from NocoDB bases to SeaTable'
date: 2026-11-19
lastmod: '2026-11-19'
categories:
    - 'import-von-daten'
author: 'bha'
url: '/help/migrate-nocodb-bases-to-seatable'
aliases:
    - '/help/migration-von-nocodb-bases-zu-seatable'
seo:
    title: 'Migrate NocoDB bases to SeaTable with a script'
    description: 'Learn how to transfer a NocoDB base to SeaTable, links, lookups and formulas included, with a Python migration script and a verification script.'
---

You want to move your NocoDB bases to SeaTable? With the migration script presented in this article, you can transfer a NocoDB base to SeaTable, **links included**, directly from the SeaTable script editor. Basic Python knowledge is helpful, but not necessary.

## How to migrate a base from NocoDB to SeaTable via script

The migration script reads your NocoDB base through the NocoDB API and recreates its tables, columns, rows, links, lookups, rollups and formulas in a SeaTable base. A second script then compares NocoDB and SeaTable so you can check that nothing has been lost along the way.

Only a few **manual entries** are required to make the scripts ready for use. After the migration, a few adjustments are still necessary. In this article, we explain how to do this.

{{< warning  type="warning" headline="Important note"  text="The migration script is functional, but still beta: it has only been tested on a test base, which probably does not cover every case. The scripts are provided as is, without any warranty, and you use them at your own risk. Always check your data after the migration. If you have any problems, please leave a post in the [SeaTable forum](https://forum.seatable.com/)." />}}

### 1\. create base

Create a [new base]({{< relref "help/startseite/bases/eine-neue-base-erstellen" >}}) in SeaTable. The name of the SeaTable base does not have to be the same as the name of the NocoDB base you want to import. You can choose the name freely.

### 2\. insert script

In the new base, open the [script sidebar]({{< relref "help/skripte/allgemein/anlegen-und-loeschen-eines-skriptes" >}}) by clicking on the script icon {{< seatable-icon icon="dtable-icon-script" >}} in the base header at the top right. Then select **Add script**. The migration script is written in the Python programming language. Therefore, select **Python**.

Now select the following code block, copy it to the clipboard and then paste it into the left window of the script editor:

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

Don't worry if you don't fully understand the code you have just copied. You only need to change the **CONFIGURATION** section at the top of the script. The **comments in the code** explain each setting. Comments are all rows with a leading hash sign ('#'). These rows are not taken into account when the script is executed, i.e. you can change, delete or add comments without affecting the functionality of the script.

Unlike the comments, the **indentations in the code** are very important when running the script. Please do not change them.

You don't need to enter a SeaTable API token: when the script runs in the script editor, it automatically uses the base in which it is stored.

### 3\. enter NocoDB API token and base ID

Fill in the following settings at the top of the CONFIGURATION section. The values must be enclosed in single quotation marks.

- `NOCODB_TOKEN`: an **API token** of your NocoDB account. In NocoDB, open the account menu, select **Account settings** and then **Tokens** to create one.
- `NOCODB_BASE_ID`: the **ID of the NocoDB base** you want to migrate. Open the base in NocoDB: the ID is the part of the URL that starts with a "p", e.g. `https://app.nocodb.com/#/wxxxxxxx/pxxxxxxxxxxxxxx/...`.
- `NOCODB_URL`: keep `https://app.nocodb.com` if you are using NocoDB Cloud. If you are using a different NocoDB server, enter its URL.

This is what it should look like, although your values will of course be different:

```
NOCODB_URL = 'https://app.nocodb.com'
NOCODB_TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
NOCODB_BASE_ID = 'pxxxxxxxxxxxxxx'
```

### 4\. adjust the options (optional)

The other settings of the CONFIGURATION section are optional. Their default values are suitable for most bases.

| **Setting** | **Default value** | **Effect** |
| ----------- | ----------------- | ---------- |
| `SIMULATION` | `True` | `True`: the script only reads NocoDB and logs what it would do, without changing anything in SeaTable. `False`: the script runs the migration. |
| `ONLY_TABLES` | `None` | Names of the tables to migrate, e.g. `['Customers', 'Orders']`. `None` migrates all tables. Links to tables that are not migrated are skipped. |
| `TABLE_PREFIX` | `''` | Prefix added to the names of the tables created in SeaTable, e.g. `'NocoDB - '`. |
| `ID_COLUMN` | `'NocoDB ID'` | Name of a column that keeps the ID of each NocoDB record, so you can trace every row back to NocoDB. `None` creates no such column. |
| `IMPORT_ATTACHMENTS` | `True` | `True`: the files of attachment columns are downloaded from NocoDB and uploaded to SeaTable. `False`: the attachment columns are created, but stay empty. |
| `PERCENT_AS_FRACTION` | `True` | NocoDB stores 50 for 50 %, while SeaTable expects 0.5. `True` converts the values. |
| `PREFER_LINK_FORMULA` | `True` | `True`: lookups and rollups are created as [link formula columns]({{< relref "help/base-editor/spaltentypen/die-spalte-formel-fuer-verknuepfungen" >}}). `False`: they are created as [formula columns]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}}). |
| `NOCODB_MAX_REQUESTS_PER_SECOND` | `4` | NocoDB Cloud allows 5 API requests per second: keep a lower value. |

Excluding attachments (`IMPORT_ATTACHMENTS = False`) can significantly reduce the runtime of the script. This is particularly useful for a migration test.

### 5\. run the script in simulation mode

First, always run the script with `SIMULATION = True`. In this mode, the script reads the whole NocoDB base, but does not change anything in SeaTable.

Now run the script by clicking **Run script**. During the execution you can see the executed steps on the right side in the editor: the tables, columns, rows and links that would be created. At the end, a **report** lists everything that needs your attention, e.g. formulas to be checked or columns that cannot be imported.

{{< warning  headline="Important note"  text="Do not close the window while the script is running, otherwise the process will be aborted. You will know that the script has ended when you see an output in the right-side panel." />}}

### 6\. check the simulation

Now check in the log whether

- all tables and all columns will be imported,
- the column types are correct and
- the links between the tables are correct.

Since the column types of NocoDB and SeaTable are not completely congruent, some column types in the SeaTable base will differ from those in the NocoDB base. The following table shows how the column types in NocoDB are transferred to SeaTable.

| **NocoDB column type** | **Import to SeaTable column type** |
| ---------------------- | ---------------------------------- |
| Attachment | File |
| AutoNumber | Number |
| Barcode | – |
| Button | – |
| Checkbox | Checkbox |
| Count | – |
| CreatedBy | Text (email address) |
| CreatedTime | Date (with time) |
| Currency | Number (currency format) |
| Date | Date |
| DateTime | Date (with time) |
| Decimal | Number (same decimals) |
| Duration | Duration |
| Email | Email |
| Formula | Formula (translated) |
| GeoData | Text |
| JSON | Long text |
| LastModifiedBy | Text (email address) |
| LastModifiedTime | Date (with time) |
| Links | Link to other records |
| LongText | Long text |
| Lookup | Link formula (lookup) |
| MultiSelect | Multiple select (with options and colors) |
| Number | Number |
| Percent | Number (percent format) |
| PhoneNumber | Text |
| QrCode | – |
| Rating | Rating (same maximum and color; NocoDB circles become stars) |
| Rollup | Link formula (rollup) |
| SingleLineText | Text |
| SingleSelect | Single select (with options and colors) |
| Time | Text |
| URL | URL |
| User | Text (email address) |
| Year | Number |

Formula columns and the NocoDB column types Lookup and Rollup play a special role:

- **Formulas** are translated automatically into SeaTable formulas. However, some NocoDB functions have no exact SeaTable equivalent. Each formula is therefore listed in the report so that you can check it.
- **Lookups and rollups** are created as link formula columns. If SeaTable rejects a link formula column, the script creates a formula column instead and mentions it in the report.
- If a computed column cannot be recreated at all, e.g. because of an unsupported rollup function, its **values are imported as static values** (numbers or text). These columns are listed in the report too.

If something is not correct, adjust the settings of step 4 and run the simulation again. You can run the simulation as often as you like.

### 7\. migrate the base

If you are satisfied with the check in step 6, the base can be migrated.

In the script, change `SIMULATION = True` to `SIMULATION = False`:

```
SIMULATION = False
```

Run the script again by clicking **Run script**. Again you can watch the execution of the script on the right side and see the tables and columns being created in the background. The script

1. creates the tables and simple columns, then inserts the rows,
2. creates the link columns and links the rows,
3. creates the computed columns: formulas, lookups and rollups.

{{< warning  headline="Important note"  text="Do not close the window while the script is running, otherwise the process will be aborted." />}}

At the end, read the report carefully: it lists the columns and formulas you should check. This is what the log of a migration looks like (shortened):

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

Lines starting with an exclamation mark (`!`) point to columns that need your attention. They are all repeated in the report at the end.

If the script stops because tables with the same names already exist in the base, delete these tables or set a `TABLE_PREFIX`. If you are not satisfied with the final result, [delete the tables]({{< relref "help/base-editor/tabellen/loeschen-einer-tabelle-aus-einer-base" >}}) created by the script and start again at step 4.

### 8\. check the result

To make sure that all data has been transferred correctly, a second script compares the NocoDB base with the SeaTable base. Like the migration script, it only reads data: it changes nothing, neither in NocoDB nor in SeaTable.

For every imported table, the verification script compares

- the number of rows (missing and extra rows),
- every simple column, value by value (numbers, dates, selects, checkboxes, texts, attachments…),
- the links: the exact linked records on the "many to one" sides, the number of links on the other sides,
- the computed columns (formulas, lookups, rollups): the value computed by SeaTable against the value computed by NocoDB. This is the check that catches badly translated formulas, time zone shifts and wrong percentage conversions.

Add a second Python script to the base and paste the following code block into it:

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

Fill in `NOCODB_URL`, `NOCODB_TOKEN` and `NOCODB_BASE_ID` as in step 3. If you changed `ONLY_TABLES`, `TABLE_PREFIX`, `ID_COLUMN` or `PERCENT_AS_FRACTION` in the migration script, use the **same values** here. Then click **Run script**.

For each table, the log shows `ok` for every column without difference and `!!` for every column with differences, with a few examples. A summary at the end lists all problems found. Display formats (currency, percent, date format) are not checked.

This is what the log of a successful check looks like (shortened):

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

### 9\. complete migration

The migration script has transferred the data. Some manual rework may still be necessary.

Firstly, check the formulas and columns listed in the report of the migration script and the differences found by the verification script.

On the other hand, you must also recreate the following elements yourself, as they are not transferred from the NocoDB base:

- views, with their filters, sorts and hidden columns,
- forms,
- automations, webhooks, scripts and extensions,
- collaborators and permissions,
- comments and record history,
- default values and validation rules,
- the column order.

The rows get a new creation date in SeaTable. If your NocoDB tables contain CreatedTime or LastModifiedTime columns, their values are imported as ordinary date columns.

Finally, **remove the NocoDB API token from both scripts**: collaborators of the base can read the scripts stored in it. If you no longer need the `NocoDB ID` column, you can delete it.

## FAQ area

{{< faq "Does the script change data in my NocoDB base?" >}}No. Both scripts only read your NocoDB base. The data in the NocoDB base is not changed.
{{< /faq >}}

{{< faq "What do I do if I receive an error message?" >}}An error message on first execution is not at all unlikely. There are plenty of reasons for this, e.g. an incorrect token, an incorrect base ID, a missing quotation mark or incorrect indentation. A single error can lead to script execution being aborted.  
If you receive an error message, this is generally not a problem. No data can be lost in NocoDB. Proceed as follows to find the cause of the error:

- In most cases, the error message will give you a hint where to find the error. Follow it, correct the entered parameters and run the script again.
- If the migration was interrupted, delete the tables already created by the script (or set a different `TABLE_PREFIX`) before running it again.
- If the error message is incomprehensible, check all entries for correctness and try again.
- If none of the tips help, get help in the [SeaTable Forum](https://forum.seatable.com/).

> **Important note**: Please remove the NocoDB API token and the base ID before posting screenshots or scripts in the forum.

{{< /faq >}}

{{< faq "Can NocoDB bases of any size be migrated?" >}}In principle, yes. However, the procedure presented in this article with the integrated Python editor is subject to a maximum runtime limit of 15 minutes, i.e. scripts that run for longer than 15 minutes are aborted. This limit can play a role for bases with many records or many file attachments. In this case, you can reduce the runtime by excluding attachments (`IMPORT_ATTACHMENTS = False`). Otherwise, you must run the Python script locally on a computer where there is no runtime limit: in this case, you also need to enter an [API token]({{< relref "help/integrationen/seatable-api/erzeugen-eines-api-tokens" >}}) of the SeaTable base with read and write permissions in `SEATABLE_API_TOKEN`.
{{< /faq >}}

{{< faq "Is it possible to import tables into an existing base?" >}}Yes. The script does not require a base to be empty, but it stops if a table with the same name as a NocoDB table already exists. In this case, use the `TABLE_PREFIX` setting. A new, empty base is still the safest choice.
{{< /faq >}}

{{< faq "Can I migrate a base from a self-hosted NocoDB server?" >}}Yes. Enter the URL of your NocoDB server in `NOCODB_URL`. The script uses the version 2 of the NocoDB API.
{{< /faq >}}
