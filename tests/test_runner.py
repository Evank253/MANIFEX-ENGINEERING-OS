import tempfile,unittest
from engineering_runner.manager import ExecutionManager
from engineering_runner.models import ProjectContract
class RunnerTests(unittest.TestCase):
    def contract(self,path):
        return ProjectContract.model_validate({"id":"TEST-PROJECT","version":"1","source":{"type":"local","path":path},"runtime":{"adapter":"shell","entrypoint":"python -c \"print('runner-ok')\"","timeout_seconds":30},"execution":{"mode":"sandboxed"},"evidence":{"required":True}})
    def test_contract_rejects_unsandboxed(self):
        m=ExecutionManager()
        with self.assertRaises(ValueError):m.register(self.contract(tempfile.gettempdir()).model_copy(update={"execution":{"mode":"unsandboxed"}}))
    def test_project_run_produces_evidence(self):
        with tempfile.TemporaryDirectory() as source:
            m=ExecutionManager();m.register(self.contract(source));r=m.start("TEST-PROJECT")
            self.assertEqual(r.result,"PASS");self.assertTrue(r.evidence_refs);self.assertIn("stdout.log",r.evidence_refs);self.assertIn("manifest.json",r.evidence_refs)
