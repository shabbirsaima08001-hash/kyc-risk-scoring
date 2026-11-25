# KYC Risk Score Calculator

A rule-based Python tool that gives every customer a **risk score** and a **risk level** (LOW, MEDIUM, HIGH).

In banks, KYC and AML (Anti-Money Laundering) teams give more attention to customers with higher risk. This tool shows the idea in a simple way.

## How it works
Each customer gets points for risk factors:

| Factor | Example points |
|---|---|
| High-risk country | up to +40 |
| Risky job (politician, cash business, crypto) | +10 to +30 |
| High monthly transactions | +5 to +25 |
| Often pays in cash | +10 |
| New customer (under 1 year) | +5 |

Risk level:
- **LOW**: score under 20
- **MEDIUM**: score 20 to 49
- **HIGH**: score 50 or more

Every score also has a **reason list**, so you can see why a customer is high risk (this is called "explainability").

## Tools
Python 3, pandas

## How to run
```bash
pip install -r requirements.txt
python generate_data.py     # makes fake customers.csv
python risk_scoring.py      # makes risk_report.csv
```

## Example output
```
KYC RISK SCORE REPORT
MEDIUM    7
LOW       7
HIGH      6
Top 5 highest-risk customers:
C0011 Chiara Costa  score=85  HIGH
    Country KP (+40); Job: Crypto trader (+20); Very high monthly transactions (+25)
```

## Change the rules
All points are in tables at the top of `risk_scoring.py`. You can change them and run again.

## Important
- All data is **fake**.
- The rules are a simple learning example, not real bank rules.

## Ideas to improve
- Add a chart of risk levels
- Read the rules from a config file
- Add unit tests
