# ADR 0003: Idempotency

## Status
Accepted

## Context
Payment operations must not double-charge when clients retry.

## Decision
Require an Idempotency-Key header for payment charge endpoints.
Store key -> result mapping with TTL (future: Redis).

## Consequences
- Pros: safe retries
- Cons: storage + lifecycle management
