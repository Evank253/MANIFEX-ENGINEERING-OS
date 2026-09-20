from pathlib import Path
import shutil, tempfile
from .models import ProjectContract
class WorkspaceManager:
    def create(self,run_id,contract): 
        root=Path(tempfile.mkdtemp(prefix=f"{run_id}-")); (root/"evidence").mkdir(); return root
    def prepare_source(self,workspace,contract):
        if contract.source.type=="local" and contract.source.path:
            src=Path(contract.source.path).resolve()
            if not src.exists(): raise FileNotFoundError(src)
            dst=workspace/"source"
            shutil.copytree(src,dst) if src.is_dir() else (dst.mkdir(),shutil.copy2(src,dst/src.name))
        elif contract.source.type=="github":
            raise NotImplementedError("GitHub source materialization requires a dedicated source broker")
        else: (workspace/"source").mkdir(exist_ok=True)
    def cleanup(self,workspace): shutil.rmtree(workspace,ignore_errors=True)
