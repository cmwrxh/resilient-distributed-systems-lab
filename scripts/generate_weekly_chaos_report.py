from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "experiments" / "weekly" / f"week-{datetime.now():%Y-%W}.md"

def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    now = datetime.now()

    content = f"""# Weekly Chaos Experiment — {now:%Y-%m-%d} (Week {now:%Y-%W})

## Hypothesis
If we inject controlled failure (latency / kill / packet loss), the system should:
- degrade gracefully
- recover within expected time
- produce useful alerts and logs

## Experiment Plan (pick one each week)
- [ ] Inject latency (e.g., +200ms)
- [ ] Kill payments-service
- [ ] Packet loss (e.g., 5–10%)
- [ ] CPU/memory pressure (limited)

## What I Ran (fill in)
- Target:
- Failure type:
- Duration:
- Expected behavior:

## Observed Results (fill in)
- Error rate:
- p95 latency:
- Time to recover:
- Alerts fired:
- Gaps:

## Decision
- [ ] Keep current settings
- [ ] Tune retries/timeouts
- [ ] Add circuit breaker
- [ ] Improve runbook/alerts

## Evidence
- Metrics: docs/metrics/metrics.json
- Daily reports: docs/journal/daily/
- Actions run: Weekly Chaos Experiment (GitHub Actions)

## Next Action (15 min)
Write one concrete improvement you will implement this week.
"""
    OUT.write_text(content, encoding="utf-8")
    print(f"Wrote weekly chaos report: {OUT}")

if __name__ == "__main__":
    main()

