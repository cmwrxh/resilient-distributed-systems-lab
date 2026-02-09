# Rollback (Lab)

## When
- Error rate spikes
- Latency regression
- Payment correctness risk

## How
- Revert last commit or last image tag (future)
- Restart affected service
- Re-run contract + smoke tests
# Rollback Procedure

Rollback when error rate spikes or latency regresses.

Steps:
1. Revert last commit.
2. Restart service.
3. Validate health endpoints.
