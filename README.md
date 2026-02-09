# resilient-distributed-systems-lab

A runnable lab for practicing reliability patterns: retries, idempotency, failure injection, and incident response.

## What’s Inside
- API Gateway (Nginx) routing to 3 services
- FastAPI microservices (users, payments, notifications)
- Prometheus + Grafana scaffolding
- Chaos scripts (kill, latency, packet loss)
- ADRs, runbooks, postmortems

## Quickstart (Local)
```bash
cd infra
docker compose up --build
