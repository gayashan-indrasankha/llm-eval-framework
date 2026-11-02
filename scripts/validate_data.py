"""Validate the synthetic benchmark design; does not call or score LLMs."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def check_cases():
    cases=json.loads((ROOT/'data/test_cases.json').read_text(encoding='utf-8'))
    assert cases, 'No test cases'
    ids=set()
    for case in cases:
        cid=case['case_id']
        assert cid not in ids, f'Duplicate case: {cid}'
        ids.add(cid)
        assert case['question'].strip() and case['reference_points'] and case['red_flags'], cid
        assert case['document_ids'], cid
        for doc_id in case['document_ids']:
            matches=list((ROOT/'data/policies').glob(f'{doc_id}_*.md'))
            assert len(matches)==1, f'Expected one policy for {doc_id}, found {len(matches)}'
            text=matches[0].read_text(encoding='utf-8')
            assert 'Synthetic' in text, f'{doc_id} must be labeled synthetic'
    return len(cases)

if __name__=='__main__':
    n=check_cases()
    print(f'Dataset validation: PASS ({n} synthetic cases; model results not assessed by this check)')
