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
```resilient-distributed-systems-lab/
├─ README.md
├─ architecture/
│  ├─ diagrams/
│  ├─ adr/
│  │  ├─ 0001-service-boundaries.md
│  │  ├─ 0002-retry-policy.md
│  │  └─ 0003-idempotency.md
│  └─ threat-model.md
├─ services/
│  ├─ api-gateway/
│  ├─ user-service/
│  ├─ payments-service/
│  └─ notifications-service/
├─ infra/
│  ├─ docker-compose.yml
│  ├─ nginx/
│  ├─ prometheus/
│  └─ grafana/
├─ chaos/
│  ├─ kill_service.sh
│  ├─ latency_injector.sh
│  └─ packet_loss.sh
├─ tests/
│  ├─ load/
│  ├─ resilience/
│  └─ contract/
├─ runbooks/
│  ├─ incident-response.md
│  ├─ rollout-canary.md
│  └─ rollback.md
└─ postmortems/
   └─ 0001-simulated-outage.md
