name: Daily Reliability Report

on:
  schedule:
    # 09:10 Nairobi (UTC+3) = 06:10 UTC
    - cron: "10 6 * * *"
  workflow_dispatch:

permissions:
  contents: write

jobs:
  report:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Generate metrics + daily report
        run: |
          python scripts/generate_metrics.py
          python scripts/generate_daily_report.py

      - name: Commit changes (if any)
        run: |
          git config user.name "cmwrxh-bot"
          git config user.email "cmwrxh-bot@users.noreply.github.com"
          git add -A
          git diff --cached --quiet || git commit -m "daily reliability simulation report"
          git push
