# RepoGuard

> An autonomous repository health and repair agent powered by TrueForge.

## Problem

Developers often spend time manually inspecting repository files, reproducing CI failures, diagnosing root causes, and validating fixes.

RepoGuard demonstrates an agent-driven workflow for investigating and safely repairing repository issues.

## What RepoGuard Does

1. Inspects a GitHub repository using GitHub MCP.
2. Correlates repository state with CI evidence.
3. Uses a sandbox for safe execution when available.
4. Diagnoses the root cause.
5. Generates a minimal repair proposal.
6. Stops for explicit human approval.
7. Validates the approved repair.
8. Uses GitHub pull requests and Qodo for review.

## Architecture

User  
→ TrueForge RepoGuard Agent  
→ GitHub MCP  
→ Repository / CI inspection  
→ Daytona Sandbox  
→ Diagnosis  
→ Human Approval  
→ Repair  
→ Verification  
→ Pull Request

```markdown
## Demo Scenario

The demonstration uses a controlled repair scenario based on
`calculate_total()`.

During the demonstration, the repository was temporarily placed in a
known-broken state where `calculate_total()` returned the untaxed
subtotal. The test expected the tax-inclusive result.

Expected:

`100 * 1.10 = 110`

Observed in the broken state:

`100`

RepoGuard diagnosed the defect and proposed the minimal repair:

```python
return round(subtotal * (1 + tax_rate), 2)
