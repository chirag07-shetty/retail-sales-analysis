import pandas as pd

df = pd.read_csv("sales_data.csv")

print("Number of rows and columns:")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nDataset information:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nSales Analysis:")

print("Total Sales:", df["Sales_amount"].sum())

print("Average Sales:", df["Sales_amount"].mean())

print("Highest Sale:", df["Sales_amount"].max())

print("Lowest Sale:", df["Sales_amount"].min())

print("Sales by category\n")
category_sales=df.groupby("Category")["Sales_amount"].sum()
print(category_sales)

print("Sales by region\n")
region_sales=df.groupby("Region")["Sales_amount"].sum()
print(region_sales)

print("\n Top selling category")
top_category=df.groupby("Category")["Sales_amount"].sum().idxmax()
top_category_sales=df.groupby("Category")["Sales_amount"].sum().max()
print(top_category)
print(top_category_sales)

print("\n Top selling product")

top_product=df.groupby("Product")["Sales_amount"].sum().idxmax()
top_product_sales=df.groupby("Product")["Sales_amount"].sum().max()
print(top_product)
print(top_product_sales)

print("\n Sales by payment method")
top_payment_method=df.groupby("Payment_method")["Sales_amount"].sum()
print(top_payment_method)

print("\n Sales by month")
top_sales_month=df.groupby("Order_date")["Sales_amount"].sum()
print(top_sales_month)

print("\nBest Sales month")
top_month=df.groupby("Order_date")["Sales_amount"].sum().idxmax()
top_month_sales=df.groupby("Order_date")["Sales_amount"].sum().max()
print(top_month)
print(top_month_sales)