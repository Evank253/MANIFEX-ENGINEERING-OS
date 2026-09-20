from __future__ import annotations
from datetime import datetime, timezone
from enum import Enum
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field

class RunStatus(str, Enum):
    REGISTERED="REGISTERED"; VALIDATING="VALIDATING"; PREPARING="PREPARING"; RUNNING="RUNNING"
    VERIFYING="VERIFYING"; COMPLETED="COMPLETED"; FAILED="FAILED"; CANCELLED="CANCELLED"; STOPPED="STOPPED"

class SourceSpec(BaseModel):
    model_config=ConfigDict(extra="forbid")
    type: Literal["local","github"]="local"
    repository: str|None=None; ref: str|None=None; commit: str|None=None; path: str|None=None

class RuntimeSpec(BaseModel):
    model_config=ConfigDict(extra="forbid")
    adapter: str="python"; entrypoint: str; working_directory: str="/workspace"
    timeout_seconds: int=Field(default=300,ge=1,le=86400); environment: dict[str,str]=Field(default_factory=dict)

class FilesystemPolicy(BaseModel):
    model_config=ConfigDict(extra="forbid")
    read:list[str]=Field(default_factory=list); write:list[str]=Field(default_factory=list)

class NetworkPolicy(BaseModel):
    model_config=ConfigDict(extra="forbid")
    allowed:list[str]=Field(default_factory=list); denied:list[str]=Field(default_factory=list)

class CapabilityPolicy(BaseModel):
    model_config=ConfigDict(extra="forbid")
    filesystem:FilesystemPolicy=Field(default_factory=FilesystemPolicy)
    network:NetworkPolicy=Field(default_factory=NetworkPolicy)
    credentials:list[str]=Field(default_factory=list); tools:list[str]=Field(default_factory=list)

class ExecutionPolicy(BaseModel):
    model_config=ConfigDict(extra="forbid")
    mode:Literal["sandboxed","unsandboxed"]="sandboxed"
    max_output_bytes:int=Field(default=2_000_000,ge=1); max_artifacts:int=Field(default=100,ge=1)

class EvidencePolicy(BaseModel):
    model_config=ConfigDict(extra="forbid")
    required:bool=True; output:str="/workspace/evidence"

class ProjectContract(BaseModel):
    model_config=ConfigDict(extra="forbid")
    id:str=Field(min_length=1,max_length=128); version:str=Field(min_length=1,max_length=64)
    source:SourceSpec=Field(default_factory=SourceSpec); runtime:RuntimeSpec
    capabilities:CapabilityPolicy=Field(default_factory=CapabilityPolicy)
    execution:ExecutionPolicy=Field(default_factory=ExecutionPolicy)
    evidence:EvidencePolicy=Field(default_factory=EvidencePolicy)

class RunRecord(BaseModel):
    model_config=ConfigDict(extra="forbid")
    run_id:str; project_id:str; project_version:str; source_commit:str|None; status:RunStatus
    started_at:datetime|None=None; ended_at:datetime|None=None; workspace:str|None=None
    environment_hash:str|None=None; runtime_adapter:str; exit_code:int|None=None
    result:str|None=None; error:str|None=None; evidence_refs:list[str]=Field(default_factory=list)
    @classmethod
    def new(cls,run_id,contract): return cls(run_id=run_id,project_id=contract.id,project_version=contract.version,source_commit=contract.source.commit,status=RunStatus.REGISTERED,runtime_adapter=contract.runtime.adapter)
    def started(self): return self.model_copy(update={"status":RunStatus.RUNNING,"started_at":datetime.now(timezone.utc)})
    def finished(self,status,*,exit_code,result=None,error=None): return self.model_copy(update={"status":status,"exit_code":exit_code,"result":result,"error":error,"ended_at":datetime.now(timezone.utc)})
