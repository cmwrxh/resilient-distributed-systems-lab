#!/usr/bin/env bash
set -euo pipefail

SERVICE="${1:-}"
LOSS="${2:-5}"

if [[ -z "$SERVICE" ]]; then
  echo "Usage: ./packet_loss.sh <service-name> [loss_percent]"
  exit 1
fi

cd infra
CID="$(docker compose ps -q "$SERVICE")"
docker exec -it "$CID" sh -c "apk add --no-cache iproute2 >/dev/null 2>&1 || true; tc qdisc add dev eth0 root netem loss ${LOSS}%"
echo "Injected ${LOSS}% packet loss into $SERVICE"
