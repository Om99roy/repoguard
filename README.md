# RepoGuard

> An autonomous repository health and repair agent powered by TrueForge.

## Problem

Small repository regressions can require a developer to inspect source files,
trace CI failures, reproduce the problem locally, determine the root cause,
and then safely apply and verify a fix.

RepoGuard demonstrates how an agent can move through that workflow while
keeping a human approval gate before repository changes.

## What RepoGuard Does

RepoGuard:

1. Inspects a GitHub repository using the GitHub MCP connector.
2. Correlates repository files with CI/test evidence.
3. Uses the TrueForge sandbox when execution is available.
4. Diagnoses the root cause of a failure.
5. Produces a minimal repair proposal.
6. Stops and requests explicit human approval.
7. Validates the approved repair through the project test workflow.
8. Uses GitHub pull requests and Qodo for code review.

## Architecture

User
→ TrueForge RepoGuard Agent
→ GitHub MCP
→ Repository / CI inspection
→ Sandbox execution
→ Diagnosis
→ Human approval
→ Repair
→ Verification
→ Pull Request

## Demo Scenario

The demonstration repository contains a deliberate defect in
`calculate_total()`.

The function returns the untaxed subtotal while the test expects the
tax-inclusive total.

Expected:

`100 * 1.10 = 110`

Observed before repair:

`100`

RepoGuard identifies the failing test, determines the root cause, and
proposes the minimal repair:

```python
return round(subtotal * (1 + tax_rate), 2)
