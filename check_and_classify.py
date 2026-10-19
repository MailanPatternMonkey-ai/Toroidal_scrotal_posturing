"""Independent finite loss calculations and a conservative relevance catalogue."""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import csv,hashlib,json,re

ROOT=Path(__file__).resolve().parent
idx=json.loads((ROOT/'content_index.json').read_text(encoding='utf-8'))
inv=json.loads((ROOT/'inventory.json').read_text(encoding='utf-8'))
by_id={i:u for u in idx for i in u['entry_ids']}


def dump(path,value):
    path.write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')


def partitions(n):
    def walk(a):
        if len(a)==n:
            yield tuple(a);return
        for k in range(max(a)+2):
            yield from walk(a+[k])
    yield from walk([0])


def floor_and_means(pi,w,p):
    masses={q:sum((p[i] for i in range(len(pi)) if pi[i]==q),F()) for q in set(pi)}
    means={q:sum((p[i]*w[i] for i in range(len(pi)) if pi[i]==q),F())/masses[q] for q in set(pi)}
    floor=sum((p[i]*(w[i]-means[pi[i]])**2 for i in range(len(pi))),F())
    return floor,means,masses


parts=list(partitions(4));assert len(parts)==15
weights=[(F(1,4),)*4,(F(1,10),F(2,10),F(3,10),F(4,10)),(F(7,10),F(1,10),F(1,10),F(1,10))]
w=(F(0),F(2),F(-1),F(3))
case_records=[];identity_checks=0;refinement_checks=0
for p in weights:
    floors={}
    for pi in parts:
        floor,means,masses=floor_and_means(pi,w,p)
        floors[pi]=floor
        qs=sorted(means)
        for values in product([F(-1),F(0),F(1),F(2),F(3)],repeat=len(qs)):
            g=dict(zip(qs,values))
            actual=sum((p[i]*(g[pi[i]]-w[i])**2 for i in range(4)),F())
            excess=sum((masses[q]*(g[q]-means[q])**2 for q in qs),F())
            assert actual==floor+excess and actual>=floor
            identity_checks+=1
        exact=sum((p[i]*(means[pi[i]]-w[i])**2 for i in range(4)),F())
        assert exact==floor
        descent=all(w[i]==w[j] for i in range(4) for j in range(4) if pi[i]==pi[j])
        assert (floor==0)==descent
        case_records.append({'weights':list(map(str,p)),'partition':pi,'minimum_loss':str(floor),
                             'attained_means':{str(q):str(means[q]) for q in qs}})
    for coarse in parts:
        for fine in parts:
            refines=all(coarse[i]==coarse[j] for i in range(4) for j in range(4) if fine[i]==fine[j])
            if refines:
                assert floors[fine]<=floors[coarse]
                refinement_checks+=1

binary=[]
for p_one in [F(1,100),F(1,4),F(1,2),F(3,4),F(99,100)]:
    p=(1-p_one,p_one)
    coarse,means,_=floor_and_means((0,0),(F(0),F(1)),p)
    refined,_,_=floor_and_means((0,1),(F(0),F(1)),p)
    assert coarse==p_one*(1-p_one) and means[0]==p_one and refined==0
    # The representation has changed, but a constant-only rule still has exactly
    # the same attainable actions and the same floor.
    constant_only_after_refinement=coarse
    binary.append({'probability_W_equals_1':str(p_one),'constant_best_action':str(p_one),
                   'erased_label_squared_loss':str(coarse),'retained_label_unrestricted_loss':str(refined),
                   'retained_label_constant_only_loss':str(constant_only_after_refinement)})

# A close pair under one metric need not share an exact observation fiber.
x,y=F(0),F(1,1000)
metric_example={'states':[str(x),str(y)],'projection':'identity',
                'coarse_distance':str(abs(x-y)),'rescaled_distance':str(10000*abs(x-y)),
                'same_exact_fiber':x==y,'explanation':'Both metrics are on the same injectively retained state; a distance of 1/1000 versus 10 is not an exact non-descent witness.'}
assert not metric_example['same_exact_fiber']
checks={'status':'PASS_WITH_DECLARED_SCOPE','source_programs_executed':False,
        'arithmetic':'Exact rational calculations; no fitting or physical observations.',
        'conditional_squared_loss':{'finite_models':len(case_records),'partitions_per_weight_vector':len(parts),
                                   'identity_fixtures':identity_checks,'refinement_comparisons':refinement_checks,
                                   'models':case_records},
        'binary_example':binary,'metric_counterexample':metric_example,
        'nonattainment_example':{'domain':'one point','target':0,'admissible_actions':'c in (0,1]',
                                'cost':'c^2','infimum':0,'attained':False,
                                'argument':'Every admissible c has positive cost, while c=1/n tends to zero.'},
        'limits':['The accompanying algebraic expansion proves the finite formula; these fixtures are supplementary.',
                  'A population law and action class are assumptions of a model, not measured facts about the archive.',
                  'No empirical 72-bank, 39-screen, toroidal sampler or physical experiment was rerun.']}
dump(ROOT/'independent_math_checks.json',checks)

manual={
    'R05-1365':('PROMOTE_SELECTED_MATHEMATICS','Selected local-solvability, native-loss and admissible-rule material; public v1 identity checked, no complete monograph audit.'),
    'R05-0574':('PARALLEL_PDF_TEXT_EXPORT','Existing text export of the selected monograph; not independent scientific evidence.'),
    'R05-0322':('SUPPORT_EXISTING_OPERATIONAL_GEOMETRY','Full text reviewed; criterion, correction and delivery distinctions already present in master.'),
    'R05-0001':('DOCUMENT_LINEAGE_CONTEXT','Opening and count-lineage passages screened; source-reported comparison, no new actor finding.'),
    'R05-0678':('CURRENT_CORRECTION_CARRY_FORWARD','Selected recurrence paragraph confirms already retained 69/198 versus 70/198 coding distinction.'),
    'R05-1399':('EXISTING_SOFTWARE_SCOPE','Guide reviewed; finite-model tools and historical test reports, not a fresh run or recovered executable package in this intake.'),
    'R05-1406':('HISTORICAL_EXECUTION_OUTPUT','Log artifact only; no fresh execution or new source binding asserted.'),
    'R05-1386':('THERMODYNAMIC_VERSION_CONTEXT','Full diff reviewed; added witnesses do not measure energy or physical savings.'),
    'R05-1392':('THERMODYNAMIC_VERSION_CONTEXT','Compared through supplied diff; original text otherwise selectively screened.'),
    'R05-1393':('THERMODYNAMIC_VERSION_CONTEXT','Compared through supplied diff; later witness additions align with current master.'),
    'R05-2353':('RESTORE_EXPLICIT_PRIOR_EMPIRICAL_STATUS','Complete lossy RTF text screen read; main conclusions cross-checked against prior plain-text source. Results source-reported, not rerun.'),
    'R05-1019':('DEFER_EMPIRICAL_QUOTIENT_CLAIM','Full text read; similarity in different metrics alone does not establish an exact same-fiber counterexample. Orbital data not revalidated.'),
    'R05-1030':('ADJACENT_HYPOTHESIS_METHOD','Opening interval/target distinction reviewed; scientific dating and causal claims not revalidated or imported.'),
    'R05-0394':('ADJACENT_APPLICATION_REFERENCE','First five PDF pages text-screened; physical interface/assembly application, not an upgrade to the current quotient proofs.'),
    'R05-0392':('MIXED_CONTEXT_DEFERRED','Lossy RTF conversion and opening screened; broader personal/history context not incorporated into geometry.'),
    'R05-0393':('MATH_BACKGROUND_DEFERRED','Lossy RTF conversion; Jacobi/hypergeometric introductory sections and headings screened. No proved mapping to the project kernel supplied by this review.'),
    'R05-3827':('MIXED_SURVEY_DEFERRED','Lossy RTF conversion; parallel long conversation material not universally proof-audited.'),
    'R05-3828':('MIXED_SURVEY_DEFERRED','Opening and subject screening only; do not promote every quoted mathematical or physical claim.'),
}
presentation=json.loads((ROOT/'reports/presentation_matches.json').read_text(encoding='utf-8'))
present={r['id']:r for r in presentation if r['matching_text_ids']}
catalog=[]
for u in idx:
    key=u['representative_id']
    if key in manual:
        disposition,note=manual[key]
    elif not u['bytes']:
        disposition,note='EMPTY_PLACEHOLDER','Zero bytes; filename supplies no recoverable content.'
    elif u['prior_exact_matches']:
        disposition,note='EXACT_PRIOR_CONTENT','Exact prior byte identity; not automatically a new result or full prior proof audit.'
    elif u.get('prior_whitespace_only_matches'):
        disposition,note='WHITESPACE_PRIOR_CONTENT','Content matches after declared whitespace normalization; original identities retained.'
    elif key in present:
        disposition,note='PRESENTATION_EQUIVALENT_WITHIN_ARCHIVE','Exact token match after the recorded line-number/paragraph-prefix removal; original byte identity remains distinct.'
    elif u['bytes']>8*1024*1024:
        disposition,note='LARGE_BODY_INVENTORY_ONLY','Full CRC/hash verified; original retained; no content-level relevance conclusion.'
    elif u['name_signals'].get('core_geometry') or u['name_signals'].get('clock_thermo'):
        disposition,note='GEOMETRY_CANDIDATE_SCREEN_ONLY','Title/keyword candidate; often an older export or alternate format. Further claim-level review required before import.'
    elif u['name_signals'].get('evidence_geometry'):
        disposition,note='OPERATIONAL_CONTEXT_SCREEN_ONLY','Potential evidence/service/lineage context; no new mathematical or causal conclusion imported.'
    else:
        disposition,note='OTHER_OR_MIXED_SCREEN_ONLY','Inventory and available text keyword screening; no blanket irrelevance or accuracy conclusion.'
    catalog.append({'id':key,'sha256':u['sha256'],'bytes':u['bytes'],'occurrences':len(u['entry_ids']),
                    'names':u['names'],'entry_ids':u['entry_ids'],'disposition':disposition,'review_note':note,
                    'prior_exact_match_count':len(u['prior_exact_matches']),
                    'prior_whitespace_match_count':len(u.get('prior_whitespace_only_matches',[]))})
dump(ROOT/'relevance_catalogue.json',{'method':'Triage labels reflect review depth and routing; keyword labels do not certify relevance, truth, novelty or completeness.',
                                   'counts':dict(Counter(r['disposition'] for r in catalog)),'contents':catalog})
with (ROOT/'relevance_catalogue.csv').open('w',newline='',encoding='utf-8-sig') as f:
    writer=csv.DictWriter(f,fieldnames=['id','disposition','bytes','occurrences','sha256','names','review_note'])
    writer.writeheader()
    for r in catalog:
        row={k:r[k] for k in writer.fieldnames}
        row['names']=' | '.join(row['names'])
        for k,v in row.items():
            if isinstance(v,str) and v.startswith(('=','+','-','@')):row[k]="'"+v
        writer.writerow(row)

# Retain exact RTF source used in the carry-forward note; extracted text remains
# a separately identified derivative with omissions declared.
obj=by_id['R05-2353']
(ROOT/'selected/R05-2353.rtf').write_bytes(Path(obj['object_path']).read_bytes())
print(json.dumps({'finite_loss_models':len(case_records),'exact_identity_fixtures':identity_checks,
                  'refinement_comparisons':refinement_checks,'balanced_binary_floor':str(F(1,4)),
                  'catalogue_dispositions':dict(Counter(r['disposition'] for r in catalog))},indent=2))
