import pandas as pd

# Sample data for demonstration
data1 = {
    "CustomerID": [1, 2, 3, 4, 5],
    "Name": ["Alice", "Bob", "Charlie", "David", "Emily"],
}

data2 = {
    "CustomerID": [1, 2, 3, 6, 7],
    "Email": [
        "alice@example.com",
        "bob@example.com",
        "charlie@example.com",
        "david@example.com",
        "emily@example.com",
    ],
}

# Create DataFrames from the sample data
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Perform an inner join on the 'CustomerID' column
merged_df = df1.set_index("CustomerID").join(df2.set_index("CustomerID"), how="inner")

# Display the merged DataFrame
print("Merged DataFrame:")
print(merged_df)
