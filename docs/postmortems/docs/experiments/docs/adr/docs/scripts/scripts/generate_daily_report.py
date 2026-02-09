from __future__ import annotations
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
METRICS = ROOT / "docs" / "metrics" / "metrics.json"
OUT = ROOT / "docs" / "journal" / "daily" / f"{datetime.now().date()}.md"

def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    now = datetime.now()

    metrics_status = "present ✅" if METRICS.exists() else "missing ⚠️"

    content = f"""# Daily Reliability Report — {now:%Y-%m-%d}

## What ran
- Metrics snapshot: {metrics_status}
- Checks: smoke (placeholder), synthetic metrics generation

## Observations
- If this is synthetic today, convert 1 metric to real Prometheus query this week.

## Next action (15-min task)
- Replace one synthetic metric with a real health endpoint check and record status codes.
"""
    OUT.write_text(content, encoding="utf-8")

if __name__ == "__main__":
    main()
