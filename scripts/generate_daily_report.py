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

## Observations
- Report is auto-generated.
- Next: replace one synthetic metric with a real health check.

## Next action (15 min)
- Add a /health endpoint call and record status + latency.
"""
    OUT.write_text(content, encoding="utf-8")
    print(f"Wrote {OUT}")

if __name__ == "__main__":
    main()
## Evidence
- Metrics file: docs/metrics/metrics.json
- Workflow: Daily Reliability Report (GitHub Actions)
