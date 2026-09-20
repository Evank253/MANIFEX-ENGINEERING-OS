# ENGINEERING-RUNNER-001

Project-agnostic engineering execution and evidence substrate.

The runner is separate from MANIFEX. Projects are portable workloads described by a versioned Project Contract; the runner owns lifecycle management, runtime adapters, workspace creation, capability policy, observation, and evidence collection.

Lifecycle:

REGISTER → VALIDATE → RESOLVE VERSION → CREATE WORKSPACE → APPLY CAPABILITIES → START → OBSERVE → TEST → COLLECT EVIDENCE → VERIFY → FINALIZE → ARCHIVE

Initial adapters: Python and shell.

API surface:
- GET /health
- POST /projects
- GET /projects
- POST /projects/{id}/runs
- GET /runs
- GET /runs/{run_id}
- GET /runs/{run_id}/logs
- GET /runs/{run_id}/evidence
- GET /capabilities

The initial implementation deliberately reports capability enforcement as policy-only and does not claim physical sandbox isolation.

A project contract can pin an immutable source commit, select an adapter, request capabilities, set resource limits, and require evidence output.

MANIFEX can consume this runner as a client; the runner does not become a MANIFEX authority layer.
