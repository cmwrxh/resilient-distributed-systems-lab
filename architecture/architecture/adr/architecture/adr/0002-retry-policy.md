# ADR 0002: Retry Policy

## Status
Accepted

## Context
Transient failures happen (timeouts, 503s). Uncontrolled retries can cause retry storms.

## Decision
Use bounded retries with exponential backoff + jitter for idempotent operations only.
Non-idempotent operations require idempotency keys.

## Consequences
- Pros: reduces cascading failures
- Cons: adds latency under failure
