import pandas as pd

# Sample sales data for demonstration
data = {
    "Product": ["A", "B", "A", "C", "B", "C", "A", "B", "C"],
    "Sales": [100, 150, 200, 120, 180, 130, 220, 160, 140],
}

# Create a DataFrame from the sample data
df = pd.DataFrame(data)

# Group the data by 'Product'
grouped_data = df.groupby("Product")

# Iterate over each group and print the group contents
for product, group_data in grouped_data:
    print(f"Product: {product}")
    print(group_data)
    print()

# Use the get_group method to retrieve specific groups
group_a = grouped_data.get_group("A")
group_b = grouped_data.get_group("B")
group_c = grouped_data.get_group("C")

# Display the retrieved groups
print("Group A:")
print(group_a)
print()

print("Group B:")
print(group_b)
print()

print("Group C:")
print(group_c)
print()

# Calculate the total sales for each category
grouped_data_sum = df.groupby("Product")["Sales"].sum().reset_index()

# Display the total sales by product category
print("Total Sales by Product Category:")
print(grouped_data_sum)


# minimum data
print(f"grouped_data.min()")
print(grouped_data.min())

# maximum data
print(f"grouped_data.max()")
print(grouped_data.max())

# mean data
print(f"grouped_data.mean()")
print(grouped_data.mean())
