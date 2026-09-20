from __future__ import annotations
import itertools, json, platform, sys
from pathlib import Path
from threading import Lock
from .adapters import ADAPTERS
from .capabilities import CapabilityBroker
from .evidence import EvidenceEngine,canonical_hash
from .models import ProjectContract,RunRecord,RunStatus
from .workspace import WorkspaceManager
class ProjectRegistry:
    def __init__(self): self._projects={}; self._lock=Lock()
    def register(self,contract):
        with self._lock:
            old=self._projects.get(contract.id)
            if old and old.version!=contract.version: raise ValueError("project id already registered at a different version")
            self._projects[contract.id]=contract; return contract
    def get(self,project_id): return self._projects[project_id]
    def list(self): return list(self._projects.values())
class ExecutionManager:
    def __init__(self):
        self.projects=ProjectRegistry(); self.workspaces=WorkspaceManager(); self.capabilities=CapabilityBroker(); self.evidence=EvidenceEngine()
        self._runs={}; self._counter=itertools.count(1); self._lock=Lock()
    def register(self,contract):
        if contract.runtime.adapter not in ADAPTERS: raise ValueError(f"unsupported runtime adapter: {contract.runtime.adapter}")
        if contract.execution.mode!="sandboxed": raise ValueError("ENGINEERING-RUNNER-001 only permits sandboxed mode")
        return self.projects.register(contract)
    def start(self,project_id):
        contract=self.projects.get(project_id)
        with self._lock:
            run_id=f"RUN-{__import__('datetime').datetime.now().year}-{next(self._counter):06d}"; record=RunRecord.new(run_id,contract); self._runs[run_id]=record
        workspace=self.workspaces.create(run_id,contract)
        try:
            self.workspaces.prepare_source(workspace,contract); self.capabilities.grant(contract.capabilities)
            record=record.model_copy(update={"status":RunStatus.PREPARING,"workspace":str(workspace),"environment_hash":canonical_hash({"python":sys.version,"platform":platform.platform()})}).started(); self._runs[run_id]=record
            output=ADAPTERS[contract.runtime.adapter].run(contract,workspace)
            status=RunStatus.COMPLETED if output.exit_code==0 else RunStatus.FAILED
            evidence_refs=self.evidence.collect(workspace,run_id=run_id,record=record.model_dump(mode="json"),stdout=output.stdout,stderr=output.stderr,command=output.command)
            record=record.finished(status,exit_code=output.exit_code,result="PASS" if output.exit_code==0 else "FAIL").model_copy(update={"evidence_refs":evidence_refs}); self._runs[run_id]=record; return record
        except Exception as exc:
            record=record.finished(RunStatus.FAILED,exit_code=None,error=f"{type(exc).__name__}: {exc}"); self._runs[run_id]=record; return record
    def get_run(self,run_id): return self._runs[run_id]
    def list_runs(self): return list(self._runs.values())
    def logs(self,run_id):
        r=self.get_run(run_id); root=Path(r.workspace)/"evidence" if r.workspace else None
        return {"stdout":(root/"stdout.log").read_text() if root and (root/"stdout.log").exists() else "","stderr":(root/"stderr.log").read_text() if root and (root/"stderr.log").exists() else ""}
    def evidence_manifest(self,run_id):
        r=self.get_run(run_id); p=Path(r.workspace)/"evidence"/"manifest.json" if r.workspace else None
        return json.loads(p.read_text()) if p and p.exists() else {}
