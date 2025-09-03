"""
Retail Store Data Analysis with Pandas
Author: Your Name
Date: YYYY-MM-DD

This script performs exploratory data analysis (EDA) 
on Malaysian retail sales data.
"""

import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# 1. Load the dataset
# -------------------------------
df = pd.read_csv("data/malaysian_retail_store.csv")

print("✅ Dataset loaded successfully!")
print("Shape:", df.shape)
print("\nFirst 5 rows:\n", df.head())

# -------------------------------
# 2. Basic summary statistics
# -------------------------------
print("\n--- Dataset Info ---")
print(df.info())

print("\n--- Missing Values ---")
print(df.isnull().sum())

print("\n--- Descriptive Statistics ---")
print(df.describe())

# -------------------------------
# 3. Business Question 1:
# Which products generate the most revenue?
# -------------------------------
revenue_by_product = (
    df.groupby("Product")["TotalAmount"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- Revenue by Product ---")
print(revenue_by_product)

# Plot
plt.figure(figsize=(8, 5))
revenue_by_product.plot(kind="bar", color="skyblue")
plt.title("Revenue by Product Category")
plt.xlabel("Product")
plt.ylabel("Total Revenue")
plt.tight_layout()
plt.savefig("outputs/revenue_by_product.png")
plt.show()

# -------------------------------
# 4. Business Question 2:
# What is the preferred payment method?
# -------------------------------
payment_counts = df["PaymentMethod"].value_counts()
payment_revenue = df.groupby("PaymentMethod")["TotalAmount"].sum()

print("\n--- Transactions by Payment Method ---")
print(payment_counts)

print("\n--- Revenue by Payment Method ---")
print(payment_revenue)

# Plot
plt.figure(figsize=(6, 6))
payment_counts.plot(kind="pie", autopct='%1.1f%%')
plt.title("Preferred Payment Methods")
plt.ylabel("")
plt.tight_layout()
plt.savefig("outputs/payment_methods.png")
plt.show()

# -------------------------------
# 5. Business Question 3:
# Which store location performs best?
# -------------------------------
revenue_by_location = (
    df.groupby("StoreLocation")["TotalAmount"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- Revenue by Store Location ---")
print(revenue_by_location)

# Plot
plt.figure(figsize=(8, 5))
revenue_by_location.plot(kind="bar", color="orange")
plt.title("Revenue by Store Location")
plt.xlabel("Store Location")
plt.ylabel("Total Revenue")
plt.tight_layout()
plt.savefig("outputs/revenue_by_location.png")
plt.show()

# -------------------------------
# 6. Save cleaned dataset (if needed)
# -------------------------------
df.to_csv("outputs/retail_store_cleaned.csv", index=False)
print("\n✅ Cleaned dataset saved to outputs/retail_store_cleaned.csv")
