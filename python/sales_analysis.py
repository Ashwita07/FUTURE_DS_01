# Business Sales Performance Analytics
# Future Interns - Task 1
# Dataset: Sample Superstore

import pandas as pd
import matplotlib.pyplot as plt

DATA_PATH = "../dataset/sales_data.csv"

# -----------------------------
# 1. Load data
# -----------------------------
df = pd.read_csv(DATA_PATH)

# -----------------------------
# 2. Data cleaning
# -----------------------------
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")

# Remove exact duplicate rows
df = df.drop_duplicates()

# Check missing values
print("Missing values:")
print(df.isnull().sum())

# -----------------------------
# 3. KPI analysis
# -----------------------------
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
total_quantity = df["Quantity"].sum()
average_order_value = total_sales / total_orders
profit_margin = (total_profit / total_sales) * 100

print("\n===== KEY PERFORMANCE INDICATORS =====")
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Total Orders: {total_orders:,}")
print(f"Total Quantity Sold: {total_quantity:,}")
print(f"Average Order Value: ${average_order_value:,.2f}")
print(f"Profit Margin: {profit_margin:.2f}%")

# -----------------------------
# 4. Revenue trend
# -----------------------------
monthly_sales = (
    df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
      .sum()
      .reset_index()
)

monthly_sales["Order Date"] = monthly_sales["Order Date"].dt.to_timestamp()

print("\n===== MONTHLY SALES =====")
print(monthly_sales.tail(12))

plt.figure(figsize=(12, 5))
plt.plot(monthly_sales["Order Date"], monthly_sales["Sales"])
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------------
# 5. Category performance
# -----------------------------
category = (
    df.groupby("Category")[["Sales", "Profit"]]
      .sum()
      .sort_values("Sales", ascending=False)
)

print("\n===== CATEGORY PERFORMANCE =====")
print(category)

# -----------------------------
# 6. Regional performance
# -----------------------------
region = (
    df.groupby("Region")[["Sales", "Profit"]]
      .sum()
      .sort_values("Sales", ascending=False)
)

print("\n===== REGIONAL PERFORMANCE =====")
print(region)

# -----------------------------
# 7. Segment performance
# -----------------------------
segment = (
    df.groupby("Segment")[["Sales", "Profit"]]
      .sum()
      .sort_values("Sales", ascending=False)
)

print("\n===== CUSTOMER SEGMENT PERFORMANCE =====")
print(segment)

# -----------------------------
# 8. Top 10 products
# -----------------------------
top_products = (
    df.groupby("Product Name")
      .agg(
          Sales=("Sales", "sum"),
          Profit=("Profit", "sum"),
          Quantity=("Quantity", "sum")
      )
      .sort_values("Sales", ascending=False)
      .head(10)
)

print("\n===== TOP 10 PRODUCTS BY SALES =====")
print(top_products)

# -----------------------------
# 9. Loss-making products
# -----------------------------
loss_products = (
    df.groupby("Product Name")["Profit"]
      .sum()
      .sort_values()
      .head(10)
)

print("\n===== 10 PRODUCTS WITH LOWEST PROFIT =====")
print(loss_products)

# -----------------------------
# 10. Discount and profit
# -----------------------------
discount_analysis = (
    df.groupby("Discount")[["Sales", "Profit"]]
      .sum()
      .sort_index()
)

print("\n===== DISCOUNT VS PROFIT =====")
print(discount_analysis)

discount_profit_correlation = df[["Discount", "Profit"]].corr().iloc[0, 1]
print(f"\nDiscount-Profit correlation: {discount_profit_correlation:.3f}")

print("\nAnalysis completed successfully.")
