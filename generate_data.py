"""Makes FAKE customers for the risk scoring tool. No real people."""
import random
import pandas as pd

random.seed(7)
names = ["Marco Rossi", "Giulia Bianchi", "Ahmed Khan", "Sara Verdi", "Luca Ferrari", "Anna Russo",
         "Ali Shah", "Elena Conti", "Paolo Greco", "Fatima Ali", "Chiara Costa", "Omar Haddad",
         "Sofia Romano", "Davide Gallo", "Maria Lombardi", "Hassan Raza", "Laura Moretti",
         "Andrea Bruno", "Nadia Sheikh", "Bruno Marino"]
countries = ["IT", "DE", "FR", "ES", "PK", "IR", "AE", "NG", "KP", "US"]
jobs = ["Employee", "Student", "Teacher", "Retired", "Self-employed", "Cash business owner",
        "Crypto trader", "Politician", "Real estate agent"]

rows = []
for i, name in enumerate(names, start=1):
    rows.append({
        "customer_id": f"C{i:04d}",
        "full_name": name,
        "country": random.choice(countries),
        "job_type": random.choice(jobs),
        "monthly_transactions_eur": random.choice([300, 800, 1500, 4000, 9000, 15000, 40000]),
        "years_as_customer": random.randint(0, 10),
        "pays_cash_often": random.choice([True, False]),
    })
pd.DataFrame(rows).to_csv("customers.csv", index=False)
print("Created customers.csv with", len(rows), "fake customers")
