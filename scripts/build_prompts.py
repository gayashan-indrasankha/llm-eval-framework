"""Build deterministic, identical, copy-paste prompts for manual testing."""
import csv, hashlib, json
from pathlib import Path
from validate_data import ROOT,check_cases

RULES='You are assisting an internal audit reviewer with synthetic GRC policy analysis. Use ONLY the synthetic policies below as evidence. Do not use outside information. Identify the policy ID for each factual conclusion. If the source does not establish something, say so. An exception is a potential finding requiring human review; never claim proven fraud or confirmed financial loss without evidence. Give a concise answer and a recommended next action when appropriate.'

def build():
    n=check_cases()
    cases=json.loads((ROOT/'data/test_cases.json').read_text(encoding='utf-8'))
    out=ROOT/'generated/prompts';out.mkdir(parents=True,exist_ok=True)
    manifest=[]
    for c in cases:
        content=[]
        for doc_id in c['document_ids']:
            files=list((ROOT/'data/policies').glob(f'{doc_id}_*.md'))
            content.append(files[0].read_text(encoding='utf-8').strip())
        prompt=f"{RULES}\n\n=== SOURCE DOCUMENTS ===\n"+'\n\n'.join(content)+f"\n\n=== QUESTION ({c['case_id']}) ===\n{c['question']}\n"
        p=out/f"{c['case_id']}.txt";p.write_bytes(prompt.encode('utf-8'))
        manifest.append({'case_id':c['case_id'],'category':c['category'],'prompt_file':p.relative_to(ROOT).as_posix(),'prompt_sha256':hashlib.sha256(prompt.encode('utf-8')).hexdigest()})
    with (ROOT/'generated/prompt_manifest.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=manifest[0].keys());w.writeheader();w.writerows(manifest)
    print(f'Prompt build: PASS ({n} deterministic prompts written to generated/prompts/)')

if __name__=='__main__':build()
