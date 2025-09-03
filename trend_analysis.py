# This code loads the Malaysian retail store CSV and computes:
# - Monthly sales trends
# - Top selling products
# - Sales by store location
# - Payment method distribution
# - Relationship of sale price vs sale volume
# It also creates a few simple visualizations and prints brief acks after each step.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1) Load data
csv_path = 'malaysian_retail_store.csv'
df = pd.read_csv(csv_path, encoding='ascii')
print('Loaded CSV with shape: ' + str(df.shape))

# 2) Basic cleaning and derived fields
# Ensure correct dtypes
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

numeric_cols = ['Quantity', 'PricePerUnit', 'TotalAmount']
for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

# Drop rows with missing critical fields
crit_cols = ['TransactionID', 'Date', 'Product', 'Quantity', 'PricePerUnit', 'TotalAmount']
keep_cols = [c for c in crit_cols if c in df.columns]
df_clean = df.dropna(subset=keep_cols)

# Derive Year-Month for grouping
df_clean['YearMonth'] = df_clean['Date'].dt.to_period('M').dt.to_timestamp()

print('Data cleaned. Remaining rows: ' + str(len(df_clean)))

# 3) Monthly sales trends (sum of TotalAmount per month)
monthly_sales = df_clean.groupby('YearMonth', as_index=False)['TotalAmount'].sum().sort_values('YearMonth')
print('Computed monthly sales trends. Rows: ' + str(len(monthly_sales)))

plt.figure(figsize=(8,4))
sns.lineplot(data=monthly_sales, x='YearMonth', y='TotalAmount', marker='o')
plt.title('Monthly Sales (TotalAmount)')
plt.xlabel('Month')
plt.ylabel('Sales (RM)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 4) Top selling products (by revenue and by quantity)
prod_rev = df_clean.groupby('Product', as_index=False)['TotalAmount'].sum().sort_values('TotalAmount', ascending=False)
prod_qty = df_clean.groupby('Product', as_index=False)['Quantity'].sum().sort_values('Quantity', ascending=False)

print('Computed top selling products by revenue and quantity.')

plt.figure(figsize=(8,4))
sns.barplot(data=prod_rev.head(10), x='Product', y='TotalAmount', color='#4C72B0')
plt.title('Top 10 Products by Revenue')
plt.xlabel('Product')
plt.ylabel('Revenue (RM)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,4))
sns.barplot(data=prod_qty.head(10), x='Product', y='Quantity', color='#55A868')
plt.title('Top 10 Products by Quantity Sold')
plt.xlabel('Product')
plt.ylabel('Units Sold')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# 5) Sales by store location
if 'StoreLocation' in df_clean.columns:
    store_sales = df_clean.groupby('StoreLocation', as_index=False)['TotalAmount'].sum().sort_values('TotalAmount', ascending=False)
    print('Computed sales by store location. Locations: ' + str(store_sales['StoreLocation'].nunique()))
    plt.figure(figsize=(8,4))
    sns.barplot(data=store_sales, x='StoreLocation', y='TotalAmount', color='#C44E52')
    plt.title('Sales by Store Location')
    plt.xlabel('Store Location')
    plt.ylabel('Revenue (RM)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
else:
    store_sales = pd.DataFrame()
    print('StoreLocation column not found.')

# 6) Payment method used (count and share of transactions)
if 'PaymentMethod' in df_clean.columns:
    pay_counts = df_clean['PaymentMethod'].value_counts(dropna=False).reset_index()
    pay_counts.columns = ['PaymentMethod', 'Count']
    pay_counts['Share'] = pay_counts['Count'] / pay_counts['Count'].sum()
    print('Computed payment method distribution. Methods: ' + str(pay_counts['PaymentMethod'].nunique()))

    plt.figure(figsize=(6,4))
    sns.barplot(data=pay_counts, x='PaymentMethod', y='Count', color='#8172B3')
    plt.title('Payment Method Usage (Count)')
    plt.xlabel('Payment Method')
    plt.ylabel('Transactions')
    plt.xticks(rotation=30, ha='right')
    plt.tight_layout()
    plt.show()
else:
    pay_counts = pd.DataFrame()
    print('PaymentMethod column not found.')

# 7) Relation of sale price vs sale volume
# Use PricePerUnit vs Quantity with bubble size by TotalAmount
rel_df = df_clean[['PricePerUnit', 'Quantity', 'TotalAmount']].dropna()
print('Prepared data for price vs volume relation. Points: ' + str(len(rel_df)))

plt.figure(figsize=(6,5))
plt.scatter(rel_df['PricePerUnit'], rel_df['Quantity'], s=np.clip(rel_df['TotalAmount'] / (rel_df['TotalAmount'].max() + 1e-9) * 300, 20, 300), alpha=0.6, c='#64B5F6', edgecolors='k')
plt.title('Price per Unit vs Quantity (Bubble size = Revenue)')
plt.xlabel('Price per Unit (RM)')
plt.ylabel('Quantity')
plt.tight_layout()
plt.show()

# 8) Compute simple correlations and KPIs for insights
kpis = {}
if len(monthly_sales) > 1:
    # Growth from first to last month
    first_val = monthly_sales.iloc[0]['TotalAmount']
    last_val = monthly_sales.iloc[-1]['TotalAmount']
    growth = (last_val - first_val) / first_val if first_val != 0 else np.nan
    kpis['monthly_sales_growth'] = growth

# Correlation between price and quantity
if rel_df.shape[0] > 1:
    kpis['corr_price_qty'] = np.corrcoef(rel_df['PricePerUnit'], rel_df['Quantity'])[0,1]

# Top product by revenue and by quantity
if not prod_rev.empty:
    kpis['top_product_revenue'] = prod_rev.iloc[0]['Product']
if not prod_qty.empty:
    kpis['top_product_quantity'] = prod_qty.iloc[0]['Product']

print('Computed KPIs and correlations: ' + str(kpis))

# Show heads for quick verification
print('Head of monthly_sales:')
print(monthly_sales.head())
print('Head of prod_rev:')
print(prod_rev.head())
print('Head of store_sales:')
print(store_sales.head() if 'StoreLocation' in df_clean.columns else store_sales)
print('Head of pay_counts:')
print(pay_counts.head())
