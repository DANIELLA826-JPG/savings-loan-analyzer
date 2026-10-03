"""
loan_scenarios.py
Step 5: Explore how different loan interest rates might change borrowing.

IMPORTANT: This is a simple SIMULATION. The assumptions below are made up
for practice, not taken from any real credit union. Change them and see
how the results change!
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

# ---------------- ASSUMPTIONS (edit these!) ----------------
TOTAL_MEMBERS = 200          # members in our fake savings group
CURRENT_RATE = 18            # current loan interest rate (% per year)
CURRENT_BORROWERS = 40       # members who borrow at the current rate (20%)
AVERAGE_LOAN = 500           # average loan size
DEMAND_BOOST_PER_POINT = 0.10  # each 1-point rate cut -> 10% more borrowers
# -----------------------------------------------------------

rows = []

# Try every rate from 10% to 20%
for rate in range(10, 21):
    points_cut = CURRENT_RATE - rate  # positive if the rate is lower than now

    # Estimate borrowers, but never more than the total number of members
    borrowers = CURRENT_BORROWERS * (1 + DEMAND_BOOST_PER_POINT * points_cut)
    borrowers = max(0, min(borrowers, TOTAL_MEMBERS))

    total_loaned = borrowers * AVERAGE_LOAN
    yearly_interest = total_loaned * rate / 100

    rows.append({
        "rate_percent": rate,
        "borrowers": round(borrowers),
        "total_loaned": round(total_loaned),
        "yearly_interest_income": round(yearly_interest),
    })

scenarios = pd.DataFrame(rows)
print("LOAN RATE SCENARIOS (simulated)")
print(scenarios.to_string(index=False))

# Which rate earns the most interest in this model?
best = scenarios.loc[scenarios["yearly_interest_income"].idxmax()]
print(f"\nHighest interest income in this model: {int(best['rate_percent'])}% "
      f"({int(best['borrowers'])} borrowers, {int(best['yearly_interest_income'])} per year)")

# Save the table and a chart
scenarios.to_csv("loan_scenarios.csv", index=False)
os.makedirs("charts", exist_ok=True)

fig, ax1 = plt.subplots(figsize=(9, 5))
ax1.bar(scenarios["rate_percent"], scenarios["borrowers"], color="#2E75B6", alpha=0.7)
ax1.set_xlabel("Loan interest rate (%)")
ax1.set_ylabel("Estimated borrowers", color="#2E75B6")

ax2 = ax1.twinx()  # second y-axis on the right
ax2.plot(scenarios["rate_percent"], scenarios["yearly_interest_income"],
         marker="o", color="#C00000")
ax2.set_ylabel("Yearly interest income", color="#C00000")

plt.title("Loan Rate Scenarios (simulated assumptions)")
fig.tight_layout()
plt.savefig("charts/loan_scenarios.png", dpi=150)
plt.show()
