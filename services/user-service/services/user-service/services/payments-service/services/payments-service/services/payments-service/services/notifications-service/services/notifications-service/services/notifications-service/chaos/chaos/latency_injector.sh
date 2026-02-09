#!/usr/bin/env bash
set -euo pipefail

SERVICE="${1:-}"
DELAY_MS="${2:-200}"

if [[ -z "$SERVICE" ]]; then
  echo "Usage: ./latency_injector.sh <service-name> [delay_ms]"
  exit 1
fi

cd infra
CID="$(docker compose ps -q "$SERVICE")"
docker exec -it "$CID" sh -c "apk add --no-cache iproute2 >/dev/null 2>&1 || true; tc qdisc add dev eth0 root netem delay ${DELAY_MS}ms"
echo "Injected ${DELAY_MS}ms latency into $SERVICE"
