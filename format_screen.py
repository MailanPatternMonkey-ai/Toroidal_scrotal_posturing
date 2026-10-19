"""Read-only PDF rendering and conservative RTF text screening.

RTF extraction is for triage; embedded objects and pictures are omitted and
equation/layout fidelity is not certified. Original bytes remain preserved.
"""
from pathlib import Path
import hashlib,json,re,zipfile
import pypdfium2 as pdfium

ROOT=Path(__file__).resolve().parent
inv=json.loads((ROOT/'inventory.json').read_text(encoding='utf-8'))
idx=json.loads((ROOT/'content_index.json').read_text(encoding='utf-8'))
by_id={i:u for u in idx for i in u['entry_ids']}
(ROOT/'renders').mkdir(exist_ok=True)
pdf=pdfium.PdfDocument(str(ROOT/'selected/R05-1365.pdf'))
rendered=[]
for page_num in [26,27,31]:
    page=pdf[page_num-1]
    img=page.render(scale=1.7).to_pil()
    target=ROOT/'renders'/f'EG-page-{page_num:03d}.png'
    img.save(target)
    rendered.append(str(target))
    page.close()
pdf.close()

TOKEN=re.compile(r"\\([a-zA-Z]+)(-?\d+)? ?|\\'([0-9a-fA-F]{2})|\\([^a-zA-Z])|([{}])|([^\\{}\r\n]+)")
DEST={'fonttbl','colortbl','stylesheet','info','pict','object','objdata','themedata','datastore',
      'listtable','listoverridetable','revtbl','rsidtbl','generator','filetbl','fldinst',
      'colorschememapping','xmlnstbl','shp','shpinst','nonshppict','private','mmathPr'}


def rtf_text(data):
    raw=data.decode('cp1252',errors='replace')
    stack=[];ignore=False;uc=1;skip=0;out=[];omitted=0
    for m in TOKEN.finditer(raw):
        word,num,hexbyte,sym,brace,plain=m.groups()
        if brace=='{':
            stack.append((ignore,uc));skip=0
        elif brace=='}':
            if stack: ignore,uc=stack.pop()
            skip=0
        elif word:
            if word in DEST:
                ignore=True;omitted+=1
            elif word=='uc' and num is not None:
                uc=int(num)
            elif word=='u' and num is not None:
                if not ignore: out.append(chr(int(num)%65536))
                skip=uc
            elif not ignore and word in ['par','line','row']:
                out.append('\n')
            elif not ignore and word in ['tab','cell']:
                out.append('\t')
            elif not ignore and word in {'emdash','endash','lquote','rquote','ldblquote','rdblquote','bullet'}:
                out.append({'emdash':'—','endash':'–','lquote':'‘','rquote':'’','ldblquote':'“','rdblquote':'”','bullet':'•'}[word])
        elif hexbyte:
            if skip:skip-=1
            elif not ignore:out.append(bytes([int(hexbyte,16)]).decode('cp1252',errors='replace'))
        elif sym:
            if sym=='*':ignore=True
            elif skip:skip-=1
            elif not ignore:out.append({'~':' ','_':'‑','-':''}.get(sym,sym))
        elif plain and not ignore:
            if skip:
                n=min(skip,len(plain));plain=plain[n:];skip-=n
            out.append(plain)
    s=''.join(out)
    s=s.encode('utf-16','surrogatepass').decode('utf-16','replace')
    return s,omitted


records=[]
with zipfile.ZipFile(ROOT/'sources/read-05.zip') as z:
    for key in ['R05-0392','R05-0393','R05-3827','R05-2353']:
        u=by_id[key]
        i=next(e['index'] for e in inv['entries'] if e['id']==key)
        data=z.read(z.infolist()[i])
        assert hashlib.sha256(data).hexdigest()==u['sha256']
        text,omitted=rtf_text(data)
        path=ROOT/'selected'/(key+'.rtf.screen.txt')
        path.write_text(text,encoding='utf-8',newline='\n')
        rec={'id':key,'names':u['names'],'source_sha256':u['sha256'],'source_bytes':len(data),
             'screen_text':str(path),'text_characters':len(text),'text_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
             'omitted_destination_occurrences':omitted,'scope':'Lossy triage extraction; no equation or layout certification.'}
        records.append(rec)
        print(json.dumps(rec,ensure_ascii=False))
        print(text[:500])
(ROOT/'reports/format_screen.json').write_text(json.dumps({'PDF_rendered_pages':rendered,'RTF_screen':records},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
