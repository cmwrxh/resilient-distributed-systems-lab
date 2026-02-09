from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
import random

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "metrics" / "metrics.json"

def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)

    now = datetime.now(timezone.utc).astimezone()
    payload = {
        "generated_at": now.isoformat(),
        "services": {
            "api-gateway": {
                "p95_latency_ms": round(random.uniform(40, 120), 2),
                "error_rate_pct": round(random.uniform(0.0, 1.5), 3),
            },
            "payments-service": {
                "p95_latency_ms": round(random.uniform(60, 180), 2),
                "error_rate_pct": round(random.uniform(0.0, 2.0), 3),
            },
        }
    }

    OUT.write_text(json.dumps(payload, indent=2), encoding="utf-8")

if __name__ == "__main__":
    main()
