"""KYC Risk Score Calculator
Gives each customer a score and a risk level: LOW, MEDIUM or HIGH.
The rules are simple and easy to change (see the tables at the top).
Output: terminal summary + risk_report.csv
"""
import pandas as pd

# --- Rules (change these to test other ideas) -------------------------------
COUNTRY_POINTS = {            # higher = more risk
    "KP": 40, "IR": 40,       # very high-risk countries
    "NG": 20, "PK": 15, "AE": 10,
}
JOB_POINTS = {
    "Politician": 30,         # PEP = Politically Exposed Person
    "Cash business owner": 20,
    "Crypto trader": 20,
    "Real estate agent": 10,
    "Self-employed": 5,
}
LOW_LIMIT = 20                # score below 20  -> LOW
HIGH_LIMIT = 50               # score 50 or more -> HIGH
# -----------------------------------------------------------------------------


def score_customer(row: pd.Series):
    """Returns (score, reasons) for one customer."""
    score = 0
    reasons = []

    pts = COUNTRY_POINTS.get(row["country"], 0)
    if pts:
        score += pts
        reasons.append(f"Country {row['country']} (+{pts})")

    pts = JOB_POINTS.get(row["job_type"], 0)
    if pts:
        score += pts
        reasons.append(f"Job: {row['job_type']} (+{pts})")

    amount = row["monthly_transactions_eur"]
    if amount >= 30000:
        score += 25
        reasons.append("Very high monthly transactions (+25)")
    elif amount >= 10000:
        score += 15
        reasons.append("High monthly transactions (+15)")
    elif amount >= 5000:
        score += 5
        reasons.append("Medium monthly transactions (+5)")

    if row["pays_cash_often"]:
        score += 10
        reasons.append("Often pays in cash (+10)")

    if row["years_as_customer"] < 1:
        score += 5
        reasons.append("New customer (+5)")

    return score, reasons


def risk_level(score: int) -> str:
    if score >= HIGH_LIMIT:
        return "HIGH"
    if score >= LOW_LIMIT:
        return "MEDIUM"
    return "LOW"


def main(path: str = "customers.csv") -> None:
    df = pd.read_csv(path)
    df["pays_cash_often"] = df["pays_cash_often"].astype(bool)

    scores, levels, why = [], [], []
    for _, row in df.iterrows():
        s, r = score_customer(row)
        scores.append(s)
        levels.append(risk_level(s))
        why.append("; ".join(r) if r else "No risk factors")

    df["risk_score"] = scores
    df["risk_level"] = levels
    df["reasons"] = why
    df = df.sort_values("risk_score", ascending=False)
    df.to_csv("risk_report.csv", index=False)

    print("=" * 50)
    print("KYC RISK SCORE REPORT")
    print("=" * 50)
    print(df["risk_level"].value_counts().to_string())
    print("-" * 50)
    print("Top 5 highest-risk customers:")
    for _, r in df.head(5).iterrows():
        print(f"{r['customer_id']} {r['full_name']:<16} score={r['risk_score']:<3} {r['risk_level']}")
        print(f"    {r['reasons']}")
    print("-" * 50)
    print("Full report saved in risk_report.csv")


if __name__ == "__main__":
    main()
