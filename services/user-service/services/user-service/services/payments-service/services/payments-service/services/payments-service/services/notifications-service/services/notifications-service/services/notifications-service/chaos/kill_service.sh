#!/usr/bin/env bash
set -euo pipefail

SERVICE="${1:-}"
if [[ -z "$SERVICE" ]]; then
  echo "Usage: ./kill_service.sh <service-name>"
  exit 1
fi

cd infra
docker compose kill "$SERVICE"
echo "Killed: $SERVICE"
