"""Preserve, hash and triage the user-supplied mixed read-05 archive.

Archive entry names never become extraction paths. No archived code is run.
Full byte inventory is distinct from selected content review.
"""
from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime, timezone
import hashlib
import json
import re
import shutil
import zipfile

ROOT=Path(__file__).resolve().parent
WORK=ROOT.parent
ORIGINAL=Path(r'C:\Users\drewd\OneDrive\Desktop\read-05.zip')
COPY=ROOT/'sources/read-05.zip'
LIMIT=8*1024*1024
for name in ['sources','objects','selected','reports']:
    (ROOT/name).mkdir(exist_ok=True)


def filehash(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda:f.read(1024*1024),b''):
            h.update(block)
    return h.hexdigest()


def dump(path,obj):
    path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')


if not COPY.exists():
    shutil.copy2(ORIGINAL,COPY)
source_sha=filehash(ORIGINAL)
assert filehash(COPY)==source_sha
print(json.dumps({'phase':'source_preserved','bytes':ORIGINAL.stat().st_size,'sha256':source_sha}),flush=True)

known=defaultdict(list)
known_normal=defaultdict(list)
for base in [WORK,WORK.parent/'outputs']:
    for p in base.rglob('*'):
        if not p.is_file() or ROOT in p.parents or p.suffix.lower() not in ['.txt','.md','.csv','.json','.html']:
            continue
        if p.stat().st_size>LIMIT:
            continue
        data=p.read_bytes()
        known[hashlib.sha256(data).hexdigest()].append(str(p))
        if p.suffix.lower() not in ['.txt','.md']:
            continue
        try:
            s=data.decode('utf-8-sig')
        except UnicodeDecodeError:
            continue
        key=hashlib.sha256(' '.join(s.split()).encode()).hexdigest()
        known_normal[key].append(str(p))

patterns={
    'core_geometry':r'geometry|geometric|quotient|toroid|gqg|maximi[sz]ation|lumpab|villain|brjuno|non.?descent|cocycle|TTSC',
    'clock_thermo':r'bifurcat|thermodynam|silver.clock|phase.closure|phase.model|predictive.fiber',
    'evidence_geometry':r'four.space|witness|lineage|RHEA|constraint.response|direct.service|correction.binding',
    'other_domain':r'CCBHC|SPARS|SUPRT|clinical|Revelation|Babylon|Hillman|poem|Aquinas|grant.report',
}
compiled={k:re.compile(v,re.I) for k,v in patterns.items()}
rows=[]
unique={}
failures=[]
names=Counter()
with zipfile.ZipFile(COPY) as z:
    for i,info in enumerate(z.infolist()):
        row={'id':f'R05-{i:04d}','index':i,'name':info.filename,'bytes':info.file_size,
             'compressed_bytes':info.compress_size,'crc32':f'{info.CRC:08x}',
             'date_time':info.date_time,'directory':info.is_dir(),
             'encrypted':bool(info.flag_bits&1),'extension':Path(info.filename).suffix.lower()}
        names[info.filename]+=1
        try:
            h=hashlib.sha256();parts=[]
            with z.open(info) as f:
                for block in iter(lambda:f.read(1024*1024),b''):
                    h.update(block)
                    if info.file_size<=LIMIT:
                        parts.append(block)
            row['sha256']=digest=h.hexdigest()
            row['body_read_crc_checked']=True
        except Exception as exc:
            row['read_error']=repr(exc)
            failures.append(row['id'])
            rows.append(row)
            continue
        if digest not in unique:
            obj={'sha256':digest,'representative_id':row['id'],'bytes':info.file_size,
                 'entry_ids':[],'names':[],'prior_exact_matches':known.get(digest,[]),
                 'name_signals':{},'body_signals':{}}
            if info.file_size and info.file_size<=LIMIT:
                data=b''.join(parts)
                dest=ROOT/'objects'/(digest+row['extension'])
                if not dest.exists():
                    dest.write_bytes(data)
                obj['object_path']=str(dest)
                if row['extension'] in ['.txt','.csv','.html','.xml','.rtf']:
                    text=None
                    for enc in ['utf-8-sig']+(['utf-16'] if data.startswith((b'\xff\xfe',b'\xfe\xff')) else []):
                        try:
                            text=data.decode(enc)
                            obj['encoding']=enc
                            break
                        except UnicodeDecodeError:
                            pass
                    if text is not None:
                        obj['lines']=len(text.splitlines())
                        obj['head']=text[:700]
                        obj['body_signals']={k:len(p.findall(text)) for k,p in compiled.items()}
                        if row['extension']=='.txt':
                            norm=hashlib.sha256(' '.join(text.split()).encode()).hexdigest()
                            obj['whitespace_sha256']=norm
                            obj['prior_whitespace_only_matches']=known_normal.get(norm,[]) if not obj['prior_exact_matches'] else []
                        obj['headings']=[{'line':n+1,'text':line[:200]} for n,line in enumerate(text.splitlines())
                                         if re.match(r'^\s*#{1,6}\s',line)][:120]
                    else:
                        obj['text_decode']='No successful supported decode; bytes preserved.'
            elif info.file_size>LIMIT:
                obj['body_text_screen']='Not decoded: above 8 MiB limit; full bytes hashed/CRC checked.'
            unique[digest]=obj
        obj=unique[digest]
        obj['entry_ids'].append(row['id'])
        if info.filename not in obj['names']:
            obj['names'].append(info.filename)
        for k,p in compiled.items():
            obj['name_signals'][k]=obj['name_signals'].get(k,False) or bool(p.search(info.filename))
        rows.append(row)
        if (i+1)%1000==0:
            print(json.dumps({'phase':'entry_integrity','entries_read':i+1,'distinct_contents':len(unique)}),flush=True)

summary={
    'entries':len(rows),'uncompressed_bytes':sum(r['bytes'] for r in rows),
    'distinct_contents_including_empty':len(unique),
    'distinct_nonempty_contents':sum(u['bytes']>0 for u in unique.values()),
    'empty_entries':sum(r['bytes']==0 for r in rows),
    'repeated_name_groups':sum(n>1 for n in names.values()),
    'different_contents_under_same_name':sum(len({r['sha256'] for r in rows if r['name']==name and 'sha256' in r})>1 for name,n in names.items() if n>1),
    'extensions_by_entry':dict(Counter(r['extension'] for r in rows)),
    'exact_prior_distinct_nonempty':sum(bool(u['prior_exact_matches']) and u['bytes']>0 for u in unique.values()),
    'whitespace_prior_distinct_nonempty':sum(bool(u.get('prior_whitespace_only_matches')) and u['bytes']>0 for u in unique.values()),
    'large_distinct_unparsed':sum(u['bytes']>LIMIT for u in unique.values()),
    'integrity_failures':failures,
}
record={'recorded_utc':datetime.now(timezone.utc).isoformat(),
        'source':{'original':str(ORIGINAL),'preserved_copy':str(COPY),'bytes':COPY.stat().st_size,
                  'sha256':source_sha,'original_mtime_ns':ORIGINAL.stat().st_mtime_ns},
        'method':'Every ZIP body streamed and CRC/SHA-256 checked. Entries keyed by central-directory index, including duplicate names. Unique objects <=8 MiB preserved; larger bodies retained in original ZIP. Text keywords are triage signals, not relevance or truth labels.',
        'normalization':'Optional UTF-8 BOM plus whitespace runs collapsed; no other text removed.',
        'prior_files_compared':sum(map(len,known.values())),'summary':summary,'entries':rows}
dump(ROOT/'inventory.json',record)
dump(ROOT/'content_index.json',list(unique.values()))
dump(ROOT/'reports/duplicate_names.json',{'repeated_names':{k:v for k,v in names.items() if v>1}})
assert filehash(ORIGINAL)==source_sha==filehash(COPY)
print(json.dumps({'phase':'complete','summary':summary},indent=2),flush=True)
new=[u for u in unique.values() if u['bytes'] and not u['prior_exact_matches'] and not u.get('prior_whitespace_only_matches')]
candidates=[u for u in new if u['name_signals'].get('core_geometry') or u['name_signals'].get('clock_thermo')]
dump(ROOT/'reports/new_geometry_candidates.json',candidates)
print(json.dumps({'new_geometry_named_distinct':len(candidates),'candidate_names':[(u['representative_id'],u['names'][:2],u['bytes']) for u in candidates[:65]]},ensure_ascii=False,indent=2))
