# MANIFEX Core Capability Registry

Status: CAPTURED INVENTORY

This registry prevents capabilities from disappearing between projects. It is intentionally separate from implementation status.

| Capability | MANIFEX Role | Evidence Status | Integration Action |
|---|---|---|---|
| Core Intelligence / Kernel | Agent execution substrate | Capture only | ADAPT/WRAP |
| Core Memory | Stateful context substrate | Capture only | ADAPT/WRAP |
| Core Judgment System | Shared release-validation layer | Not yet verified implemented | BUILD |
| Multi-Judge Validation | Independent output review | Capture only | BUILD |
| Evidence Ledger | Evidence-first trust | Capture only | BUILD |
| E0–E5 Evidence Ladder | Evidence classification | Defined | ADAPT |
| Provenance Ledger | Source/asset lineage | Capture only | BUILD |
| Build Index | Engineering filing cabinet | Capture only | BUILD |
| Agent Identity | Scoped actor model | Capture only | BUILD |
| Tenant Isolation | Security boundary | Capture only | BUILD |
| MCP / Tool Registry | Tool fabric | Capture only | BUILD |
| Secret Vault | Credential boundary | Capture only | BUILD |
| Execution Sandbox | Controlled execution | Capture only | BUILD |
| Black-Box Audit Log | Forensic run history | Capture only | BUILD |
| Policy / Honesty Gate | Release control | Capture only | BUILD |
| PESG / Z3 | Formal verification capability | Existing concept; integration unverified | WRAP |
| Assurance / Certification | Evidence-backed qualification | Capture only | ADAPT/BUILD |
| TwinLab | Controlled evaluation | Capture only | BUILD |
| Genesis-20 | Initial platform evaluation suite | Capture only | ADAPT |
| Reality Engine | Integration/gap analysis | Capture only | BUILD |
| ARK | Reusable knowledge capability | Existing concept; integration unverified | WRAP |
| Vibe Developer/Coder | Engineering automation | Existing concept; integration unverified | WRAP/ADAPT |
| API / SDK | External control surface | Capture only | BUILD |
| Control Center | Human governance interface | Capture only | BUILD |
| Deployment / Cloud Ops | Production execution | Capture only | BUILD |
| Observability | Metrics/logs/traces | Capture only | BUILD |
| Security Fabric | Platform protection | Capture only | BUILD |
| IP / Legal Controls | Asset protection | Capture only | ADAPT |
| Public/Private Classification | Repository governance | Defined | ADAPT |
| Creator Access Policy | Product access governance | Captured from prior product docs | ADAPT |

## Rule

A registry entry is not a claim that the capability is implemented. Implementation status must be established by executable evidence.

## Global architecture

```text
                    ┌───────────────────────────┐
                    │       MANIFEX Control      │
                    │       Center / API        │
                    └─────────────┬─────────────┘
                                  │
                         Intent / TaskIR
                                  │
                    ┌─────────────▼─────────────┐
                    │ Reality + Build Index     │
                    │ Assets / Dependencies     │
                    └─────────────┬─────────────┘
                                  │
                    ┌─────────────▼─────────────┐
                    │ Agent Runtime + Memory    │
                    │ ARK + Vibe + MCP          │
                    └─────────────┬─────────────┘
                                  │
                    ┌─────────────▼─────────────┐
                    │ Execution / Verification  │
                    │ Sandbox + Tests + Z3/PESG  │
                    └─────────────┬─────────────┘
                                  │
                    ┌─────────────▼─────────────┐
                    │     CORE JUDGMENT         │
                    │ Multi-Judge + Evidence    │
                    │ Provenance + Policy       │
                    └─────────────┬─────────────┘
                                  │
                    ┌─────────────▼─────────────┐
                    │ Release / Hold / Reject   │
                    │ Escalate + Audit          │
                    └─────────────┬─────────────┘
                                  │
                    ┌─────────────▼─────────────┐
                    │ Evidence + Provenance     │
                    │ TwinLab + Observability   │
                    └───────────────────────────┘
```

## Non-negotiable behavior

1. Generation and judgment are separate concerns.
2. Evidence must be inspectable.
3. Unsupported certainty becomes UNKNOWN/NOT MEASURED rather than being promoted.
4. Every imported asset has provenance.
5. Protected source repositories remain read-only unless explicit authorization changes that status.
6. Frozen systems remain frozen.
7. Existing working capabilities are integrated before replacement is considered.
8. Every verified claim points to executable evidence.
