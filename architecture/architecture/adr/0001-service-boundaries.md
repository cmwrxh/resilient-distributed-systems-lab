# ADR 0001: Service Boundaries

## Status
Accepted

## Context
We want a small lab system that demonstrates failure modes, retries, idempotency, and observability.

## Decision
Create three domain services (users, payments, notifications) behind an API gateway.

## Consequences
- Pros: clear ownership, easy to inject failures per service
- Cons: network hops add latency; need contracts and retries
