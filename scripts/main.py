import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('data/data.csv', encoding='latin1')

# Clean data
df.dropna(inplace=True)
df = df[df['Quantity'] > 0]

# Create Revenue column
df['Revenue'] = df['Quantity'] * df['UnitPrice']

# Convert date
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# ===== EDA =====

# Top countries
country_sales = df.groupby('Country')['Revenue'].sum().sort_values(ascending=False).head(10)
country_sales.plot(kind='bar')

plt.figure(figsize=(10,5))  # makes it wider

country_sales.plot(kind='bar')
plt.title("Top Countries by Revenue")
plt.xticks(rotation=45)  # rotate labels
plt.tight_layout()

plt.show()

# Monthly trend
df['Month'] = df['InvoiceDate'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Revenue'].sum()
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.show()

top_products = df.groupby('Description')['Revenue'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
top_products.plot(kind='bar')
plt.title("Top 10 Products")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Save cleaned data
df.to_csv('output/cleaned_data.csv', index=False)

print("Project completed successfully!")