"""
generate_data.py
Creates FAKE savings data for a small community savings group.
No real member information is used anywhere in this project.
"""

import numpy as np
import pandas as pd

# Makes the random numbers repeatable, so you get the same data every run
np.random.seed(42)

NUM_MEMBERS = 200

# Every day of one year (365 days)
days = pd.date_range(start="2025-01-01", end="2025-12-31", freq="D")

rows = []  # we'll collect one row per deposit here

for member_id in range(1, NUM_MEMBERS + 1):
    # Each member has their own typical deposit size (between 5 and 40)
    typical_deposit = np.random.randint(5, 41)

    for day in days:
        # Members save more often on weekdays (market days) than weekends
        if day.dayofweek < 5:
            chance_of_saving = 0.60
        else:
            chance_of_saving = 0.25

        # Deposit happens only if a random number falls under the chance
        if np.random.random() < chance_of_saving:
            # Amount varies a little around the member's typical deposit
            amount = round(typical_deposit * np.random.uniform(0.7, 1.3), 2)
            rows.append({"date": day, "member_id": member_id, "amount": amount})

# Turn the list of rows into a pandas DataFrame (a table)
data = pd.DataFrame(rows)

# Save it as a CSV file you can open in Excel
data.to_csv("savings_data.csv", index=False)

print("Done! Created savings_data.csv")
print(f"Total deposits: {len(data)}")
print(data.head())
