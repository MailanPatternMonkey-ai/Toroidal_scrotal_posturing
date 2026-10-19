"""Extract selected review copies and PDF text without executing content."""
from pathlib import Path
import hashlib,json,re,zipfile
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parent
idx=json.loads((ROOT/'content_index.json').read_text(encoding='utf-8'))
inv=json.loads((ROOT/'inventory.json').read_text(encoding='utf-8'))
by_id={e['id']:u for u in idx for e in [{'id':i} for i in u['entry_ids']]}
chosen=['R05-0001','R05-0009','R05-0315','R05-0322','R05-0678','R05-0906',
        'R05-1019','R05-1030','R05-1172','R05-1173','R05-1386','R05-1392','R05-1393',
        'R05-1399','R05-1406','R05-4097','R05-3828']
records=[]
for key in chosen:
    obj=by_id[key]
    src=Path(obj['object_path'])
    dest=ROOT/'selected'/(key+src.suffix)
    dest.write_bytes(src.read_bytes())
    records.append({'id':key,'original_names':obj['names'],'source_sha256':obj['sha256'],
                    'selected_copy':str(dest),'format':'byte-identical source copy'})

with zipfile.ZipFile(ROOT/'sources/read-05.zip') as z:
    for key in ['R05-1365','R05-0394']:
        obj=by_id[key]
        entry=next(e for e in inv['entries'] if e['id']==key)
        data=z.read(z.infolist()[entry['index']])
        assert hashlib.sha256(data).hexdigest()==obj['sha256']
        dest=ROOT/'selected'/(key+'.pdf')
        dest.write_bytes(data)
        pdf=PdfReader(dest)
        page_ids=range(len(pdf.pages)) if key=='R05-1365' else range(min(5,len(pdf.pages)))
        extracts=[]
        for i in page_ids:
            text=pdf.pages[i].extract_text() or ''
            extracts.append(f'=== PDF PAGE {i+1} ===\n'+text)
        textpath=ROOT/'selected'/(key+'.pdf.txt')
        textpath.write_text('\n\n'.join(extracts),encoding='utf-8',newline='\n')
        rec={'id':key,'original_names':obj['names'],'source_sha256':obj['sha256'],
             'selected_copy':str(dest),'text_copy':str(textpath),'pdf_pages':len(pdf.pages),
             'pages_extracted':[i+1 for i in page_ids], 'format':'PDF text extraction; layout not inferred'}
        records.append(rec)
        print(json.dumps(rec,ensure_ascii=False))
        print(textpath.read_text(encoding='utf-8')[:3500])

(ROOT/'selected_manifest.json').write_text(json.dumps(records,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

# Additional presentation normalization is a declared lookup aid, never a new
# original identity. Numbered readbacks are matched only after their prefixes
# are removed, and the result is recorded separately from exact bytes.
base_tokens={}
for u in idx:
    if not u.get('object_path') or Path(u['object_path']).suffix!='.txt': continue
    text=Path(u['object_path']).read_text(encoding=u.get('encoding','utf-8'),errors='replace')
    token=' '.join(text.split())
    base_tokens.setdefault(hashlib.sha256(token.encode()).hexdigest(),[]).append(u['representative_id'])
derived=[]
for u in idx:
    if not u.get('object_path') or Path(u['object_path']).suffix!='.txt': continue
    text=Path(u['object_path']).read_text(encoding=u.get('encoding','utf-8'),errors='replace')
    nonblank=[x for x in text.splitlines() if x.strip()]
    mode=None
    if nonblank and sum(bool(re.match(r'^\d{4,5} ',x)) for x in nonblank)>=.8*len(nonblank):
        mode='leading 4-5-digit line numbers only'
        cleaned=re.sub(r'^\d{4,5} ','',text,flags=re.M)
    elif nonblank and sum(bool(re.match(r'^\[word/[^]]+\] ',x)) for x in nonblank)>=.8*len(nonblank):
        mode='leading word-part paragraph markers only'
        cleaned=re.sub(r'^\[word/[^]]+\] ','',text,flags=re.M)
    if mode:
        digest=hashlib.sha256(' '.join(cleaned.split()).encode()).hexdigest()
        matches=[x for x in base_tokens.get(digest,[]) if x!=u['representative_id']]
        derived.append({'id':u['representative_id'],'transformation':mode,'matching_text_ids':matches,
                        'normalized_sha256':digest})
(ROOT/'reports/presentation_matches.json').write_text(json.dumps(derived,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'selected_sources':len(records),'presentation_matches':sum(bool(x['matching_text_ids']) for x in derived)},indent=2))
