from fastapi import FastAPI,HTTPException
from .manager import ExecutionManager
from .models import ProjectContract
app=FastAPI(title="ENGINEERING-RUNNER-001",version="0.1.0")
manager=ExecutionManager()
@app.get("/health")
def health(): return {"status":"ok","runner":"ENGINEERING-RUNNER-001","version":"0.1.0"}
@app.post("/projects")
def register_project(contract:ProjectContract):
    try:return manager.register(contract)
    except ValueError as exc:raise HTTPException(400,str(exc))
@app.get("/projects")
def projects():return manager.projects.list()
@app.post("/projects/{project_id}/runs")
def start_run(project_id:str):
    try:return manager.start(project_id).model_dump(mode="json")
    except KeyError:raise HTTPException(404,"project not found")
@app.get("/runs")
def runs():return [r.model_dump(mode="json") for r in manager.list_runs()]
@app.get("/runs/{run_id}")
def run(run_id:str):
    try:return manager.get_run(run_id).model_dump(mode="json")
    except KeyError:raise HTTPException(404,"run not found")
@app.get("/runs/{run_id}/logs")
def logs(run_id:str):
    try:return manager.logs(run_id)
    except KeyError:raise HTTPException(404,"run not found")
@app.get("/runs/{run_id}/evidence")
def evidence(run_id:str):
    try:return manager.evidence_manifest(run_id)
    except KeyError:raise HTTPException(404,"run not found")
@app.get("/capabilities")
def capabilities():return {"adapters":["python","shell"],"enforcement_level":"policy-only","physical_isolation_proven":False}
