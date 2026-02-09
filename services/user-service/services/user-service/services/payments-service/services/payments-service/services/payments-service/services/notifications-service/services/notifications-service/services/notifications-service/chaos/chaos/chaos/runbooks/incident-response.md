# Incident Response (Lab)

## Detect
- Gateway 5xx spike or service health failing

## Triage
- Identify failing service
- Confirm crash vs latency vs network

## Mitigate
- Restart service / rollback change
- Reduce load (stop load test)

## Recover
- Validate /health and a primary endpoint
- Remove chaos rules (tc qdisc del ...)

## Learn
- Write postmortem in /postmortems
