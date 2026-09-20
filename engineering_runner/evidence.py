from __future__ import annotations
import hashlib,json
from datetime import datetime,timezone
from pathlib import Path
def canonical_hash(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
class EvidenceEngine:
    def collect(self,workspace,*,run_id,record,stdout,stderr,command):
        evidence=workspace/"evidence"; evidence.mkdir(exist_ok=True)
        manifest={"run_id":run_id,"timestamp":datetime.now(timezone.utc).isoformat(),"record":record,"command":command,"stdout_sha256":hashlib.sha256(stdout.encode()).hexdigest(),"stderr_sha256":hashlib.sha256(stderr.encode()).hexdigest()}
        (evidence/"stdout.log").write_text(stdout,encoding="utf-8"); (evidence/"stderr.log").write_text(stderr,encoding="utf-8")
        (evidence/"manifest.json").write_text(json.dumps(manifest,indent=2,sort_keys=True),encoding="utf-8")
        (evidence/"hashes.json").write_text(json.dumps({"manifest_sha256":canonical_hash(manifest),"stdout_sha256":manifest["stdout_sha256"],"stderr_sha256":manifest["stderr_sha256"]},indent=2,sort_keys=True),encoding="utf-8")
        return [str(p.relative_to(workspace)) for p in evidence.iterdir()]
