# MANIFEX Integration Reality & Missing Capabilities

Status: ARCHITECTURE CAPTURE / NOT AN IMPLEMENTATION CLAIM
Branch: `Python-3`

## Purpose

This document captures the capabilities identified across the KCN/MANIFEX design work so they are not lost while the executable MANIFEX system is assembled. It is an integration inventory, not evidence that every capability is currently implemented.

## Current repository reality

The `Python-3` branch is presently a very small repository surface. Therefore capabilities below are classified explicitly as **CAPTURED**, **PLANNED**, **IMPLEMENTED**, or **VERIFIED** rather than being represented as completed merely because they are specified here.

## MANIFEX target system

MANIFEX is the cloud-hosted **Engineering Intelligence & Execution OS**. Its job is to turn engineering intent into controlled, inspectable, verifiable execution while preserving provenance, evidence, governance, and reusable assets.

Core rule:

> Reuse → Adapt → Wrap → Build only what is missing → Verify everything.

## Capability inventory

### 1. Control Plane / Control Center
- Multi-tenant workspace model
- Identity and authorization
- Project/workspace isolation
- System health and readiness
- Run history
- approvals and release controls
- operational dashboard
- capability/asset discovery

Status: PLANNED / CAPTURED

### 2. Intent & Intake
- Natural-language engineering intent intake
- Task normalization
- TaskIR / canonical request representation
- Requirements extraction
- Constraints and acceptance criteria
- Dependency detection
- risk classification
- execution-plan generation

Status: CAPTURED / PLANNED

### 3. Reality Engine / Integration Reality Audit
- Inspect source repositories and artifacts
- Determine source/version/files/dependencies/interfaces/runnability/tests/evidence
- Detect duplicates and reusable capabilities
- Identify gaps between requested and existing functionality
- Produce KEEP / ADAPT / WRAP / FREEZE / BUILD / REPLACE / RETIRE recommendations
- Never replace working assets without evidence

Status: CAPTURED / PLANNED

### 4. Build Index / Filing Cabinet
A persistent registry for everything MANIFEX knows about:
- source repositories
- immutable commits
- tree hashes
- copied assets
- artifacts
- APIs
- tools
- agents
- prompts
- datasets
- test suites
- benchmarks
- deployments
- evidence
- provenance
- licenses and legal notices
- capabilities and dependencies

Every indexed asset should have a stable MANIFEX identifier.

Status: CAPTURED / PLANNED

### 5. Provenance System
Append-only provenance record containing, where applicable:
- source repository
- source commit SHA
- source tree hash
- access mode (`READ_ONLY` for existing creator repositories unless explicitly authorized)
- MANIFEX copy ID
- source revision/tree hash
- MANIFEX working-copy path
- integration action
- evidence level E0–E5
- modifications
- verification results
- timestamps
- actor/tool responsible

Status: CAPTURED / PLANNED

### 6. Evidence Ledger
Evidence must be first-class data.

E0–E5 ladder:
- E0: claim only
- E1: artifact exists
- E2: runtime/execution evidence
- E3: reproduced verification
- E4: independent verification
- E5: cross-system / cross-environment verification

Rules:
- readiness is not evidence
- documentation is not execution
- benchmark claims require reproducible evidence
- unsupported claims remain NOT MEASURED
- no layer grants trust upward without evidence

Status: CAPTURED / PLANNED

### 7. CORE Judgment System
A shared validation service that can be called by every MANIFEX application or product.

Purpose:
- independently judge generated outputs before release
- evaluate evidence sufficiency
- detect contradictions
- detect unsupported assertions
- check provenance
- check policy/governance constraints
- determine whether an output should be released, held, rejected, or escalated

Important separation:

**Generation is not judgment.**

The judgment layer should not be described as guaranteeing truth. It determines whether the available evidence and policy conditions are sufficient for a release decision.

Suggested decisions:
- PASS
- FAIL
- UNKNOWN
- ESCALATE
- HOLD

Status: CAPTURED / CORE PACKAGE NOT YET VERIFIED AS IMPLEMENTED

### 8. Multi-Judge Validation

A judgment request may be evaluated by multiple independent judges with structured findings, for example:
- evidence judge
- consistency judge
- provenance judge
- policy/governance judge
- security/safety judge
- execution/test judge
- domain-specific judge

The aggregator should preserve individual findings rather than returning only a single opaque score.

Status: CAPTURED / PLANNED

### 9. Agent Runtime
- Agent identity
- agent roles
- scoped permissions
- task intake
- reasoning/execution state
- tool selection
- memory access
- execution boundaries
- approvals
- result normalization
- run IDs
- cancellation/timeouts
- audit trail

Status: CAPTURED / PLANNED

### 10. Memory System
- tenant-scoped memory
- project-scoped memory
- agent-scoped memory where appropriate
- write/retrieve lifecycle
- memory references in outputs
- provenance for memory-derived claims
- retention/deletion policy
- isolation tests

Required observable lifecycle:

**write → retrieve → use → provenance**

Status: CAPTURED / PLANNED

### 11. MCP / Tool Fabric
- Tool registry
- capability discovery
- tool identity
- schemas
- permissions
- credentials/secrets binding
- sandboxed invocation
- tool result provenance
- health/readiness
- rate limits
- failure handling

Status: CAPTURED / PLANNED

### 12. ARK
ARK is retained as a reusable knowledge/reasoning/build capability within MANIFEX rather than treated as an isolated product.

Status: CAPTURED / INTEGRATION TARGET

### 13. Vibe Developer / Vibe Coder
- requirement-to-code workflow
- repository-aware engineering
- controlled edits
- test generation/execution
- dependency awareness
- code review/verification
- provenance for generated changes
- no uncontrolled writes to protected source repositories

Status: CAPTURED / INTEGRATION TARGET

### 14. Execution Sandbox
- isolated execution
- resource limits
- filesystem boundaries
- network policy
- process controls
- secret isolation
- reproducible environment metadata
- cleanup

Status: PLANNED

### 15. Secret Vault
- encrypted secret storage
- scoped access
- ephemeral credential injection
- audit logging
- no secrets in prompts/logs/artifacts
- rotation/revocation hooks

Status: PLANNED

### 16. Verification / Testing Fabric
- unit tests
- integration tests
- end-to-end tests
- contract tests
- regression tests
- security tests
- adversarial tests
- deterministic fixtures
- reproducibility metadata
- test evidence linked to exact source revision

Status: CAPTURED / PLANNED

### 17. PESG / Z3 Verification
Retain the existing verification concepts as reusable services where technically appropriate:
- symbolic constraints
- satisfiability checks
- entailment checks
- MODEL / UNSAT / UNKNOWN outcomes
- premise ablation
- provenance linkage

Do not present a solver-backed subsystem as general intelligence.

Status: CAPTURED / INTEGRATION TARGET

### 18. Honesty / Release Gate
A release gate should prevent unsupported certainty.

Examples:
- no evidence → NOT MEASURED
- insufficient evidence → UNKNOWN / HOLD
- contradiction → ESCALATE / FAIL
- passing evidence + policy → PASS

Status: CAPTURED / PLANNED

### 19. Black-Box Audit Log
Record immutable execution events such as:
- request
- identity
- plan
- agent
- tool call
- tool result
- memory reference
- judgment
- policy decision
- execution
- artifact
- deployment
- final release decision

Logs should support forensic reconstruction of a run.

Status: CAPTURED / PLANNED

### 20. Assurance / Certification Layer
Reusable commands/services for:
- validate
- certify
- qualify
- regression-check
- evidence export
- readiness assessment

Certification must reference evidence and exact revisions rather than being a decorative status label.

Status: CAPTURED / PLANNED

### 21. TwinLab / Evaluation Lab
A controlled environment for comparing:
- builds
- agents
- prompts
- tools
- models
- workflows
- releases

Include:
- deterministic datasets
- baseline comparisons
- repeated trials
- failure analysis
- statistical summaries
- artifact capture

Status: CAPTURED / PLANNED

### 22. Genesis-20
The existing 20-test evaluation concept should be preserved as **MANIFEX Genesis-20**, then expanded as the platform matures.

Do not convert historical benchmark numbers into MANIFEX performance claims without reproducing them.

Status: CAPTURED / PLANNED

### 23. Benchmark Methodology
Preserve the categories previously identified:
- Trust
- Validation
- Governance
- Psychological Safety Alignment
- Operational Readiness
- IP Protection Posture

Historical values may be retained as prior/internal benchmark artifacts, but should be labeled according to their actual evidence status. They are not automatically independent industry benchmarks.

Status: CAPTURED

### 24. Security Architecture
- tenant isolation
- RBAC/ABAC
- least privilege
- sandboxing
- secrets isolation
- audit trails
- supply-chain awareness
- dependency scanning
- prompt/tool injection defenses
- data boundary enforcement
- secure artifact handling
- deployment hardening

Status: PLANNED

### 25. Deployment / Cloud Operations
- cloud deployment
- environment separation
- CI/CD
- health checks
- observability
- metrics
- logs
- traces
- rollback
- versioned releases
- deployment provenance

MANIFEX target is cloud-hosted/deployed, not merely a local application.

Status: CAPTURED / PLANNED

### 26. Observability
- request tracing
- agent-run tracing
- tool latency/errors
- model latency/errors
- queue depth
- resource usage
- test outcomes
- judgment outcomes
- release decisions
- deployment state

Status: PLANNED

### 27. API / SDK Surface
A stable API layer should expose core MANIFEX capabilities:
- create task
- inspect task
- run agent
- invoke tool
- retrieve memory
- write memory
- submit judgment
- inspect evidence
- inspect provenance
- execute verification
- retrieve artifacts
- compare builds
- deploy
- inspect deployment

Status: PLANNED

### 28. Artifact / IP Protection
- artifact ownership metadata
- license tracking
- public/private classification
- creator-owned assets
- private build isolation
- export controls
- provenance
- legal notices
- patent/copyright notice references where applicable

Status: CAPTURED / PLANNED

### 29. Creator Access Policy
The creator/free-access policy captured in prior product documentation should remain an explicit product-policy object, not an undocumented assumption.

Status: CAPTURED

### 30. Public / Private Repository Governance
MANIFEX should distinguish:
- public source
- private source
- creator-owned protected source
- third-party source
- generated working copy
- frozen reference

Existing creator repositories are read-only integration sources by default.

Status: CAPTURED / GOVERNANCE REQUIREMENT

## Known missing implementation layers

Based on the current visible MANIFEX repository state, the highest-priority missing executable layers are:

1. Core application/backend skeleton
2. Persistent database/data model
3. Build Index implementation
4. Provenance ledger implementation
5. Evidence ledger implementation
6. CORE Judgment System implementation
7. Multi-judge orchestration and aggregation
8. Agent runtime
9. Memory service
10. MCP/tool registry and execution fabric
11. Secret vault integration
12. sandboxed execution
13. verification/test runner
14. policy/honesty release gate
15. black-box audit/event bus
16. TwinLab/Genesis-20 harness
17. API surface
18. Control Center UI
19. observability
20. cloud deployment/CI/CD
21. security controls and isolation tests
22. end-to-end acceptance suite

## Protected / frozen assets

### AEGIS 0.3
AEGIS 0.3 remains frozen. MANIFEX may integrate it as an immutable reference/capability, but must not silently modify or rewrite it.

### Historical benchmark claims
Claims such as large run counts, accuracy percentages, latency results, or cross-system superiority are not promoted to verified MANIFEX metrics unless reproducible evidence is available.

## Integration contract

For every imported capability, MANIFEX should record:

```text
source_repository
source_commit_sha
source_tree_hash
access=READ_ONLY
manifex_copy_id
working_copy
integration_action
integration_revision
modifications
verification_commands
verification_result
evidence_level
provenance_record
```

## Definition of done

A capability is not considered complete because it exists in documentation. A capability becomes **VERIFIED** only when MANIFEX can execute an appropriate verification path and preserve the resulting evidence and provenance.

The maturity path is:

**Runnable → Stateful → Verifiable → Measurable → Assurable**
