from __future__ import annotations
import os, shlex, subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol
from .models import ProjectContract

@dataclass(frozen=True)
class ExecutionOutput:
    exit_code:int; stdout:str; stderr:str; command:list[str]

class RuntimeAdapter(Protocol):
    name:str
    def validate(self,contract:ProjectContract)->None: ...
    def run(self,contract:ProjectContract,workspace:Path)->ExecutionOutput: ...

class PythonAdapter:
    name="python"
    def validate(self,contract): 
        if not contract.runtime.entrypoint: raise ValueError("python adapter requires an entrypoint")
    def run(self,contract,workspace):
        self.validate(contract); ep=contract.runtime.entrypoint
        command=["python","-m",ep.removeprefix("python -m ")] if ep.startswith("python -m ") else shlex.split(ep)
        env=os.environ.copy(); env.update(contract.runtime.environment)
        p=subprocess.run(command,cwd=workspace,env=env,capture_output=True,text=True,timeout=contract.runtime.timeout_seconds,check=False)
        return ExecutionOutput(p.returncode,p.stdout,p.stderr,command)

class ShellAdapter:
    name="shell"
    def validate(self,contract):
        if not contract.runtime.entrypoint: raise ValueError("shell adapter requires an entrypoint")
    def run(self,contract,workspace):
        self.validate(contract); env=os.environ.copy(); env.update(contract.runtime.environment)
        p=subprocess.run(contract.runtime.entrypoint,cwd=workspace,env=env,capture_output=True,text=True,timeout=contract.runtime.timeout_seconds,shell=True,check=False)
        return ExecutionOutput(p.returncode,p.stdout,p.stderr,["/bin/sh","-c",contract.runtime.entrypoint])

ADAPTERS={"python":PythonAdapter(),"shell":ShellAdapter()}
