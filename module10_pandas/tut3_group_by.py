import pandas as pd

# Sample sales data for demonstration
data = {
    "Product": ["A", "B", "A", "C", "B", "C", "A", "B", "C"],
    "Sales": [100, 150, 200, 120, 180, 130, 220, 160, 140],
}

# Create a DataFrame from the sample data
df = pd.DataFrame(data)

# Group the data by 'Product' and calculate the total sales for each category
grouped_data = df.groupby("Product")

for product, sales in grouped_data:
    print(product)
    print(sales)
    print()

# Group the data by 'Product' and calculate the total sales for each category
grouped_data_sum = df.groupby("Product")["Sales"].sum().reset_index()

# Display the grouped data
print("Total Sales by Product Category:")
print(grouped_data_sum)
