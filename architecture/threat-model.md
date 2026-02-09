# Threat Model (Lab)

## Assets
- Payment charge intent (must not double-charge)
- User identifiers
- Service availability

## Threats
- Replay / duplicate requests
- Request forgery between services
- Config leakage (secrets in repo)
- DoS via retry storms

## Controls (MVP)
- Idempotency keys for payments
- Minimal gateway routing (single entry point)
- No secrets committed (env vars only)
- Runbooks + rate limits (future)
