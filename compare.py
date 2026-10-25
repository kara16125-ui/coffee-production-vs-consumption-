import pandas as pd
import matplotlib.pyplot as plt

# 1. Load both files (keep only the columns we need)
prod = pd.read_csv("offee_production.csv")
cons = pd.read_csv("offee_domestic_consumption.csv")

prod = prod[["Country", "Total_production"]]
cons = cons[["Country", "Total_domestic_consumption"]]

# 2. Merge on Country
merged = pd.merge(prod, cons, on="Country")
print(merged.shape)   # should be about (55, 3)

# 3. New columns
merged["surplus"] = merged["Total_production"] - merged["Total_domestic_consumption"]
merged["consumption_pct"] = (
    merged["Total_domestic_consumption"] / merged["Total_production"] * 100
)

# 4. Q1: Which countries have the biggest surplus (net sellers)?
sellers = merged.sort_values("surplus", ascending=False).head(5)
print(sellers[["Country", "surplus"]])

plt.bar(sellers["Country"], sellers["surplus"])
plt.title("Top 5 countries: production minus consumption")
plt.ylabel("Surplus")
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()

# 5. Q2: Which countries consume the largest share of their own production?
users = merged.sort_values("consumption_pct", ascending=False).head(5)
print(users[["Country", "consumption_pct"]])

# 6. Q3: Do any countries consume more than they produce?
buyers = merged[merged["surplus"] < 0]
print(buyers[["Country", "surplus"]])