"""
analyze_savings.py
Step 3: Summarize the fake savings data month by month using pandas.
"""

import pandas as pd

# 1. Load the CSV file into a DataFrame (a table)
data = pd.read_csv("savings_data.csv", parse_dates=["date"])

# 2. Add a "month" column so we can group deposits by month (e.g. 2025-01)
data["month"] = data["date"].dt.to_period("M")

# 3. Group by month and calculate a few numbers for each one
monthly = data.groupby("month").agg(
    total_saved=("amount", "sum"),         # all money deposited that month
    average_deposit=("amount", "mean"),    # typical size of one deposit
    num_deposits=("amount", "count"),      # how many deposits were made
    active_members=("member_id", "nunique"),  # how many different members saved
)

# 4. Round the numbers so they look clean
monthly = monthly.round(2)

# 5. Month-over-month growth: how much did total savings change vs last month?
monthly["growth_percent"] = (monthly["total_saved"].pct_change() * 100).round(1)

print("MONTHLY SUMMARY")
print(monthly)

# 6. Which day of the week do members save the most?
data["weekday"] = data["date"].dt.day_name()
by_weekday = data.groupby("weekday")["amount"].sum().round(2)
by_weekday = by_weekday.sort_values(ascending=False)

print("\nTOTAL SAVED BY DAY OF WEEK")
print(by_weekday)

# 7. Save the monthly table so we can use it later in the Excel report
monthly.to_csv("monthly_summary.csv")
print("\nSaved monthly_summary.csv")
