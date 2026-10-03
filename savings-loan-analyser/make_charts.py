"""
make_charts.py
Step 4: Turn the savings summaries into charts with matplotlib.
Run generate_data.py and analyze_savings.py first.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

# Folder where the chart images will be saved (handy for your README)
os.makedirs("charts", exist_ok=True)

# ---------- Chart 1: total savings per month (line chart) ----------
monthly = pd.read_csv("monthly_summary.csv")

plt.figure(figsize=(9, 5))
plt.plot(monthly["month"], monthly["total_saved"], marker="o", color="#1F3864")
plt.title("Total Savings per Month (2025)")
plt.xlabel("Month")
plt.ylabel("Total saved")
plt.xticks(rotation=45)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("charts/monthly_savings.png", dpi=150)
plt.show()

# ---------- Chart 2: total savings by day of week (bar chart) ----------
data = pd.read_csv("savings_data.csv", parse_dates=["date"])
data["weekday"] = data["date"].dt.day_name()

# Put the days in calendar order instead of alphabetical order
order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
by_weekday = data.groupby("weekday")["amount"].sum().reindex(order)

plt.figure(figsize=(9, 5))
plt.bar(by_weekday.index, by_weekday.values, color="#2E75B6")
plt.title("Total Savings by Day of Week")
plt.xlabel("Day")
plt.ylabel("Total saved")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/savings_by_weekday.png", dpi=150)
plt.show()

print("Charts saved in the 'charts' folder.")
