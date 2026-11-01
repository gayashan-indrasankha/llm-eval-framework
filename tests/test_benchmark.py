import csv, hashlib, json, subprocess, sys, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from validate_data import check_cases
from build_prompts import build

class BenchmarkTests(unittest.TestCase):
    def test_case_schema(self): self.assertEqual(check_cases(),12)
    def test_all_document_ids_are_valid(self):
        for c in json.loads((ROOT/'data/test_cases.json').read_text(encoding='utf-8')):
            self.assertTrue(all(list((ROOT/'data/policies').glob(d+'_*')) for d in c['document_ids']))
    def test_reference_points_and_red_flags(self):
        cases=json.loads((ROOT/'data/test_cases.json').read_text(encoding='utf-8'))
        self.assertTrue(all(len(c['reference_points'])>=2 and len(c['red_flags'])>=1 for c in cases))
    def test_prompt_hashes_match(self):
        build()
        with (ROOT/'generated/prompt_manifest.csv').open(encoding='utf-8',newline='') as f:rows=list(csv.DictReader(f))
        self.assertEqual(len(rows),12)
        for row in rows:
            blob=(ROOT/row['prompt_file']).read_bytes()
            self.assertEqual(hashlib.sha256(blob).hexdigest(),row['prompt_sha256'])
    def test_no_evaluation_scores_prepopulated(self):
        with (ROOT/'data/evaluation_runs_template.csv').open(encoding='utf-8',newline='') as f:
            rows=list(csv.DictReader(f))
        self.assertEqual(rows,[])

if __name__=='__main__':unittest.main()
