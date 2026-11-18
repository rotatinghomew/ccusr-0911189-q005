import copy
import json
from pathlib import Path
import subprocess
import sys
import unittest

from bulletin_trial.workflow import report


class WorkflowTest(unittest.TestCase):
    def setUp(self):
        self.path = Path(__file__).resolve().parents[1] / 'data' / 'sample.json'
        self.data = json.loads(self.path.read_text(encoding='utf-8'))

    def test_entry(self):
        result = subprocess.run([sys.executable, '-m', 'bulletin_trial', 'rounds', str(self.path)],
                                check=True, capture_output=True, text=True)
        self.assertEqual(json.loads(result.stdout), report(self.data))

    def test_assignment_does_not_follow_execution(self):
        rows = report(self.data)['cells']
        self.assertEqual((rows[2]['assigned'], rows[2]['actual']), ('paper','audio'))
        self.assertEqual((rows[1]['returned'], rows[1]['missing']), (1,1))
        self.assertEqual(rows[0]['topic'], rows[1]['topic'])

    def test_unserved_station(self):
        self.assertEqual(report(self.data)['unserved'], [['B',2]])
